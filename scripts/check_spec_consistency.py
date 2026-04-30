#!/usr/bin/env python3
"""
check_spec_consistency.py — assert PAX spec source-of-truth integrity.

`docs/pax_spec.yaml` is the source of truth for the PAX format's moving parts:
current version, valid versions, controlled vocabularies, per-entity field
manifests, script defaults. This script asserts that every other place that
encodes any of those facts agrees with the YAML — and exits non-zero on the
first drift detected, with a per-mismatch report so the contributor knows
exactly what to fix.

CI calls this script before validate-pack and before publish-artifacts.
PRs cannot merge and releases cannot ship if it fails.

Usage:
    python3 scripts/check_spec_consistency.py                # text mode
    python3 scripts/check_spec_consistency.py --json         # machine-readable

Exit codes:
    0 — all checks pass; spec, guide, scripts, docs, and packs all agree
    1 — at least one drift detected; report printed to stdout/stderr
    2 — usage error or missing source-of-truth file
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml is required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


REPO_ROOT = Path(__file__).resolve().parent.parent
SPEC_PATH = REPO_ROOT / "docs" / "pax_spec.yaml"
GUIDE_PATH = REPO_ROOT / "docs" / "PAX_CREATION_GUIDE.md"


# ---------------------------------------------------------------------------
# Drift report
# ---------------------------------------------------------------------------

class Drift:
    def __init__(self) -> None:
        self.mismatches: list[dict] = []

    def add(self, file: str, line: int | None, what: str, claims: Any, expected: Any) -> None:
        self.mismatches.append({
            "file": file,
            "line": line,
            "what": what,
            "claims": claims,
            "expected": expected,
        })

    def __bool__(self) -> bool:
        return bool(self.mismatches)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def find_line(text: str, pattern: str) -> int | None:
    m = re.search(pattern, text, re.M)
    if not m:
        return None
    return text[: m.start()].count("\n") + 1


def _extract_str_tuple(node) -> list[str] | None:
    """Return [str,...] if node is a literal tuple of str, or wraps one
    inside `tuple(... or ("a", "b", ...))`. Otherwise None."""
    import ast
    # Bare literal: ("a", "b") or ["a", "b"]
    if isinstance(node, (ast.Tuple, ast.List)):
        out = []
        for el in node.elts:
            if isinstance(el, ast.Constant) and isinstance(el.value, str):
                out.append(el.value)
            else:
                return None
        return out
    # Wrapped: tuple(EXPR) — recurse into the BoolOp's right side if any.
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "tuple":
        if len(node.args) == 1:
            inner = node.args[0]
            # Look for `<something> or (literal,)` shape — the literal is the right operand.
            if isinstance(inner, ast.BoolOp) and isinstance(inner.op, ast.Or):
                # The fallback is the LAST operand (defense-in-depth literal).
                return _extract_str_tuple(inner.values[-1])
            # Otherwise try direct extraction.
            return _extract_str_tuple(inner)
    # Generator-expression-fallback shape: NAME = tuple(... for ... in ...) or (literal,)
    if isinstance(node, ast.BoolOp) and isinstance(node.op, ast.Or):
        return _extract_str_tuple(node.values[-1])
    return None


def _legacy_alias_for(spec: dict, canonical_name: str) -> str:
    """Return the legacy alias name for a canonical manifest field, or the
    canonical itself if no legacy is declared."""
    for entry in spec.get("legacy_field_aliases") or []:
        if entry.get("canonical") == canonical_name:
            return entry.get("legacy_name") or canonical_name
    return canonical_name


def load_spec() -> dict:
    if not SPEC_PATH.exists():
        print(f"ERROR: source-of-truth file not found: {SPEC_PATH}", file=sys.stderr)
        sys.exit(2)
    with SPEC_PATH.open() as f:
        return yaml.safe_load(f) or {}


# ---------------------------------------------------------------------------
# Individual checks
# ---------------------------------------------------------------------------

def check_guide_header(spec: dict, drift: Drift) -> None:
    """Title + header version stamp + last-updated date."""
    text = GUIDE_PATH.read_text()
    cur = spec["current_version"]
    last = spec["last_updated"]

    # Line 1: # PAX vN Specification & Creation Guide
    m = re.match(r"^# PAX v(\d+) ", text)
    if not m:
        drift.add(str(GUIDE_PATH), 1, "guide title format", text.split("\n", 1)[0], f"# PAX v{cur.split('.')[0]} Specification & Creation Guide")
    elif m.group(1) != cur.split(".")[0]:
        drift.add(str(GUIDE_PATH), 1, "guide title major version", m.group(1), cur.split(".")[0])

    # Line 3: > **Schema version:** N.N — Last updated: YYYY-MM-DD
    m = re.search(r"^> \*\*Schema version:\*\* (\S+) — Last updated: (\S+)", text, re.M)
    if not m:
        drift.add(str(GUIDE_PATH), 3, "guide header line", "—", f"> **Schema version:** {cur} — Last updated: {last}")
    else:
        if m.group(1) != cur:
            drift.add(str(GUIDE_PATH), 3, "guide schema version stamp", m.group(1), cur)
        if m.group(2) != last:
            drift.add(str(GUIDE_PATH), 3, "guide last-updated date", m.group(2), last)


def check_guide_schema_block(spec: dict, drift: Drift) -> None:
    """SCHEMA block enums must match spec['enums']."""
    text = GUIDE_PATH.read_text()
    block = re.search(r"<!-- PAX_SCHEMA_START.*?-->(.+?)<!-- PAX_SCHEMA_END", text, re.DOTALL)
    if not block:
        drift.add(str(GUIDE_PATH), None, "missing PAX_SCHEMA markers", "—", "block present")
        return

    parsed: dict[str, list[str]] = {}
    for line in block.group(1).splitlines():
        m = re.match(r"\*\*(\w+) values:\*\*\s*(.+)", line.strip())
        if m:
            parsed[m.group(1)] = [v.strip() for v in m.group(2).split(",") if v.strip()]

    expected = spec["enums"]
    for key, want in expected.items():
        # YAML 'null' deserializes to Python None; the SCHEMA block writes it as the string "null".
        want_str = [str(x) if x is not None else "null" for x in want]
        got = parsed.get(key)
        if got is None:
            drift.add(str(GUIDE_PATH), None, f"SCHEMA block missing enum '{key}'", None, want_str)
        elif got != want_str:
            drift.add(str(GUIDE_PATH), None, f"SCHEMA block enum '{key}' mismatch", got, want_str)
    for key in parsed:
        if key not in expected:
            drift.add(str(GUIDE_PATH), None, f"SCHEMA block has extra enum '{key}'", parsed[key], "—")


def check_guide_fields_block(spec: dict, drift: Drift) -> None:
    """FIELDS block entity manifest must match spec['entities']."""
    text = GUIDE_PATH.read_text()
    block = re.search(r"<!-- PAX_FIELDS_START.*?-->(.+?)<!-- PAX_FIELDS_END", text, re.DOTALL)
    if not block:
        drift.add(str(GUIDE_PATH), None, "missing PAX_FIELDS markers", "—", "block present")
        return
    fence = re.search(r"```yaml\s*\n(.+?)```", block.group(1), re.DOTALL)
    if not fence:
        drift.add(str(GUIDE_PATH), None, "FIELDS block has no ```yaml fence", "—", "fence present")
        return
    parsed = (yaml.safe_load(fence.group(1)) or {}).get("entities") or {}
    expected = spec["entities"]
    for ent, want in expected.items():
        got = parsed.get(ent)
        if got is None:
            drift.add(str(GUIDE_PATH), None, f"FIELDS block missing entity '{ent}'", None, want)
            continue
        if got != want:
            drift.add(str(GUIDE_PATH), None, f"FIELDS block entity '{ent}' mismatch", got, want)
    for ent in parsed:
        if ent not in expected:
            drift.add(str(GUIDE_PATH), None, f"FIELDS block has extra entity '{ent}'", parsed[ent], "—")


def check_guide_version_history(spec: dict, drift: Drift) -> None:
    """Latest row of the version-history table matches spec; rows match version_history list."""
    text = GUIDE_PATH.read_text()
    # Find the table — header line then rows like: | 4.0 | 2026-04-29 | ... |
    rows = re.findall(r"^\|\s*(\d+\.\d+)\s*\|\s*(\d{4}-\d{2}-\d{2})\s*\|", text, re.M)
    if not rows:
        drift.add(str(GUIDE_PATH), None, "version-history table not found", "—", "rows present")
        return
    expected = [(v["version"], v["date"]) for v in spec["version_history"]]
    if rows != expected:
        drift.add(str(GUIDE_PATH), None, "version-history rows mismatch", rows, expected)


def check_validate_pax(spec: dict, drift: Drift) -> None:
    """validate_pax.py constants must match spec values."""
    import ast

    path = REPO_ROOT / "scripts" / "validate_pax.py"
    text = path.read_text()

    # Parse the module and find each top-level assignment of interest. We
    # extract the literal string tuple out of either:
    #   NAME = ("a", "b", ...)
    #   NAME = tuple(_SPEC.get(...) or ("a", "b", ...))
    # The literal tuple is the defense-in-depth fallback; the consistency
    # check enforces it agrees with pax_spec.yaml.
    tree = ast.parse(text)
    found: dict[str, list[str]] = {}
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if len(node.targets) != 1 or not isinstance(node.targets[0], ast.Name):
            continue
        target = node.targets[0].id
        literal = _extract_str_tuple(node.value)
        if literal is not None:
            found[target] = literal

    def _check(const_name: str, want: list[str]) -> None:
        got = found.get(const_name)
        if got is None:
            drift.add(str(path), None, f"{const_name} not found", None, want)
        elif got != want:
            drift.add(str(path), find_line(text, rf"^{const_name}\s*="), f"{const_name} mismatch", got, want)

    _check("VALID_PAX_TYPES", list(spec["pax_types"]))
    _check("VALID_SCHEMA_VERSIONS", list(spec["valid_versions"]))
    _check("DATASET_FORMATS", list(spec["enums"]["dataset_format"]))
    _check("PLAYBOOK_ACTIONS", list(spec["enums"]["playbook_action"]))
    pax_required = [x for x in spec["entities"]["pax_yaml"]["required"] if isinstance(x, str)]
    _check("REQUIRED_PAX_YAML_FIELDS", pax_required)
    _check("REQUIRED_KNOWLEDGE_FILES", list(spec["required_knowledge_files"]))


def check_build_pax(spec: dict, drift: Drift) -> None:
    """build_pax.py default schema-version fallback matches spec.
    Accepts either the canonical or legacy field name, since the live code
    reads canonical first and falls back to legacy.
    """
    path = REPO_ROOT / "scripts" / "build_pax.py"
    text = path.read_text()
    canon = spec["manifest_field_names"]["built_against_schema"]
    legacy = _legacy_alias_for(spec, canon)
    want = spec["defaults"]["build_pax_schema_fallback"]
    pattern = rf'_read_yaml_field\(text,\s*"(?:{canon}|{legacy})",\s*"([^"]+)"\)'
    matches = [m for m in re.finditer(pattern, text) if m.group(1)]
    if not matches:
        drift.add(str(path), None, f"build_pax schema fallback not found", None, want)
        return
    # The non-empty fallback must match spec; an empty-string fallback is the
    # canonical read in the two-stage shape and is fine.
    bad = [m for m in matches if m.group(1) != want]
    if bad:
        m = bad[0]
        drift.add(str(path), text[: m.start()].count("\n") + 1, "build_pax schema fallback mismatch", m.group(1), want)


def check_generate_registry(spec: dict, drift: Drift) -> None:
    """generate-registry.py default schema-version fallback matches spec.
    Same canonical-or-legacy logic as check_build_pax.
    """
    path = REPO_ROOT / "scripts" / "generate-registry.py"
    text = path.read_text()
    canon = spec["manifest_field_names"]["built_against_schema"]
    legacy = _legacy_alias_for(spec, canon)
    want = spec["defaults"]["registry_schema_fallback"]
    pattern = rf'manifest\.get\("(?:{canon}|{legacy})",\s*"([^"]+)"\)'
    matches = [m for m in re.finditer(pattern, text) if m.group(1)]
    if not matches:
        drift.add(str(path), None, "generate-registry schema fallback not found", None, want)
        return
    bad = [m for m in matches if m.group(1) != want]
    if bad:
        m = bad[0]
        drift.add(str(path), text[: m.start()].count("\n") + 1, "generate-registry schema fallback mismatch", m.group(1), want)


def check_doc_valid_versions(spec: dict, drift: Drift) -> None:
    """README.md and CLAUDE.md valid-versions enumerations must include exactly spec.valid_versions."""
    want = list(spec["valid_versions"])
    for name in ("README.md", "CLAUDE.md"):
        path = REPO_ROOT / name
        if not path.exists():
            continue
        text = path.read_text()
        m = re.search(r"Valid `schema_version`:\s*(.+)", text)
        if not m:
            continue  # the doc may not enumerate versions; that's fine
        listed = re.findall(r"\d+\.\d+", m.group(1))
        if listed != want:
            drift.add(str(path), find_line(text, r"Valid `schema_version`:"), f"{name} valid-versions list mismatch", listed, want)


def check_whats_new_header(spec: dict, drift: Drift) -> None:
    """Guide must have a `## What's New in v{major(current_version)}` heading.
    Cheapest possible check against narrative drift on the highest-likelihood
    paragraph (the "what's new" lead).
    """
    text = GUIDE_PATH.read_text()
    major = spec["current_version"].split(".")[0]
    pattern = rf"^## What's New in v{major}\b"
    if not re.search(pattern, text, re.M):
        drift.add(str(GUIDE_PATH), None, f"missing `## What's New in v{major}` heading", "—", f"## What's New in v{major} ...")


def check_guide_inline_examples(spec: dict, drift: Drift) -> None:
    """Walk fenced YAML/JSON blocks in the guide. For any line that assigns
    one of the known spec-typed keys (built_against_schema, pax_type,
    direction, format inside a dataset/yaml example, finding_type, etc.),
    assert the value is in the spec's enum / valid_versions list.

    Closes the "inline example uses an outdated value" class of drift.
    """
    text = GUIDE_PATH.read_text()

    valid_versions = set(spec["valid_versions"])
    enums = spec["enums"]

    # Map example keys to spec list. Only check keys whose meaning is
    # unambiguous in PAX example contexts.
    key_to_values: dict[str, set[str]] = {
        "built_against_schema": valid_versions,
        "pax_type": set(enums["pax_type"]),
        "direction": set(enums["direction"]),
        "finding_type": set(enums["finding_type"]),
        "evidence_type": set(enums["evidence_type"]),
        "construct_type": set(enums["construct_type"]),
        "study_design": set(enums["study_design"]),
        "level_of_analysis": set(enums["level_of_analysis"]),
        "measurement_level": set(enums["measurement_level"]),
        "relationship_type": set(enums["relationship_type"]),
        "effect_size_type": set(enums["effect_size_type"]),
        "alias_type": set(enums["alias_type"]),
        "unit_of_analysis": set(enums["unit_of_analysis"]),
        "relation_type": set(enums["relation_type"]),
        "operationalization_status": set(enums["operationalization_status"]),
        "canonical_status": set(enums["canonical_status"]),
        "construct_kind": set(enums["construct_kind"]),
    }

    # Iterate fenced blocks tagged yaml or json. Each match yields the
    # block's start offset (so we can compute line numbers) and its body.
    for fence in re.finditer(r"```(yaml|json)\s*\n(.+?)```", text, re.DOTALL):
        body = fence.group(2)
        body_start_line = text[: fence.start(2)].count("\n") + 1

        for line_offset, line in enumerate(body.splitlines()):
            stripped = line.strip()
            # Skip comments and clearly-non-data lines.
            if not stripped or stripped.startswith("#"):
                continue
            # YAML form: key: value   or   "key": value   or   - {key: value, ...}
            # JSON form: "key": value
            for key, allowed in key_to_values.items():
                m = re.search(rf'(?:^|\b|"){key}"?\s*:\s*"?([\w.\-]+)"?', stripped)
                if not m:
                    continue
                val = m.group(1)
                # Allow placeholder ellipses and clearly-illustrative tokens.
                if val in ("...", "<value>", "<...>"):
                    continue
                if val not in allowed:
                    drift.add(
                        str(GUIDE_PATH),
                        body_start_line + line_offset,
                        f"inline example {key} value not in spec",
                        val,
                        sorted(allowed),
                    )


def check_scripts_for_unregistered_enums(spec: dict, drift: Drift) -> None:
    """AST-scan every scripts/*.py file for module-level tuple/list literals
    that look like enum vocabularies. Any such literal must either:
      (a) live in scripts/validate_pax.py (already covered by check_validate_pax), or
      (b) be the literal value of a registered fallback (e.g., the inner
          tuple of `tuple(_SPEC.get(...) or ("a", ...))`), or
      (c) be in EXEMPT_LITERALS below.

    The signature: a module-level Assign of a Name to a Tuple/List of >=3
    string Constants, all matching `[a-z][a-z0-9_]*`. That's the shape of an
    enum vocab; it's rare enough in non-spec code that false positives are
    manageable.

    Catches the "someone adds a new VALID_FOO constant in a new script
    without registering coverage" failure mode.
    """
    import ast

    # Constants in this set are intentionally not checked against the spec
    # (e.g., they're internal to a script and aren't spec state).
    EXEMPT: set[tuple[str, str]] = {
        # (filename, constant_name) — add carve-outs deliberately, with reason.
    }

    # Constants that ARE spec state and ARE checked elsewhere — record them
    # here so we don't double-report. check_validate_pax handles these.
    KNOWN_REGISTERED: set[tuple[str, str]] = {
        ("validate_pax.py", "VALID_PAX_TYPES"),
        ("validate_pax.py", "VALID_SCHEMA_VERSIONS"),
        ("validate_pax.py", "DATASET_FORMATS"),
        ("validate_pax.py", "PLAYBOOK_ACTIONS"),
        ("validate_pax.py", "REQUIRED_PAX_YAML_FIELDS"),
        ("validate_pax.py", "REQUIRED_KNOWLEDGE_FILES"),
    }

    enum_member_re = re.compile(r"^[a-z][a-z0-9_\-]*$")

    def _looks_like_enum_literal(node) -> list[str] | None:
        if not isinstance(node, (ast.Tuple, ast.List)):
            return None
        items: list[str] = []
        for el in node.elts:
            if isinstance(el, ast.Constant) and isinstance(el.value, str):
                items.append(el.value)
            else:
                return None
        if len(items) < 3:
            return None
        if not all(enum_member_re.match(s) and len(s) <= 40 for s in items):
            return None
        return items

    scripts_dir = REPO_ROOT / "scripts"
    for py in sorted(scripts_dir.glob("*.py")):
        # The consistency check itself defines lots of literals; skip self.
        if py.name == "check_spec_consistency.py":
            continue
        try:
            tree = ast.parse(py.read_text())
        except SyntaxError:
            continue
        for node in tree.body:
            if not isinstance(node, ast.Assign) or len(node.targets) != 1:
                continue
            tgt = node.targets[0]
            if not isinstance(tgt, ast.Name):
                continue
            literal = _looks_like_enum_literal(node.value)
            # Walk into tuple(_SPEC.get(...) or (literal,)) shape — that's the
            # canonical "spec-driven with literal fallback" pattern.
            if literal is None and isinstance(node.value, ast.Call):
                if isinstance(node.value.func, ast.Name) and node.value.func.id == "tuple" and node.value.args:
                    inner = node.value.args[0]
                    if isinstance(inner, ast.BoolOp) and isinstance(inner.op, ast.Or):
                        literal = _looks_like_enum_literal(inner.values[-1])
            if literal is None:
                continue
            key = (py.name, tgt.id)
            if key in EXEMPT or key in KNOWN_REGISTERED:
                continue
            drift.add(
                str(py),
                node.lineno,
                f"unregistered enum-shaped literal {tgt.id!r}",
                literal,
                "either load from pax_spec.yaml, or register coverage in scripts/check_spec_consistency.py KNOWN_REGISTERED, or add an EXEMPT carve-out with a reason",
            )


def check_packs(spec: dict, drift: Drift) -> None:
    """Every pax/*/pax.yaml's schema_version must be in valid_versions."""
    field_name = spec["manifest_field_names"]["built_against_schema"]
    valid = set(spec["valid_versions"])
    packs_dir = REPO_ROOT / "pax"
    for p in sorted(packs_dir.glob("*/pax.yaml")):
        manifest = yaml.safe_load(p.read_text()) or {}
        v = str(manifest.get(field_name, ""))
        if not v:
            drift.add(str(p), None, f"missing {field_name}", None, f"one of {sorted(valid)}")
        elif v not in valid:
            drift.add(str(p), None, f"{field_name} not in valid_versions", v, sorted(valid))


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description="Assert PAX spec consistency.")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = parser.parse_args()

    spec = load_spec()

    # Self-consistency: latest version_history entry must match current_version + last_updated.
    drift = Drift()
    if spec["version_history"]:
        latest = spec["version_history"][0]
        if latest["version"] != spec["current_version"]:
            drift.add(str(SPEC_PATH), None, "version_history[0].version != current_version", latest["version"], spec["current_version"])
        if latest["date"] != spec["last_updated"]:
            drift.add(str(SPEC_PATH), None, "version_history[0].date != last_updated", latest["date"], spec["last_updated"])

    check_guide_header(spec, drift)
    check_whats_new_header(spec, drift)
    check_guide_schema_block(spec, drift)
    check_guide_fields_block(spec, drift)
    check_guide_version_history(spec, drift)
    check_guide_inline_examples(spec, drift)
    check_validate_pax(spec, drift)
    check_scripts_for_unregistered_enums(spec, drift)
    check_build_pax(spec, drift)
    check_generate_registry(spec, drift)
    check_doc_valid_versions(spec, drift)
    check_packs(spec, drift)

    if args.json:
        print(json.dumps({
            "ok": not drift,
            "mismatches": drift.mismatches,
        }))
        return 0 if not drift else 1

    if not drift:
        print(f"OK — spec consistent across guide, scripts, docs, and {len(list((REPO_ROOT / 'pax').glob('*/pax.yaml')))} packs.")
        return 0

    print(f"FAIL — {len(drift.mismatches)} drift point(s):\n")
    for m in drift.mismatches:
        loc = m["file"]
        if m["line"]:
            loc += f":{m['line']}"
        print(f"  - {loc}")
        print(f"    {m['what']}")
        print(f"      claims:   {m['claims']!r}")
        print(f"      expected: {m['expected']!r}")
        print()
    print(f"Source of truth: docs/pax_spec.yaml. Edit there first; then re-run this check.")
    return 1


if __name__ == "__main__":
    sys.exit(main())

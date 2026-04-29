#!/usr/bin/env python3
"""validate_pax.py — PR-time PAX structural validator.

Reads docs/PAX_CREATION_GUIDE.md as the contract:
  - <!-- PAX_SCHEMA_START --> ... <!-- PAX_SCHEMA_END -->   controlled vocabularies
  - <!-- PAX_FIELDS_START --> ... <!-- PAX_FIELDS_END -->   per-entity field manifest

Validates a single PAX directory against that contract. Designed to run
both locally (developer pre-flight) and in CI (validate-pack.yml).

Usage:
    python3 scripts/validate_pax.py pax/<pack-name>
    python3 scripts/validate_pax.py pax/<pack-name> --guide docs/PAX_CREATION_GUIDE.md

Exit codes:
    0 — all checks passed
    1 — validation errors (printed to stdout grouped by check)
    2 — usage error (bad args, missing files)

Background: pax-market#85 (the issue this implements).
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

# YAML is needed for pax.yaml + the FIELDS_START block.
try:
    import yaml
except ImportError:
    print("ERROR: pyyaml is required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_GUIDE = REPO_ROOT / "docs" / "PAX_CREATION_GUIDE.md"

VALID_PAX_TYPES = ("paper", "topic", "field", "engine", "enterprise")
VALID_SCHEMA_VERSIONS = ("1.0", "2.0", "3.0", "4.0")
DATASET_FORMATS = ("csv", "parquet", "excel")
PLAYBOOK_ACTIONS = (
    "engine",
    "ingest_dataset",
    "data_quality_gate",
    "register_dataset",
    "derive_observations",
)

# Entities whose JSON file is REQUIRED if the pack has any findings.
# (Other entities — propositions, canonical_constructs, etc. — are optional.)
REQUIRED_KNOWLEDGE_FILES = ("constructs.json", "sources.json", "findings.json")


# ---------------------------------------------------------------------------
# Guide parsers
# ---------------------------------------------------------------------------

def parse_schema_block(guide_text: str) -> dict[str, list[str]]:
    """Extract enum vocabularies from <!-- PAX_SCHEMA_START -->..<!-- PAX_SCHEMA_END -->.
    Lines look like: **field_name values:** v1, v2, v3"""
    m = re.search(r"<!-- PAX_SCHEMA_START.*?-->(.+?)<!-- PAX_SCHEMA_END", guide_text, re.DOTALL)
    if not m:
        raise RuntimeError("guide is missing PAX_SCHEMA_START/END markers")
    block = m.group(1)
    enums: dict[str, list[str]] = {}
    for line in block.splitlines():
        em = re.match(r"\*\*(\w+) values:\*\*\s*(.+)", line.strip())
        if em:
            name = em.group(1)
            values = [v.strip() for v in em.group(2).split(",") if v.strip()]
            enums[name] = values
    if not enums:
        raise RuntimeError("PAX_SCHEMA block parsed but contains no enums")
    return enums


def parse_fields_block(guide_text: str) -> dict[str, dict]:
    """Extract per-entity field manifest from <!-- PAX_FIELDS_START --> ... <!-- PAX_FIELDS_END -->.
    The block contains a yaml fenced section under `entities:`."""
    m = re.search(r"<!-- PAX_FIELDS_START.*?-->(.+?)<!-- PAX_FIELDS_END", guide_text, re.DOTALL)
    if not m:
        raise RuntimeError("guide is missing PAX_FIELDS_START/END markers")
    block = m.group(1)
    ym = re.search(r"```yaml\s*\n(.+?)```", block, re.DOTALL)
    if not ym:
        raise RuntimeError("PAX_FIELDS block has no ```yaml fence")
    parsed = yaml.safe_load(ym.group(1))
    return parsed.get("entities") or {}


def field_spec_name(spec: Any) -> str:
    """Field-manifest entries are either bare strings or {name, type, enum} dicts."""
    if isinstance(spec, dict):
        return spec.get("name", "")
    return str(spec)


def field_spec_type(spec: Any) -> tuple[str, str | None]:
    """Returns (type, enum-vocab-name) for a manifest field spec, or ('', None)."""
    if isinstance(spec, dict):
        return spec.get("type", ""), spec.get("enum")
    return "", None


# ---------------------------------------------------------------------------
# Pack helpers
# ---------------------------------------------------------------------------

def safe_load_json(p: Path) -> Any:
    try:
        with p.open() as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError as e:
        return e


def normalize_to_list(data: Any) -> list:
    if data is None:
        return []
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        return [data]
    return []


def collect_ids(items: list, key: str = "id") -> set[str]:
    return {x.get(key) for x in items if isinstance(x, dict) and x.get(key)}


# ---------------------------------------------------------------------------
# Validation passes
# ---------------------------------------------------------------------------

class Validator:
    def __init__(self, pack_dir: Path, enums: dict[str, list[str]], fields: dict[str, dict]):
        self.pack_dir = pack_dir
        self.pack_name = pack_dir.name
        self.enums = enums
        self.fields = fields
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def err(self, msg: str) -> None:
        self.errors.append(msg)

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)

    # -------------------------------------------------------------------
    # Pass 1: file presence
    # -------------------------------------------------------------------

    def check_files(self) -> None:
        if not (self.pack_dir / "pax.yaml").exists():
            self.err("missing pax.yaml")
        knowledge = self.pack_dir / "knowledge"
        if not knowledge.is_dir():
            self.err("missing knowledge/ directory")
            return
        for fname in REQUIRED_KNOWLEDGE_FILES:
            if not (knowledge / fname).exists():
                self.err(f"missing knowledge/{fname}")
        # domain.json or domains.json
        if not (knowledge / "domain.json").exists() and not (knowledge / "domains.json").exists():
            self.err("missing knowledge/domain.json (or domains.json)")

    # -------------------------------------------------------------------
    # Pass 2: manifest
    # -------------------------------------------------------------------

    def check_manifest(self) -> dict | None:
        path = self.pack_dir / "pax.yaml"
        if not path.exists():
            return None
        try:
            with path.open() as f:
                manifest = yaml.safe_load(f) or {}
        except yaml.YAMLError as e:
            self.err(f"pax.yaml: invalid YAML: {e}")
            return None
        if not isinstance(manifest, dict):
            self.err(f"pax.yaml: top-level must be a mapping, got {type(manifest).__name__}")
            return None

        # Required fields per PAX_FIELDS manifest (with sensible fallback).
        spec = self.fields.get("pax_yaml", {}) or {}
        required = spec.get("required") or list(REQUIRED_PAX_YAML_FIELDS)
        for field in required:
            name = field_spec_name(field)
            if name and not manifest.get(name):
                self.err(f"pax.yaml: missing required field '{name}'")

        # Name conventions
        name = manifest.get("name", "")
        if name and not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            self.err(f"pax.yaml: name '{name}' must be lower-kebab-case")
        if name and name != self.pack_name:
            self.err(f"pax.yaml: name '{name}' does not match directory name '{self.pack_name}'")

        # version: semver-ish (M.m.p with optional -prerelease)
        version = str(manifest.get("version", ""))
        if version and not re.fullmatch(r"\d+\.\d+\.\d+(-[\w.-]+)?", version):
            self.err(f"pax.yaml: version '{version}' is not a valid semver")

        # schema_version: enum
        sv = str(manifest.get("schema_version", ""))
        if sv and sv not in VALID_SCHEMA_VERSIONS:
            self.err(f"pax.yaml: schema_version '{sv}' not in {VALID_SCHEMA_VERSIONS}")

        # pax_type: enum
        pt = manifest.get("pax_type")
        if pt and pt not in VALID_PAX_TYPES:
            self.err(f"pax.yaml: pax_type '{pt}' not in {VALID_PAX_TYPES}")

        return manifest

    # -------------------------------------------------------------------
    # Pass 3: knowledge JSON syntax
    # -------------------------------------------------------------------

    def check_knowledge_json(self) -> dict[str, Any]:
        knowledge = self.pack_dir / "knowledge"
        loaded: dict[str, Any] = {}
        if not knowledge.is_dir():
            return loaded
        for json_path in knowledge.glob("*.json"):
            data = safe_load_json(json_path)
            if isinstance(data, json.JSONDecodeError):
                self.err(f"knowledge/{json_path.name}: invalid JSON: {data}")
            else:
                loaded[json_path.name] = data
        return loaded

    # -------------------------------------------------------------------
    # Pass 4: per-entity required fields + types + enums
    # -------------------------------------------------------------------

    def check_entity_fields(self, knowledge: dict[str, Any]) -> None:
        # Map filename → entity-name in PAX_FIELDS manifest.
        file_to_entity = {
            "domain.json":                      "domain",
            "domains.json":                     "domain",
            "sources.json":                     "source",
            "constructs.json":                  "construct",
            "findings.json":                    "finding",
            "propositions.json":                "proposition",
            "construct_relationships.json":     "construct_relationship",
            "construct_relations.json":         "construct_relation",
            "canonical_constructs.json":        "canonical_construct",
        }
        for fname, entity in file_to_entity.items():
            if fname not in knowledge:
                continue
            spec = self.fields.get(entity)
            if not spec:
                continue
            items = normalize_to_list(knowledge[fname])
            for idx, item in enumerate(items):
                if not isinstance(item, dict):
                    self.err(f"{fname}[{idx}]: must be an object, got {type(item).__name__}")
                    continue
                self._check_required(item, spec.get("required") or [], fname, idx)
                self._check_typed_fields(item, spec.get("recommended") or [], fname, idx, severity="recommended")
                self._check_typed_fields(item, spec.get("optional") or [], fname, idx, severity="optional")

    def _check_required(self, item: dict, required: list, fname: str, idx: int) -> None:
        for field in required:
            name = field_spec_name(field)
            type_, enum_ref = field_spec_type(field)
            if name and item.get(name) in (None, "", []):
                self.err(f"{fname}[{idx}]: missing required field '{name}'")
                continue
            self._check_one_field(item, name, type_, enum_ref, fname, idx)

    def _check_typed_fields(self, item: dict, fields: list, fname: str, idx: int, severity: str) -> None:
        for field in fields:
            name = field_spec_name(field)
            type_, enum_ref = field_spec_type(field)
            if not name or item.get(name) is None:
                continue
            self._check_one_field(item, name, type_, enum_ref, fname, idx)

    def _check_one_field(self, item: dict, name: str, type_: str, enum_ref: str | None, fname: str, idx: int) -> None:
        v = item.get(name)
        if v is None:
            return
        # Type checks (per PAX_FIELDS manifest)
        if type_ == "list" and not isinstance(v, list):
            self.err(f"{fname}[{idx}].{name}: must be a JSON array, got {type(v).__name__} ({v!r:.40s})")
            return
        if type_ == "integer" and not isinstance(v, int):
            self.err(f"{fname}[{idx}].{name}: must be an integer, got {type(v).__name__}")
            return
        if type_ == "number" and not isinstance(v, (int, float)):
            self.err(f"{fname}[{idx}].{name}: must be a number, got {type(v).__name__}")
            return
        if type_ == "text" and not isinstance(v, str):
            self.err(f"{fname}[{idx}].{name}: must be a string, got {type(v).__name__}")
            return
        # Enum membership
        if type_ == "enum" and enum_ref:
            # PAX_FIELDS manifest references enum names like UNIT_OF_ANALYSIS;
            # the SCHEMA block keys are lowercase like unit_of_analysis.
            key = enum_ref.lower()
            allowed = self.enums.get(key)
            if allowed is None:
                # Strip _VALUES, _TYPES suffixes that some entries use.
                for suffix in ("_values", "_types"):
                    if key.endswith(suffix):
                        allowed = self.enums.get(key[: -len(suffix)])
                        break
            if allowed is not None and v not in allowed:
                self.err(f"{fname}[{idx}].{name}: '{v}' not in allowed values {allowed}")

    # -------------------------------------------------------------------
    # Pass 4b: known list-typed fields whose PAX_FIELDS entry is a bare
    # string in 'required' (no type info available). Hardcoded here.
    # Catches the JELambert/pax-market#84 class of bug.
    # -------------------------------------------------------------------

    KNOWN_LIST_FIELDS = {
        "finding": ["construct_ids", "sub_domain_ids", "covariates_controlled"],
        "construct": ["aliases", "measures", "domain_ids"],
        "proposition": [],
    }

    def check_known_list_shapes(self, knowledge: dict[str, Any]) -> None:
        for fname, entity in (
            ("findings.json",   "finding"),
            ("constructs.json", "construct"),
            ("propositions.json","proposition"),
        ):
            if fname not in knowledge:
                continue
            items = normalize_to_list(knowledge[fname])
            for idx, item in enumerate(items):
                if not isinstance(item, dict):
                    continue
                for field in self.KNOWN_LIST_FIELDS.get(entity, []):
                    v = item.get(field)
                    if v is None:
                        continue
                    if isinstance(v, str):
                        self.err(f"{fname}[{idx}].{field}: must be a JSON array, got string. Convert \"a,b,c\" → [\"a\",\"b\",\"c\"].")

    # -------------------------------------------------------------------
    # Pass 5: cross-file FK references
    # -------------------------------------------------------------------

    def check_fk_refs(self, knowledge: dict[str, Any], manifest: dict | None) -> None:
        # Collect known IDs across the entity files exactly once.
        known_constructs = collect_ids(normalize_to_list(knowledge.get("constructs.json")))
        known_domains = collect_ids(normalize_to_list(knowledge.get("domain.json"))) | collect_ids(normalize_to_list(knowledge.get("domains.json")))
        known_sources = collect_ids(normalize_to_list(knowledge.get("sources.json")))
        known_canonical = collect_ids(normalize_to_list(knowledge.get("canonical_constructs.json")))
        known_propositions = collect_ids(normalize_to_list(knowledge.get("propositions.json")))

        # ---- findings → constructs / domains / sub_domains / sources ----
        findings = normalize_to_list(knowledge.get("findings.json"))
        if findings:
            mc, md, ms = set(), set(), set()
            for fnd in findings:
                if not isinstance(fnd, dict):
                    continue
                cs = fnd.get("construct_ids", [])
                if isinstance(cs, str):
                    cs = [s.strip() for s in cs.split(",") if s.strip()]
                for cid in cs:
                    if cid and cid not in known_constructs:
                        mc.add(cid)
                d = fnd.get("domain_id")
                if d and d not in known_domains:
                    md.add(d)
                for sd in (fnd.get("sub_domain_ids") or []):
                    if sd and sd not in known_domains:
                        md.add(sd)
                src = fnd.get("source_id")
                if not src and isinstance(fnd.get("source"), dict):
                    src = fnd["source"].get("id")
                if src and known_sources and src not in known_sources:
                    ms.add(src)
            if mc:
                self.err(f"findings reference {len(mc)} undefined construct_id(s): {sorted(mc)}")
            if md:
                self.err(f"findings reference {len(md)} undefined domain/sub_domain id(s): {sorted(md)}")
            if ms:
                self.err(f"findings reference {len(ms)} undefined source_id(s): {sorted(ms)}")

        # ---- propositions → constructs ----
        propositions = normalize_to_list(knowledge.get("propositions.json"))
        if propositions:
            missing = set()
            for p in propositions:
                if not isinstance(p, dict):
                    continue
                for f in ("construct_from", "construct_to"):
                    cid = p.get(f)
                    if cid and cid not in known_constructs:
                        missing.add(cid)
            if missing:
                self.err(f"propositions reference {len(missing)} undefined construct_id(s) in construct_from/construct_to: {sorted(missing)}")

        # ---- construct_relationships → constructs ----
        rels = normalize_to_list(knowledge.get("construct_relationships.json"))
        if rels:
            missing = set()
            for r in rels:
                if not isinstance(r, dict):
                    continue
                for f in ("construct_from", "construct_to", "from_construct", "to_construct"):
                    cid = r.get(f)
                    if cid and cid not in known_constructs:
                        missing.add(cid)
            if missing:
                self.err(f"construct_relationships reference {len(missing)} undefined construct_id(s): {sorted(missing)}")

        # ---- construct_relations (v3 backbone) → canonical_constructs ----
        crels = normalize_to_list(knowledge.get("construct_relations.json"))
        if crels:
            missing = set()
            for r in crels:
                if not isinstance(r, dict):
                    continue
                for f in ("from_id", "to_id"):
                    cid = r.get(f)
                    if cid and known_canonical and cid not in known_canonical:
                        missing.add(cid)
            if missing:
                self.err(f"construct_relations reference {len(missing)} undefined canonical_construct id(s): {sorted(missing)}")

        # ---- constructs.canonical_id → canonical_constructs ----
        constructs = normalize_to_list(knowledge.get("constructs.json"))
        if constructs and known_canonical:
            missing = set()
            for c in constructs:
                if not isinstance(c, dict):
                    continue
                cid = c.get("canonical_id")
                if cid and cid not in known_canonical:
                    missing.add(cid)
            if missing:
                self.err(f"constructs reference {len(missing)} undefined canonical_id(s): {sorted(missing)}")

        # ---- pax.yaml provides:* → matching knowledge entities ----
        # NOTE: provides.findings is denormalized metadata — findings don't
        # carry an id field per PAX_FIELDS, so there's nothing to FK against.
        # Only check entities that actually have ids: constructs, sources,
        # propositions.
        if isinstance(manifest, dict):
            provides = manifest.get("provides") or {}
            if isinstance(provides, dict):
                checks = (
                    ("constructs",   known_constructs,   "constructs.json"),
                    ("sources",      known_sources,      "sources.json"),
                    ("propositions", known_propositions, "propositions.json"),
                )
                for key, known_set, fname in checks:
                    declared = provides.get(key)
                    if not isinstance(declared, list):
                        continue
                    if not known_set:
                        # Entity file absent or has no ids → can't FK-check.
                        continue
                    missing = {x for x in declared if x and x not in known_set}
                    if missing:
                        self.err(f"pax.yaml provides.{key} declares {len(missing)} id(s) not present in {fname}: {sorted(missing)}")

    # -------------------------------------------------------------------
    # Pass 6: provides.datasets[] (v4)
    # -------------------------------------------------------------------

    def check_datasets(self, manifest: dict | None) -> None:
        """Issue #106 — validate provides.datasets[] entries.

        Each entry must have dataset_id/display_name/format/unit_of_analysis.
        bundled=true → file exists at parquet_relpath (default
        datasets/<dataset_id>.parquet).  bundled=false → source_url present.
        sha256, if set on a bundled file, must match the bytes.
        """
        if not isinstance(manifest, dict):
            return
        provides = manifest.get("provides") or {}
        if not isinstance(provides, dict):
            return
        datasets = provides.get("datasets")
        if datasets is None:
            return
        if not isinstance(datasets, list):
            self.err(f"pax.yaml provides.datasets must be a list, got {type(datasets).__name__}")
            return

        # PAX with datasets MUST declare schema_version 4.0+.
        sv = str(manifest.get("schema_version", ""))
        if sv and sv not in ("4.0",):
            self.err(f"pax.yaml: provides.datasets requires schema_version '4.0', got '{sv}'")

        seen_ids: set[str] = set()
        for idx, d in enumerate(datasets):
            if not isinstance(d, dict):
                self.err(f"pax.yaml provides.datasets[{idx}] must be a mapping")
                continue

            for required in ("dataset_id", "display_name", "format", "unit_of_analysis"):
                if not d.get(required):
                    self.err(f"pax.yaml provides.datasets[{idx}]: missing required field '{required}'")

            ds_id = d.get("dataset_id", "")
            if ds_id in seen_ids:
                self.err(f"pax.yaml provides.datasets: duplicate dataset_id '{ds_id}'")
            elif ds_id:
                seen_ids.add(ds_id)

            fmt = d.get("format")
            if fmt and fmt not in DATASET_FORMATS:
                self.err(f"pax.yaml provides.datasets[{idx}]: format '{fmt}' not in {DATASET_FORMATS}")

            uoa = d.get("unit_of_analysis")
            uoa_enum = self.enums.get("unit_of_analysis", [])
            if uoa and uoa_enum and uoa not in uoa_enum:
                # warning, not error — UoA may legitimately extend over time
                self.warn(f"pax.yaml provides.datasets[{idx}]: unit_of_analysis '{uoa}' not in canonical enum")

            bundled = bool(d.get("bundled"))
            relpath = d.get("parquet_relpath") or f"datasets/{ds_id}.parquet" if ds_id else None

            if bundled:
                if not relpath:
                    continue
                full = self.pack_dir / relpath
                if not full.exists():
                    self.err(
                        f"pax.yaml provides.datasets[{idx}]: bundled=true but file not found at {relpath}"
                    )
                    continue
                expected_sha = d.get("sha256")
                if expected_sha:
                    import hashlib
                    actual = hashlib.sha256(full.read_bytes()).hexdigest()
                    if actual != expected_sha:
                        self.err(
                            f"pax.yaml provides.datasets[{idx}]: sha256 mismatch — manifest={expected_sha[:12]}..., file={actual[:12]}..."
                        )
            else:
                if not d.get("source_url"):
                    self.err(
                        f"pax.yaml provides.datasets[{idx}]: bundled=false requires non-empty source_url"
                    )

    # -------------------------------------------------------------------
    # Driver
    # -------------------------------------------------------------------

    def run(self) -> bool:
        self.check_files()
        manifest = self.check_manifest()
        knowledge = self.check_knowledge_json()
        self.check_entity_fields(knowledge)
        self.check_known_list_shapes(knowledge)
        self.check_fk_refs(knowledge, manifest)
        self.check_datasets(manifest)
        return not self.errors


# Fallback for pax.yaml required fields if the FIELDS manifest can't be parsed.
REQUIRED_PAX_YAML_FIELDS = ("name", "version", "description", "schema_version", "pax_type")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a PAX directory against the canonical guide.")
    parser.add_argument("pack_dir", type=Path, help="Path to a pax/<name>/ directory")
    parser.add_argument("--guide", type=Path, default=DEFAULT_GUIDE,
                        help="Path to PAX_CREATION_GUIDE.md (default: docs/PAX_CREATION_GUIDE.md)")
    parser.add_argument("--json", action="store_true",
                        help="Emit machine-readable JSON to stdout (used by CI to build PR comments).")
    args = parser.parse_args()

    pack_dir = args.pack_dir
    if not pack_dir.is_dir():
        print(f"ERROR: not a directory: {pack_dir}", file=sys.stderr)
        return 2

    guide_path = args.guide
    if not guide_path.is_file():
        print(f"ERROR: guide not found: {guide_path}", file=sys.stderr)
        return 2

    guide_text = guide_path.read_text()
    try:
        enums = parse_schema_block(guide_text)
    except RuntimeError as e:
        print(f"ERROR parsing guide PAX_SCHEMA: {e}", file=sys.stderr)
        return 2
    try:
        fields = parse_fields_block(guide_text)
    except RuntimeError as e:
        print(f"ERROR parsing guide PAX_FIELDS: {e}", file=sys.stderr)
        return 2

    validator = Validator(pack_dir, enums, fields)
    ok = validator.run()

    if args.json:
        # Machine-readable mode: single-line JSON to stdout, human messages
        # go to stderr so they don't pollute the parse.
        out = {
            "pack": pack_dir.name,
            "ok": ok,
            "errors": validator.errors,
            "warnings": validator.warnings,
        }
        print(json.dumps(out))
        return 0 if ok else 1

    if validator.warnings:
        print(f"\n⚠ {pack_dir.name}: warnings:")
        for w in validator.warnings:
            print(f"  - {w}")
    if validator.errors:
        print(f"\n✗ {pack_dir.name}: {len(validator.errors)} error(s):")
        for e in validator.errors:
            print(f"  - {e}")
        return 1
    print(f"\n✓ {pack_dir.name}: all checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())

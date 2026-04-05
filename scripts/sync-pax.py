#!/usr/bin/env python3
"""
sync-pax.py — Read PAX directories from the praxis repo and generate:
  1. Hugo content pages (content/packs/<name>/index.md)
  2. .pax.tar.gz archives (static/packs/<name>.pax.tar.gz)
  3. Registry JSON (data/registry.json) — enriched with full knowledge details
  4. Construct index (data/constructs.json) — cross-pack construct map

Usage:
  python scripts/sync-pax.py [--praxis-dir /path/to/praxis]

Defaults to ../praxis relative to the marketplace repo root.
"""

import argparse
from collections import defaultdict
import hashlib
import json
import re
import sys
import tarfile
from pathlib import Path

import yaml


SKIP_DIRS = {"roundtrip-pax", "roundtrip-constructs", "import-basic", "import-with-install"}

MARKETPLACE_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = MARKETPLACE_ROOT / "content" / "packs"
STATIC_DIR = MARKETPLACE_ROOT / "static" / "packs"
DATA_DIR = MARKETPLACE_ROOT / "data"

REGISTRY_SCHEMA_VERSION = "2.0"


# ---------------------------------------------------------------------------
# Utility
# ---------------------------------------------------------------------------

def load_json(path: Path):
    """Load a JSON file, returning [] if missing or invalid."""
    if not path.exists():
        return []
    try:
        with open(path) as f:
            data = json.load(f)
        if isinstance(data, dict):
            return [data]
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, Exception):
        return []


def load_yaml(path: Path):
    """Load a YAML file, returning {} if missing."""
    if not path.exists():
        return {}
    try:
        with open(path) as f:
            return yaml.safe_load(f) or {}
    except Exception:
        return {}


def has_directory(pax_dir: Path, name: str) -> bool:
    d = pax_dir / name
    if not d.is_dir():
        return False
    return any(f for f in d.rglob("*") if f.is_file() and not f.name.startswith("."))


def read_readme(pax_dir: Path) -> str:
    readme = pax_dir / "README.md"
    if readme.exists():
        return readme.read_text().strip()
    return ""


def format_size(size_bytes: int) -> str:
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    else:
        return f"{size_bytes / (1024 * 1024):.1f} MB"


def shorten_authors(author: str) -> str:
    parts = [a.strip() for a in re.split(r';| and ', author) if a.strip()]
    if not parts:
        return author

    def surname(a):
        if "," in a:
            return a.split(",")[0].strip()
        tokens = a.split()
        return tokens[-1] if tokens else a

    surnames = [surname(p) for p in parts]
    if len(surnames) == 1:
        return surnames[0]
    elif len(surnames) == 2:
        return f"{surnames[0]} & {surnames[1]}"
    return f"{surnames[0]} et al."


# ---------------------------------------------------------------------------
# Knowledge extraction — the enrichment layer
# ---------------------------------------------------------------------------

def extract_domain(pax_dir: Path) -> dict | None:
    """Extract domain metadata from domain.json."""
    domains = load_json(pax_dir / "knowledge" / "domain.json")
    if not domains:
        return None
    d = domains[0]
    return {
        "id": d.get("id", ""),
        "display_name": d.get("display_name", ""),
        "description": d.get("description", ""),
        "research_questions": d.get("research_questions", []),
        "temporal_scope": d.get("temporal_scope", ""),
        "population": d.get("population", ""),
        "level_of_analysis": d.get("level_of_analysis", ""),
    }


def extract_constructs_detail(pax_dir: Path) -> list[dict]:
    """Extract full construct definitions with aliases."""
    constructs = load_json(pax_dir / "knowledge" / "constructs.json")
    result = []
    for c in constructs:
        aliases_raw = c.get("aliases", [])
        aliases = [a["alias"] if isinstance(a, dict) else str(a) for a in aliases_raw]
        result.append({
            "id": c.get("id", ""),
            "display_name": c.get("display_name", c.get("id", "")),
            "definition": c.get("definition", ""),
            "aliases": aliases,
            "construct_type": c.get("construct_type", ""),
        })
    return result


def extract_findings_detail(pax_dir: Path) -> list[dict]:
    """Extract full findings with text, direction, effect size, method."""
    findings = load_json(pax_dir / "knowledge" / "findings.json")
    result = []
    for f in findings:
        result.append({
            "finding_text": f.get("finding_text", ""),
            "construct_ids": f.get("construct_ids", []),
            "direction": f.get("direction", ""),
            "effect_size": f.get("effect_size", ""),
            "confidence": f.get("confidence", ""),
            "method_used": f.get("method_used", ""),
            "finding_type": f.get("finding_type", ""),
            "evidence_type": f.get("evidence_type", ""),
        })
    return result


def extract_propositions_detail(pax_dir: Path) -> list[dict]:
    """Extract propositions with text and direction."""
    props = load_json(pax_dir / "knowledge" / "propositions.json")
    result = []
    for p in props:
        result.append({
            "id": p.get("id", ""),
            "proposition_text": p.get("proposition_text", ""),
            "construct_from": p.get("construct_from", ""),
            "construct_to": p.get("construct_to", ""),
            "direction": p.get("direction", ""),
            "scope_conditions": p.get("scope_conditions", ""),
        })
    return result


def extract_sources_detail(pax_dir: Path) -> list[dict]:
    """Extract source/bibliographic metadata."""
    # Sources can be in sources.json or embedded in findings
    sources = load_json(pax_dir / "knowledge" / "sources.json")
    if sources:
        result = []
        for s in sources:
            result.append({
                "id": s.get("id", ""),
                "title": s.get("title", ""),
                "authors": s.get("authors", ""),
                "year": s.get("year"),
                "doi": s.get("doi"),
                "source_type": s.get("source_type", ""),
            })
        return result

    # Fall back: extract unique sources from findings
    findings = load_json(pax_dir / "knowledge" / "findings.json")
    seen = set()
    result = []
    for f in findings:
        src = f.get("source", {})
        if isinstance(src, dict) and src.get("id") and src["id"] not in seen:
            seen.add(src["id"])
            result.append({
                "id": src.get("id", ""),
                "title": src.get("title", ""),
                "authors": src.get("authors", ""),
                "year": src.get("year"),
                "doi": src.get("doi"),
                "source_type": src.get("source_type", ""),
            })
    return result


def extract_playbooks_detail(pax_dir: Path) -> list[dict]:
    """Extract playbook summaries with step counts and engines."""
    pb_dir = pax_dir / "playbooks"
    if not pb_dir.is_dir():
        return []
    result = []
    for pb_file in sorted(pb_dir.glob("*.yaml")):
        pb = load_yaml(pb_file)
        if not pb:
            continue
        steps = pb.get("steps", [])
        engines_used = list({
            s.get("engine") for s in steps
            if isinstance(s, dict) and s.get("engine")
        })
        result.append({
            "id": pb.get("id", pb_file.stem),
            "display_name": pb.get("display_name", pb_file.stem),
            "description": pb.get("description", ""),
            "estimated_runtime": pb.get("estimated_runtime", ""),
            "step_count": len(steps),
            "engines_used": engines_used,
        })
    return result


# ---------------------------------------------------------------------------
# Title derivation (unchanged)
# ---------------------------------------------------------------------------

def derive_title(manifest: dict) -> str:
    name = manifest.get("name", "")
    desc = manifest.get("description", "")
    pax_type = manifest.get("pax_type", "topic")
    author = manifest.get("author", "")

    if pax_type == "paper" and author:
        year_match = re.search(r'(\d{4})', name)
        year = f" ({year_match.group(1)})" if year_match else ""
        short_author = shorten_authors(author)
        quoted = re.search(r'"([^"]+)"', desc)
        if quoted:
            return f"{short_author}{year} — {quoted.group(1)}"
        first_sentence = desc.split(".")[0].strip()
        if len(first_sentence) < 60:
            return f"{short_author}{year} — {first_sentence}"
        return f"{short_author}{year}"

    for sep in ["—", "–", " - "]:
        if sep in desc:
            prefix = desc.split(sep)[0].strip()
            if len(prefix) < 80:
                return prefix
            break

    return name.replace("-", " ").replace("_", " ").title()


# ---------------------------------------------------------------------------
# Body generation for packs without README
# ---------------------------------------------------------------------------

def generate_body(manifest: dict, pax_dir: Path) -> str:
    knowledge_dir = pax_dir / "knowledge"
    sections = []

    domains = load_json(knowledge_dir / "domain.json")
    if domains:
        d = domains[0]
        parts = [f"**Domain:** {d.get('display_name', d.get('id', ''))}"]
        if d.get("description"):
            parts.append(f"\n{d['description']}")
        meta = []
        if d.get("temporal_scope"):
            meta.append(f"**Temporal scope:** {d['temporal_scope']}")
        if d.get("population"):
            meta.append(f"**Population:** {d['population']}")
        if meta:
            parts.append("\n" + " | ".join(meta))
        sections.append("\n".join(parts))

    findings = load_json(knowledge_dir / "findings.json")
    if findings:
        lines = ["## Key Findings", ""]
        for f in findings[:8]:
            text = f.get("finding_text", "")
            direction = f.get("direction", "")
            confidence = f.get("confidence", "")
            if text:
                meta_parts = [p for p in [direction, confidence] if p]
                suffix = f" *({', '.join(meta_parts)})*" if meta_parts else ""
                lines.append(f"- {text}{suffix}")
        if len(findings) > 8:
            lines.append(f"\n*...and {len(findings) - 8} more findings*")
        sections.append("\n".join(lines))

    propositions = load_json(knowledge_dir / "propositions.json")
    if propositions:
        lines = ["## Theoretical Propositions", ""]
        for p in propositions:
            text = p.get("proposition_text", "")
            direction = p.get("direction", "")
            if text:
                arrow = {"positive": "+", "negative": "−", "null": "∅"}.get(direction, "→")
                lines.append(f"- [{arrow}] {text}")
        sections.append("\n".join(lines))

    sources = load_json(knowledge_dir / "sources.json")
    if sources:
        lines = ["## Sources", ""]
        for s in sources[:5]:
            title = s.get("title", "")
            authors = s.get("authors", "")
            year = s.get("year", "")
            doi = s.get("doi", "")
            if title:
                cite = f"- {authors} ({year}). *{title}*." if authors and year else f"- *{title}*"
                if doi:
                    cite += f" DOI: {doi}"
                lines.append(cite)
        sections.append("\n".join(lines))

    return "\n\n".join(sections)


# ---------------------------------------------------------------------------
# Archive creation
# ---------------------------------------------------------------------------

def create_archive(pax_dir: Path, output_path: Path) -> tuple[str, int]:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with tarfile.open(output_path, "w:gz") as tar:
        for item in sorted(pax_dir.rglob("*")):
            if item.is_file():
                arcname = str(item.relative_to(pax_dir))
                if "__pycache__" in arcname or arcname.startswith("."):
                    continue
                tar.add(item, arcname=arcname)
    sha256 = hashlib.sha256(output_path.read_bytes()).hexdigest()
    size = output_path.stat().st_size
    return sha256, size


# ---------------------------------------------------------------------------
# Front matter builder (enriched)
# ---------------------------------------------------------------------------

def build_front_matter(manifest: dict, pax_dir: Path, archive_size: str = "") -> dict:
    provides = manifest.get("provides", {})
    constructs_ids = provides.get("constructs", [])
    findings_ids = provides.get("findings", [])
    engines_ids = provides.get("engines", [])
    playbook_ids = provides.get("playbooks", [])
    proposition_ids = provides.get("propositions", [])

    knowledge_dir = pax_dir / "knowledge"

    # Extract rich detail from knowledge files
    constructs_detail = extract_constructs_detail(pax_dir)
    findings_detail = extract_findings_detail(pax_dir)
    propositions_detail = extract_propositions_detail(pax_dir)
    sources_detail = extract_sources_detail(pax_dir)
    playbooks_detail = extract_playbooks_detail(pax_dir)
    domain = extract_domain(pax_dir)

    # Counts
    construct_count = len(constructs_detail) or len(constructs_ids)
    finding_count = len(findings_detail) or len(findings_ids)
    proposition_count = len(propositions_detail) or len(proposition_ids)

    # ID lists (backward compat) — prefer detail-derived
    constructs = [c["id"] for c in constructs_detail] if constructs_detail else constructs_ids
    findings = [f.get("finding_text", "")[:60] for f in findings_detail] if findings_detail else findings_ids

    # Engine names from registry file or provides
    engine_names = engines_ids[:]
    if not engine_names:
        engine_reg = pax_dir / "engines" / "registry.json"
        if engine_reg.exists():
            eng_data = load_json(engine_reg)
            engine_names = [e.get("id", e.get("name", "")) for e in eng_data if isinstance(e, dict)]

    # Playbook names
    playbook_names = [p["id"] for p in playbooks_detail] if playbooks_detail else playbook_ids

    has_playbooks = bool(playbook_names)
    has_data = has_directory(pax_dir, "data")
    name = manifest.get("name", pax_dir.name)
    created = manifest.get("created", "")

    fm = {
        "title": derive_title(manifest),
        "pax_name": name,
        "version": str(manifest.get("version", "0.0.0")),
        "pax_type": manifest.get("pax_type", "topic"),
        "description": manifest.get("description", ""),
        "author": manifest.get("author", ""),
        "created": str(created) if created else "",
        "license": manifest.get("license", ""),
        "tags": manifest.get("tags", []),
        # ID lists (backward compat)
        "constructs": constructs,
        "engines": engine_names,
        "playbook_names": playbook_names,
        # Counts
        "construct_count": construct_count,
        "finding_count": finding_count,
        "proposition_count": proposition_count,
        "has_playbooks": has_playbooks,
        "has_data_sources": has_data,
        # Rich detail
        "domain": domain,
        "constructs_detail": constructs_detail,
        "findings_detail": findings_detail,
        "propositions_detail": propositions_detail,
        "sources_detail": sources_detail,
        "playbooks_detail": playbooks_detail,
        # Download
        "download_url": f"/packs/{name}.pax.tar.gz",
        "download_size": archive_size,
    }

    # Sort weight
    year = 0
    if created:
        year_match = re.search(r'(\d{4})', str(created))
        if year_match:
            year = int(year_match.group(1))
    fm["weight"] = 10000 - year

    return fm


# ---------------------------------------------------------------------------
# Construct index — cross-pack discovery
# ---------------------------------------------------------------------------

def build_construct_index(all_packs: list[dict]) -> dict:
    """Build a construct-centric index mapping constructs to packs and findings."""
    index = {}

    for pack in all_packs:
        pack_name = pack["pax_name"]

        # Build a lookup of findings by construct for this pack
        construct_findings = defaultdict(list)
        for f in pack.get("findings_detail", []):
            for cid in f.get("construct_ids", []):
                construct_findings[cid].append(f.get("direction", ""))

        for c in pack.get("constructs_detail", []):
            cid = c["id"]
            if cid not in index:
                index[cid] = {
                    "id": cid,
                    "display_name": c.get("display_name", cid),
                    "definition": c.get("definition", ""),
                    "aliases": c.get("aliases", []),
                    "packs": [],
                }
            # Prefer the longest definition
            if len(c.get("definition", "")) > len(index[cid]["definition"]):
                index[cid]["definition"] = c["definition"]
                index[cid]["display_name"] = c.get("display_name", cid)
            # Merge aliases
            existing = set(index[cid]["aliases"])
            for a in c.get("aliases", []):
                if a not in existing:
                    index[cid]["aliases"].append(a)
                    existing.add(a)

            # Determine primary direction from findings
            directions = construct_findings.get(cid, [])
            primary_direction = ""
            if directions:
                from collections import Counter
                counts = Counter(d for d in directions if d)
                if counts:
                    primary_direction = counts.most_common(1)[0][0]

            index[cid]["packs"].append({
                "pack": pack_name,
                "pack_title": pack["title"],
                "direction": primary_direction,
                "finding_count": len(construct_findings.get(cid, [])),
            })

    # Add pack_count and sort by it
    for cid in index:
        index[cid]["pack_count"] = len(index[cid]["packs"])

    return index


def compute_related_packs(all_packs: list[dict], construct_index: dict) -> dict[str, list[str]]:
    """Compute related packs for each pack based on shared constructs."""
    # Build construct → pack set for weighting
    construct_pack_count = {cid: len(c["packs"]) for cid, c in construct_index.items()}

    related = {}
    for pack in all_packs:
        name = pack["pax_name"]
        pack_constructs = set(pack.get("constructs", []))
        if not pack_constructs:
            related[name] = []
            continue

        scores = defaultdict(float)
        for other in all_packs:
            other_name = other["pax_name"]
            if other_name == name:
                continue
            other_constructs = set(other.get("constructs", []))
            shared = pack_constructs & other_constructs
            if not shared:
                continue
            # Weight: constructs shared by fewer packs are more meaningful
            score = sum(1.0 / construct_pack_count.get(c, 1) for c in shared)
            scores[other_name] = score

        # Top 3 related
        top = sorted(scores, key=scores.get, reverse=True)[:3]
        related[name] = top

    return related


# ---------------------------------------------------------------------------
# Content page writer
# ---------------------------------------------------------------------------

def write_content_page(fm: dict, body: str, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "index.md"
    lines = ["---"]
    lines.append(yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False).strip())
    lines.append("---")
    lines.append("")
    if body:
        lines.append(body)
        lines.append("")
    output_file.write_text("\n".join(lines))


# ---------------------------------------------------------------------------
# Main sync
# ---------------------------------------------------------------------------

def sync_packs(praxis_dir: Path):
    pax_root = praxis_dir / "pax"
    if not pax_root.is_dir():
        print(f"Error: PAX directory not found at {pax_root}")
        sys.exit(1)

    all_packs = []  # Collect all front matter for cross-pack analysis

    for pax_dir in sorted(pax_root.iterdir()):
        if not pax_dir.is_dir() or pax_dir.name in SKIP_DIRS:
            continue

        manifest_path = pax_dir / "pax.yaml"
        if not manifest_path.exists():
            print(f"  Skipping {pax_dir.name}: no pax.yaml")
            continue

        print(f"  Processing {pax_dir.name}...")

        with open(manifest_path) as f:
            manifest = yaml.safe_load(f)

        archive_path = STATIC_DIR / f"{pax_dir.name}.pax.tar.gz"
        sha256, size_bytes = create_archive(pax_dir, archive_path)
        archive_size = format_size(size_bytes)
        print(f"    Archive: {archive_size}")

        fm = build_front_matter(manifest, pax_dir, archive_size)
        fm["_sha256"] = sha256  # Temp field for registry

        # Count detail items
        detail_counts = []
        if fm["constructs_detail"]:
            detail_counts.append(f"{len(fm['constructs_detail'])} constructs")
        if fm["findings_detail"]:
            detail_counts.append(f"{len(fm['findings_detail'])} findings")
        if fm["propositions_detail"]:
            detail_counts.append(f"{len(fm['propositions_detail'])} propositions")
        if fm["playbooks_detail"]:
            detail_counts.append(f"{len(fm['playbooks_detail'])} playbooks")
        if fm["sources_detail"]:
            detail_counts.append(f"{len(fm['sources_detail'])} sources")
        if detail_counts:
            print(f"    Detail: {', '.join(detail_counts)}")

        all_packs.append(fm)

    # Cross-pack analysis
    print("\n  Computing cross-pack relationships...")
    construct_index = build_construct_index(all_packs)
    print(f"    Construct index: {len(construct_index)} unique constructs across {len(all_packs)} packs")

    related_map = compute_related_packs(all_packs, construct_index)

    # Write content pages and build registry
    registry = []
    for fm in all_packs:
        name = fm["pax_name"]
        sha256 = fm.pop("_sha256")

        # Add related packs
        fm["related_packs"] = related_map.get(name, [])

        # Read README or auto-generate body
        pax_dir = pax_root / name
        body = read_readme(pax_dir)
        if not body:
            body = generate_body({}, pax_dir)

        write_content_page(fm, body, CONTENT_DIR / name)

        # Registry entry (includes detail fields)
        entry = {
            "name": name,
            "title": fm["title"],
            "version": fm["version"],
            "pax_type": fm["pax_type"],
            "description": fm["description"],
            "author": fm["author"],
            "license": fm["license"],
            "tags": fm["tags"],
            "schema_version": REGISTRY_SCHEMA_VERSION,
            # Counts (backward compat)
            "constructs": fm["constructs"],
            "construct_count": fm["construct_count"],
            "finding_count": fm["finding_count"],
            "proposition_count": fm["proposition_count"],
            "has_playbooks": fm["has_playbooks"],
            "has_data_sources": fm["has_data_sources"],
            "engines": fm["engines"],
            "playbooks": fm["playbook_names"],
            # Rich detail
            "domain": fm["domain"],
            "constructs_detail": fm["constructs_detail"],
            "findings_detail": fm["findings_detail"],
            "propositions_detail": fm["propositions_detail"],
            "sources_detail": fm["sources_detail"],
            "playbooks_detail": fm["playbooks_detail"],
            "related_packs": fm["related_packs"],
            # Download
            "download_url": fm["download_url"],
            "download_sha256": sha256,
            "download_size": fm["download_size"],
        }
        registry.append(entry)

    # Write outputs
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    registry_path = DATA_DIR / "registry.json"
    with open(registry_path, "w") as f:
        json.dump(registry, f, indent=2)
    print(f"\n  Registry: {len(registry)} packs ({registry_path.stat().st_size / 1024:.1f} KB)")

    constructs_path = DATA_DIR / "constructs.json"
    with open(constructs_path, "w") as f:
        json.dump(construct_index, f, indent=2)
    print(f"  Constructs: {len(construct_index)} unique constructs ({constructs_path.stat().st_size / 1024:.1f} KB)")


def main():
    parser = argparse.ArgumentParser(description="Sync PAX packs to marketplace")
    parser.add_argument(
        "--praxis-dir",
        type=Path,
        default=MARKETPLACE_ROOT.parent / "praxis",
        help="Path to the praxis repository root",
    )
    args = parser.parse_args()
    print(f"Syncing PAX packs from {args.praxis_dir}...")
    sync_packs(args.praxis_dir)
    print("Done!")


if __name__ == "__main__":
    main()

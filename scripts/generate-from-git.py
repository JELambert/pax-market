#!/usr/bin/env python3
"""
generate-from-git.py — Generate marketplace content from pack directories in the repo.

Reads packs/*/pax.yaml + knowledge/*.json (committed to git) and generates:
  1. Hugo content pages (content/packs/<name>/index.md)
  2. Registry JSON (data/registry.json) — thin install contract
  3. Construct index (data/constructs.json) — cross-pack construct map
  4. .pax.tar.gz archives (static/packs/<name>.pax.tar.gz)

NO database dependency. Everything comes from the git repo.

Usage:
  python scripts/generate-from-git.py
"""

import hashlib
import json
import re
import sys
import tarfile
from collections import Counter, defaultdict
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
PACKS_DIR = REPO_ROOT / "packs"
CONTENT_DIR = REPO_ROOT / "content" / "packs"
STATIC_DIR = REPO_ROOT / "static" / "packs"
DATA_DIR = REPO_ROOT / "data"

MARKETPLACE_BASE_URL = "https://pax-market.com"
REGISTRY_SCHEMA_VERSION = "1.0"

ACRONYMS = {"ml", "ai", "gdp", "nlp", "rfm", "ols", "ucdp", "stem", "api", "sql", "csv"}


# ---------------------------------------------------------------------------
# File helpers
# ---------------------------------------------------------------------------

def load_json(path: Path) -> list:
    if not path.exists():
        return []
    try:
        with open(path) as f:
            data = json.load(f)
        return data if isinstance(data, list) else [data] if isinstance(data, dict) else []
    except Exception:
        return []


def load_yaml_file(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        with open(path) as f:
            return yaml.safe_load(f) or {}
    except Exception:
        return {}


def fix_acronyms(title: str) -> str:
    return " ".join(w.upper() if w.lower() in ACRONYMS else w for w in title.split())


def shorten_authors(author: str) -> str:
    parts = [a.strip() for a in re.split(r';| and ', author) if a.strip()]
    if not parts:
        return author
    def surname(a):
        return a.split(",")[0].strip() if "," in a else (a.split()[-1] if a.split() else a)
    surnames = [surname(p) for p in parts]
    if len(surnames) == 1:
        return surnames[0]
    elif len(surnames) == 2:
        return f"{surnames[0]} & {surnames[1]}"
    return f"{surnames[0]} et al."


def derive_title(name: str, desc: str, pax_type: str, author: str) -> str:
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
    return fix_acronyms(name.replace("-", " ").replace("_", " ").title())


def format_size(size_bytes: int) -> str:
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    return f"{size_bytes / (1024 * 1024):.1f} MB"


# ---------------------------------------------------------------------------
# Pack processing
# ---------------------------------------------------------------------------

def process_pack(pack_dir: Path) -> dict | None:
    """Process a single pack directory into marketplace content."""
    manifest = load_yaml_file(pack_dir / "pax.yaml")
    if not manifest.get("name"):
        return None

    name = manifest["name"]
    desc = manifest.get("description", "")
    pax_type = manifest.get("pax_type", "topic")
    author = manifest.get("author", "")
    version = str(manifest.get("version", "1.0.0"))
    provides = manifest.get("provides", {})

    knowledge_dir = pack_dir / "knowledge"

    # Extract knowledge from files
    constructs = load_json(knowledge_dir / "constructs.json")
    findings = load_json(knowledge_dir / "findings.json")
    propositions = load_json(knowledge_dir / "propositions.json")
    sources = load_json(knowledge_dir / "sources.json")
    domain_data = load_json(knowledge_dir / "domain.json")

    # Construct details
    constructs_detail = []
    for c in constructs:
        aliases_raw = c.get("aliases", [])
        aliases = [a["alias"] if isinstance(a, dict) else str(a) for a in aliases_raw]
        constructs_detail.append({
            "id": c.get("id", ""),
            "display_name": c.get("display_name", c.get("id", "")),
            "definition": c.get("definition", ""),
            "aliases": aliases,
            "construct_type": c.get("construct_type", ""),
        })

    # Finding details
    findings_detail = []
    for f in findings:
        cids = f.get("construct_ids", [])
        if isinstance(cids, str):
            cids = [x.strip() for x in cids.split(",") if x.strip()]
        findings_detail.append({
            "finding_text": f.get("finding_text", ""),
            "construct_ids": cids,
            "direction": f.get("direction", ""),
            "effect_size": f.get("effect_size", ""),
            "confidence": f.get("confidence", ""),
            "method_used": f.get("method_used", ""),
        })

    # Proposition details
    propositions_detail = [
        {
            "id": p.get("id", ""),
            "proposition_text": p.get("proposition_text", ""),
            "construct_from": p.get("construct_from", ""),
            "construct_to": p.get("construct_to", ""),
            "direction": p.get("direction", ""),
        }
        for p in propositions
    ]

    # Source details (from sources.json or embedded in findings)
    sources_detail = []
    seen_sources = set()
    for s in sources:
        sid = s.get("id", "")
        if sid not in seen_sources:
            seen_sources.add(sid)
            sources_detail.append({
                "id": sid, "title": s.get("title", ""),
                "authors": s.get("authors", ""), "year": s.get("year"),
                "doi": s.get("doi"), "source_type": s.get("source_type", ""),
            })
    # Also extract from findings if sources.json is empty
    if not sources_detail:
        for f in findings:
            src = f.get("source", {})
            if isinstance(src, dict) and src.get("id") and src["id"] not in seen_sources:
                seen_sources.add(src["id"])
                sources_detail.append({
                    "id": src.get("id", ""), "title": src.get("title", ""),
                    "authors": src.get("authors", ""), "year": src.get("year"),
                    "doi": src.get("doi"), "source_type": src.get("source_type", ""),
                })

    # Domain
    domain = None
    if domain_data:
        d = domain_data[0]
        domain = {
            "id": d.get("id", ""),
            "display_name": d.get("display_name", ""),
            "description": d.get("description", ""),
            "research_questions": d.get("research_questions", []),
            "temporal_scope": d.get("temporal_scope", ""),
            "population": d.get("population", ""),
            "level_of_analysis": d.get("level_of_analysis", ""),
        }

    # Playbooks from disk
    playbooks_detail = []
    pb_dir = pack_dir / "playbooks"
    if pb_dir.is_dir():
        for pb_file in sorted(pb_dir.glob("*.yaml")):
            pb = load_yaml_file(pb_file)
            if not pb:
                continue
            steps = pb.get("steps", [])
            engines_used = list({s.get("engine") for s in steps if isinstance(s, dict) and s.get("engine")})
            playbooks_detail.append({
                "id": pb.get("id", pb_file.stem),
                "display_name": pb.get("display_name", pb_file.stem.replace("_", " ").title()),
                "description": pb.get("description", ""),
                "estimated_runtime": pb.get("estimated_runtime", ""),
                "step_count": len(steps),
                "engines_used": engines_used,
            })

    # Engines
    engine_names = provides.get("engines", [])
    if not engine_names:
        eng_reg = pack_dir / "engines" / "registry.json"
        if eng_reg.exists():
            eng_data = load_json(eng_reg)
            engine_names = [e.get("id", "") for e in eng_data if isinstance(e, dict)]

    # IDs
    construct_ids = [c["id"] for c in constructs_detail] or provides.get("constructs", [])
    playbook_names = [p["id"] for p in playbooks_detail] or provides.get("playbooks", [])

    # Tags
    tags = manifest.get("tags", [])
    if not tags:
        tags = [pax_type]

    # Archive
    STATIC_DIR.mkdir(parents=True, exist_ok=True)
    archive_path = STATIC_DIR / f"{name}.pax.tar.gz"
    with tarfile.open(archive_path, "w:gz") as tar:
        for item in sorted(pack_dir.rglob("*")):
            if item.is_file():
                arcname = str(item.relative_to(pack_dir))
                if "__pycache__" in arcname or arcname.startswith("."):
                    continue
                tar.add(item, arcname=arcname)
    sha256 = hashlib.sha256(archive_path.read_bytes()).hexdigest()
    archive_size = format_size(archive_path.stat().st_size)

    title = derive_title(name, desc, pax_type, author)

    return {
        "name": name,
        "title": title,
        "version": version,
        "pax_type": pax_type,
        "description": desc,
        "author": author,
        "created": manifest.get("created", ""),
        "license": manifest.get("license", ""),
        "tags": tags,
        "constructs": construct_ids,
        "engines": engine_names,
        "playbook_names": playbook_names,
        "construct_count": len(constructs_detail) or len(construct_ids),
        "finding_count": len(findings_detail),
        "proposition_count": len(propositions_detail),
        "has_playbooks": bool(playbooks_detail or playbook_names),
        "has_data_sources": (pack_dir / "data").is_dir(),
        "domain": domain,
        "constructs_detail": constructs_detail,
        "findings_detail": findings_detail,
        "propositions_detail": propositions_detail,
        "sources_detail": sources_detail,
        "playbooks_detail": playbooks_detail,
        "download_url": f"{MARKETPLACE_BASE_URL}/packs/{name}.pax.tar.gz",
        "download_sha256": sha256,
        "download_size": archive_size,
        "published_by": "Praxis Agent",
    }


# ---------------------------------------------------------------------------
# Cross-pack analysis
# ---------------------------------------------------------------------------

def build_construct_index(all_packs: list[dict]) -> dict:
    index = {}
    for pack in all_packs:
        pack_name = pack["name"]
        construct_findings = defaultdict(list)
        for f in pack.get("findings_detail", []):
            for cid in f.get("construct_ids", []):
                construct_findings[cid].append(f.get("direction", ""))

        for c in pack.get("constructs_detail", []):
            cid = c["id"]
            if cid not in index:
                index[cid] = {"id": cid, "display_name": c.get("display_name", cid),
                              "definition": c.get("definition", ""), "aliases": c.get("aliases", []),
                              "packs": []}
            if len(c.get("definition", "")) > len(index[cid]["definition"]):
                index[cid]["definition"] = c["definition"]
                index[cid]["display_name"] = c.get("display_name", cid)
            existing = set(index[cid]["aliases"])
            for a in c.get("aliases", []):
                if a not in existing:
                    index[cid]["aliases"].append(a)
                    existing.add(a)
            directions = construct_findings.get(cid, [])
            primary = ""
            if directions:
                counts = Counter(d for d in directions if d)
                if counts:
                    primary = counts.most_common(1)[0][0]
            index[cid]["packs"].append({"pack": pack_name, "pack_title": pack["title"],
                                        "direction": primary,
                                        "finding_count": len(construct_findings.get(cid, []))})
    for cid in index:
        index[cid]["pack_count"] = len(index[cid]["packs"])
    return index


def compute_related_packs(all_packs: list[dict], construct_index: dict) -> dict[str, list[str]]:
    construct_pack_count = {cid: len(c["packs"]) for cid, c in construct_index.items()}
    related = {}
    for pack in all_packs:
        name = pack["name"]
        pc = set(pack.get("constructs", []))
        if not pc:
            related[name] = []
            continue
        scores = defaultdict(float)
        for other in all_packs:
            if other["name"] == name:
                continue
            shared = pc & set(other.get("constructs", []))
            if shared:
                scores[other["name"]] = sum(1.0 / construct_pack_count.get(c, 1) for c in shared)
        related[name] = sorted(scores, key=scores.get, reverse=True)[:3]
    return related


# ---------------------------------------------------------------------------
# Hugo content generation
# ---------------------------------------------------------------------------

def generate_body(pack: dict) -> str:
    sections = []
    domain = pack.get("domain")
    if domain and domain.get("display_name"):
        parts = [f"**Domain:** {domain['display_name']}"]
        if domain.get("description"):
            parts.append(f"\n{domain['description']}")
        meta = []
        if domain.get("temporal_scope"):
            meta.append(f"**Temporal scope:** {domain['temporal_scope']}")
        if domain.get("population"):
            meta.append(f"**Population:** {domain['population']}")
        if meta:
            parts.append("\n" + " | ".join(meta))
        sections.append("\n".join(parts))

    findings = pack.get("findings_detail", [])
    if findings:
        lines = ["## Key Findings", ""]
        for f in findings[:8]:
            text = f.get("finding_text", "")
            if text:
                meta_parts = [p for p in [f.get("direction"), f.get("confidence")] if p]
                suffix = f" *({', '.join(meta_parts)})*" if meta_parts else ""
                lines.append(f"- {text}{suffix}")
        if len(findings) > 8:
            lines.append(f"\n*...and {len(findings) - 8} more findings*")
        sections.append("\n".join(lines))

    props = pack.get("propositions_detail", [])
    if props:
        lines = ["## Theoretical Propositions", ""]
        for p in props:
            text = p.get("proposition_text", "")
            if text:
                arrow = {"positive": "+", "negative": "−", "null": "∅"}.get(p.get("direction", ""), "→")
                lines.append(f"- [{arrow}] {text}")
        sections.append("\n".join(lines))

    return "\n\n".join(sections)


def write_content_page(pack: dict, body: str):
    out_dir = CONTENT_DIR / pack["name"]
    out_dir.mkdir(parents=True, exist_ok=True)

    # Sort weight
    year = 0
    created = pack.get("created", "")
    if created:
        ym = re.search(r'(\d{4})', str(created))
        if ym:
            year = int(ym.group(1))

    fm = {k: v for k, v in pack.items() if k not in ("download_sha256",)}
    fm["pax_name"] = pack["name"]
    fm["weight"] = 10000 - year

    lines = ["---"]
    lines.append(yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False).strip())
    lines.append("---")
    lines.append("")
    if body:
        lines.append(body)
        lines.append("")
    (out_dir / "index.md").write_text("\n".join(lines))


# ---------------------------------------------------------------------------
# Registry generation
# ---------------------------------------------------------------------------

def generate_registry(all_packs: list[dict]) -> dict:
    """Generate the thin registry.json install contract."""
    packs = []
    for p in all_packs:
        packs.append({
            "name": p["name"],
            "version": p["version"],
            "description": p["description"],
            "pax_type": p["pax_type"],
            "domain_id": (p.get("domain") or {}).get("id", ""),
            "quality_score": 0,  # computed separately if needed
            "construct_count": p["construct_count"],
            "finding_count": p["finding_count"],
            "source_count": len(p.get("sources_detail", [])),
            "sha256": p.get("download_sha256", ""),
            "download_url": p["download_url"],
            "dependencies": [],
            "engines": p.get("engines", []),
            "has_playbooks": p["has_playbooks"],
            "published_at": "",
            "tags": p.get("tags", []),
        })
    return {
        "schema_version": REGISTRY_SCHEMA_VERSION,
        "generated_at": "",
        "base_url": MARKETPLACE_BASE_URL,
        "packs": packs,
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    if not PACKS_DIR.is_dir():
        print(f"No packs/ directory found at {PACKS_DIR}")
        sys.exit(1)

    print(f"Scanning {PACKS_DIR}...")
    all_packs = []

    for pack_dir in sorted(PACKS_DIR.iterdir()):
        if not pack_dir.is_dir():
            continue
        if not (pack_dir / "pax.yaml").exists():
            continue

        pack = process_pack(pack_dir)
        if pack:
            all_packs.append(pack)
            detail = []
            if pack["constructs_detail"]:
                detail.append(f"{len(pack['constructs_detail'])}c")
            if pack["findings_detail"]:
                detail.append(f"{len(pack['findings_detail'])}f")
            if pack["playbooks_detail"]:
                detail.append(f"{len(pack['playbooks_detail'])}pb")
            print(f"  {pack['name']}: {' '.join(detail)}")

    # Cross-pack analysis
    print(f"\nComputing cross-pack relationships...")
    construct_index = build_construct_index(all_packs)
    related_map = compute_related_packs(all_packs, construct_index)
    print(f"  {len(construct_index)} unique constructs")

    # Add related packs
    for pack in all_packs:
        pack["related_packs"] = related_map.get(pack["name"], [])

    # Write Hugo content pages
    for pack in all_packs:
        body = generate_body(pack)
        write_content_page(pack, body)

    # Write registry.json
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    registry = generate_registry(all_packs)
    reg_path = DATA_DIR / "registry.json"
    with open(reg_path, "w") as f:
        json.dump(registry, f, indent=2)
    # Also copy to static/ for serving at site root
    (REPO_ROOT / "static" / "registry.json").write_text(json.dumps(registry, indent=2))
    print(f"\nRegistry: {len(all_packs)} packs ({reg_path.stat().st_size / 1024:.1f} KB)")

    # Write constructs.json
    ci_path = DATA_DIR / "constructs.json"
    with open(ci_path, "w") as f:
        json.dump(construct_index, f, indent=2)
    print(f"Constructs: {len(construct_index)} ({ci_path.stat().st_size / 1024:.1f} KB)")

    print(f"\nDone! {len(all_packs)} packs processed.")


if __name__ == "__main__":
    main()

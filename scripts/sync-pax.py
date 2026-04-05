#!/usr/bin/env python3
"""
sync-pax.py — Generate marketplace content from the Praxis PostgreSQL database.

Reads all knowledge from the DB (single source of truth), generates:
  1. Hugo content pages (content/packs/<name>/index.md)
  2. .pax.tar.gz archives (static/packs/<name>.pax.tar.gz) — from disk if available
  3. Registry JSON (data/registry.json) — enriched with full knowledge details
  4. Construct index (data/constructs.json) — cross-pack construct map

Usage:
  python scripts/sync-pax.py --db-url postgresql://... [--praxis-dir /path/to/praxis]

The --praxis-dir is only used for archive creation (tar.gz). All knowledge
comes from the database.
"""

import argparse
from collections import defaultdict, Counter
import hashlib
import json
import os
import re
import sys
import tarfile
from pathlib import Path

import yaml

try:
    import psycopg2
    import psycopg2.extras
except ImportError:
    psycopg2 = None


MARKETPLACE_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = MARKETPLACE_ROOT / "content" / "packs"
STATIC_DIR = MARKETPLACE_ROOT / "static" / "packs"
DATA_DIR = MARKETPLACE_ROOT / "data"

REGISTRY_SCHEMA_VERSION = "2.0"


# ---------------------------------------------------------------------------
# Database access
# ---------------------------------------------------------------------------

def get_db_connection(db_url: str):
    """Get a psycopg2 connection from a PostgreSQL DATABASE_URL.

    Refuses to connect to SQLite — marketplace sync MUST use PostgreSQL
    to avoid split-brain with the MCP server.
    """
    if "sqlite" in db_url.lower():
        print("ERROR: sync-pax.py requires PostgreSQL, not SQLite.")
        print("  The MCP server uses PostgreSQL — syncing from SQLite would create split-brain.")
        print("  Set DATABASE_URL to your PostgreSQL connection string or source /opt/praxis/.env")
        sys.exit(1)
    if not psycopg2:
        print("ERROR: psycopg2 not installed. Run: pip install psycopg2-binary")
        sys.exit(1)
    if not db_url.startswith("postgresql"):
        print(f"ERROR: Expected postgresql:// URL, got: {db_url[:30]}...")
        sys.exit(1)
    conn = psycopg2.connect(db_url)
    return conn


def query(conn, sql: str, params: dict = None) -> list[dict]:
    """Run a SELECT and return list of dicts."""
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(sql, params or {})
    rows = [dict(r) for r in cur.fetchall()]
    cur.close()
    return rows


# ---------------------------------------------------------------------------
# Knowledge extraction from DB
# ---------------------------------------------------------------------------

def extract_published_packs(conn) -> list[dict]:
    """Get all published packs with their metadata."""
    return query(conn, """
        SELECT ip.name, ip.version, ip.pax_type, ip.description, ip.provides_json,
               ip.pax_dir, ip.install_status,
               pp.quality_score, pp.published_at, pp.published_by, pp.status as pub_status
        FROM installed_pax ip
        JOIN pax_publications pp ON ip.name = pp.name
        WHERE pp.status IN ('published', 'deprecated')
        ORDER BY ip.name
    """)


def extract_domain_for_pack(conn, construct_ids: list[str]) -> dict | None:
    """Get domain info from the first construct's domain."""
    if not construct_ids:
        return None
    rows = query(conn, """
        SELECT d.id, d.display_name, d.description, d.temporal_scope,
               d.population, d.level_of_analysis
        FROM domains d
        JOIN domain_constructs dc ON d.id = dc.domain_id
        WHERE dc.construct_id = %(cid)s
        LIMIT 1
    """, {"cid": construct_ids[0]})
    if not rows:
        return None
    d = rows[0]
    # Get research questions
    rqs = query(conn, """
        SELECT question FROM domain_research_questions WHERE domain_id = %(did)s
    """, {"did": d["id"]})
    return {
        "id": d["id"],
        "display_name": d["display_name"] or "",
        "description": d["description"] or "",
        "research_questions": [r["question"] for r in rqs],
        "temporal_scope": d["temporal_scope"] or "",
        "population": d["population"] or "",
        "level_of_analysis": d["level_of_analysis"] or "",
    }


def extract_constructs_for_pack(conn, construct_ids: list[str]) -> list[dict]:
    """Get full construct definitions with aliases."""
    if not construct_ids:
        return []
    result = []
    for cid in construct_ids:
        rows = query(conn, "SELECT * FROM constructs WHERE id = %(id)s", {"id": cid})
        if not rows:
            continue
        c = rows[0]
        aliases = query(conn, "SELECT alias, alias_type FROM construct_aliases WHERE construct_id = %(id)s", {"id": cid})
        result.append({
            "id": c["id"],
            "display_name": c.get("display_name", cid),
            "definition": c.get("definition", ""),
            "aliases": [a["alias"] for a in aliases],
            "construct_type": c.get("construct_type", ""),
        })
    return result


def extract_findings_for_pack(conn, construct_ids: list[str]) -> list[dict]:
    """Get findings that reference this pack's constructs."""
    if not construct_ids:
        return []
    results = []
    seen = set()
    for cid in construct_ids:
        rows = query(conn, """
            SELECT id, source_id, finding_text, construct_ids, direction,
                   effect_size, confidence, method_used, finding_type, evidence_type
            FROM findings WHERE construct_ids LIKE %(p)s
            LIMIT 20
        """, {"p": f"%{cid}%"})
        for f in rows:
            fid = f["id"]
            if fid in seen:
                continue
            seen.add(fid)
            raw_cids = f.get("construct_ids", "")
            if raw_cids:
                cids = [x.strip() for x in raw_cids.split(",") if x.strip()]
            else:
                cids = []
            results.append({
                "finding_text": f.get("finding_text", ""),
                "construct_ids": cids,
                "direction": f.get("direction", ""),
                "effect_size": f.get("effect_size", ""),
                "confidence": f.get("confidence", ""),
                "method_used": f.get("method_used", ""),
                "finding_type": f.get("finding_type", ""),
                "evidence_type": f.get("evidence_type", ""),
            })
    return results


def extract_propositions_for_pack(conn, proposition_ids: list[str]) -> list[dict]:
    """Get propositions by ID."""
    if not proposition_ids:
        return []
    results = []
    for pid in proposition_ids:
        rows = query(conn, "SELECT * FROM propositions WHERE id = %(id)s", {"id": pid})
        if rows:
            p = rows[0]
            results.append({
                "id": p["id"],
                "proposition_text": p.get("proposition_text", ""),
                "construct_from": p.get("construct_from", ""),
                "construct_to": p.get("construct_to", ""),
                "direction": p.get("direction", ""),
                "scope_conditions": p.get("scope_conditions", ""),
            })
    return results


def extract_sources_for_findings(conn, findings: list[dict]) -> list[dict]:
    """Get unique sources referenced by findings."""
    source_ids = set(f.get("source_id") for f in findings if isinstance(f, dict) and f.get("source_id"))
    # Also search finding text for source references
    results = []
    seen = set()
    for sid in source_ids:
        if sid in seen:
            continue
        seen.add(sid)
        rows = query(conn, "SELECT * FROM sources WHERE id = %(id)s", {"id": sid})
        if rows:
            s = rows[0]
            results.append({
                "id": s["id"],
                "title": s.get("title", ""),
                "authors": s.get("authors", ""),
                "year": s.get("year"),
                "doi": s.get("doi"),
                "source_type": s.get("source_type", ""),
            })
    return results


def extract_playbooks_for_pack(conn, pax_name: str, provides: dict) -> list[dict]:
    """Get playbook summaries from provides_json.

    Playbooks don't have their own DB table yet, but provides_json
    lists playbook IDs, and engine_construct_mappings tells us which
    engines are associated. We build summaries from what's available.
    """
    playbook_ids = provides.get("playbooks", [])
    if not playbook_ids:
        return []
    # We know the playbook IDs but not their full YAML content from DB.
    # Build minimal summaries using what we have.
    results = []
    for pb_id in playbook_ids:
        results.append({
            "id": pb_id,
            "display_name": pb_id.replace("_", " ").replace("-", " ").title(),
            "description": "",
            "estimated_runtime": "",
            "step_count": 0,
            "engines_used": [],
        })
    return results


def extract_engines_for_pack(conn, pax_name: str, provides: dict) -> list[str]:
    """Get engine names from DB — provides_json first, then engine_construct_mappings."""
    engines = provides.get("engines", [])
    if engines:
        return engines
    # Query engine_construct_mappings for engines linked to this pack's constructs
    construct_ids = provides.get("constructs", [])
    if not construct_ids:
        return []
    placeholders = ", ".join(f"'{cid}'" for cid in construct_ids[:20])
    rows = query(conn, f"""
        SELECT DISTINCT engine_id FROM engine_construct_mappings
        WHERE construct_id IN ({placeholders})
    """)
    return [r["engine_id"] for r in rows]


def extract_data_sources_for_pack(conn, pax_name: str) -> bool:
    """Check if this pack has registered data sources in the DB."""
    rows = query(conn, "SELECT count(*) as c FROM data_sources WHERE pax_name = %(n)s", {"n": pax_name})
    return rows[0]["c"] > 0 if rows else False


# ---------------------------------------------------------------------------
# Title derivation
# ---------------------------------------------------------------------------

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


ACRONYMS = {"ml", "ai", "gdp", "nlp", "rfm", "ols", "ucdp", "stem", "api", "sql", "csv", "rct"}


def fix_acronyms(title: str) -> str:
    """Fix common acronyms after title-casing (Ml → ML, Ai → AI)."""
    words = title.split()
    return " ".join(w.upper() if w.lower() in ACRONYMS else w for w in words)


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


# ---------------------------------------------------------------------------
# Archive + content helpers
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
    return sha256, output_path.stat().st_size


def format_size(size_bytes: int) -> str:
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    return f"{size_bytes / (1024 * 1024):.1f} MB"


def write_content_page(fm: dict, body: str, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    lines = ["---"]
    lines.append(yaml.dump(fm, default_flow_style=False, allow_unicode=True, sort_keys=False).strip())
    lines.append("---")
    lines.append("")
    if body:
        lines.append(body)
        lines.append("")
    (output_dir / "index.md").write_text("\n".join(lines))


def generate_body(findings: list[dict], propositions: list[dict], domain: dict | None) -> str:
    """Generate markdown body from DB-sourced knowledge."""
    sections = []
    if domain:
        parts = [f"**Domain:** {domain.get('display_name', '')}"]
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

    if propositions:
        lines = ["## Theoretical Propositions", ""]
        for p in propositions:
            text = p.get("proposition_text", "")
            if text:
                arrow = {"positive": "+", "negative": "−", "null": "∅"}.get(p.get("direction", ""), "→")
                lines.append(f"- [{arrow}] {text}")
        sections.append("\n".join(lines))

    return "\n\n".join(sections)


# ---------------------------------------------------------------------------
# Cross-pack analysis
# ---------------------------------------------------------------------------

def build_construct_index(all_packs: list[dict]) -> dict:
    index = {}
    for pack in all_packs:
        pack_name = pack["pax_name"]
        construct_findings = defaultdict(list)
        for f in pack.get("findings_detail", []):
            for cid in f.get("construct_ids", []):
                construct_findings[cid].append(f.get("direction", ""))

        for c in pack.get("constructs_detail", []):
            cid = c["id"]
            if cid not in index:
                index[cid] = {"id": cid, "display_name": c.get("display_name", cid),
                              "definition": c.get("definition", ""), "aliases": c.get("aliases", []), "packs": []}
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
                                        "direction": primary, "finding_count": len(construct_findings.get(cid, []))})
    for cid in index:
        index[cid]["pack_count"] = len(index[cid]["packs"])
    return index


def compute_related_packs(all_packs: list[dict], construct_index: dict) -> dict[str, list[str]]:
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
            if other["pax_name"] == name:
                continue
            shared = pack_constructs & set(other.get("constructs", []))
            if shared:
                scores[other["pax_name"]] = sum(1.0 / construct_pack_count.get(c, 1) for c in shared)
        related[name] = sorted(scores, key=scores.get, reverse=True)[:3]
    return related


# ---------------------------------------------------------------------------
# Main sync
# ---------------------------------------------------------------------------

def sync_packs(db_url: str, praxis_dir: Path | None = None):
    print(f"  Connecting to database...")
    conn = get_db_connection(db_url)

    published = extract_published_packs(conn)
    print(f"  {len(published)} published packs from DB")

    all_packs = []

    for row in published:
        name = row["name"]
        print(f"  Processing {name}...")

        provides = json.loads(row.get("provides_json") or "{}") if row.get("provides_json") else {}
        construct_ids = provides.get("constructs", [])
        proposition_ids = provides.get("propositions", [])
        author = row.get("author") or ""
        # Map mcp_agent to readable name
        published_by = row.get("published_by", "mcp_agent")
        if published_by == "mcp_agent":
            published_by = "Praxis Agent"

        # Extract all knowledge from DB
        domain = extract_domain_for_pack(conn, construct_ids)
        constructs_detail = extract_constructs_for_pack(conn, construct_ids)
        findings_detail = extract_findings_for_pack(conn, construct_ids)
        propositions_detail = extract_propositions_for_pack(conn, proposition_ids)
        sources_detail = extract_sources_for_findings(conn, findings_detail)

        # Engines and playbooks from DB
        engine_names = extract_engines_for_pack(conn, name, provides)
        playbooks_detail = extract_playbooks_for_pack(conn, name, provides)
        playbook_names = [p["id"] for p in playbooks_detail]
        has_data = extract_data_sources_for_pack(conn, name)

        # Archive — use cached if available, rebuild from disk if possible
        archive_size = ""
        sha256 = ""
        pax_dir = None
        if praxis_dir:
            candidate = praxis_dir / "pax" / name
            if candidate.is_dir():
                pax_dir = candidate
        if pax_dir and pax_dir.is_dir():
            archive_path = STATIC_DIR / f"{name}.pax.tar.gz"
            sha256, size_bytes = create_archive(pax_dir, archive_path)
            archive_size = format_size(size_bytes)
            print(f"    Archive: {archive_size}")
        else:
            existing = STATIC_DIR / f"{name}.pax.tar.gz"
            if existing.exists():
                sha256 = hashlib.sha256(existing.read_bytes()).hexdigest()
                archive_size = format_size(existing.stat().st_size)
                print(f"    Archive: {archive_size} (cached)")
            else:
                print(f"    No archive available")

        # Counts
        construct_count = len(constructs_detail) or len(construct_ids)
        finding_count = len(findings_detail)
        proposition_count = len(propositions_detail) or len(proposition_ids)

        # Build title
        desc = row.get("description") or ""
        title = derive_title(name, desc, row.get("pax_type", "topic"), author)

        # Sort weight
        year = 0
        created = row.get("created") or ""
        if created:
            ym = re.search(r'(\d{4})', str(created))
            if ym:
                year = int(ym.group(1))

        fm = {
            "title": title,
            "pax_name": name,
            "version": row.get("version", "1.0.0"),
            "pax_type": row.get("pax_type", "topic"),
            "description": desc,
            "author": author,
            "created": str(created),
            "license": "",
            "tags": [],  # Tags come from provides or manifest — minimal without disk
            # ID lists
            "constructs": construct_ids,
            "engines": engine_names,
            "playbook_names": playbook_names,
            # Counts
            "construct_count": construct_count,
            "finding_count": finding_count,
            "proposition_count": proposition_count,
            "has_playbooks": bool(playbook_names),
            "has_data_sources": has_data,
            # Rich detail
            "domain": domain,
            "constructs_detail": constructs_detail,
            "findings_detail": findings_detail,
            "propositions_detail": propositions_detail,
            "sources_detail": sources_detail,
            "playbooks_detail": playbooks_detail,
            # Publication metadata
            "quality_score": row.get("quality_score", 0) or 0,
            "published_at": str(row.get("published_at", "")),
            "published_by": published_by,
            "pub_status": row.get("pub_status", "published"),
            # Download
            "download_url": f"/packs/{name}.pax.tar.gz" if sha256 else "",
            "download_size": archive_size,
            # Internal
            "_sha256": sha256,
            "weight": 10000 - year,
        }

        # Tags from provides or pack name
        tags = provides.get("tags", [])
        if not tags:
            tags = [row.get("pax_type", "topic"), name.split("-")[0]]
        fm["tags"] = tags

        detail_counts = []
        if constructs_detail: detail_counts.append(f"{len(constructs_detail)} constructs")
        if findings_detail: detail_counts.append(f"{len(findings_detail)} findings")
        if propositions_detail: detail_counts.append(f"{len(propositions_detail)} propositions")
        if playbooks_detail: detail_counts.append(f"{len(playbooks_detail)} playbooks")
        if sources_detail: detail_counts.append(f"{len(sources_detail)} sources")
        if detail_counts:
            print(f"    Detail: {', '.join(detail_counts)}")

        all_packs.append(fm)

    # Cross-pack analysis
    print(f"\n  Computing cross-pack relationships...")
    construct_index = build_construct_index(all_packs)
    print(f"    Construct index: {len(construct_index)} unique constructs across {len(all_packs)} packs")

    related_map = compute_related_packs(all_packs, construct_index)

    # Write content pages and registry
    registry = []
    for fm in all_packs:
        name = fm["pax_name"]
        sha256 = fm.pop("_sha256")
        fm["related_packs"] = related_map.get(name, [])

        body = generate_body(fm.get("findings_detail", []), fm.get("propositions_detail", []), fm.get("domain"))
        write_content_page(fm, body, CONTENT_DIR / name)

        entry = {k: v for k, v in fm.items() if not k.startswith("_") and k != "weight"}
        entry["download_sha256"] = sha256
        entry["schema_version"] = REGISTRY_SCHEMA_VERSION
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

    conn.close()


def main():
    parser = argparse.ArgumentParser(description="Sync PAX marketplace from database")
    parser.add_argument("--db-url", type=str, default=os.environ.get("DATABASE_URL", ""),
                        help="PostgreSQL connection URL (or set DATABASE_URL env var)")
    parser.add_argument("--praxis-dir", type=Path, default=None,
                        help="Path to praxis repo (for archive creation and playbooks)")
    # Legacy flags (backward compat)
    parser.add_argument("--published-only", action="store_true", help="(default behavior, kept for compat)")
    parser.add_argument("--db-path", type=Path, default=None, help="(legacy, use --db-url instead)")
    args = parser.parse_args()

    db_url = args.db_url
    if not db_url and args.db_path:
        db_url = str(args.db_path)
    if not db_url:
        print("ERROR: No database URL. Set DATABASE_URL env var or pass --db-url")
        sys.exit(1)

    praxis_dir = args.praxis_dir
    if not praxis_dir:
        # Try common locations
        for candidate in [MARKETPLACE_ROOT.parent / "praxis", Path("/opt/praxis")]:
            if candidate.is_dir():
                praxis_dir = candidate
                break

    print(f"Syncing PAX marketplace from database...")
    if praxis_dir:
        print(f"  Praxis dir: {praxis_dir} (for archives/playbooks)")
    sync_packs(db_url, praxis_dir)
    print("Done!")


if __name__ == "__main__":
    main()

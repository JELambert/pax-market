#!/usr/bin/env python3
"""
sync-pax.py — Read PAX directories from the praxis repo and generate:
  1. Hugo content pages (content/packs/<name>/index.md)
  2. .pax.tar.gz archives (static/packs/<name>.pax.tar.gz)
  3. Registry JSON (data/registry.json)

Usage:
  python scripts/sync-pax.py [--praxis-dir /path/to/praxis]

Defaults to ../praxis relative to the marketplace repo root.
"""

import argparse
import hashlib
import json
import re
import sys
import tarfile
from pathlib import Path

import yaml


# PAX directories that are test fixtures, not real packs
SKIP_DIRS = {"roundtrip-pax", "roundtrip-constructs", "import-basic", "import-with-install"}

MARKETPLACE_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = MARKETPLACE_ROOT / "content" / "packs"
STATIC_DIR = MARKETPLACE_ROOT / "static" / "packs"
DATA_DIR = MARKETPLACE_ROOT / "data"


def load_json(path: Path):
    """Load a JSON file, returning [] if missing or invalid."""
    if not path.exists():
        return []
    try:
        with open(path) as f:
            data = json.load(f)
        # Normalize: some files are a single dict, some are arrays
        if isinstance(data, dict):
            return [data]
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, Exception):
        return []


def has_directory(pax_dir: Path, name: str) -> bool:
    """Check if a PAX has a non-empty subdirectory with real files."""
    d = pax_dir / name
    if not d.is_dir():
        return False
    return any(f for f in d.rglob("*") if f.is_file() and not f.name.startswith("."))


def read_readme(pax_dir: Path) -> str:
    """Read README.md content if it exists."""
    readme = pax_dir / "README.md"
    if readme.exists():
        return readme.read_text().strip()
    return ""


def shorten_authors(author: str) -> str:
    """Shorten author string to citation form: 'Surname & Surname' or 'Surname et al.'"""
    # Split on semicolons (primary separator) or ' and '
    parts = [a.strip() for a in re.split(r';| and ', author) if a.strip()]
    if not parts:
        return author

    def surname(a: str) -> str:
        # Handle "Last, First" format
        if "," in a:
            return a.split(",")[0].strip()
        # Handle "First Last" format
        tokens = a.split()
        return tokens[-1] if tokens else a

    surnames = [surname(p) for p in parts]
    if len(surnames) == 1:
        return surnames[0]
    elif len(surnames) == 2:
        return f"{surnames[0]} & {surnames[1]}"
    else:
        return f"{surnames[0]} et al."


def derive_title(manifest: dict) -> str:
    """Extract a clean, short title from the manifest.

    Strategy:
    1. For paper PAX: build "Author (Year) — Title" from description + author field
    2. If description has a dash-separated prefix, use that
    3. Fall back to humanizing the kebab-case name
    """
    name = manifest.get("name", "")
    desc = manifest.get("description", "")
    pax_type = manifest.get("pax_type", "topic")
    author = manifest.get("author", "")

    # For papers: try to build "Author (Year) — Title"
    if pax_type == "paper" and author:
        year_match = re.search(r'(\d{4})', name)
        year = f" ({year_match.group(1)})" if year_match else ""
        short_author = shorten_authors(author)

        # Check for quoted title in description
        quoted = re.search(r'"([^"]+)"', desc)
        if quoted:
            return f"{short_author}{year} — {quoted.group(1)}"

        # Try first sentence of description as subtitle (cap at 60 chars)
        first_sentence = desc.split(".")[0].strip()
        if len(first_sentence) < 60:
            return f"{short_author}{year} — {first_sentence}"

        # Just author + year
        return f"{short_author}{year}"

    # Try dash-separated prefix (common in descriptions)
    for sep in ["—", "–", " - "]:
        if sep in desc:
            prefix = desc.split(sep)[0].strip()
            # Only use if reasonably short (< 80 chars)
            if len(prefix) < 80:
                return prefix
            break

    # Fall back to humanized name
    return name.replace("-", " ").replace("_", " ").title()


def generate_body(manifest: dict, pax_dir: Path) -> str:
    """Generate markdown body content from knowledge files when no README exists."""
    knowledge_dir = pax_dir / "knowledge"
    sections = []

    # Domain info
    domains = load_json(knowledge_dir / "domain.json")
    if domains:
        d = domains[0]
        domain_name = d.get("display_name", d.get("id", ""))
        domain_desc = d.get("description", "")
        temporal = d.get("temporal_scope", "")
        population = d.get("population", "")

        parts = [f"**Domain:** {domain_name}"]
        if domain_desc:
            parts.append(f"\n{domain_desc}")
        meta = []
        if temporal:
            meta.append(f"**Temporal scope:** {temporal}")
        if population:
            meta.append(f"**Population:** {population}")
        if meta:
            parts.append("\n" + " | ".join(meta))
        sections.append("\n".join(parts))

    # Key findings
    findings = load_json(knowledge_dir / "findings.json")
    if findings:
        lines = ["## Key Findings", ""]
        for f in findings[:8]:  # Cap at 8 to keep it readable
            text = f.get("finding_text", "")
            direction = f.get("direction", "")
            confidence = f.get("confidence", "")
            if text:
                meta_parts = []
                if direction:
                    meta_parts.append(direction)
                if confidence:
                    meta_parts.append(confidence)
                suffix = f" *({', '.join(meta_parts)})*" if meta_parts else ""
                lines.append(f"- {text}{suffix}")
        if len(findings) > 8:
            lines.append(f"\n*...and {len(findings) - 8} more findings*")
        sections.append("\n".join(lines))

    # Propositions
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

    # Source info
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


def create_archive(pax_dir: Path, output_path: Path) -> tuple[str, int]:
    """Create a .pax.tar.gz archive and return (sha256, size_bytes)."""
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


def format_size(size_bytes: int) -> str:
    """Human-readable file size."""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    else:
        return f"{size_bytes / (1024 * 1024):.1f} MB"


def build_front_matter(manifest: dict, pax_dir: Path, archive_size: str = "") -> dict:
    """Build Hugo front matter from PAX manifest and knowledge files."""
    provides = manifest.get("provides", {})
    constructs = provides.get("constructs", [])
    findings = provides.get("findings", [])
    engines = provides.get("engines", [])
    playbooks = provides.get("playbooks", [])
    propositions = provides.get("propositions", [])

    knowledge_dir = pax_dir / "knowledge"

    # Count from provides first, fall back to knowledge files
    construct_count = len(constructs) or len(load_json(knowledge_dir / "constructs.json"))
    finding_count = len(findings) or len(load_json(knowledge_dir / "findings.json"))
    proposition_count = len(propositions) or len(load_json(knowledge_dir / "propositions.json"))

    # Detect playbook names from directory
    playbook_names = playbooks[:]
    if not playbook_names:
        pb_dir = pax_dir / "playbooks"
        if pb_dir.is_dir():
            playbook_names = [f.stem for f in sorted(pb_dir.glob("*.yaml")) if f.is_file()]

    # Detect engine names from registry
    engine_names = engines[:]
    if not engine_names:
        engine_reg = pax_dir / "engines" / "registry.json"
        if engine_reg.exists():
            eng_data = load_json(engine_reg)
            engine_names = [e.get("id", e.get("name", "")) for e in eng_data if isinstance(e, dict)]

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
        "constructs": constructs,
        "findings": findings,
        "engines": engine_names,
        "playbooks": playbook_names,
        "propositions": propositions,
        "construct_count": construct_count,
        "finding_count": finding_count,
        "proposition_count": proposition_count,
        "has_playbooks": has_playbooks,
        "has_data_sources": has_data,
        "download_url": f"/packs/{name}.pax.tar.gz",
        "download_size": archive_size,
    }

    # Sort weight: newer packs first (parse year from created or name)
    year = 0
    if created:
        year_match = re.search(r'(\d{4})', str(created))
        if year_match:
            year = int(year_match.group(1))
    fm["weight"] = 10000 - year  # Lower weight = appears first in Hugo

    return fm


def write_content_page(fm: dict, body: str, output_dir: Path):
    """Write a Hugo content page with YAML front matter."""
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


def sync_packs(praxis_dir: Path):
    """Main sync: read all PAX dirs and generate content + archives."""
    pax_root = praxis_dir / "pax"
    if not pax_root.is_dir():
        print(f"Error: PAX directory not found at {pax_root}")
        sys.exit(1)

    registry = []

    for pax_dir in sorted(pax_root.iterdir()):
        if not pax_dir.is_dir():
            continue
        if pax_dir.name in SKIP_DIRS:
            continue

        manifest_path = pax_dir / "pax.yaml"
        if not manifest_path.exists():
            print(f"  Skipping {pax_dir.name}: no pax.yaml")
            continue

        print(f"  Processing {pax_dir.name}...")

        with open(manifest_path) as f:
            manifest = yaml.safe_load(f)

        # Create archive first so we can include size in front matter
        archive_path = STATIC_DIR / f"{pax_dir.name}.pax.tar.gz"
        sha256, size_bytes = create_archive(pax_dir, archive_path)
        archive_size = format_size(size_bytes)
        print(f"    Archive: {archive_size} (sha256: {sha256[:12]}...)")

        # Build front matter
        fm = build_front_matter(manifest, pax_dir, archive_size)

        # Read README for body content, or auto-generate
        body = read_readme(pax_dir)
        if not body:
            body = generate_body(manifest, pax_dir)
            if body:
                print(f"    Auto-generated body content ({len(body)} chars)")

        # Write Hugo content page
        write_content_page(fm, body, CONTENT_DIR / pax_dir.name)

        # Add to registry
        registry_entry = {
            "name": fm["pax_name"],
            "title": fm["title"],
            "version": fm["version"],
            "pax_type": fm["pax_type"],
            "description": fm["description"],
            "author": fm["author"],
            "license": fm["license"],
            "tags": fm["tags"],
            "constructs": fm["constructs"],
            "construct_count": fm["construct_count"],
            "finding_count": fm["finding_count"],
            "proposition_count": fm["proposition_count"],
            "has_playbooks": fm["has_playbooks"],
            "has_data_sources": fm["has_data_sources"],
            "engines": fm["engines"],
            "playbooks": fm["playbooks"],
            "download_url": fm["download_url"],
            "download_sha256": sha256,
            "download_size": archive_size,
        }
        registry.append(registry_entry)

    # Write registry JSON
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    registry_path = DATA_DIR / "registry.json"
    with open(registry_path, "w") as f:
        json.dump(registry, f, indent=2)
    print(f"\n  Registry: {len(registry)} packs written to {registry_path}")


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

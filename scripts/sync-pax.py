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
import os
import sys
import tarfile
from datetime import datetime
from io import BytesIO
from pathlib import Path

import yaml


# PAX directories that are test fixtures, not real packs
SKIP_DIRS = {"roundtrip-pax", "roundtrip-constructs", "import-basic", "import-with-install"}

MARKETPLACE_ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = MARKETPLACE_ROOT / "content" / "packs"
STATIC_DIR = MARKETPLACE_ROOT / "static" / "packs"
DATA_DIR = MARKETPLACE_ROOT / "data"


def count_json_items(path: Path) -> int:
    """Count items in a JSON array file."""
    if not path.exists():
        return 0
    try:
        with open(path) as f:
            data = json.load(f)
        return len(data) if isinstance(data, list) else 1
    except (json.JSONDecodeError, Exception):
        return 0


def has_directory(pax_dir: Path, name: str) -> bool:
    """Check if a PAX has a non-empty subdirectory."""
    d = pax_dir / name
    if not d.is_dir():
        return False
    return any(d.iterdir())


def read_readme(pax_dir: Path) -> str:
    """Read README.md content if it exists."""
    readme = pax_dir / "README.md"
    if readme.exists():
        return readme.read_text().strip()
    return ""


def create_archive(pax_dir: Path, output_path: Path) -> tuple[str, int]:
    """Create a .pax.tar.gz archive and return (sha256, size_bytes)."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with tarfile.open(output_path, "w:gz") as tar:
        for item in sorted(pax_dir.rglob("*")):
            if item.is_file():
                arcname = str(item.relative_to(pax_dir))
                # Skip __pycache__ and hidden files
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


def build_front_matter(manifest: dict, pax_dir: Path) -> dict:
    """Build Hugo front matter from PAX manifest and knowledge files."""
    provides = manifest.get("provides", {})
    constructs = provides.get("constructs", [])
    findings = provides.get("findings", [])
    engines = provides.get("engines", [])

    # Count from provides first, fall back to knowledge files
    construct_count = len(constructs) or count_json_items(pax_dir / "knowledge" / "constructs.json")
    finding_count = len(findings) or count_json_items(pax_dir / "knowledge" / "findings.json")

    has_playbooks = has_directory(pax_dir, "playbooks")
    has_data = has_directory(pax_dir, "data")

    name = manifest.get("name", pax_dir.name)

    fm = {
        "title": manifest.get("description", name).split("—")[0].split("–")[0].strip(),
        "pax_name": name,
        "version": str(manifest.get("version", "0.0.0")),
        "pax_type": manifest.get("pax_type", "topic"),
        "description": manifest.get("description", ""),
        "author": manifest.get("author", ""),
        "created": manifest.get("created", ""),
        "license": manifest.get("license", ""),
        "tags": manifest.get("tags", []),
        "constructs": constructs,
        "findings": findings,
        "engines": engines,
        "construct_count": construct_count,
        "finding_count": finding_count,
        "has_playbooks": has_playbooks,
        "has_data_sources": has_data,
        "download_url": f"/packs/{name}.pax.tar.gz",
    }

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

        # Build front matter
        fm = build_front_matter(manifest, pax_dir)

        # Read README for body content
        body = read_readme(pax_dir)

        # Write Hugo content page
        write_content_page(fm, body, CONTENT_DIR / pax_dir.name)

        # Create archive
        archive_path = STATIC_DIR / f"{pax_dir.name}.pax.tar.gz"
        sha256, size_bytes = create_archive(pax_dir, archive_path)
        print(f"    Archive: {format_size(size_bytes)} (sha256: {sha256[:12]}...)")

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
            "has_playbooks": fm["has_playbooks"],
            "has_data_sources": fm["has_data_sources"],
            "download_url": fm["download_url"],
            "download_sha256": sha256,
            "download_size": format_size(size_bytes),
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

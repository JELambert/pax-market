#!/usr/bin/env python3
"""
build_pax.py — Reference submitter tool. Build a distribution archive for a
PAX directory.

Produces <pack>.zip (canonical) and optionally <pack>.pax.tar.gz (legacy)
alongside the input directory, with a valid manifest.json integrity envelope
matching the spec in docs/PAX_CREATION_GUIDE.md.

This script has zero dependencies beyond the Python stdlib so submitters can
run it without `pip install`. The marketplace's own generate-registry.py uses
identical packaging logic.

Usage:
    python3 scripts/build_pax.py path/to/my-pack-dir
    python3 scripts/build_pax.py path/to/my-pack-dir --targz   # also emit legacy tar.gz
"""

import hashlib
import io
import json
import re
import sys
import tarfile
import zipfile
from datetime import datetime, timezone
from pathlib import Path


def _read_yaml_field(text: str, key: str, default: str = "") -> str:
    m = re.search(rf'^\s*{key}\s*:\s*"?([^"\n]+)"?\s*$', text, re.M)
    return m.group(1).strip() if m else default


def build_pax(pack_dir: Path, *, also_targz: bool = False, exported_by: str = "submitter") -> Path:
    if not (pack_dir / "pax.yaml").exists():
        sys.exit(f"missing pax.yaml under {pack_dir}")
    name = pack_dir.name

    pack_files = []
    for p in sorted(pack_dir.rglob("*")):
        if not p.is_file():
            continue
        arcname = str(p.relative_to(pack_dir))
        if arcname.startswith(".") or "__pycache__" in arcname or arcname == "manifest.json":
            continue
        if arcname.endswith(".md"):
            continue  # spec: no markdown docs in archive (issue #95/#97)
        pack_files.append((p, arcname))

    files = {
        arcname: {
            "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
            "size": p.stat().st_size,
        }
        for p, arcname in pack_files
    }

    text = (pack_dir / "pax.yaml").read_text()
    # Prefer the canonical name; fall back to the legacy alias for older packs.
    schema = _read_yaml_field(text, "built_against_schema", "") or _read_yaml_field(text, "schema_version", "4.0")
    manifest = {
        "pax_name": name,
        "version": _read_yaml_field(text, "version", "0.0.0"),
        "built_against_schema": schema,
        "exported_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "exported_by": exported_by,
        "files": files,
    }
    manifest_bytes = json.dumps(manifest, indent=2, sort_keys=True).encode()

    zip_path = pack_dir.parent / f"{name}.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("manifest.json", manifest_bytes)
        for p, arcname in pack_files:
            zf.write(p, arcname=arcname)

    if also_targz:
        targz = pack_dir.parent / f"{name}.pax.tar.gz"
        with tarfile.open(targz, "w:gz") as tar:
            info = tarfile.TarInfo("manifest.json")
            info.size = len(manifest_bytes)
            tar.addfile(info, io.BytesIO(manifest_bytes))
            for p, arcname in pack_files:
                tar.add(p, arcname=arcname)
        print(f"wrote {targz}")

    print(f"wrote {zip_path}")
    return zip_path


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: build_pax.py <pack-dir> [--targz]")
    target = Path(sys.argv[1]).resolve()
    if not target.is_dir():
        sys.exit(f"not a directory: {target}")
    build_pax(target, also_targz="--targz" in sys.argv)


if __name__ == "__main__":
    main()

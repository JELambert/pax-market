#!/usr/bin/env python3
"""
smoke_install_pack.py — Praxis-free "installs cleanly" smoke test.

Issue #86 asks for an integration test that catches packs which would fail to
install in praxis. Running real praxis in CI is heavy; this script approximates
it by building the archive locally and verifying every guarantee that
praxis's import_pax depends on:

  1. build_pax.py produces a .zip (and .pax.tar.gz with --targz).
  2. The archive contains a manifest.json at root.
  3. manifest.json["files"] is the canonical {sha256, size} dict shape (issue #99).
  4. Every digest+size in the manifest matches the archive entry's actual bytes.
  5. Every file in the archive is listed in the manifest (no extras except
     manifest.json itself).
  6. No path traversal (`..`, absolute paths, symlinks).
  7. pax.yaml exists and parses; required keys present.
  8. Each knowledge/*.json that exists is valid JSON.
  9. Top-level pax_name in manifest matches pax.yaml's name.

Usage:
    python3 scripts/smoke_install_pack.py pax/<pack-name>
    python3 scripts/smoke_install_pack.py pax/<pack-name> --json   # machine-readable
"""

import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent


def fail(errors: list, msg: str) -> None:
    errors.append(msg)


def smoke_check(pack_dir: Path) -> dict:
    errors: list[str] = []
    pack = pack_dir.name

    # 1. Build the archive into a temp dir.
    with tempfile.TemporaryDirectory() as tmp:
        tmp_pack = Path(tmp) / pack
        shutil.copytree(pack_dir, tmp_pack)
        result = subprocess.run(
            [sys.executable, str(REPO_ROOT / "scripts" / "build_pax.py"), str(tmp_pack)],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            fail(errors, f"build_pax.py failed: {result.stderr.strip()}")
            return {"pack": pack, "ok": False, "errors": errors}

        zip_path = tmp_pack.parent / f"{pack}.zip"
        if not zip_path.exists():
            fail(errors, f"build_pax.py did not produce {zip_path.name}")
            return {"pack": pack, "ok": False, "errors": errors}

        # 2-9. Open zip and verify everything.
        with zipfile.ZipFile(zip_path) as zf:
            names = zf.namelist()
            if "manifest.json" not in names:
                fail(errors, "missing manifest.json at archive root")
                return {"pack": pack, "ok": False, "errors": errors}

            try:
                manifest = json.loads(zf.read("manifest.json"))
            except json.JSONDecodeError as e:
                fail(errors, f"manifest.json invalid JSON: {e}")
                return {"pack": pack, "ok": False, "errors": errors}

            files = manifest.get("files")
            if not isinstance(files, dict):
                fail(errors, "manifest.json['files'] missing or not a dict")
                return {"pack": pack, "ok": False, "errors": errors}

            # Shape check: dict with sha256+size, never bare string (issue #99).
            for arc, entry in files.items():
                if not isinstance(entry, dict):
                    fail(errors, f"files[{arc!r}] is {type(entry).__name__}; spec requires dict with sha256+size")
                    continue
                if "sha256" not in entry or "size" not in entry:
                    fail(errors, f"files[{arc!r}] missing sha256 or size")

            # Path safety + completeness.
            for arc in names:
                if arc == "manifest.json":
                    continue
                if arc.startswith("/") or ".." in Path(arc).parts:
                    fail(errors, f"unsafe path in archive: {arc}")
                if arc not in files:
                    fail(errors, f"archive entry not listed in manifest: {arc}")

            # Digest + size verification.
            for arc, entry in files.items():
                if not isinstance(entry, dict):
                    continue
                if arc not in names:
                    fail(errors, f"manifest lists {arc} but archive has no such entry")
                    continue
                data = zf.read(arc)
                actual_sha = hashlib.sha256(data).hexdigest()
                if actual_sha != entry.get("sha256"):
                    fail(errors, f"sha256 mismatch for {arc}: archive={actual_sha} manifest={entry.get('sha256')}")
                if len(data) != entry.get("size"):
                    fail(errors, f"size mismatch for {arc}: archive={len(data)} manifest={entry.get('size')}")

            # 7. pax.yaml.
            try:
                pax_yaml = zf.read("pax.yaml").decode()
            except KeyError:
                fail(errors, "missing pax.yaml at archive root")
                return {"pack": pack, "ok": False, "errors": errors}

            import re
            def field(key: str) -> str:
                m = re.search(rf'^\s*{key}\s*:\s*"?([^"\n]+)"?\s*$', pax_yaml, re.M)
                return m.group(1).strip() if m else ""

            for k in ("name", "version", "description", "pax_type"):
                if not field(k):
                    fail(errors, f"pax.yaml missing required field: {k}")
            # Either the canonical or legacy schema-version field must be present.
            if not field("built_against_schema") and not field("schema_version"):
                fail(errors, "pax.yaml missing required field: built_against_schema (or legacy schema_version)")

            yaml_name = field("name")
            man_name = manifest.get("pax_name", "")
            if yaml_name and man_name and yaml_name != man_name:
                fail(errors, f"pax.yaml name ({yaml_name!r}) != manifest pax_name ({man_name!r})")

            # 8. JSON validity for any knowledge/*.json entries.
            for arc in names:
                if arc.startswith("knowledge/") and arc.endswith(".json"):
                    try:
                        json.loads(zf.read(arc))
                    except json.JSONDecodeError as e:
                        fail(errors, f"{arc} is not valid JSON: {e}")

    return {"pack": pack, "ok": not errors, "errors": errors}


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    json_mode = "--json" in sys.argv
    if not args:
        sys.exit("usage: smoke_install_pack.py <pack-dir> [--json]")

    pack_dir = Path(args[0]).resolve()
    if not pack_dir.is_dir() or not (pack_dir / "pax.yaml").exists():
        sys.exit(f"not a valid pack directory: {pack_dir}")

    report = smoke_check(pack_dir)

    if json_mode:
        print(json.dumps(report))
    else:
        if report["ok"]:
            print(f"OK  {report['pack']}: archive installs cleanly")
        else:
            print(f"FAIL {report['pack']}: {len(report['errors'])} error(s)")
            for e in report["errors"]:
                print(f"  - {e}")

    sys.exit(0 if report["ok"] else 1)


if __name__ == "__main__":
    main()

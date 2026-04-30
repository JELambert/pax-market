# Contributing to the PAX Specification

The PAX format is governed by two files. Editing them in the wrong order is
the most common way to ship inconsistent state, so the rule is short and
strict:

> **Always edit `docs/pax_spec.yaml` first. Then update `docs/PAX_CREATION_GUIDE.md` and any code that references the changed value. CI will refuse to merge if anything is out of sync.**

## Source of truth

| File | Role |
|---|---|
| `docs/pax_spec.yaml` | **Source of truth** for moving parts: current version, valid versions, controlled vocabularies, per-entity field manifests, script defaults, version history. |
| `docs/PAX_CREATION_GUIDE.md` | Hand-authored prose, rationale, examples, validation checklists. The two parsed islands inside it (the `<!-- PAX_SCHEMA_START -->` and `<!-- PAX_FIELDS_START -->` blocks) are human-readable mirrors of `pax_spec.yaml`. CI asserts they match. |
| `docs/PLAYBOOK_FORMAT.md` | Playbook action vocabulary and SQL surface. References values from the SCHEMA block in the creation guide. |

Nothing is generated. The guide is hand-edited markdown, the YAML is
hand-edited YAML, and CI proves they agree. If the assertion fires, the
diff in the CI output tells you exactly which file and line is out of sync.

## Common spec changes — checklist

### Bumping `current_version` (e.g., 4.0 → 4.1)

1. Edit `docs/pax_spec.yaml`:
   - `current_version: "4.1"`
   - `valid_versions: [..., "4.1"]`
   - `last_updated: "YYYY-MM-DD"` (today)
   - prepend a new `version_history` entry with version + date + summary
2. Edit `docs/PAX_CREATION_GUIDE.md`:
   - title (line 1) and header (line 3) reference the new version
   - "What's New in v4.1" section
   - prepend a row to the version-history table
   - update inline examples (`built_against_schema: "4.1"`) where the example is meant to show the current spec
3. Run `python3 scripts/check_spec_consistency.py` locally. Fix anything it flags.

### Adding a controlled-vocabulary value (enum)

1. Edit `docs/pax_spec.yaml` — add the value to the relevant list under `enums:`.
2. Mirror the change in the SCHEMA block of `docs/PAX_CREATION_GUIDE.md` (the `**foo values:** a, b, c` line).
3. If the enum is also hardcoded as a tuple in `scripts/validate_pax.py` (currently only `pax_type`, `dataset_format`, `playbook_action`, schema versions), update the literal-tuple fallback to match.
4. Run `python3 scripts/check_spec_consistency.py`.

### Adding or modifying an entity field

1. Edit the relevant entity in `docs/pax_spec.yaml` under `entities:`.
2. Mirror the change in the FIELDS block of `docs/PAX_CREATION_GUIDE.md`.
3. Run `python3 scripts/check_spec_consistency.py`.

### Renaming a manifest field

This is the heaviest change. The recent `schema_version` → `built_against_schema` rename is the worked example — see commit history for what it touched. Always:

1. Update `docs/pax_spec.yaml` `manifest_field_names` and any `entities.pax_yaml.required` reference.
2. Update every `pax/*/pax.yaml` (one-time `sed`).
3. Update the validator to accept both names (canonical preferred, legacy with a deprecation warning) for at least one release cycle.
4. Update build/registry scripts to emit the canonical name and accept the legacy name on read.
5. Update the guide examples + checklist + version-history entry.
6. The consistency-check script likely needs a small regex update to recognize the new code shape.

## Deprecating a legacy field name

Renaming a manifest field doesn't end the day the rename ships. The validator keeps accepting the legacy name until a declared sunset date. To deprecate cleanly:

1. In `docs/pax_spec.yaml`, append an entry under `legacy_field_aliases`:
   ```yaml
   legacy_field_aliases:
     - canonical: <new_name>
       legacy_name: <old_name>
       deprecated_at: "YYYY-MM-DD"   # date warnings start (usually today)
       remove_after: "YYYY-MM-DD"    # date hard-failure starts (usually +90d)
       migration: "Human-readable instruction for migrating."
   ```
2. The validator will:
   - silently accept the legacy name before `deprecated_at`,
   - emit a deprecation warning between `deprecated_at` and `remove_after`,
   - hard-fail with the migration instruction once today >= `remove_after`.
3. Any code that needs to read either name should use the canonical-or-legacy fallback pattern (e.g., `manifest.get(canon) or manifest.get(legacy)`); CI's consistency check accepts that shape.
4. After `remove_after` lands and any external consumers have caught up, remove the alias entry from `pax_spec.yaml` and the legacy fallback from scripts. The validator then fails fast with a more direct "unknown field" error.

Bumping `remove_after` to extend a window is a deliberate spec change — make it consciously, not as a way to dodge a failing CI.

## What CI enforces

`scripts/check_spec_consistency.py` runs in two workflows:

- `.github/workflows/validate-pack.yml` — every PR. Fail = merge blocked.
- `.github/workflows/publish-artifacts.yml` — every push to `main`. Fail = release not generated.

It asserts:

- Guide title and header version stamp match `current_version` + `last_updated`.
- Guide has a `## What's New in v<major(current_version)>` heading (catches the most likely narrative-drift case).
- Guide SCHEMA block enums match `enums` exactly.
- Guide FIELDS block entity manifest matches `entities` exactly.
- Guide version-history table rows match `version_history` (in order).
- **Inline examples in the guide.** Every fenced YAML/JSON block is scanned for `built_against_schema:`, `pax_type:`, `direction:`, `finding_type:`, `unit_of_analysis:`, etc. Values must be in the spec's enum or `valid_versions` list. Catches stale example values after a rename or enum removal.
- `scripts/validate_pax.py` literal-tuple fallbacks match the YAML.
- **Every `scripts/*.py` is AST-scanned** for module-level tuple/list literals of ≥3 short lowercase strings — the signature of an enum vocabulary. Any such literal must either (a) be one of the registered fallbacks in `validate_pax.py`, (b) appear in the consistency check's `KNOWN_REGISTERED` set, or (c) appear in `EXEMPT` with a reason. Catches "someone added a new spec-state constant in a new script and didn't register coverage."
- `scripts/build_pax.py` and `scripts/generate-registry.py` schema-version fallbacks match `defaults`.
- `README.md` and `CLAUDE.md` valid-versions enumerations match `valid_versions`.
- Every `pax/*/pax.yaml`'s `built_against_schema` is in `valid_versions`.

When CI fails, the output names the file, the line, what it claims, and what `pax_spec.yaml` says. Fix the file CI pointed at, not the YAML — the YAML is the source.

## Why this exists

A previous version of this repo had ~47 places that independently encoded the same spec facts (current version, valid versions, enum lists, entity field manifests). Drift was constant and silent. This file plus `docs/pax_spec.yaml` plus the consistency check eliminated the silent class. Drift now fails the build with a clear pointer.

If you find a new place that holds spec state and isn't checked, open a PR adding it to `scripts/check_spec_consistency.py`. The check's coverage is itself something that drifts — keep it complete.

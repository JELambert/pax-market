# PAX Documentation (Canonical)

This is the canonical home of the PAX authoring/usage guides.

## Files

- **`PAX_CREATION_GUIDE.md`** — How to author a PAX (manifest, constructs, findings, sources, playbooks, schema enums). The single source of truth for the schema. Edit here.
- **`PAX_USAGE_GUIDE.md`** — How to consume a published PAX (install, run engines, reproduce findings). Edit here.

## How edits propagate

1. Edit a guide in this directory and open a PR. CI validates the `<!-- PAX_SCHEMA_START -->` and `<!-- PAX_FIELDS_START -->` markers are intact.
2. On merge to `main`, `publish-artifacts.yml` creates a fresh `latest` GitHub Release with both guides as assets, alongside the existing registry artifacts.
3. **pax-website** (the marketplace site) fetches the guides from the release on its next build cycle (~5 min via the homelab autodeploy timer). They appear at:
   - `https://pax-market.com/PAX_CREATION_GUIDE.md`
   - `https://pax-market.com/PAX_USAGE_GUIDE.md`
4. **praxis** (the runtime engine) keeps a vendored copy of `PAX_CREATION_GUIDE.md` at `praxis/docs/PAX_CREATION_GUIDE.md`. Its `sync-guide.yml` workflow runs hourly to pull the latest from this repo's release.

## Why this lives here

The creation guide is the authoring contract for pack contributors. Contributors interact with `pax-market`, not with the runtime engine. Keeping the guide with the registry that consumes it (and not with the engine that processes it) reduces operational friction — see migration tracker JELambert/pax-market#72.

## Don't

- Don't remove or rename the `<!-- PAX_SCHEMA_START -->`, `<!-- PAX_SCHEMA_END -->`, `<!-- PAX_FIELDS_START -->`, or `<!-- PAX_FIELDS_END -->` markers. Praxis parses them at import time.
- Don't edit the vendored copy in praxis directly — the sync workflow will revert it.

# PAX Registry

## What This Is
Git-based registry for PAX (Portable Analytical eXpertise) packages. This repo IS the source of truth for published packs AND the canonical home of the PAX authoring/usage guides — no database dependency. The website frontend lives in the separate `pax-website` repo; the runtime engine lives in `praxis` (which vendors a copy of the creation guide from here).

**Browse at [pax-market.com](https://pax-market.com)**

## Architecture (Three-Repo Split)
```
This repo (pax-market) = REGISTRY + canonical docs
  pax/<name>/                    ← Pack source directories (currently 14 packs)
  docs/PAX_CREATION_GUIDE.md     ← Canonical authoring spec (parsed by praxis at import time)
  docs/PAX_USAGE_GUIDE.md        ← Canonical usage guide (LLM-feedable)
  scripts/generate-registry.py   ← Builds artifacts from pax/
  .github/workflows/
    validate-pack.yml            ← PR validation (schema, JSON, etc.)
    auto-merge-pack.yml          ← Auto-merge non-community PRs
    stamp-published-by.yml       ← Auto-stamp PR submitter login on community manifests
    publish-artifacts.yml        ← Creates GitHub Release on push to main (registry + guides)
    deploy-marketplace.yml       ← Build verification

pax-website repo = FRONTEND
  Fetches release artifacts (registry JSON + both guides) from this repo
  Generates Hugo pages from full-catalog.json
  Deploys to pax-market.com via homelab CT 105 (5-min poll)

praxis repo = RUNTIME ENGINE
  Vendors docs/PAX_CREATION_GUIDE.md → praxis/docs/PAX_CREATION_GUIDE.md
  pax_schema.py parses the vendored copy at import time (regex on PAX_SCHEMA_START / PAX_FIELDS_START blocks)
  .github/workflows/sync-guide.yml refreshes the vendored copy hourly from this repo's `latest` release
```

## Key Commands
- `python3 scripts/generate-registry.py` — Generate artifacts to `dist/`
- Artifacts: `dist/registry.json`, `dist/constructs.json`, `dist/full-catalog.json`, `dist/pax/*.pax.tar.gz`
- Release assets (from `publish-artifacts.yml`): the four `dist/` files above + `dist/pax-archives.tar` + `docs/PAX_CREATION_GUIDE.md` + `docs/PAX_USAGE_GUIDE.md`

## How Packs Are Published
1. Contributor submits pack via [submit.pax-market.com](https://submit.pax-market.com) or opens a PR
2. `validate-pack.yml` validates schema on the PR
3. `stamp-published-by.yml` injects `published_by: <PR-author-login>` into manifests missing the field (community attribution)
4. Non-community PRs auto-merge; community PRs require manual review
5. On merge to `main` → `publish-artifacts.yml` creates/updates GitHub Release (`latest` tag) with all 6 assets
6. pax-website detects new release → fetches artifacts → rebuilds → deploys to pax-market.com

## How Guide Edits Propagate
1. Edit `docs/PAX_CREATION_GUIDE.md` or `docs/PAX_USAGE_GUIDE.md` in a PR.
2. `publish-artifacts.yml`'s "Verify guide markers" step asserts `<!-- PAX_SCHEMA_START -->` and `<!-- PAX_FIELDS_START -->` are intact (loud failure otherwise).
3. On merge → fresh release with both guides as assets.
4. **pax-website** fetches the release → guides served at `https://pax-market.com/PAX_CREATION_GUIDE.md` and `.../PAX_USAGE_GUIDE.md` within 5 min.
5. **praxis** `sync-guide.yml` runs hourly → pulls `PAX_CREATION_GUIDE.md` from this repo's release → commits as `praxis-sync-bot` to praxis main → next praxis release picks up the new schema.

## CI Workflows
- **validate-pack.yml** — Runs on PRs with `pax/**` changes. Checks required fields, valid enums, JSON validity.
- **stamp-published-by.yml** — Runs on PRs with `pax/**/pax.yaml` changes. Auto-stamps `published_by: <PR-author-login>` if not declared.
- **auto-merge-pack.yml** — Enables squash merge on valid pack PRs. Skips community PRs (labeled `community`, from a fork, or authored by anyone other than the repo owner) — those need manual review.
- **publish-artifacts.yml** — On push to main affecting `pax/**`, `scripts/generate-registry.py`, or `docs/**`, runs `generate-registry.py` and creates GitHub Release with all artifacts (4 registry + 2 guides).
- **deploy-marketplace.yml** — Build verification.

## Project Structure
```
pax/                         14 pack directories (source of truth for packs)
docs/                        Canonical PAX guides
  PAX_CREATION_GUIDE.md      Authoring spec — praxis parses this at import time
  PAX_USAGE_GUIDE.md         LLM-feedable usage guide
  README.md                  How edits propagate to website + praxis
scripts/
  generate-registry.py       Builds dist/ artifacts from pax/
.github/workflows/
  validate-pack.yml          PR validation
  stamp-published-by.yml     Auto-attribution
  auto-merge-pack.yml        Auto-merge for non-community PRs
  publish-artifacts.yml      Artifact + guide release on merge
  deploy-marketplace.yml     Build verify
dist/                        .gitignored — build output
```

## Pack Schema
- Required manifest fields: `name`, `version`, `description`, `pax_type`, `schema_version`
- Valid `pax_type`: paper, topic, field, engine, enterprise
- Valid `schema_version`: "1.0", "2.0", "3.0"
- Knowledge files: `constructs.json`, `findings.json`, `sources.json`, `domain.json`
- Optional: `propositions.json`, `construct_relationships.json`, `playbooks/*.yaml`
- v3 additions: `canonical_constructs.json`, `construct_relations.json` (canonical-construct backbone); `unit_of_analysis`, `scope_conditions`, `sample_n` on findings; `canonical_id`, `operationalization_id`, `coding_rule` on constructs

## Task Delegation

Spawn subagents to isolate context, parallelize independent work, or offload bulk mechanical tasks. Don't spawn when the parent needs the reasoning, when synthesis requires holding things together, or when spawn overhead dominates.

Pick the cheapest model that can do the subtask well:
- Haiku: bulk mechanical work, no judgment
- Sonnet: scoped research, code exploration, in-scope synthesis
- Opus: subtasks needing real planning or tradeoffs

If a subagent realizes it needs a higher tier than itself, return to the parent.

Parent owns final output and cross-spawn synthesis. User instructions override.

## Don't
- Don't remove or rename the `<!-- PAX_SCHEMA_START -->`, `<!-- PAX_SCHEMA_END -->`, `<!-- PAX_FIELDS_START -->`, or `<!-- PAX_FIELDS_END -->` markers in `docs/PAX_CREATION_GUIDE.md`. Praxis parses them at import time; corruption breaks every consumer.
- Don't edit the praxis vendored copy (`praxis/docs/PAX_CREATION_GUIDE.md`) directly — it'll be overwritten on the next sync.
- Don't hardcode schema version lists in new code — they belong in the SCHEMA_START block.

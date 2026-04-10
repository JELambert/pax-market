# PAX Registry

## What This Is
Git-based registry for PAX (Portable Analytical eXpertise) packages. This repo IS the source of truth for published packs — no database dependency. The website frontend lives in the separate `pax-website` repo.

**Browse at [pax-market.com](https://pax-market.com)**

## Architecture (Two-Repo Split)
```
This repo (pax-market) = REGISTRY
  pax/<name>/                    ← Pack source directories (64+ packs)
  scripts/generate-registry.py   ← Builds artifacts from pax/
  .github/workflows/
    validate-pack.yml            ← PR validation
    auto-merge-pack.yml          ← Auto-merge non-community PRs
    publish-artifacts.yml        ← Creates GitHub Release on push to main

pax-website repo = FRONTEND
  Fetches artifacts from this repo's GitHub Releases
  Generates Hugo pages from full-catalog.json
  Deploys to pax-market.com
```

## Key Commands
- `python3 scripts/generate-registry.py` — Generate artifacts to `dist/`
- Artifacts: `dist/registry.json`, `dist/constructs.json`, `dist/full-catalog.json`, `dist/pax/*.pax.tar.gz`

## How Packs Are Published
1. Contributor submits pack via [submit.pax-market.com](https://submit.pax-market.com) or opens a PR
2. `validate-pack.yml` validates schema on the PR
3. Non-community PRs auto-merge; community PRs require manual review
4. On merge to `main` → `publish-artifacts.yml` creates/updates GitHub Release (`latest` tag)
5. pax-website detects new release → fetches artifacts → rebuilds → deploys to pax-market.com

## CI Workflows
- **validate-pack.yml** — Runs on PRs with `pax/**` changes. Checks required fields, valid enums, JSON validity.
- **auto-merge-pack.yml** — Enables squash merge on valid pack PRs. Skips PRs labeled `community`.
- **publish-artifacts.yml** — On push to main, runs `generate-registry.py` and creates GitHub Release with all artifacts.

## Project Structure
```
pax/                         64+ pack directories (source of truth)
scripts/
  generate-registry.py       Builds dist/ artifacts from pax/
  generate-from-git.py       LEGACY (monorepo generator, being removed)
.github/workflows/
  validate-pack.yml          PR validation
  auto-merge-pack.yml        Auto-merge for non-community PRs
  publish-artifacts.yml      Artifact publishing on merge
dist/                        .gitignored — build output
```

## Pack Schema
- Required manifest fields: `name`, `version`, `description`, `pax_type`, `schema_version`
- Valid `pax_type`: paper, topic, field, engine, enterprise
- Valid `schema_version`: "1.0", "2.0"
- Knowledge files: `constructs.json`, `findings.json`, `sources.json`, `domain.json`
- Optional: `propositions.json`, `construct_relationships.json`, `playbooks/*.yaml`

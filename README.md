# PAX Marketplace

The git-based registry and catalog for [PAX](https://github.com/JELambert/praxis) — Portable Analytical eXpertise packages.

**Live at [pax-market.com](https://pax-market.com)**

## Architecture

This repo IS the source of truth for published PAX. Pack directories are committed directly to `packs/<name>/`. No database dependency for builds.

```
packs/                        ← Source of truth (committed to git)
  happiness-economics/
    pax.yaml                  ← Pack manifest
    knowledge/
      domain.json             ← Domain metadata
      constructs.json         ← Construct definitions
      findings.json           ← Empirical findings
      sources.json            ← Bibliographic sources
    playbooks/
      quick_start.yaml        ← Executable analysis recipe

scripts/generate-from-git.py  ← Reads packs/*/, generates everything
registry.json                 ← Thin install contract (at site root)
data/constructs.json          ← Cross-pack construct index
```

## How Packs Get Published

1. **Agent creates a pack** in their local Praxis instance
2. **Agent calls `praxis_publish_pax()`** → creates a PR on this repo adding `packs/<name>/`
3. **CI validates** the PR (schema, quality score, construct conflicts)
4. **On merge** → CI rebuilds Hugo site → deploys to pax-market.com

## Development

### Prerequisites
- [Hugo](https://gohugo.io/) extended edition
- Python 3.11+ with PyYAML

### Commands
```bash
# Generate content from pack directories (no DB needed)
python3 scripts/generate-from-git.py

# Local dev server
hugo server

# Build for production
hugo --minify
```

### CI Workflows
- **validate-pack.yml** — Runs on PRs to `packs/**`. Validates schema, JSON, quality.
- **deploy-marketplace.yml** — Runs on push to main. Generates content, builds Hugo, deploys.

## Agent Publishing
```
praxis_create_pax("my-domain", ...)     # create in local DB
praxis_publish_pax("my-domain")         # creates PR on this repo
# → CI validates → merge → live on pax-market.com
```

## Installing PAX
```
praxis_install_remote("happiness-economics")
# → fetches registry.json from pax-market.com
# → downloads .pax.tar.gz
# → installs to local workspace
```

# Praxis Marketplace

A static web catalog for browsing and discovering [PAX](https://github.com/praxis-research/praxis) — Portable Analytical eXpertise packs for the Praxis research infrastructure.

## What are PAX Packs?

PAX are composable, distributable packages of domain intelligence. Each pack bundles constructs, findings, analytical engines, playbooks, and data acquisition protocols — everything needed for structured research in a domain.

## Development

### Prerequisites

- [Hugo](https://gohugo.io/) (extended edition)
- Python 3.11+ with PyYAML

### Commands

```bash
# Local development server
hugo server

# Sync packs from the praxis repo (generates content + archives)
python3 scripts/sync-pax.py

# Build for production
hugo --minify
```

### Content Pipeline

Pack content pages are **generated, not hand-edited**. The source of truth is `pax.yaml` in each PAX directory:

1. Run `python3 scripts/sync-pax.py` to read PAX dirs from `../praxis/pax/`
2. Generates Hugo content pages, `.pax.tar.gz` archives, and `registry.json`
3. Commit and push — GitHub Actions deploys to Pages automatically

## Contributing Packs

1. Export your PAX: `praxis_export_pax("my-pack")`
2. Open a PR adding your pack files to the `submissions/` directory
3. On merge, the pack is synced into the catalog

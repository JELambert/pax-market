# PAX Marketplace

A static web catalog for browsing and discovering [PAX](https://github.com/JELambert/praxis) — Portable Analytical eXpertise for the Praxis research infrastructure.

**Live at [pax-market.com](https://pax-market.com)**

## What is PAX?

PAX are composable, distributable packages of domain intelligence. Each PAX bundles constructs, findings, analytical engines, playbooks, and data acquisition protocols — everything needed for structured research in a domain.

## Development

### Prerequisites

- [Hugo](https://gohugo.io/) (extended edition)
- Python 3.11+ with PyYAML

### Commands

```bash
# Local development server
hugo server

# Sync PAX from the praxis repo (generates content + archives)
python3 scripts/sync-pax.py

# Build for production
hugo --minify

# Deploy to Proxmox (sync + build + deploy)
./scripts/deploy.sh
```

### Content Pipeline

PAX content pages are **generated, not hand-edited**. The source of truth is `pax.yaml` in each PAX directory:

1. Run `python3 scripts/sync-pax.py` to read PAX dirs from `../praxis/pax/`
2. Generates Hugo content pages, `.pax.tar.gz` archives, and `registry.json`
3. Commit and push — GitHub Actions deploys to Pages automatically

### Agent Publishing

Agents can publish PAX directly via the Praxis MCP:

```
praxis_create_pax("my-domain", ...)    → creates PAX
praxis_publish_pax("my-domain")        → publishes to pax-market.com
```

## Contributing PAX

1. Export your PAX: `praxis_export_pax("my-pax")`
2. Open a PR adding your PAX files
3. Or publish directly via `praxis_publish_pax()` if you have MCP access

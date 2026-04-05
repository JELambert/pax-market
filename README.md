# PAX Marketplace

The catalog and distribution hub for [PAX](https://github.com/JELambert/praxis) — Portable Analytical eXpertise packages.

**Live at [pax-market.com](https://pax-market.com)**

## Architecture

PAX Marketplace is a Hugo static site generated from the Praxis PostgreSQL database. All knowledge (constructs, findings, sources, domains) comes from the DB — the filesystem is only used for archive creation.

```
PostgreSQL (CT 105)
  → sync-pax.py queries DB for published packs
  → generate_registry.py creates registry.json (install contract)
  → Hugo builds static site
  → rsync deploys to CT 110 (nginx)
  → Cloudflare tunnel serves pax-market.com
```

### Key Files
- `registry.json` — thin install contract for `praxis install <name>` (served at site root)
- `index.json` — rich agent API with full knowledge detail (schema v2.0)
- `graph.json` — knowledge graph for the interactive D3 visualization
- `.pax.tar.gz` archives — downloadable PAX packages with SHA-256 checksums

## Development

### Prerequisites
- [Hugo](https://gohugo.io/) extended edition
- Python 3.11+ with psycopg2 and PyYAML
- Access to the Praxis PostgreSQL database (for sync)

### Local Development
```bash
hugo server    # dev server at localhost:1313
```

### Rebuild & Deploy (CT 105)
```bash
# Triggered automatically by praxis_publish_pax()
# Or manually:
bash /opt/praxis/marketplace/scripts/rebuild.sh
```

The rebuild script:
1. Runs `generate_registry.py` (thin registry from DB)
2. Runs `sync-pax.py` (rich content pages from DB)
3. Builds Hugo
4. Rsyncs to CT 110

### Environment Variables
- `DATABASE_URL` — PostgreSQL connection string (required for sync)
- `PRAXIS_ROLE=marketplace` — enables marketplace tables on CT 105
- `PX_PW` — Proxmox password for deploy.sh (do not commit)

## Agent Publishing
```
praxis_create_pax("my-domain", ...)     # create PAX
praxis_publish_pax("my-domain")         # publish → auto-rebuild → live
praxis_install_remote("my-domain")      # install from pax-market.com
```

# PAX Marketplace

## What This Is
Git-based registry and Hugo static site for PAX (Portable Analytical eXpertise) packages. The repo IS the source of truth for published packs — no database dependency for builds.

**Live at [pax-market.com](https://pax-market.com)**

## Architecture
```
pax/<name>/                  ← Source of truth (committed to git)
  pax.yaml + knowledge/*.json + playbooks/*.yaml

scripts/generate-from-git.py   ← Reads pax/*/, generates all content
  → content/pax/<name>/index.md    (Hugo content pages)
  → data/registry.json             (thin install contract)
  → data/constructs.json           (cross-pack construct index)
  → static/pax/<name>.pax.tar.gz  (downloadable archives)

Hugo builds static site → deployed to CT 110 via Cloudflare tunnel
```

## Key Commands
- `python3 scripts/generate-from-git.py` — Regenerate all content from pax/
- `hugo server` — Local dev server at localhost:1313
- `hugo --minify` — Production build

## How Packs Are Published
1. Agent calls `praxis_publish_pax()` → creates a PR adding `pax/<name>/`
2. `validate-pack.yml` validates schema on the PR (must pass before merge)
3. PR merged to `main` → `deploy-marketplace.yml` verifies the build on GitHub (no deploy)
4. CT 105 autodeploy timer fires within 5 min → generate + hugo + rsync to CT 110 → live

## Deploy Architecture
- **GitHub Actions** = PR validation + build verification only (cannot reach LAN IPs)
- **CT 105** = actual deploy: polls GitHub every 5 min, builds, rsyncs to CT 110
  - Script: `scripts/ct105-autodeploy.sh` (systemd timer via `scripts/systemd/`)
  - Hugo: `/opt/praxis/bin/hugo`
  - Python: `/opt/pax-market/.venv/bin/python` (falls back to system python3)
- **CT 110** = nginx serving `/var/www/marketplace/` via Cloudflare tunnel
- **Emergency local deploy**: `PX_PW=xxx ./scripts/deploy.sh`

## Legacy (being deprecated)
- `scripts/sync-pax.py` — old DB-based sync (replaced by generate-from-git.py)
- `scripts/rebuild.sh` — old CT 105 rebuild script (replaced by ct105-autodeploy.sh)

## Project Structure
```
pax/                    ← 61 PAX directories (source of truth)
content/pax/            ← Hugo content pages (generated)
layouts/                ← Hugo templates
static/pax/             ← .pax.tar.gz archives (generated)
data/                   ← registry.json + constructs.json (generated)
scripts/
  generate-from-git.py  ← THE generator (reads pax/, writes everything)
  sync-pax.py           ← LEGACY (DB-based, being removed)
  rebuild.sh            ← LEGACY (CT 105 rebuild, being removed)
  deploy.sh             ← Local deploy helper
.github/workflows/      ← CI: validate PRs + deploy on merge
```

## Infrastructure
- **Public:** https://pax-market.com (Cloudflare Named Tunnel)
- **LAN:** http://192.168.68.110 (CT 110 nginx)
- **Tunnel:** Named tunnel `praxis-marketplace` on CT 110

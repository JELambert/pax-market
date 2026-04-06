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
2. CI validates (`.github/workflows/validate-pack.yml`)
3. On merge, CI rebuilds (`.github/workflows/deploy-marketplace.yml`)
4. No DB, no CT 105 rebuild.sh — everything from git

## Legacy (being deprecated)
- `scripts/sync-pax.py` — old DB-based sync (replaced by generate-from-git.py)
- `scripts/rebuild.sh` — old CT 105 rebuild script (replaced by GitHub Actions)
- `.venv` on CT 105 — no longer needed for marketplace builds

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

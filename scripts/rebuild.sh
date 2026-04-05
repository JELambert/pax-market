#!/bin/bash
# rebuild.sh — Rebuild marketplace on CT 105 and deploy to CT 110
#
# Flow: git pull → generate registry → sync from DB → Hugo build → deploy
#
# Called by marketplace.py:rebuild_marketplace() after a pack is published.
# Marketplace repo: /opt/pax-market (git clone of JELambert/pax-market)
# Praxis repo: /opt/praxis (has generate_registry.py in marketplace/scripts/)

set -euo pipefail

PRAXIS_DIR="/opt/praxis"
MARKETPLACE_DIR="/opt/pax-market"
HUGO_BIN="/opt/praxis/bin/hugo"
PYTHON="$MARKETPLACE_DIR/.venv/bin/python"
UV_BIN="/root/.local/bin/uv"
CT110_IP="192.168.68.110"

# Load env vars
if [ -f "$PRAXIS_DIR/.env" ]; then
    export $(grep -v '^#' "$PRAXIS_DIR/.env" | xargs)
fi

# Step 0: Pull latest from git
echo "==> Pulling latest from git..."
cd "$MARKETPLACE_DIR"
git pull --ff-only origin main 2>&1 || echo "  (git pull skipped)"

# Step 1: Generate registry.json (from praxis repo tooling)
echo "==> Generating registry.json..."
cd "$PRAXIS_DIR" && $UV_BIN run python marketplace/scripts/generate_registry.py
cd "$MARKETPLACE_DIR"
cp "$PRAXIS_DIR/marketplace/data/registry.json" static/registry.json

# Step 2: Sync rich content from database
echo "==> Syncing published packs from database..."
"$PYTHON" scripts/sync-pax.py --praxis-dir "$PRAXIS_DIR"

# Step 3: Build Hugo
echo "==> Building Hugo site..."
"$HUGO_BIN" --minify

# Step 4: Deploy to CT 110
echo "==> Deploying to CT 110..."
rsync -a --delete public/ "root@${CT110_IP}:/var/www/marketplace/"

echo "==> Rebuild complete!"

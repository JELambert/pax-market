#!/bin/bash
# rebuild.sh — Rebuild marketplace on CT 105 and deploy to CT 110
#
# Flow: git pull → generate registry → sync from DB → Hugo build → deploy
#
# Called by marketplace.py:rebuild_marketplace() after a pack is published.

set -euo pipefail

PRAXIS_DIR="/opt/praxis"
MARKETPLACE_DIR="/opt/praxis/marketplace"
HUGO_BIN="/opt/praxis/bin/hugo"
PYTHON="$MARKETPLACE_DIR/.venv/bin/python"
UV_BIN="/root/.local/bin/uv"
CT110_IP="192.168.68.110"

# Load env vars
if [ -f "$PRAXIS_DIR/.env" ]; then
    export $(grep -v '^#' "$PRAXIS_DIR/.env" | xargs)
fi

# Step 0: Pull latest from git (single source of truth for templates/config)
echo "==> Pulling latest from git..."
cd "$MARKETPLACE_DIR"
git pull --ff-only origin main 2>&1 || echo "  (git pull skipped — may be detached or no remote changes)"

# Step 1: Generate registry.json (thin install contract) via praxis tooling
echo "==> Generating registry.json..."
cd "$PRAXIS_DIR" && $UV_BIN run python marketplace/scripts/generate_registry.py
cd "$MARKETPLACE_DIR"

# Copy registry.json to Hugo static dir (served at site root)
cp "$PRAXIS_DIR/marketplace/data/registry.json" static/registry.json

# Step 2: Sync rich content from database (index.json, content pages, archives)
echo "==> Syncing published packs from database..."
"$PYTHON" scripts/sync-pax.py --praxis-dir "$PRAXIS_DIR"

# Step 3: Build Hugo
echo "==> Building Hugo site..."
"$HUGO_BIN" --minify

# Step 4: Deploy to CT 110
echo "==> Deploying to CT 110..."
rsync -a --delete public/ "root@${CT110_IP}:/var/www/marketplace/"

echo "==> Rebuild complete!"

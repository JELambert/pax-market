#!/bin/bash
# rebuild.sh — Rebuild marketplace on CT 105 and deploy to CT 110
#
# Called by marketplace.py:rebuild_marketplace() after a pack is published.
# Also callable manually or via cron.
#
# Expects to run on CT 105 at /opt/praxis/marketplace/scripts/rebuild.sh

set -euo pipefail

PRAXIS_DIR="/opt/praxis"
MARKETPLACE_DIR="/opt/praxis/marketplace"
HUGO_BIN="/opt/praxis/bin/hugo"
CT110_IP="192.168.68.110"
UV_BIN="/root/.local/bin/uv"
export PATH="/root/.local/bin:$PATH"

# Load DATABASE_URL from .env for sync-pax.py's --published-only mode
if [ -f "$PRAXIS_DIR/.env" ]; then
    export $(grep -v '^#' "$PRAXIS_DIR/.env" | xargs)
fi

cd "$MARKETPLACE_DIR"

# Step 1: Sync published packs
# sync-pax.py uses MARKETPLACE_ROOT (parent of scripts/) for output dirs,
# so we run it from within the marketplace dir but use uv from the praxis project
echo "==> Syncing published packs..."
cd "$PRAXIS_DIR" && $UV_BIN run python "$MARKETPLACE_DIR/scripts/sync-pax.py" \
    --praxis-dir "$PRAXIS_DIR" --published-only
cd "$MARKETPLACE_DIR"

# Step 2: Build Hugo
echo "==> Building Hugo site..."
"$HUGO_BIN" --minify

# Step 3: Deploy to CT 110
echo "==> Deploying to CT 110..."
rsync -a --delete public/ "root@${CT110_IP}:/var/www/marketplace/"

echo "==> Rebuild complete!"

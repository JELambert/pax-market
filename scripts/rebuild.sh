#!/bin/bash
# rebuild.sh — Rebuild marketplace on CT 105 and deploy to CT 110
#
# All knowledge comes from PostgreSQL (single source of truth).
# Filesystem is only used for archives and playbooks.
#
# Called by marketplace.py:rebuild_marketplace() after a pack is published.

set -euo pipefail

PRAXIS_DIR="/opt/praxis"
MARKETPLACE_DIR="/opt/praxis/marketplace"
HUGO_BIN="/opt/praxis/bin/hugo"
PYTHON="$MARKETPLACE_DIR/.venv/bin/python"
CT110_IP="192.168.68.110"

# Load DATABASE_URL from .env
if [ -f "$PRAXIS_DIR/.env" ]; then
    export $(grep -v '^#' "$PRAXIS_DIR/.env" | xargs)
fi

cd "$MARKETPLACE_DIR"

# Step 1: Sync from database
echo "==> Syncing published packs from database..."
"$PYTHON" scripts/sync-pax.py --praxis-dir "$PRAXIS_DIR"

# Step 2: Build Hugo
echo "==> Building Hugo site..."
"$HUGO_BIN" --minify

# Step 3: Deploy to CT 110
echo "==> Deploying to CT 110..."
rsync -a --delete public/ "root@${CT110_IP}:/var/www/marketplace/"

echo "==> Rebuild complete!"

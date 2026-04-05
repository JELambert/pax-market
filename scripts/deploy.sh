#!/bin/bash
# deploy.sh — Build and deploy PAX Marketplace to Proxmox CT 110
#
# Usage:
#   ./scripts/deploy.sh              # sync packs + build + deploy
#   ./scripts/deploy.sh --build-only # build + deploy (skip pack sync)
#   ./scripts/deploy.sh --url        # just show the current tunnel URL
#
# Prerequisites: hugo, python3, pyyaml, sshpass

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
PX_HOST="192.168.68.70"
PX_PW="vaultlock1"
CT_ID="110"

ssh_cmd() {
  sshpass -p "$PX_PW" ssh -o StrictHostKeyChecking=no -o LogLevel=ERROR "root@$PX_HOST" "$@"
}

ct_exec() {
  ssh_cmd "pct exec $CT_ID -- bash -c $(printf '%q' "$1")"
}

DOMAIN="https://pax-market.com"

if [ "${1:-}" = "--url" ]; then
  echo "Marketplace URL: $DOMAIN"
  echo "  LAN: http://192.168.68.110"
  exit 0
fi

cd "$PROJECT_DIR"

# Step 1: Sync packs (unless --build-only)
if [ "${1:-}" != "--build-only" ]; then
  echo "==> Syncing PAX packs from praxis repo..."
  python3 scripts/sync-pax.py
  echo
fi

# Step 2: Build Hugo
echo "==> Building Hugo site..."
hugo --minify
echo

# Step 3: Deploy to container
echo "==> Deploying to CT $CT_ID (192.168.68.110)..."
ct_exec "rm -rf /var/www/marketplace && mkdir -p /var/www/marketplace"
tar czf - -C public . | ssh_cmd "pct exec $CT_ID -- tar xzf - -C /var/www/marketplace"
echo "  Deployed $(du -sh public | cut -f1) to /var/www/marketplace"

# Step 4: Show access URLs
echo
echo "==> Deployment complete!"
echo "  LAN: http://192.168.68.110"
echo "  Public: $DOMAIN"

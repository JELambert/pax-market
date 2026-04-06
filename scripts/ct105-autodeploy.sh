#!/bin/bash
# ct105-autodeploy.sh — PAX Marketplace auto-deploy from CT 105
#
# Run via systemd timer every 5 minutes.
# Checks GitHub for new commits on main; if found:
#   git pull → generate-from-git.py → hugo --minify → rsync to CT 110
#
# Safe to run when already up to date (no-op).
# Never modifies CT 110's live site unless the build fully succeeds.
#
# Logs to /var/log/pax-autodeploy.log

set -euo pipefail

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
REPO_DIR="/opt/pax-market"
CT110_WEBROOT="root@192.168.68.110:/var/www/marketplace/"
STAGING_DIR="/tmp/pax-marketplace-staging"
LOG_FILE="/var/log/pax-autodeploy.log"
PYTHON_BIN="/opt/pax-market/.venv/bin/python"
HUGO_BIN="/opt/praxis/bin/hugo"
LOCK_FILE="/var/run/pax-autodeploy.lock"

# Fall back to system python3 if venv not present
if [ ! -f "$PYTHON_BIN" ]; then
    PYTHON_BIN="python3"
fi

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOG_FILE"
}

# ---------------------------------------------------------------------------
# Lock: prevent overlapping runs
# ---------------------------------------------------------------------------
exec 200>"$LOCK_FILE"
if ! flock -n 200; then
    log "Already running (lock held). Skipping this cycle."
    exit 0
fi

# ---------------------------------------------------------------------------
# Check for new commits
# ---------------------------------------------------------------------------
cd "$REPO_DIR"

log "Fetching origin/main..."
git fetch origin main --quiet 2>>"$LOG_FILE"

LOCAL_HASH=$(git rev-parse HEAD)
REMOTE_HASH=$(git rev-parse origin/main)

if [ "$LOCAL_HASH" = "$REMOTE_HASH" ]; then
    log "Already up to date at ${LOCAL_HASH:0:8}. Nothing to do."
    exit 0
fi

log "New commits detected: ${LOCAL_HASH:0:8} → ${REMOTE_HASH:0:8}"
git log --oneline "${LOCAL_HASH}..${REMOTE_HASH}" 2>>"$LOG_FILE" | while read -r line; do
    log "  $line"
done

# ---------------------------------------------------------------------------
# Pull latest
# ---------------------------------------------------------------------------
log "Pulling origin/main..."
git pull --ff-only origin main >>"$LOG_FILE" 2>&1

NEW_HASH=$(git rev-parse HEAD)
log "Now at ${NEW_HASH:0:8}"

# ---------------------------------------------------------------------------
# Generate content
# ---------------------------------------------------------------------------
log "Running generate-from-git.py..."
if ! "$PYTHON_BIN" scripts/generate-from-git.py >>"$LOG_FILE" 2>&1; then
    log "ERROR: generate-from-git.py failed. Aborting — CT 110 unchanged."
    git reset --hard "${LOCAL_HASH}" >>"$LOG_FILE" 2>&1
    exit 1
fi

# ---------------------------------------------------------------------------
# Hugo build into staging dir
# ---------------------------------------------------------------------------
log "Building Hugo site..."
rm -rf "$STAGING_DIR"

if ! "$HUGO_BIN" --minify --destination "$STAGING_DIR" >>"$LOG_FILE" 2>&1; then
    log "ERROR: Hugo build failed. Aborting — CT 110 unchanged."
    git reset --hard "${LOCAL_HASH}" >>"$LOG_FILE" 2>&1
    exit 1
fi

# ---------------------------------------------------------------------------
# Verify build output
# ---------------------------------------------------------------------------
if [ ! -f "$STAGING_DIR/index.html" ]; then
    log "ERROR: No index.html in staging. Aborting."
    git reset --hard "${LOCAL_HASH}" >>"$LOG_FILE" 2>&1
    exit 1
fi

if [ ! -f "$STAGING_DIR/registry.json" ]; then
    log "ERROR: registry.json missing from staging. Aborting."
    git reset --hard "${LOCAL_HASH}" >>"$LOG_FILE" 2>&1
    exit 1
fi

HTML_COUNT=$(find "$STAGING_DIR" -name '*.html' | wc -l)
PACK_COUNT=$(find "$STAGING_DIR/pax" -name '*.pax.tar.gz' 2>/dev/null | wc -l)
log "Build verified: ${HTML_COUNT} HTML files, ${PACK_COUNT} pack archives"

if [ "$HTML_COUNT" -lt 10 ]; then
    log "ERROR: Suspiciously few HTML files (${HTML_COUNT}). Refusing to deploy."
    git reset --hard "${LOCAL_HASH}" >>"$LOG_FILE" 2>&1
    exit 1
fi

# ---------------------------------------------------------------------------
# rsync to CT 110
# ---------------------------------------------------------------------------
log "Deploying to CT 110 via rsync..."
if ! rsync -a --delete "$STAGING_DIR/" "$CT110_WEBROOT" >>"$LOG_FILE" 2>&1; then
    log "ERROR: rsync to CT 110 failed. Live site may be in an inconsistent state — check CT 110."
    exit 1
fi

rm -rf "$STAGING_DIR"

log "Deployment complete: ${NEW_HASH:0:8} (${HTML_COUNT} pages, ${PACK_COUNT} pack archives)"
log "  Live: https://pax-market.com"

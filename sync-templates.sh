#!/bin/bash
# Sync templates and static files to platform-specific directories
set -e

for dir in snow-flask-whoami-aws snow-flask-whoami-az snow-flask-whoami-gpc; do
    if [ -d "$dir" ]; then
        echo "Syncing to $dir..."
        cp -r templates/* "$dir/templates/" 2>/dev/null || mkdir -p "$dir/templates" && cp -r templates/* "$dir/templates/"
        cp -r static/* "$dir/static/" 2>/dev/null || mkdir -p "$dir/static" && cp -r static/* "$dir/static/"
    fi
done

echo "Sync complete."

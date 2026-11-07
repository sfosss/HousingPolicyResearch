#!/usr/bin/env bash
# Compatibility entry point; keep one authoritative setup implementation.
set -euo pipefail
exec bash "$(dirname -- "${BASH_SOURCE[0]}")/../setup.sh" "$@"

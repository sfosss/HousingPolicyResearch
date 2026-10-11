#!/bin/bash
# Restored from PR #35; run the shared checker from any working directory.
set -eu

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="${SCRIPT_DIR}/preflight_check.py"

if ! command -v python3 >/dev/null 2>&1; then
    echo "Error: Python 3.8+ is required and python3 is not in PATH" >&2
    exit 1
fi
if [ ! -f "${PYTHON_SCRIPT}" ]; then
    echo "Error: preflight_check.py not found at ${PYTHON_SCRIPT}" >&2
    exit 1
fi

# Preserve the checker's exit status. No credentials or .env file are required.
exec python3 "${PYTHON_SCRIPT}" "$@"


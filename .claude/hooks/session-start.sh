#!/bin/bash
# SessionStart hook: install Python dependencies for Claude Code on the web.
# Local sessions skip it, since this Mac already has its own Python setup.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

cd "$CLAUDE_PROJECT_DIR"
python3 -m pip install --quiet -r requirements.txt pytest

# Tests import from src/ (see [tool.pytest.ini_options] in pyproject.toml)
if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  echo "export PYTHONPATH=\"$CLAUDE_PROJECT_DIR/src\"" >> "$CLAUDE_ENV_FILE"
fi

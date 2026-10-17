#!/bin/bash
# SessionStart hook: prepare Python for Claude Code on the web.
# Local developers install requirements.txt explicitly.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# Only the startup-matched hook passes --install. Other events just restore env.
if [ "${1:-}" = "--install" ]; then
  cd "$CLAUDE_PROJECT_DIR"
  python3 -m pip install --quiet -r requirements.txt
  exit 0
fi

# Tests import from src/ (see [tool.pytest.ini_options] in pyproject.toml)
if [ -n "${CLAUDE_ENV_FILE:-}" ]; then
  echo "export PYTHONPATH=\"$CLAUDE_PROJECT_DIR/src\"" >> "$CLAUDE_ENV_FILE"
fi

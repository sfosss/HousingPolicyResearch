#!/usr/bin/env bash
# Install development tooling without credentials or formatting tracked files.
set -euo pipefail

repo_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$repo_root"
python3 -c 'import sys; assert sys.version_info >= (3, 11), "Python 3.11+ required"'
git rev-parse --is-inside-work-tree >/dev/null

if [ ! -x .venv/bin/python ]; then
    python3 -m venv .venv
fi
.venv/bin/python -c 'import sys; assert sys.version_info >= (3, 11), "Existing .venv requires Python 3.11+; recreate it with a supported interpreter"'
.venv/bin/python -m pip install --disable-pip-version-check -r requirements.txt
.venv/bin/python -m pip check
.venv/bin/pre-commit validate-config
.venv/bin/pre-commit install --install-hooks
if [ ! -e .env ]; then
    (umask 077; cp .env.template .env)
fi
.venv/bin/python -m pytest -q

echo "Setup complete. Activate with: source $repo_root/.venv/bin/activate"
echo "Run quality checks explicitly: pre-commit run --all-files"
echo "Live integrations are optional; configure an ignored .env separately."

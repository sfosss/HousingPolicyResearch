# Repository instructions

This repository contains housing policy research and Python tooling.

- Use Python 3.11+ and Git. Run `bash setup.sh` from any directory to install the local `.venv`, development dependencies, and pre-commit hooks.
- Activate `.venv` before running `python -m pytest -q` or `pre-commit run --all-files`.
- Keep `requirements.txt` and the dependency list in `pyproject.toml` synchronized.
- Tests must use fixtures or mocks for external services. Setup and unit tests require no API keys.
- Keep credentials in ignored local configuration or Actions secrets; never commit credential values.
- Root `CLAUDE.md` and `.github/copilot-instructions.md` contain additional tool and repository guidance.
- Agent instructions must be readable in a fresh clone. Keep personal configuration outside the repository; do not commit symlinks pointing outside the checkout.
- Preserve research artifacts and canonical legislation. Follow APA guidance and record AI-authored documentation in `docs/generative-output-version-control.md`.

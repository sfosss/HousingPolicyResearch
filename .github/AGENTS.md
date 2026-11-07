# GitHub automation instructions

Follow the repository's root `AGENTS.md` and `.github/copilot-instructions.md`.

- CI validation uses Python 3.11, `python -m pip check`, `python -m pytest -q`, and `pre-commit run --all-files`.
- Keep validation jobs read-only and use commit SHA references for Actions changed in a repair.
- Keep secrets in step-level environment variables. Never interpolate secrets or untrusted event text into shell source.
- Distinguish skipped optional integrations from successful live calls. Missing required credentials must fail manually requested integrations clearly.

# CLAUDE.md

TCAP housing subsidy reform research: policy documents (Markdown, DOCX, PDF),
datasets, and Python tooling in `src/` and `scripts/`.

## Commands

- Tests: `python3 -m pytest -q tests` (pytest adds `src` via `pyproject.toml`)
- Format / lint: `black --check .` and `flake8` (also run by pre-commit, with mdformat)
- Secret scan (manual stage; not run by ordinary pre-commit): `pre-commit run detect-secrets --hook-stage manual --all-files`
- Dependencies: `requirements.txt` (mirrored in `pyproject.toml`; keep the two in sync)

## Rules

- Never commit `.env` or API keys. Variable names are listed in `.env.template`.
- `.secrets.baseline` is the detect-secrets baseline; update it only on purpose.
- Many root-level files are reports and duplicates ("... 2.md"); ask before moving or deleting them.

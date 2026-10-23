#!/usr/bin/env python3
"""Check repository tooling and write reports without network access.

Usage: python scripts/preflight_check.py --help
Maintainer: Housing Policy Research team. Created: 2026-10-21.
Requires Python 3.11+ and Git; no third-party Python packages are needed.
"""

import argparse
import ast
import json
import platform
import shutil
import sys
from pathlib import Path


MINIMUM_PYTHON = (3, 11)
REQUIRED_FILES = (
    "pyproject.toml",
    "requirements.txt",
    "scripts/validate_connections.py",
    "src/chatgpt_notion_sync/__init__.py",
)


def collect_checks(repo_root):
    """Validate prerequisites, required tooling files, and Python syntax."""
    checks = []

    def record(name, passed, detail):
        checks.append({"name": name, "passed": passed, "detail": detail})

    record("Python", sys.version_info >= MINIMUM_PYTHON, platform.python_version())
    record("Git", shutil.which("git") is not None, "git must be on PATH")
    for relative_path in REQUIRED_FILES:
        record(
            relative_path,
            (repo_root / relative_path).is_file(),
            "required tooling file",
        )

    for directory in ("scripts", "src/chatgpt_notion_sync"):
        sources = sorted((repo_root / directory).rglob("*.py"))
        record(directory, bool(sources), "must contain Python sources")
        for source in sources:
            relative_path = source.relative_to(repo_root).as_posix()
            try:
                tree = ast.parse(
                    source.read_text(encoding="utf-8-sig"),
                    filename=relative_path,
                    feature_version=MINIMUM_PYTHON,
                )
                # Parsing alone accepts context-invalid statements such as a
                # module-level return. Compile without executing the source.
                compile(tree, relative_path, "exec")
            except (OSError, UnicodeError, SyntaxError) as error:
                record(
                    "Syntax: " + relative_path,
                    False,
                    "{} at line {}".format(
                        type(error).__name__, getattr(error, "lineno", "?")
                    ),
                )
            else:
                record("Syntax: " + relative_path, True, "valid Python")
    return checks


def main(argv=None):
    """Write both reports and return nonzero when any required check fails."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    parser.add_argument(
        "--reports-dir",
        type=Path,
        default=Path("reports/preflight"),
    )
    args = parser.parse_args(argv)
    repo_root = args.repo_root.resolve()
    reports_dir = args.reports_dir
    if not reports_dir.is_absolute():
        reports_dir = repo_root / reports_dir

    checks = collect_checks(repo_root)
    passed = all(check["passed"] for check in checks)
    report = {
        "platform": platform.system(),
        "architecture": platform.machine(),
        "passed": passed,
        "checks": checks,
    }
    reports_dir.mkdir(parents=True, exist_ok=True)
    (reports_dir / "preflight.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8"
    )

    lines = [
        "# Repository tooling preflight",
        "",
        "Result: " + ("PASS" if passed else "FAIL"),
        "",
        "| Check | Result | Detail |",
        "| --- | --- | --- |",
    ]
    for check in checks:
        lines.append(
            "| {} | {} | {} |".format(
                check["name"],
                "PASS" if check["passed"] else "FAIL",
                check["detail"],
            )
        )
    markdown = "\n".join(lines) + "\n"
    (reports_dir / "preflight.md").write_text(markdown, encoding="utf-8")
    print(markdown)
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())

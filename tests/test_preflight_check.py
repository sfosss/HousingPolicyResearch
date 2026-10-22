"""Regression tests for the preflight command used on all Actions runners."""

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/preflight_check.py"
SPEC = importlib.util.spec_from_file_location("preflight_check", SCRIPT)
preflight = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(preflight)


class PreflightTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "repo with spaces"
        self.root.mkdir()
        for relative_path in preflight.REQUIRED_FILES:
            target = self.root / relative_path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("", encoding="utf-8")

    def run_preflight(self):
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--repo-root", str(self.root)],
            cwd=self.temp.name,
            capture_output=True,
            text=True,
        )

    def read_report(self):
        report_dir = self.root / "reports/preflight"
        markdown = (report_dir / "preflight.md").read_text(encoding="utf-8")
        json_text = (report_dir / "preflight.json").read_text(encoding="utf-8")
        report = json.loads(json_text)
        self.assertIn("PASS" if report["passed"] else "FAIL", markdown)
        return report

    def test_cli_succeeds_from_other_directory_and_writes_both_reports(self):
        result = self.run_preflight()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue(self.read_report()["passed"])

    def test_missing_required_file_fails_but_still_writes_reports(self):
        (self.root / "requirements.txt").unlink()
        result = self.run_preflight()
        self.assertEqual(result.returncode, 1, result.stderr)
        report = self.read_report()
        self.assertFalse(report["passed"])
        self.assertTrue(
            any(
                check["name"] == "requirements.txt" and not check["passed"]
                for check in report["checks"]
            )
        )

    def test_invalid_python_fails_with_source_and_line(self):
        broken_script = self.root / "scripts/broken.py"
        broken_script.write_text("def broken(:\n", encoding="utf-8")
        result = self.run_preflight()
        self.assertEqual(result.returncode, 1, result.stderr)
        report = self.read_report()
        self.assertTrue(
            any(
                check["name"] == "Syntax: scripts/broken.py"
                and check["detail"] == "SyntaxError at line 1"
                for check in report["checks"]
            )
        )

    def test_missing_git_is_a_failed_check(self):
        with patch.object(preflight.shutil, "which", return_value=None):
            checks = preflight.collect_checks(self.root)
        self.assertFalse(
            next(check for check in checks if check["name"] == "Git")["passed"]
        )

    def test_newer_grammar_fails_even_on_newer_interpreter(self):
        (self.root / "scripts/newer.py").write_text(
            "match 1:\n    case 1:\n        pass\n", encoding="utf-8"
        )
        result = self.run_preflight()
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertFalse(self.read_report()["passed"])

    def test_context_invalid_statements_fail_without_executing_source(self):
        for statement in ("return 1\n", "break\n", "continue\n"):
            with self.subTest(statement=statement):
                (self.root / "scripts/context.py").write_text(
                    statement, encoding="utf-8"
                )
                result = self.run_preflight()
                output = result.stdout + result.stderr
                self.assertEqual(result.returncode, 1, output)
                self.assertFalse(self.read_report()["passed"])

    def test_valid_source_is_compiled_without_execution(self):
        (self.root / "scripts/safe.py").write_text(
            "raise RuntimeError('must not execute')\n", encoding="utf-8"
        )
        result = self.run_preflight()
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertTrue(self.read_report()["passed"])


if __name__ == "__main__":
    unittest.main()

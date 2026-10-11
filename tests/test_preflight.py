"""Regression tests for recovered preflight scripts; no network or disk scans."""
import contextlib
import importlib.util
import io
import json
import os
import subprocess
import tempfile
import unittest
from collections import namedtuple
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "capstone" / "scripts" / "preflight_check.py"
SPEC = importlib.util.spec_from_file_location("preflight_check", SCRIPT)
preflight = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(preflight)
Usage = namedtuple("Usage", "total used free")


def completed(code=0, stdout=""):
    return subprocess.CompletedProcess([], code, stdout, "")


class PreflightTests(unittest.TestCase):
    def test_disk_thresholds(self):
        for free_gib, expected in [(1, "fail"), (2, "warn"), (9, "warn"), (10, "pass")]:
            with self.subTest(free_gib=free_gib):
                checker = preflight.PreflightChecker()
                usage = Usage(100 * 1024**3, (100 - free_gib) * 1024**3, free_gib * 1024**3)
                with patch.object(preflight.shutil, "disk_usage", return_value=usage):
                    result = checker.check_disk_space()
                self.assertEqual(result["status"], expected)
                self.assertEqual(bool(checker.errors), expected == "fail")

    def test_api_uses_platform_null_device(self):
        checker = preflight.PreflightChecker()
        with patch.object(checker, "run_command", return_value=completed(stdout="200")) as run:
            self.assertEqual(checker.check_github_api()["status"], "pass")
        self.assertIn(os.devnull, run.call_args.args[0])

    def test_unreachable_api_warns(self):
        checker = preflight.PreflightChecker()
        with patch.object(checker, "run_command", return_value=None):
            self.assertEqual(checker.check_github_api()["status"], "warn")
        self.assertTrue(checker.warnings)
        self.assertFalse(checker.errors)

    def test_smart_nonzero_health_failure_is_critical(self):
        checker = preflight.PreflightChecker()
        with patch.object(preflight.shutil, "which", return_value="/mock/smartctl"), patch.object(
            checker, "run_command",
            side_effect=[completed(stdout="/dev/disk0\n/dev/disk1\n"),
                         completed(8, "SMART overall-health: FAILED!"), None],
        ):
            result = checker.check_smart_health()
        self.assertEqual(result["status"], "fail")
        self.assertEqual(result["disks"][0]["health"], "FAILED")
        self.assertTrue(checker.errors)

    def test_smart_bitmask_without_text_is_critical(self):
        checker = preflight.PreflightChecker()
        with patch.object(preflight.shutil, "which", return_value="/mock/smartctl"), patch.object(
            checker, "run_command",
            side_effect=[completed(stdout="/dev/disk0\n"), completed(8)],
        ):
            self.assertEqual(checker.check_smart_health()["status"], "fail")

    def test_smart_unavailable_is_inconclusive(self):
        checker = preflight.PreflightChecker()
        with patch.object(preflight.shutil, "which", return_value="/mock/smartctl"), patch.object(
            checker, "run_command",
            side_effect=[completed(stdout="/dev/disk0\n"), None],
        ):
            result = checker.check_smart_health()
        self.assertEqual(result["status"], "warn")
        self.assertEqual(result["disks"][0]["health"], "unknown")
        self.assertFalse(checker.errors)

    def test_rosetta_zero_is_not_evidence_of_translation(self):
        checker = preflight.PreflightChecker()
        with patch.object(preflight.platform, "machine", return_value="arm64"), patch.object(
            preflight.shutil, "which", return_value=None
        ), patch.object(checker, "run_command", side_effect=[
            completed(stdout="/mock/xcode"), completed(1), completed(stdout="0\n")
        ]):
            result = checker.check_macos_specific()
        self.assertEqual(result["rosetta2"], "not_running")

    def test_icloud_location_does_not_scan_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            cloud = home / "Library" / "Mobile Documents" / "com~apple~CloudDocs"
            for in_cloud, status in [(True, "warn"), (False, "skip")]:
                repository = cloud / "project" if in_cloud else home / "project"
                fake_file = repository / "capstone" / "scripts" / "preflight_check.py"
                checker = preflight.PreflightChecker()
                with patch.object(preflight.Path, "home", return_value=home), patch.object(
                    preflight, "__file__", str(fake_file)
                ), patch.object(preflight.os, "walk", side_effect=AssertionError("Must not scan")):
                    self.assertEqual(checker.check_icloud_sync()["status"], status)

    def test_check_exception_becomes_reported_failure(self):
        checker = preflight.PreflightChecker()
        with patch.object(preflight.platform, "system", return_value="Linux"), patch.object(
            checker, "check_python_environment", side_effect=OSError("test failure")
        ), patch.object(checker, "check_git_config", return_value={"status": "pass"}), patch.object(
            checker, "check_github_api", return_value={"status": "pass"}
        ), patch.object(checker, "check_disk_space", return_value={"status": "pass"}), contextlib.redirect_stdout(io.StringIO()):
            checker.run_all_checks()
        self.assertEqual(checker.results["overall_status"], "fail")
        self.assertEqual(checker.results["checks"]["python_environment"]["status"], "error")

    def test_main_writes_both_reports_and_preserves_failure(self):
        for status, exit_code in [("warn", 0), ("fail", 1)]:
            with self.subTest(status=status), tempfile.TemporaryDirectory() as tmp:
                script = Path(tmp) / "capstone" / "scripts" / "preflight_check.py"
                script.parent.mkdir(parents=True)

                def fake_checks(checker):
                    checker.results["overall_status"] = status
                    checker.results["checks"] = {"example": {"status": status, "detail": "⚠ UTF-8"}}
                    checker.warnings = ["example warning"] if status == "warn" else []
                    checker.errors = ["example failure"] if status == "fail" else []
                    checker.results.update(warnings=checker.warnings, errors=checker.errors)

                with patch.object(preflight, "__file__", str(script)), patch.object(
                    preflight.PreflightChecker, "run_all_checks", fake_checks
                ), contextlib.redirect_stdout(io.StringIO()), self.assertRaises(SystemExit) as raised:
                    preflight.main()
                self.assertEqual(raised.exception.code, exit_code)
                reports = script.parent.parent / "reports"
                json_report, = reports.glob("*.json")
                markdown_report, = reports.glob("*.md")
                self.assertEqual(json.loads(json_report.read_text(encoding="utf-8"))["overall_status"], status)
                self.assertIn("⚠ UTF-8", markdown_report.read_text(encoding="utf-8"))

    @unittest.skipIf(os.name == "nt", "Bash wrapper test runs on POSIX")
    def test_shell_wrappers_resolve_script_and_preserve_exit(self):
        with tempfile.TemporaryDirectory(prefix="preflight space ") as tmp:
            directory = Path(tmp)
            python = directory / "python3"
            python.write_text('#!/bin/sh\nprintf "%s\\n" "$1"\nexit 7\n', encoding="utf-8")
            python.chmod(0o755)
            env = dict(os.environ, PATH=str(directory) + os.pathsep + os.environ["PATH"])
            for name in ["preflight_linux.sh", "preflight_macos.sh"]:
                result = subprocess.run(
                    ["bash", str(SCRIPT.parent / name)], cwd=directory,
                    env=env, text=True, capture_output=True, timeout=10,
                )
                self.assertEqual(result.returncode, 7)
                self.assertEqual(Path(result.stdout.strip()), SCRIPT)


if __name__ == "__main__":
    unittest.main()

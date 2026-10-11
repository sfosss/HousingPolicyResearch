#!/usr/bin/env python3
"""
Preflight Health Check Script - Linux, macOS, and Windows
Version: 0.3.1

Performs comprehensive system health checks optimized for Apple Silicon (arm64) macOS.
Features:
- macOS-specific checks (Homebrew, Xcode Command Line Tools, Rosetta 2)
- SMART disk health monitoring (best-effort, requires smartctl)
- Repository location warning for iCloud Drive (no file scanning)
- Python environment verification
- Git configuration validation
- GitHub API connectivity test
- Generates JSON and Markdown reports

This script is dry-run safe: it only produces local reports and does not modify system state.
"""

import os
import sys
import json
import platform
import subprocess
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Any, Optional

VERSION = "0.3.1"

# Disk space thresholds (in GB)
MIN_FREE_SPACE_GB = 2
WARNING_FREE_SPACE_GB = 10


class PreflightChecker:
    """Main preflight check orchestrator."""

    def __init__(self):
        self.results: Dict[str, Any] = {
            "version": VERSION,
            "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "platform": {
                "system": platform.system(),
                "release": platform.release(),
                "machine": platform.machine(),
                "processor": platform.processor(),
            },
            "checks": {},
        }
        self.warnings: List[str] = []
        self.errors: List[str] = []

    def run_command(
        self, cmd: List[str], timeout: int = 10, check: bool = False
    ) -> Optional[subprocess.CompletedProcess]:
        """Execute a command and return the result."""
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=timeout,
                check=check,
            )
            return result
        except (subprocess.TimeoutExpired, subprocess.CalledProcessError, OSError):
            return None

    def check_python_environment(self) -> Dict[str, Any]:
        """Verify Python installation and environment."""
        check_result = {
            "status": "pass",
            "python_version": sys.version,
            "executable": sys.executable,
            "virtual_env": os.environ.get("VIRTUAL_ENV"),
        }

        # Check Python version (require 3.8+)
        version_info = sys.version_info
        if version_info.major < 3 or (version_info.major == 3 and version_info.minor < 8):
            check_result["status"] = "fail"
            self.errors.append(f"Python 3.8+ required, found {sys.version_info.major}.{sys.version_info.minor}")

        return check_result

    def check_git_config(self) -> Dict[str, Any]:
        """Verify Git installation and configuration."""
        check_result = {"status": "pass", "git_version": None, "config": {}}

        # Check Git installation
        git_version = self.run_command(["git", "--version"])
        if git_version and git_version.returncode == 0:
            check_result["git_version"] = git_version.stdout.strip()
        else:
            check_result["status"] = "fail"
            self.errors.append("Git is not installed or not in PATH")
            return check_result

        # Check Git configuration
        for key in ["user.name", "user.email"]:
            result = self.run_command(["git", "config", "--global", key])
            if result and result.returncode == 0:
                check_result["config"][key] = result.stdout.strip()
            else:
                check_result["status"] = "warn"
                self.warnings.append(f"Git config '{key}' not set")

        return check_result

    def check_github_api(self) -> Dict[str, Any]:
        """Test GitHub API connectivity."""
        check_result = {"status": "pass", "api_reachable": False}

        # Simple connectivity test using curl
        result = self.run_command(
            ["curl", "-s", "-o", os.devnull, "-w", "%{http_code}", "https://api.github.com"],
            timeout=15
        )

        if result and result.returncode == 0:
            status_code = result.stdout.strip()
            if status_code.startswith("2") or status_code == "304":
                check_result["api_reachable"] = True
                check_result["status_code"] = status_code
            else:
                check_result["status"] = "warn"
                check_result["status_code"] = status_code
                self.warnings.append(f"GitHub API returned status {status_code}")
        else:
            check_result["status"] = "warn"
            self.warnings.append("Cannot reach GitHub API")

        return check_result

    def check_macos_specific(self) -> Dict[str, Any]:
        """macOS-specific checks (Homebrew, Xcode CLT, Rosetta 2)."""
        check_result = {
            "status": "pass",
            "homebrew": False,
            "xcode_clt": False,
            "rosetta2": False,
            "is_arm64": platform.machine() == "arm64",
        }

        # Check Homebrew
        brew_path = shutil.which("brew")
        if brew_path:
            check_result["homebrew"] = True
            check_result["homebrew_path"] = brew_path
            brew_version = self.run_command(["brew", "--version"])
            if brew_version and brew_version.returncode == 0:
                check_result["homebrew_version"] = brew_version.stdout.strip().split("\n")[0]
        else:
            check_result["status"] = "warn"
            self.warnings.append("Homebrew not found (recommended for macOS development)")

        # Check Xcode Command Line Tools
        xcode_select = self.run_command(["xcode-select", "-p"])
        if xcode_select and xcode_select.returncode == 0:
            check_result["xcode_clt"] = True
            check_result["xcode_path"] = xcode_select.stdout.strip()
        else:
            check_result["status"] = "warn"
            self.warnings.append("Xcode Command Line Tools not installed")

        # Check Rosetta 2 (for arm64 Macs)
        if check_result["is_arm64"]:
            rosetta_check = self.run_command(["pgrep", "-q", "oahd"])
            # Alternative check via sysctl
            rosetta_sysctl = self.run_command(["sysctl", "-n", "kern.proc_translated"])
            if (rosetta_check and rosetta_check.returncode == 0) or \
               (rosetta_sysctl and rosetta_sysctl.returncode == 0
                and rosetta_sysctl.stdout.strip() == "1"):
                check_result["rosetta2"] = True
            else:
                # Rosetta may not be running if no x86 apps are active
                check_result["rosetta2"] = "not_running"

        return check_result

    def check_smart_health(self) -> Dict[str, Any]:
        """Check SMART disk health (best-effort, requires smartctl)."""
        check_result = {
            "status": "skip",
            "smartctl_available": False,
            "disks": [],
        }

        # Check if smartctl is available
        smartctl_path = shutil.which("smartctl")
        if not smartctl_path:
            check_result["message"] = "smartctl not available (install via: brew install smartmontools)"
            return check_result

        check_result["smartctl_available"] = True
        check_result["status"] = "pass"

        # Try to list disks (may require sudo)
        disk_list = self.run_command(["smartctl", "--scan"], timeout=5)
        if not disk_list or disk_list.returncode != 0:
            check_result["status"] = "warn"
            check_result["message"] = "Could not scan for disks (may require sudo)"
            self.warnings.append("SMART disk scan failed (consider running with sudo)")
            return check_result

        # Parse disk list and check health
        for line in disk_list.stdout.strip().split("\n"):
            if not line.strip():
                continue

            parts = line.split()
            if len(parts) >= 1:
                disk_device = parts[0]
                disk_info = {"device": disk_device, "health": "unknown"}

                # Get SMART health status
                health_check = self.run_command(
                    ["smartctl", "-H", disk_device], timeout=5
                )
                # smartctl uses a bitmask exit status, including health failures.
                if health_check is None:
                    if check_result["status"] != "fail":
                        check_result["status"] = "warn"
                    self.warnings.append(f"SMART health check unavailable for {disk_device}")
                elif "FAILED" in health_check.stdout or health_check.returncode & 8:
                    disk_info["health"] = "FAILED"
                    check_result["status"] = "fail"
                    self.errors.append(f"SMART health check FAILED for {disk_device}")
                elif health_check.returncode == 0 and "PASSED" in health_check.stdout:
                    disk_info["health"] = "PASSED"
                else:
                    if check_result["status"] != "fail":
                        check_result["status"] = "warn"
                    self.warnings.append(f"SMART health check inconclusive for {disk_device}")

                check_result["disks"].append(disk_info)

        return check_result

    def check_icloud_sync(self) -> Dict[str, Any]:
        """Warn only when this repository is inside iCloud Drive.

        Repository location is not evidence of cloud sync completion or failure.
        Do not traverse the user's iCloud files or infer sync state from xattrs.
        """
        icloud_path = (
            Path.home() / "Library" / "Mobile Documents" / "com~apple~CloudDocs"
        ).resolve()
        repository_path = Path(__file__).resolve().parents[2]
        try:
            repository_path.relative_to(icloud_path)
        except ValueError:
            return {
                "status": "skip",
                "message": "Repository is outside iCloud Drive; sync state not checked",
            }
        self.warnings.append("Repository is in iCloud Drive; sync state is unknown")
        return {
            "status": "warn",
            "repository_in_icloud_drive": True,
            "message": "Location only; sync state is unknown",
        }

    def check_disk_space(self) -> Dict[str, Any]:
        """Check available disk space."""
        check_result = {"status": "pass"}

        try:
            stat = shutil.disk_usage(Path.home())
            check_result["total_gb"] = round(stat.total / (1024**3), 2)
            check_result["used_gb"] = round(stat.used / (1024**3), 2)
            check_result["free_gb"] = round(stat.free / (1024**3), 2)
            check_result["percent_used"] = round((stat.used / stat.total) * 100, 1)

            # Error if less than 2GB free (check critical condition first)
            if stat.free < MIN_FREE_SPACE_GB * 1024**3:
                check_result["status"] = "fail"
                self.errors.append(
                    f"Critical disk space: only {check_result['free_gb']}GB free"
                )
            # Warn if less than 10GB free
            elif stat.free < WARNING_FREE_SPACE_GB * 1024**3:
                check_result["status"] = "warn"
                self.warnings.append(
                    f"Low disk space: only {check_result['free_gb']}GB free"
                )

        except Exception as e:
            check_result["status"] = "fail"
            check_result["error"] = str(e)
            self.errors.append(f"Failed to check disk space: {str(e)}")

        return check_result

    def run_all_checks(self):
        """Execute all preflight checks."""
        print(f"Running preflight checks (version {VERSION})...\n")

        # Run each check
        checks = [
            ("python_environment", self.check_python_environment),
            ("git_config", self.check_git_config),
            ("github_api", self.check_github_api),
            ("disk_space", self.check_disk_space),
        ]

        # Add macOS-specific checks
        if platform.system() == "Darwin":
            checks.extend([
                ("macos_specific", self.check_macos_specific),
                ("smart_health", self.check_smart_health),
                ("icloud_sync", self.check_icloud_sync),
            ])

        for check_name, check_func in checks:
            print(f"Checking {check_name}...", end=" ")
            try:
                result = check_func()
                self.results["checks"][check_name] = result
                status = result.get("status", "unknown")

                status_symbol = {
                    "pass": "✓",
                    "warn": "⚠",
                    "fail": "✗",
                    "skip": "○",
                }.get(status, "?")

                print(f"{status_symbol} {status}")

            except Exception as e:
                print(f"✗ error")
                self.results["checks"][check_name] = {
                    "status": "error",
                    "error": str(e),
                }
                self.errors.append(f"Check '{check_name}' failed with error: {str(e)}")

        # Add warnings and errors to results
        self.results["warnings"] = self.warnings
        self.results["errors"] = self.errors

        # Determine overall status
        if self.errors:
            self.results["overall_status"] = "fail"
        elif self.warnings:
            self.results["overall_status"] = "warn"
        else:
            self.results["overall_status"] = "pass"

    def save_json_report(self, output_path: Path):
        """Save results as JSON."""
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(self.results, f, indent=2)
        print(f"\n✓ JSON report saved to: {output_path}")

    def save_markdown_report(self, output_path: Path):
        """Save results as Markdown."""
        lines = [
            f"# Preflight Check Report",
            f"",
            f"**Version:** {VERSION}  ",
            f"**Timestamp:** {self.results['timestamp']}  ",
            f"**Platform:** {self.results['platform']['system']} {self.results['platform']['release']} ({self.results['platform']['machine']})  ",
            f"**Overall Status:** {self.results['overall_status'].upper()}",
            f"",
            f"## Check Results",
            f"",
        ]

        for check_name, check_result in self.results["checks"].items():
            status = check_result.get("status", "unknown")
            status_emoji = {
                "pass": "✅",
                "warn": "⚠️",
                "fail": "❌",
                "skip": "⏭️",
                "error": "💥",
            }.get(status, "❓")

            lines.append(f"### {status_emoji} {check_name.replace('_', ' ').title()}")
            lines.append(f"")
            lines.append(f"**Status:** {status}")
            lines.append(f"")

            # Add relevant details
            for key, value in check_result.items():
                if key != "status" and value is not None:
                    if isinstance(value, (dict, list)):
                        lines.append(f"**{key}:**")
                        lines.append(f"```json")
                        lines.append(json.dumps(value, indent=2))
                        lines.append(f"```")
                    else:
                        lines.append(f"**{key}:** {value}  ")

            lines.append(f"")

        # Add warnings section
        if self.warnings:
            lines.append(f"## ⚠️ Warnings ({len(self.warnings)})")
            lines.append(f"")
            for warning in self.warnings:
                lines.append(f"- {warning}")
            lines.append(f"")

        # Add errors section
        if self.errors:
            lines.append(f"## ❌ Errors ({len(self.errors)})")
            lines.append(f"")
            for error in self.errors:
                lines.append(f"- {error}")
            lines.append(f"")

        with open(output_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        print(f"✓ Markdown report saved to: {output_path}")


def main():
    """Main entry point."""
    # Set output directory
    output_dir = Path(__file__).parent.parent / "reports"
    output_dir.mkdir(exist_ok=True)

    # Generate timestamp for filenames
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S_%f")

    # Run checks
    checker = PreflightChecker()
    checker.run_all_checks()

    # Save reports
    json_path = output_dir / f"preflight_check_{timestamp}.json"
    md_path = output_dir / f"preflight_check_{timestamp}.md"

    checker.save_json_report(json_path)
    checker.save_markdown_report(md_path)

    # Print summary
    print(f"\n{'='*60}")
    print(f"Preflight Check Summary")
    print(f"{'='*60}")
    print(f"Overall Status: {checker.results['overall_status'].upper()}")
    print(f"Warnings: {len(checker.warnings)}")
    print(f"Errors: {len(checker.errors)}")
    print(f"{'='*60}\n")

    # Exit with appropriate code
    if checker.errors:
        sys.exit(1)
    elif checker.warnings:
        sys.exit(0)  # Warnings don't fail the check
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()


# Preflight health checks

The platform wrappers and shared checker were recovered from
[PR #35](https://github.com/sfosss/HousingPolicyResearch/pull/35),
commit `067873ae7369dad5a8dc2facfd8eabdb89814742`. The workflows were present
on main while these scripts were absent.

Run from the repository root:

```bash
bash capstone/scripts/preflight_linux.sh
# macOS:
bash capstone/scripts/preflight_macos.sh
```

On Windows with PowerShell:

```powershell
.\capstone\scripts\preflight_windows.ps1
```

Python 3.8+ is required. The wrappers also work from other working directories.
No token, .env file, installation, sudo, or system configuration change is needed.
The checker runs read-only commands and writes local reports.

JSON and UTF-8 Markdown reports are written to
`capstone/reports/preflight_check_<UTC timestamp>.{json,md}`.
Exit 0 means pass or warnings; exit 1 means a critical failure.
Git configuration and API connectivity failures are warnings; missing Git,
unsupported Python, less than 2 GiB free space, or confirmed SMART failure
are critical. Free disk space below 10 GiB is a warning.

macOS adds best-effort Homebrew, Xcode, Rosetta and SMART diagnostics.
Unavailable SMART access is inconclusive; the script does not elevate privileges.
The iCloud check only identifies whether the repository is inside iCloud Drive.
It does not enumerate personal files or determine sync state.

Recovery fixes include portable `os.devnull`, explicit UTF-8 report encoding,
SMART bitmask failure handling, accurate Rosetta translation detection, and
preservation of Python exit codes. Wrappers do not source arbitrary .env code.

Run focused regression tests without additional packages:

```bash
python3 -m unittest discover -s tests -p 'test_preflight.py' -v
```

The workflow runs the regression tests on all three platforms. Windows uses a
sparse checkout of the scripts and test because unrelated research paths include
a trailing-space directory name that Windows cannot check out.

The existing workflow uses `continue-on-error: true` for the checker.
Inspect the preflight step outcome and report `overall_status`; a green job
alone does not prove every diagnostic passed. Workflow policy is unchanged.


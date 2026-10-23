# CI repair reconciliation — 2026-10-23

Version: 1.0. Proposed for review. Baseline: `873590d24b0cf24c35dc4e5c47aa807295a39838`.

## Decisions

- #134: closed without merging. It removed the working test dependencies, agent Markdown exclusion and newer Setup Validation action pins.
- #132: closed as incorporated through merged #130. Main retains #133's later Black and urllib3 pins.
- #123: the missing-script/Windows-checkout repair is superseded by merged #128/#129. Preserve main's `scripts/preflight_check.py` and staged three-platform workflow. Its older capstone checker, SMART/Rosetta diagnostics and wrappers remain in its branch/history for optional future work; they are not required for repository tooling readiness.
- #122: retain only the independently useful audit and current-document credential cleanup. Preserve main's existing setup, formatter and preflight files. This follow-up supersedes the old conflicting bundle after validation; original commits remain available.

## #122 file disposition

| Original paths                                                                                                                   | Reconciliation                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| .flake8; .github/workflows/setup-validation.yml; .github/workflows/preflight.yml                                                 | Preserve working main versions. No legacy pins or duplicate checker.                                                                                                                  |
| .github/workflows/blank.yml                                                                                                      | Keep existing placeholder out of required checks. Its removal is unnecessary for this repair.                                                                                         |
| .github/workflows/codeql.yml; .github/workflows/copilot-setup-steps.yml; .github/workflows/generate_policy_proposal.yml          | Keep main implementations. Action modernization belongs in a separate follow-up. CodeQL currently covers Actions only.                                                                |
| .github/workflows/generate_policy_proposal 2.yml; .github/workflows/preflight 2.yml                                              | Already removed on main.                                                                                                                                                              |
| .github/workflows/publish-reports.yml                                                                                            | Preserve rendering/release/artifact behavior; remove direct pushes to protected main. Published outputs remain release assets and workflow artifacts.                                 |
| .github/workflows/repository-audit.yml; .github/dependabot.yml                                                                   | Defer new schedules, permissions and grouped-update policy for separate review. No extra scheduled audit is enabled.                                                                  |
| scripts/audit_repository_state.py; tests/test_repository_audit.py                                                                | Retain manual audit command and tests. Prune ignored trees and never read symlinked files/directories; add a regression covering external links.                                      |
| .gitignore                                                                                                                       | Add only generated assessment/local-manifest ignores.                                                                                                                                 |
| 00_admin/examples/collaboration-sources.example.json; docs/COLLABORATIVE_DATA_INTAKE.md; docs/REPOSITORY_SECURITY_PERMISSIONS.md | Retain scoped intake/permission guidance with current implementation limits stated.                                                                                                   |
| SECURITY.md; SECURITY-CHECKLIST.md; SECURITY-REMEDIATION.md; 00_admin/settings.yaml                                              | Remove repeated credential material. State rotation/history/settings verification as pending; manual secret hook remains manual. No credential rotation or history rewrite performed. |
| README.md; docs/OPEN_TASK_REVIEW_2026-09-20.md; docs/environment-integrations.md                                                 | Do not import stale setup/snapshot claims. This decision record supplies current scope and sequencing.                                                                                |
| .pre-commit-config.yaml                                                                                                          | Preserve main's manual secret scan and agent-file exclusion. Enabling a blocking scan requires separate validation.                                                                   |

## Required checks

The active [Main CI validation ruleset](https://github.com/sfosss/HousingPolicyResearch/rules/25730785) targets only the default branch, requires up-to-date branches and checks supplied by GitHub Actions:

- `validate`
- `Preflight Checks (Linux)`
- `Preflight Checks (Windows)`
- `Preflight Checks (macOS arm64)`

It has no bypass actors. Existing deletion/force-push protections remain. Classic branch rules were absent in the administration UI. The placeholder `CI / build` is deliberately not a required check.

## Validation and limits

The isolated local checkout was reconstructed through the GitHub connection because local network/DNS access and GitHub CLI authentication were unavailable. Its pre-change Git tree exactly matched main tree `527275cef0acfa675b3522605463bc2a5319023e`. The local baseline passed 24 tests and all configured formatting hooks. The reconciled audit adds five tests; local pytest reports 29 passed and pip check passes. Native Python 3.11 and matrix validation must pass on the final PR revision before integration.

The audit's hosted endpoint behavior is not exercised live in local tests. Alert permissions can be unavailable; reports must retain coverage limits. Provider-side rotation, complete secret scanning, Git history cleanup, live external integrations, PDF rendering and release publication are not certified. The publication workflow is not run during this review because it creates releases.

## Integration order

1. Preserve merged #130 and current dependency pins; #134/#132 are retired.
1. Verify this reconciliation's native checks; retire #122/#123 in favor of the recorded dispositions and reviewed follow-up.
1. Validate and review the separate action modernization PR, including upload/download compatibility on all preflight platforms.
1. Refresh the later PR against the then-current main and require fresh checks before any merge. Keep publication release assets/artifacts; generated commits must not bypass required checks.

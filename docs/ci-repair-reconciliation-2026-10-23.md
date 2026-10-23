# CI repair reconciliation — 2026-10-23

Version: 1.4. Proposed for review. Baseline: `873590d24b0cf24c35dc4e5c47aa807295a39838`.

## Decisions

- #134: closed without merging. It removed the working test dependencies, agent Markdown exclusion and newer Setup Validation action pins.
- #132: closed as incorporated through merged #130. Main retains #133's later Black and urllib3 pins.
- #123: the missing-script/Windows-checkout repair is superseded by merged #128/#129. Preserve main's `scripts/preflight_check.py` and staged three-platform workflow. Its older capstone checker, SMART/Rosetta diagnostics and wrappers remain in its branch/history for optional future work; they are not required for repository tooling readiness.
- #122: retain only the independently useful audit and current-document credential cleanup. Preserve main's existing setup, formatter and preflight files. This follow-up supersedes the old conflicting bundle after validation; original commits remain available.

## #122 file disposition

| Original paths                                                                                                                   | Reconciliation                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| .flake8; .github/workflows/setup-validation.yml; .github/workflows/preflight.yml                                                 | Preserve working main versions. No legacy pins or duplicate checker.                                                                                                                                                                                                |
| .github/workflows/blank.yml                                                                                                      | Keep existing placeholder out of required checks. Its removal is unnecessary for this repair.                                                                                                                                                                       |
| .github/workflows/codeql.yml; .github/workflows/copilot-setup-steps.yml                                                          | Keep main implementations. Action modernization belongs in a separate follow-up. CodeQL currently covers Actions only.                                                                                                                                              |
| .github/workflows/generate_policy_proposal 2.yml; .github/workflows/preflight 2.yml                                              | Already removed on main.                                                                                                                                                                                                                                            |
| .github/workflows/publish-reports.yml                                                                                            | Preserve rendering/release/artifact behavior; remove direct pushes to protected main. Published outputs remain release assets and workflow artifacts.                                                                                                               |
| .github/workflows/repository-audit.yml; .github/dependabot.yml                                                                   | Defer new schedules, permissions and grouped-update policy for separate review. No extra scheduled audit is enabled.                                                                                                                                                |
| scripts/audit_repository_state.py; tests/test_repository_audit.py                                                                | Retain manual audit command and tests. Prune ignored trees and never read symlinked files/directories; add a regression covering external links.                                                                                                                    |
| .gitignore                                                                                                                       | Add only generated assessment/local-manifest ignores.                                                                                                                                                                                                               |
| 00_admin/examples/collaboration-sources.example.json; docs/COLLABORATIVE_DATA_INTAKE.md; docs/REPOSITORY_SECURITY_PERMISSIONS.md | Retain scoped intake/permission guidance with current implementation limits stated.                                                                                                                                                                                 |
| SECURITY.md; SECURITY-CHECKLIST.md; SECURITY-REMEDIATION.md; 00_admin/settings.yaml                                              | Remove repeated credential material from incident documents and correct the malformed data-path configuration key. State rotation/history/settings verification as pending; manual secret hook remains manual. No credential rotation or history rewrite performed. |
| README.md; docs/OPEN_TASK_REVIEW_2026-09-20.md; docs/environment-integrations.md                                                 | Do not import stale setup/snapshot claims. This decision record supplies current scope and sequencing.                                                                                                                                                              |
| .pre-commit-config.yaml                                                                                                          | Preserve main's manual secret scan and agent-file exclusion. Enabling a blocking scan requires separate validation.                                                                                                                                                 |

## Required checks

The active [Main CI validation ruleset](https://github.com/sfosss/HousingPolicyResearch/rules/25730785) targets only the default branch, requires up-to-date branches and checks supplied by GitHub Actions:

- `validate`
- `Preflight Checks (Linux)`
- `Preflight Checks (Windows)`
- `Preflight Checks (macOS arm64)`

It has no bypass actors. Existing deletion/force-push protections remain. Classic branch rules were absent in the administration UI. The placeholder `CI / build` is deliberately not a required check.

## Validation and limits

The isolated local checkout was reconstructed through the GitHub connection because local network/DNS access and GitHub CLI authentication were unavailable. Its pre-change Git tree exactly matched main tree `527275cef0acfa675b3522605463bc2a5319023e`. The local baseline passed 24 tests and all configured formatting hooks. The reconciled audit initially added five tests. Review fixes add regressions for unavailable API summaries, strict manifest fields/types and Markdown table escaping; local pytest now reports 51 passed and pip check passes. Native Python 3.11 and matrix validation must pass on the final PR revision before integration.

The audit's hosted endpoint behavior is not exercised live in local tests. Alert permissions can be unavailable; reports must retain coverage limits. Provider-side rotation, complete secret scanning, Git history cleanup, live external integrations, PDF rendering and release publication are not certified. The publication workflow is not run during this review because it creates releases.

## Integration order

1. Preserve merged #130 and current dependency pins; #134/#132 are retired.
1. Verify this reconciliation's native checks; retire #122/#123 in favor of the recorded dispositions and reviewed follow-up.
1. Validate and review the separate action modernization PR, including upload/download compatibility on all preflight platforms.
1. Refresh the later PR against the then-current main and require fresh checks before any merge. Keep publication release assets/artifacts; generated commits must not bypass required checks.

## Code review fixes

The first review identified three report/validation defects. Failed or unqueried GitHub alert families now render as unavailable, not zero. Manifest objects accept only declared fields and scalar metadata types, rejecting credential/link fields and nested objects. Markdown table cells escape delimiters and normalize newlines. Targeted regressions accompany each fix.

## Proposal output branches

Proposal generation now force-adds only its ignored output file and pushes the resulting commit to a unique generated/policy-proposal-RUN_ID-ATTEMPT branch. Main is not pushed. The workflow retains checkout authentication for that limited write, keeps its existing credential gate and token permissions, and reports a comparison link for opening a reviewed PR. A local bare-remote regression confirms that the output is committed on the generated branch while remote main remains unchanged. Live generation and Notion posting are not executed.

## Coverage review

Task discovery uses Git's tracked/untracked file inventory with standard ignore rules and negations, skips symlinked paths, and rejects invalid or inaccessible roots. The root must be inside a Git working tree. Empty trackers retain their headers. Both partial and complete API failure remain unavailable rather than zero/missing credentials; pagination accepts GitHub's canonical repository URL alias while rejecting other origins. Manual proposal runs explicitly check out main so their comparison link uses the actual source branch. These cases have fixture-based regressions and no live API calls.

## Portable report encoding

JSON and Markdown report files are written explicitly as UTF-8. A CLI regression disables UTF-8 locale coercion and verifies that emoji status values survive both output formats. Local regression count: 51.

## CLI and manifest coverage

Default stdout is explicitly UTF-8-capable, matching file output. A supplied empty manifest is recorded as zero declared sources rather than omitted input; older reports without that provenance are marked unknown. Fixture regressions cover both cases. Local suite: 51 tests.

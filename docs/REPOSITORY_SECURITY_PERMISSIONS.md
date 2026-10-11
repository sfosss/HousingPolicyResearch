# Repository security and implementation permissions

## Principle

Assessment and remediation use separate credentials. The scheduled assessment
is deliberately read-only; it must never close issues, dismiss alerts, rewrite
history, modify settings, or push implementation changes. Remediation is
performed through reviewed pull requests or an administrator's short-lived,
least-privilege session.

## Required access by operation

| Operation | GitHub Actions permission | Human/fine-grained token access | Execution path |
| --- | --- | --- | --- |
| Read files and compare the checked-out version | `contents: read` | Contents: read | Unified assessment workflow |
| Enumerate open issues and pull requests | `issues: read`, `pull-requests: read` | Issues: read; Pull requests: read | Unified assessment workflow |
| Enumerate CodeQL, Dependabot, and secret-scanning alerts | `security-events: read` | Code scanning, Dependabot alerts, and secret scanning alerts: read | Unified assessment workflow |
| Upload the sanitized assessment | `actions: read` plus the artifact service's run-scoped token | No personal token | Unified assessment workflow |
| Change implementation files on a branch | Do not grant a scheduled workflow | Contents: read/write for the selected repository | Contributor branch and reviewed PR |
| Update/close issues or PRs | Do not grant a scheduled workflow | Issues: read/write; Pull requests: read/write | Maintainer review after reconciliation |
| Dismiss or resolve security alerts | Do not grant a scheduled workflow | The corresponding security-alert permission: read/write | Security maintainer review with justification |
| Change branch protection, security features, or Actions policy | Not available to the assessment workflow | Repository Administration: read/write | Repository administrator settings change |
| Rewrite published history after a secret incident | Never use the Actions token | Repository contents/administration plus coordinated force-push authority | Time-bounded incident procedure |

GitHub may withhold security-alert APIs from the default Actions token depending
on repository visibility and organization policy. If the assessment reports a
403 for an alert family, use a fine-grained token stored as an Actions secret,
scoped to this repository and **read-only** for that alert family. Do not replace
`GITHUB_TOKEN` with a classic personal access token or grant write permissions to
the scheduled workflow.

## One comprehensive two-version approach

“Local” and “hosted” are two views of the same work, not independent sources of
truth:

1. Run `scripts/audit_repository_state.py` in CI so the exact checked-out commit
   and current hosted issues, pull requests, and alert counts are captured in one
   timestamped report.
2. Reconcile each still-relevant local task into exactly one hosted issue. Include
   an owner, acceptance criteria, current deadline, and links to its source row
   and any implementation PR.
3. Archive local trackers only after their retained work is linked. Close hosted
   duplicates only after citing the surviving issue or completed deliverable.
4. Implement code and workflow fixes on a branch and merge through required
   checks. Handle repository settings and alert resolution separately with an
   administrator or security-maintainer credential.
5. Re-run the assessment at the merged revision and retain the sanitized report
   as evidence. Never include secret values or secret locations in the artifact.

Box, ChatGPT, and Claude collaboration sources form a third, non-authoritative
evidence layer. They are inventoried through an ignored local manifest and then
curated through the intake procedure in `COLLABORATIVE_DATA_INTAKE.md`; they are
never mounted into scheduled CI or treated as writable repository replicas.

## Local invocation

```bash
# Local files only
python scripts/audit_repository_state.py --markdown-output repository-assessment.md

# Local files and hosted state; token remains in the process environment
GITHUB_TOKEN=... python scripts/audit_repository_state.py \
  --repo OWNER/REPOSITORY \
  --json-output repository-assessment.json \
  --markdown-output repository-assessment.md
```

Generated assessment files are operational artifacts and should not be committed.

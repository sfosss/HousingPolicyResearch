# Open task and repository maintenance review — 2026-09-20

## Scope and limitation

The initial review covered task/status artifacts and workflow definitions in the
checked-out repository. Hosted state was unavailable in that environment. The
new read-only unified assessment workflow now evaluates the checked-out commit and
hosted issues, pull requests, and security alerts in the same run. Permission or
API failures are recorded per alert family instead of being mistaken for zero
open findings. See `REPOSITORY_SECURITY_PERMISSIONS.md` for the distinct,
least-privilege assessment and remediation roles.

## Disposition

| Item | Evidence | Disposition |
| --- | --- | --- |
| Root operations tracker | `NYC_Housing_Subsidy_Ops_Tasks_Notion.csv` contains 19 `Not Started` and one `Intake/Triage` row with 2025 dates | **Archive as a historical planning snapshot.** Do not bulk-mark complete: outcomes are not evidenced. Create fresh issues only for work that still has an owner, current deadline, and acceptance criteria. |
| Expanded TCAP tracker | `TCAP_PET/NYC_Housing_Subsidy_Ops_Tasks_Notion.csv` contains 27 `Not Started` and one `In Progress` row | **Archive/reconcile.** It overlaps the root tracker and conflicts with project-completion documents. Re-open verified gaps in one authoritative tracker. |
| Risk/status tracker copies | Root and `docs/tcap/tracking/` copies each contain 20 stale rows | **Archive duplicates.** Preserve one read-only historical copy; do not operate from both. |
| Backup and `data/` task CSVs | Each is a one-row intake snapshot | **Keep only as provenance or archive.** They are not active queues. |
| Implementation checklists/plans | Dates and setup instructions are from 2025 while later completion records exist | **Close as superseded** after linking the relevant completion record. Retain for audit history. |
| Duplicate workflows ending in ` 2.yml` | Byte-for-byte/near duplicate scheduled automation | **Removed.** Duplicate schedules waste runner time and can create competing commits. |
| Starter `blank.yml` | Placeholder “Hello, world” CI | **Removed.** It supplied no validation signal. |
| Report publishing workflow | Targets absent `30_drafts`/`40_outputs`, grants broad write privileges, and uses obsolete artifact tooling | **Removed/archived.** Restore only with current paths, immutable action pins, and a reviewed release design. |
| Proposal generator | Current script and artifact path exist | **Retained and hardened.** Dependencies are installed from the pinned repository manifest, action revisions are immutable, and checkout credentials are not persisted. |
| Preflight workflow | Cross-platform checks remain potentially useful | **Retained one canonical copy.** The duplicate malformed copy was removed. |
| Setup validation and CodeQL | Active security/quality controls | **Retained and hardened.** CodeQL now analyzes Python as well as Actions. |

## Unified local-and-hosted follow-up

1. Configure the canonical remote, fetch/prune all refs, and compare every open
   PR with the default branch. Close drafts that are superseded or have no unique
   commits; update/rebase relevant work; never merge an unreviewed stale branch.
2. Triage every open issue against a single authoritative tracker. Close
   duplicates and completed items with evidence; add owners, dates, and acceptance
   criteria to retained tasks.
3. Review Dependabot, CodeQL, and secret-scanning alerts after this commit lands.
   Do not dismiss an alert without a documented false-positive or compensating
   control.
4. Enable branch protection, required checks, secret scanning/push protection,
   and private vulnerability reporting in GitHub settings.

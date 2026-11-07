# Legacy source inventory — read-only preservation map (2026-10-26)

Observed in the repository's main tree before registry creation:

- `Capstone/data:sources/`: large collection of PDFs, HTML, datasets and other research artifacts.
- `Capstone/Housing_Research_Reference_Tracker_APA.docx`: existing APA reference tracker.
- `00_admin/Policy_Research_News_LIVE_Tracker.csv`: active news/policy tracker.
- `00_admin/recovery_queue/review_shortlists_20260525/03_citations_sources_clean_review.tsv`: historical citation recovery shortlist.
- `00_admin/recovery_queue/archive_policy_recovery_candidates_20260525_131844.tsv`: recovery candidate inventory.
- `docs/resource-index.md`: existing documentation index.
- `60_logs/NYC_Housing_Subsidy_Policy_News_LIVE_20251226.csv`: historical news log.

**No migration, deduplication, archival, or deletion performed.** Some historical root documentation references an older GitHub remote; verify the active remote and local checkout before any local sync. Existing news entries may contain advocacy recommendations and secondary-source descriptions: do not silently promote these into verified legal authority.

Next: reconcile metadata and provenance, review privacy and licensing, then propose a separately reviewable import.

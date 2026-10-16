# Adaptive Policy Research Loop

This directory is the dated, review-ready output of the NYC Public Equity Transfer Framework (PETF) and Tenant Co-op Acquisition Program (TCAP) research system.

## Operating model

The loop runs on weekdays and performs seven controlled stages:

1. **Collect** official RSS items plus normalized Web, Midpage and Box packets.
1. **Constrain** results to NYC housing, household stability, civil-rights and implementation relevance.
1. **Normalize and deduplicate** with canonical URLs, content hashes and stable event IDs.
1. **Map and score** each development against PETF/TCAP sections and the Critical–Considerations scale.
1. **Draft proposed redlines** in a separate file; canonical legislation is never edited automatically.
1. **Validate** URLs, jurisdiction, mapping, redline coverage, connector health and counsel-review gates.
1. **Publish** the master CSV, dated brief, source packet, source index and ChatGPT export; optionally mirror outputs to Box.

## Human review gate

Every generated redline begins with `PROPOSED—HUMAN REVIEW REQUIRED`. Critical items receive `Needs Counsel Review` status and update one persistent GitHub review issue. Promotion from a reviewed High item to Critical clears the old approval and requires fresh counsel review. Only a named reviewer may change a CSV disposition to `Accepted`; accepted language must then be applied to canonical legislation in a separate pull request.

## Daily output

`policy-research/YYYYMMDD/` contains:

- `DAILY_BRIEF.md`
- `PROPOSED_REDLINES.md`
- `SOURCE_PACKET.json`
- `QA_REPORT.json`
- `CRITICAL_ALERT.md`
- `RUN_COMPLETE.json` after all local outputs and Box results have been finalized

The authoritative event ledger is `datasets/NYC_Housing_Subsidy_Policy_News_LIVE.csv`. Generated policy indexes are `indexes/POLICY_SOURCE_INDEX.csv` and `.md`; the curated `SOURCE_INDEX` files are preserved. Machine-readable handoff is written to `exports-for-chatgpt/`.

Incoming records match persisted event IDs, canonical URLs or content hashes. A content revision keeps the original event ID and resets the review disposition only when both snapshots have timezone-aware `source_updated_at` values and the incoming version is newer. Stale, equal-version conflicting, or unversioned revisions retain stored evidence and produce a QA error. For older unversioned records, a reviewer must establish the source version before automatic revisions can resume. Unchanged evidence preserves its review. Missing publication dates stay empty; RFC publication dates support named time zones.

The CSV reader accepts a UTF-8 BOM and validates identity columns and row shape before rewriting. Malformed ledgers are preserved and produce diagnostic outputs. On retry, missing/incomplete prior dated outputs are rebuilt from ledger rows; recovered QA explicitly records that the original connector diagnostics are unavailable. This recovers the persisted snapshot, not earlier revisions no longer present in the ledger.

QA and Critical alerts include unresolved Critical records from the entire ledger, even on days with no new intake. A Critical record is resolved only when marked `Accepted` with a named reviewer. Unresolved Critical items, invalid URLs, missing daily mappings/redlines and connector errors fail QA. Strict mode returns a nonzero exit status after writing diagnostic artifacts. Completed artifacts are still uploaded and proposed through an automation PR when strict QA fails, so new Critical rows remain available for review. No canonical legislation is amended.

## Importance scale

- **Critical (85–100):** enacted/effective authority, adverse court action, funding interruption or civil-rights issue that may block implementation; counsel review required.
- **High (70–84):** likely material change to legal pathway, financing, agency authority or tenant-equity protection.
- **Medium (50–69):** meaningful implementation effect requiring tracked revision or model update.
- **Low (30–49):** limited operational effect; monitor and address during routine revision.
- **Considerations (0–29):** contextual signal without a present drafting requirement.

## Connector schema

Place JSON files in `intake/connectors/web`, `midpage`, or `box`. A packet is either an array or `{ "items": [...] }`. Each item should contain:

```json
{
  "headline": "Required",
  "summary": "Factual source-grounded summary",
  "source_url": "https://...",
  "source_name": "Agency or publication",
  "date_published": "YYYY-MM-DD",
  "source_updated_at": "2026-10-16T12:00:00Z",
  "jurisdiction": "NYC",
  "agency": "HPD",
  "document_type": "Rule/Report/Bill/Opinion/News",
  "primary_source": true
}
```

Jurisdiction is required and must be NYC, New York City, NY, New York or Federal (case-insensitive). Missing or unsupported values are diagnosed rather than silently skipped. Statewide/federal material must also mention NYC/boroughs or a configured city agency/program, target HPD/HRA/NYCHA, or carry an operator-verified `applies_to_nyc: true` assertion. HUD alone and generic housing terms do not establish NYC applicability. Scope and mapping keywords use whole terms/phrases.

Source URLs must be absolute HTTP(S) links with a valid host and no embedded user credentials. Known authentication, API-key, token, signature and signed-URL query parameters are removed before hashing or export; this also handles encoded names, nested URL/query values and credential fragments. Public identifiers, opinion fragments and search queries remain. Persisted URL copies are sanitized without discarding an unchanged review. Feed and Box exception diagnostics retain error classes rather than raw request/redirect URLs. Opaque secrets in paths or unknown parameter names require public-link review; structural validation does not prove anonymous reachability. Use JSON booleans for `primary_source` (the strings `"true"` and `"false"` are also accepted). Malformed packets and rejected items appear in `connector_errors`; valid sibling items and other sources still run.

For **Midpage**, include only opinions that have passed `analyzeOpinion`. Require this `opinion_analysis` object in every Midpage packet, including Midpage records relayed through Box/Web:

```json
{
  "tool": "analyzeOpinion",
  "status": "completed",
  "analysis_id": "Actual analysis identifier",
  "opinion_url": "https://public-opinion-url",
  "analyzed_at": "2026-10-16T12:00:00Z",
  "proposition": "Exact supported legal proposition",
  "scope_limit": "Applicability and limits"
}
```

The opinion URL must match the packet source URL. Missing/incomplete evidence is rejected and diagnosed. Preserve the supported proposition and limits in the factual summary as well. This is operator-supplied analysis evidence; the offline pipeline does not authenticate the analysis identifier against Midpage. Midpage results are legal research inputs, not automatic holdings applicable to PETF/TCAP.

`config/policy_map.json` selects the full root `NYC-Draft-Legislation.md` package as its drafting reference. Every rule names an existing section and paragraph; configuration and QA validate those coordinates against the document. This locates a proposed amendment without asserting that the draft is enacted law.

Official RSS/Atom intake accepts namespaced entries, processes every available entry (the former `max_items` truncation is removed), and reports empty/unrecognized feeds. Transient timeouts, connection errors, HTTP 429 and selected 5xx failures get at most three attempts with one- and two-second backoff. Feeds cannot recover entries already removed by the publisher.

For **Web/Perplexity Premium**, prioritize statutes, budgets, audits, agency guidance and official releases. Secondary reporting may identify an issue but should not be the sole basis for a Critical redline.

## Box configuration

Set repository secrets:

- `BOX_ACCESS_TOKEN`
- `BOX_INBOX_FOLDER_ID` for inbound normalized JSON packets
- `BOX_OUTPUT_FOLDER_ID` for briefs, redlines, source packets, QA and indexes

Box is a collaboration mirror. GitHub remains authoritative for sources/facts and version history. Use a Box app or short-lived token with access limited to the two configured folders.

Recurring output names create new Box file versions after a name conflict. Content uploads finish before the final QA report is mirrored. Local QA and both ChatGPT exports include upload failures. If the final QA upload itself fails, the local diagnostics remain authoritative; Box may retain an older report.

## Required GitHub setup

1. Add repository label `policy-review` (optional; the workflow falls back if missing).
1. Add Box secrets if Box synchronization is required.
1. Configure `WEB_RESEARCH_JSON` or pass `web_packet` in manual dispatch.
1. Configure `MIDPAGE_RESEARCH_JSON` or pass `midpage_packet` after legal research.
1. Protect the default branch and require review for canonical legislation.
1. Run the workflow manually once with `strict=false`; inspect QA before enabling strict mode. Set repository variable `POLICY_LOOP_STRICT=true` to enforce strict weekday runs; unset or `false` keeps the initial diagnostic mode. Manual dispatch uses its own `strict` input independently.
1. Allow GitHub Actions to create pull requests in repository Actions settings. The workflow requires contents, issues and pull-request write permissions; it never bypasses protected-branch review.
1. Generated artifacts use one PR on `automation/adaptive-policy-loop/<base-branch>`. Pending PR artifacts are restored before intake so reviewed dispositions survive later scheduled runs. Completed output is proposed even when strict QA fails; the workflow remains failed. Review/merge the generated ledger and diagnostics through the normal protected-branch process. Workflow artifacts are retained for 14 days as a fallback if PR publication fails.
1. Critical alerts update the persistent open issue titled `Critical PETF/TCAP policy review`. Historical date-specific issues are not automatically closed.

## Self-assessment

Each run records primary-source rate, section-mapping rate, redline coverage, unresolved Critical items, connector failures and invariant checks. Failed sources remain visible in `QA_REPORT.json`; they are never silently discarded. Scoring rules are versioned in `config/policy_map.json`, so changes are reviewable and reproducible.

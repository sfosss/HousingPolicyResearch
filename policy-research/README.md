# Adaptive Policy Research Loop

This directory is the dated, review-ready output of the NYC Public Equity Transfer Framework (PETF) and Tenant Co-op Acquisition Program (TCAP) research system.

## Operating model

The loop runs on weekdays and performs seven controlled stages:

1. **Collect** official RSS items plus normalized Web, Midpage and Box packets.
2. **Constrain** results to NYC housing, household stability, civil-rights and implementation relevance.
3. **Normalize and deduplicate** with canonical URLs, content hashes and stable event IDs.
4. **Map and score** each development against PETF/TCAP sections and the Critical–Considerations scale.
5. **Draft proposed redlines** in a separate file; canonical legislation is never edited automatically.
6. **Validate** URLs, jurisdiction, mapping, redline coverage, connector health and counsel-review gates.
7. **Publish** the master CSV, dated brief, source packet, source index and ChatGPT export; optionally mirror outputs to Box.

## Human review gate

Every generated redline begins with `PROPOSED—HUMAN REVIEW REQUIRED`. Critical items receive `Needs Counsel Review` status and create a GitHub issue. Only a named reviewer may change a CSV disposition to `Accepted`; accepted language must then be applied to canonical legislation in a separate pull request.

## Daily output

`policy-research/YYYYMMDD/` contains:

- `DAILY_BRIEF.md`
- `PROPOSED_REDLINES.md`
- `SOURCE_PACKET.json`
- `QA_REPORT.json`
- `CRITICAL_ALERT.md`

The authoritative event ledger is `datasets/NYC_Housing_Subsidy_Policy_News_LIVE.csv`. Source-of-truth indexes are `indexes/SOURCE_INDEX.csv` and `.md`. Machine-readable handoff is written to `exports-for-chatgpt/`.

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
  "jurisdiction": "NYC",
  "agency": "HPD",
  "document_type": "Rule/Report/Bill/Opinion/News",
  "primary_source": true
}
```

For **Midpage**, include only opinions that have passed `analyzeOpinion`; put the exact supported proposition and scope limit in `summary`, and use the opinion or deep-link URL. Midpage results are legal research inputs, not automatic holdings applicable to PETF/TCAP.

For **Web/Perplexity Premium**, prioritize statutes, budgets, audits, agency guidance and official releases. Secondary reporting may identify an issue but should not be the sole basis for a Critical redline.

## Box configuration

Set repository secrets:

- `BOX_ACCESS_TOKEN`
- `BOX_INBOX_FOLDER_ID` for inbound normalized JSON packets
- `BOX_OUTPUT_FOLDER_ID` for briefs, redlines, source packets, QA and indexes

Box is a collaboration mirror. GitHub remains authoritative for sources/facts and version history. Use a Box app or short-lived token with access limited to the two configured folders.

## Required GitHub setup

1. Add repository label `policy-review` (optional; the workflow falls back if missing).
2. Add Box secrets if Box synchronization is required.
3. Configure `WEB_RESEARCH_JSON` or pass `web_packet` in manual dispatch.
4. Configure `MIDPAGE_RESEARCH_JSON` or pass `midpage_packet` after legal research.
5. Protect the default branch and require review for canonical legislation.
6. Run the workflow manually once with `strict=false`; inspect QA before enabling strict mode.

## Self-assessment

Each run records primary-source rate, section-mapping rate, redline coverage, unresolved Critical items, connector failures and invariant checks. Failed sources remain visible in `QA_REPORT.json`; they are never silently discarded. Scoring rules are versioned in `config/policy_map.json`, so changes are reviewable and reproducible.

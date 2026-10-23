# NYC Housing Subsidy Reform Policy Proposal — Report Blueprint

This blueprint standardizes the research-to-publication workflow for the NYC Housing Subsidy Reform policy report and keeps generative outputs aligned with data, legal requirements, and automation targets.

## 1. Report Outcomes

- Convert rental subsidies into tenant ownership via the Public Equity Transfer Framework with neutral budget impact.
- Publish presentation-ready artifacts: master report, slide deck, 1-pager, 2-page briefing memo, appendices, and annotated comments log.
- Ensure every quantitative or legal claim has an APA 7th citation and is logged for audit.

## 2. Source Data & Inputs

- **Housing Reform Forecast:** `docs/housing_reform_forecast_20251018-235748.csv` and `.json` for baseline projections.
- **Housing Reset Index:** `docs/Housing_Reset_Index/` (Python environment for index scoring; see `requirements.txt`).
- **Legislation Drafts:** `NYC-Draft-Legislation.md` for statutory anchors; align updates with this file.
- **Implementation Guides:** `Agency-Implementation-Guide.md` and `Advocacy-Toolkit.md` for operational language and stakeholder framing.

> Graphs may be generated from the forecast CSV/JSON or updated with new datasets that conform to the existing schema. Store rendered images in `docs/figures/` and reference them in the report appendices.

## 3. Standard Structure (Template)

1. Executive Summary (1–2 pages)
1. Context & Problem Statement (NYC scope only)
1. Policy Design: Public Equity Transfer Framework
1. Comparative Analysis (NYC vs. peer jurisdictions)
1. Budget Neutrality & ROI Model
1. Legal Readiness (federal/state/local) with Title IV/IX/ADA/504 review
1. Implementation Plan (agencies, roles, timelines)
1. Risk Mitigations & Equity Impact
1. Automation & Data Governance
1. Appendices: data tables, charts, legislative language, checklists

## 4. Roles & Persona Outputs

- **Municipal CFO / Policy Analyst:** Neutral budget tables, ROI projections, sensitivity charts, and funding source reallocations.
- **Civil-Rights Attorney:** Statutory compliance memo, waiver inventory (HUD MTW, state co-op provisions), and fair housing risk log.

## 5. Versioning & File Naming

- Master report filename: `Housing_Subsidy_Reform_MASTER_v[VERSION]_[YYYYMMDD].docx`.
- Increment version and tag in Git for each QA-approved draft; archive prior versions under `Archive/`.
- Track citations in a centralized Works Cited file and mirror entries in Notion and Zotero.

## 6. Data & Citation Controls

- Maintain `.env` (excluded from Git) with keys for OpenAI, Notion, GitHub, and Zotero to enable scripted pulls and pushes.
- Use Output Automater scripts to export fact tables to CSV and sync to Notion/Zotero for auditability.
- Log every graph or table with source path, query parameters, and generation timestamp.

## 7. Reverse-Connection Checklist (ChatGPT ↔ Codex ↔ Notion ↔ GitHub ↔ Zotero)

1. **Secrets Present:** Confirm `.env` matches GitHub Secrets keys and scopes.
1. **Dry Runs:** Execute CLI/API smoke tests for each platform; save logs to `logs/connection-checks/`.
1. **Sync Paths:**
   - ChatGPT → GitHub (prompt + response archives)
   - GitHub → Notion (publish docs/tasks)
   - Notion → Zotero (reading lists → collections)
   - Zotero → GitHub (annotations exports)
1. **Audit:** Review logs to ensure no credential leakage; rotate keys after tests.

## 8. Budget & ROI Modeling Steps (Recipe)

1. Ingest forecast data from `docs/housing_reform_forecast_*.csv`.
1. Apply scenario toggles: subsidy-to-equity conversion rate, per-unit support caps, credit-union participation levels.
1. Run Housing Reset Index scoring to prioritize buildings/tracts.
1. Produce tables: baseline vs. reform costs, 10-year ROI, sensitivity matrices.
1. Generate charts (PNG/SVG) and embed references in the appendices.
1. Validate all figures against Fact Check List; document in Works Cited and log files.

## 9. Legal & Legislative Insertions

- Align proposed statutes with placeholders in `NYC-Draft-Legislation.md` and track changes in a redline-friendly format.
- Maintain a waiver request inventory (HUD MTW, state co-op law updates) with status and owner.
- Standardize citation of NYC Administrative Code, NYS Real Property Law, and cooperative corporate law sections.

## 10. Task Breakdown for Generative Output

- Draft prompt library aligned to the Pattern Integration Matrix (store under `docs/prompts/`).
- Implement evaluation harness to score outputs for accuracy, citation coverage, and compliance.
- Schedule monthly Fact Check List runs; log issues in GitHub Issues and Notion.
- Build automation scripts for reverse flows; add unit tests and linting where code exists.

## 11. Delivery Readiness Checklist

- [ ] All required artifacts (report, deck, briefs, appendices) are present and versioned.
- [ ] Citations validated and synchronized to Notion/Zotero.
- [ ] Budget and ROI tables reproducible from checked-in data/scripts.
- [ ] Legal review completed with attorney persona memo attached.
- [ ] Connection logs updated and keys rotated post-testing.

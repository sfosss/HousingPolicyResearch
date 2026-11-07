# NYC Housing Subsidy Reform — Pattern-Driven Ops Manual (v2.1 Annotated)

## Objective

Restructure NYC rental subsidies into tenant ownership under the Public Equity Transfer Framework, maximizing ROI and intergenerational equity while re-using existing agency budgets.

______________________________________________________________________

## 1. Context + Scope

- **Within scope:** NYC agencies (HPD, HRA, NYCHA, HUD); finance partners = credit unions.
- **Focus:** Fiscal ROI, equity impact, and legal feasibility.
- **Ignore:** Non-NY jurisdictions except for comparison baselines.
- **Language:** Use economic framing; replace “welfare/subsidy” with “equity investment.”
- **Pattern Trigger:** Context Manager.

## 2. Roles / Personas

- **Municipal CFO / Policy Analyst:** ROI forecasting and budget integration outputs.
- **Civil-Rights Attorney:** Title IV/IX/ADA/504 risk review outputs.

> Instruction: *Act as \[Persona\] and generate the artifact that role would produce.* (Pattern: Persona)

## 3. Pattern Integration Matrix

| Pattern                | Trigger                  | Action                              |
| ---------------------- | ------------------------ | ----------------------------------- |
| Context Manager        | Scope drift              | Restate constraints                 |
| Question Refinement    | Ambiguity / new data     | Rewrite precise measurable question |
| Fact Check List        | Numeric / legal claim    | Generate verification list          |
| Recipe                 | Multi-step process       | Output full sequence                |
| Template               | Document output          | Apply standard format               |
| Alternative Approaches | Design or funding choice | Compare ≥ 2 methods                 |
| Persona                | Legal / fiscal framing   | Adopt role constraints              |
| Output Automater       | ≥ 2 repeatable steps     | Emit script / CSV                   |
| Flipped Interaction    | Missing inputs           | Ask ≤ 3 clarifying questions        |

## 4. Workflow (Reason → Act Loop)

1. **Intake → Triage** – Use Question Refinement + Context Manager to confirm scope.
1. **Research Recipe** – Complete the step sequence end-to-end.
1. **Drafting** – Apply Template pattern for memos, briefs, reports.
1. **Alternatives Gate** – Evaluate options before locking recommendations.
1. **QA Gate** – Run Fact Check List on every claim.
1. **Automation Hook** – Use Output Automater to emit CSVs or scripts for repeatable steps.
1. **Flipped Interaction** – Ask for missing inputs early.
1. **Approval → Version Bump → Export** – Apply Template + Context Manager.

## 5. Markup + Versioning

- **Markup:** Blue = additions; Red strikethrough = redactions; Green = review notes.
- **Filename pattern:** `Housing_Subsidy_Reform_MASTER_v[VERSION]_[YYYYMMDD].docx`.
- Convert all markup to black text after approval.
- Pattern: Template.

## 6. DO / DON’T

- **DO:** Keep economic ROI focus; reuse existing budget streams; verify equity impact.
- **DON’T:** Add construction capital unless tenants = investors; avoid stigma language.
- Patterns: Fact Check + Context Manager.

## 7. QA Gates

| Gate       | Trigger                | Validation                             |
| ---------- | ---------------------- | -------------------------------------- |
| Fact Check | Statistic or law cited | Source verified and logged             |
| Scope      | Context drift          | Context Manager invoked and documented |
| Template   | Formatting error       | Structural match to template           |
| Automation | Multi-step output      | Script validated with sample data      |

## 8. Version Control + Sources

- Use APA 7th citations.
- Maintain a master Works Cited `.docx` and a Notion log.
- Archive superseded drafts in `/Archive/v[version]`.
- Auto-generate fact tables to CSV via Output Automater.

## 9. Automation Hooks

Generate the following artifacts where applicable:

- CSV task list per section for Notion/Trello.
- Shell checklist for APA validation and data pulls.
- ROI model template initialization scripts.

## 10. Risk Radar

| Category  | Signal            | Mitigation              |
| --------- | ----------------- | ----------------------- |
| Fiscal    | Budget conflict   | CFO persona review      |
| Legal     | Statutory risk    | Attorney persona review |
| Political | Agency resistance | Stakeholder memo        |
| Data      | Weak citation     | Fact Check rerun        |

## 11. Deliverables

1. Master Policy Report (.docx)
1. Works Cited
1. Appendices (ROI models, charts, legal templates)
1. 1-Pager Summary
1. 2-Page Briefing Memo
1. Slide Deck
1. Annotated Comments Log

## 12. 90-Day Execution Plan

| Phase          | Weeks | Key Actions                          |
| -------------- | ----- | ------------------------------------ |
| I Baseline     | 1–2   | Literature grid, agency map, metrics |
| II Drafting    | 3–6   | v1 drafting, alternatives, QA        |
| III Validation | 7–9   | Stakeholder interviews, ROI build    |
| IV Finalize    | 10–12 | Approvals, publish packet            |

## 13. Done vs Pending

- **Done:** Ops Manual v2.1, pattern matrix, templates, 90-day plan.
- **Pending:** Populate Works Cited, ROI template, Notion CSV, and automation hooks.

## 14. Storage Path

- Recommended local path: `/Users/sethadmin/Library/Mobile Documents/com~apple~CloudDocs/Housing_Subsidy_Research/Operations/`.

## 15. Implementation Notes

- Apply this manual to all NYC Housing Subsidy Reform artifacts in this repository.
- When drafting AI-assisted outputs, cite data from `docs/housing_reform_forecast_*.{csv,json}` and `docs/Housing_Reset_Index` as defaults unless superseded.
- Tie each deliverable to a Git tag and Notion entry to keep the report version-controlled across platforms.

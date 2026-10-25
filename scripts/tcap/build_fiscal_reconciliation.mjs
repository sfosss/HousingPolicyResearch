import fs from "node:fs/promises";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const workbook = Workbook.create();
const sheet = workbook.worksheets.add("Fiscal reconciliation");
sheet.showGridLines = false;
sheet.getRange("A1").values = [["TCAP fiscal reconciliation v1 — internal claims, not certified forecasts"]];
sheet.getRange("A3:C3").values = [["Input / claim", "Value", "Source and status"]];
sheet.getRange("A4:C15").values = [
  ["CityFHEPS illustrative annual ratio / HH", 21154, "CBC Feb 2025: $1.1B / ~52,000; rounded ratio, not reported mean. https://cbcny.org/research/cityfheps-hits-1-billion"],
  ["HPD HCV annual cost / unit", 16896, "NYS Comptroller: $1,408/month, Nov 2024. https://www.osc.ny.gov/reports/budget/fed-funding-ny/section-8-housing-choice-vouchers"],
  ["TCAP annual operating subsidy / HH", 21800, "Internal PET_TCAP_Policy_Proposal_v5_2.md §IV.A; unverified"],
  ["Single-channel capital / unit", 165000, "Internal PET_TCAP_Policy_Proposal_v5_2.md §IV.B; rounded planning input"],
  ["Audit-stated 10-year public investment / HH", 241993, "TCAP_Fiscal_Model_Audit_v2.md, Issue 3; composition not reconciled to capital plus operating cost"],
  ["Audit-stated 10-year member equity / HH", 66582, "TCAP_Fiscal_Model_Audit_v2.md, Issue 3; internal amortization scenario"],
  ["Audit-stated 10-year building equity / HH", 10184, "TCAP_Fiscal_Model_Audit_v2.md, Issue 3; internal estimate"],
  ["Published direct asset ROI claim", 0.308, "PET_TCAP_Policy_Proposal_v5_2.md §IV.C; denominator undisclosed"],
  ["Three-channel weighted cost / unit", 212969, "PET_TCAP_Final_Submission_Package_20260411.md §4.9; internal model"],
  ["Borough-model weighted cost / unit", 254167, "TCAP_Borough_Fiscal_Model_v1.md; distinct model and channel scope"],
  ["Borough-model 10-year equity / HH", 86555, "TCAP_Borough_Fiscal_Model_v1.md; distinct model"],
  ["Pilot unit count", 1000, "PET_TCAP_Policy_Proposal_v5_2.md §IV.D; planning scenario"],
];
sheet.getRange("A18:C18").values = [["Recalculated output", "Formula result", "Interpretation"]];
const outputs = [
  [19, "Annual TCAP premium vs illustrative CityFHEPS", "=B6-B4", "Different programs and periods; not a budget saving"],
  [20, "Premium as % of illustrative CityFHEPS", "=B19/B4", "Rounds to about 3.1%"],
  [21, "Audit-stated 10-year assets / HH", "=B9+B10", "Member plus building equity"],
  [22, "Assets / audit-stated investment", "=B21/B8", "31.7%; not the claimed 30.8%"],
  [23, "Difference from published direct ROI", "=B22-B11", "Percentage-point discrepancy; denominator unresolved"],
  [24, "Member equity / single-channel capital", "=B9/B7", "Different basis from 10-year public investment"],
  [25, "Borough equity / borough total cost", "=B14/B13", "34.1%; distinct scenario"],
  [26, "Pilot capital", "=B7*B15", "1,000 units × single-channel input"],
  [27, "Pilot annual operating subsidy", "=B6*B15", "1,000 households × annual input"],
  [28, "Pilot member equity", "=B9*B15", "Audit-stated 10-year equity × units"],
  [29, "Borough less three-channel cost / unit", "=B13-B12", "Different model scopes; do not silently average"],
];
for (const [row, label, formula, note] of outputs) {
  sheet.getRange(`A${row}`).values = [[label]];
  sheet.getRange(`B${row}`).formulas = [[formula]];
  sheet.getRange(`C${row}`).values = [[note]];
}
sheet.getRange("A32:C34").values = [
  ["Unresolved: 30.8%", null, "No numerator/denominator pair in the supplied audit reproduces this claim."],
  ["Unresolved: break-even", null, "Year 12–13, 18–19, and 23–27 use incompatible definitions and scenarios; no dated cash-flow series supplied."],
  ["Unresolved: 6.2:1 societal ROI", null, "Externality valuations and counterfactual attribution are not supplied in a reproducible series."],
];
sheet.getRange("A1:C1").format.fill = "#17365D";
sheet.getRange("A1:C1").format.font.color = "#FFFFFF";
sheet.getRange("A3:C3").format.fill = "#D9EAF7";
sheet.getRange("A18:C18").format.fill = "#D9EAF7";
sheet.getRange("A1:C34").format.rowHeight = 22;
sheet.getRange("A:A").format.columnWidth = 43;
sheet.getRange("B:B").format.columnWidth = 20;
sheet.getRange("C:C").format.columnWidth = 115;
sheet.getRange("B4:B15").setNumberFormat("#,##0.00");
sheet.getRange("B19:B29").setNumberFormat("#,##0.00");
for (const row of [11, 20, 22, 23, 24, 25]) sheet.getRange(`B${row}`).setNumberFormat("0.0%");
sheet.freezePanes.freezeRows(3);
workbook.recalculate();
const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save("data/tcap/2026-04/TCAP_Fiscal_Reconciliation_v1.xlsx");
const preview = await workbook.render({ sheetName: "Fiscal reconciliation", range: "A1:C34", scale: 1.25, format: "png" });
await fs.writeFile("/tmp/tcap-fiscal-reconciliation-preview.png", new Uint8Array(await preview.arrayBuffer()));

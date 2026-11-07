# Fiscal reconciliation v1

The [versioned workbook](../../../data/tcap/2026-04/TCAP_Fiscal_Reconciliation_v1.xlsx) traces every included input to a source and recalculates the direct comparisons. The [builder](../../../scripts/tcap/build_fiscal_reconciliation.mjs) makes the formulas reproducible. The source files are the [April fiscal audit](model-sources/TCAP_Fiscal_Model_Audit_v2.md), [borough model](model-sources/TCAP_Borough_Fiscal_Model_v1.md), and [acquisition channels model](model-sources/TCAP_Acquisition_Channels_Model_v1.md). These are unverified project working papers. The workbook is a reconciliation of draft claims, not an agency-certified forecast.

| Check                                                           |                                            Result | Disposition                                                                |
| --------------------------------------------------------------- | ------------------------------------------------: | -------------------------------------------------------------------------- |
| TCAP annual operating premium over illustrative CityFHEPS ratio |                             $646/household, 3.05% | Arithmetic verified; the two inputs are different estimates and periods.   |
| Ten-year member plus building equity                            |                                 $76,766/household | Sum of the fiscal audit's $66,582 and $10,184 assumptions.                 |
| Assets divided by audit-stated ten-year public investment       |                                            31.72% | $76,766 ÷ $241,993. Does not reproduce the published 30.8%.                |
| Member equity divided by $165,000 capital                       |                                            40.35% | Different denominator; not a substitute for direct ROI.                    |
| Borough-model equity divided by borough-model cost              |                                            34.05% | $86,555 ÷ $254,167. Different model from the $212,969 three-channel claim. |
| 1,000-unit pilot capital, annual subsidy, member equity         | $165 million; $21.8 million/year; $66.582 million | Correct multiplication of the selected assumptions.                        |

The April fiscal audit itself states **31.7%** from $76,766 of ten-year assets and $241,993 of public investment. Elsewhere it calls **30.8%** the direct ROI without showing a matching denominator. Those are different claims. The $241,993 investment is also not reconciled to the proposal's $165,000 capital input plus recurring subsidy, so even 31.7% is only a faithful reproduction of that audit's ratio.

The **$165,000** planning figure is not the exact midpoint of $128,000–$200,000; the midpoint is **$164,000**. The **$212,969** three-channel and **$254,167** borough-weighted costs differ by **$41,198 per unit** and use distinct scenario descriptions. They cannot be averaged or substituted without a channel-level source schedule.

No supplied workbook provides a comparable dated series for capital deployment, operating subsidy, member equity, building value, salvage value, and discounting. Consequently, the claimed **Years 12–13** and **Years 23–27** break-even points and **6.2:1** social ROI cannot be recomputed. The borough model explicitly says it could not replicate the baseline Years 12–13 using its stated assumptions.

Before choosing a controlling forecast, obtain the original model's period-by-period cash flows and define: (1) public investment and its capital/operating components, (2) household equity valuation and restrictions, (3) the comparator population and time period, (4) any shelter and health counterfactuals, and (5) the break-even definition. Until then, the workbook intentionally leaves unsupported headline outputs unresolved rather than filling them with invented values.

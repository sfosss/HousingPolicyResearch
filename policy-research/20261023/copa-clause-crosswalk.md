# COPA / TCAP clause crosswalk (candidate baseline) — Issue #146

Status: PROPOSED. AI-assisted working draft; source cutoff October 23, 2026 (prepared October 26, 2026).
Not approved-baseline redlines. No canonical policy file modified. No policy approval, incorporation, or mayoral signature is established.

## 1. Verification record

| Item | Result | Status |
| --- | --- | --- |
| Official record | Legistar ID 8027957 displays "Enacted (Mayor's Desk for Signature)"; no enactment date or law number | Mayoral action, law number, effective date: NOT verified |
| Fiscal attachment 58 (Int. 905-A) | `policy-research/20261023/copa-fiscal-original.docx.base64` decodes to 34,420 bytes (matches issue), SHA-256 `1bc3195cefffae3b634b6e4f2a08b8aff343a3dae8ed45f606f1a62786cdc7c6` | Preserved; recorded here |
| Fiscal extraction | `policy-research/20261023/copa-fiscal-extracted.txt`, page markers 1 and 2 | Page-linked text only; table visual check was done in the issue update, not repeated here |
| Candidate baseline | `docs/exports/legal-frameworks/LOCAL_LAW_C_COPA_TCAP_Integration.md`, 131 lines, SHA-256 `31e5ebe07f2b0054db7325ffa2a9eea37fb21d329230f3c88799b3f3a02b2c3e` | NOT authenticated as v1.1 baseline |
| Approved v1.1 baseline | `PET_TCAP_Legislative_Portfolio_v1_1_20260919.pdf` | NOT FOUND. No file matching `*20260919*` exists in this checkout |

Retrieval history (preserved): the web reader returned HTTP 410 twice; direct HTTPS download then succeeded (issue update, Oct 23). The earlier "could not be recovered" statement is superseded.

Limits of this run: the checkout is a shallow clone with a single commit (2b33382), so the history/branch search for the exact baseline could not be completed. Only `main` and this branch exist. The Git blob id of the candidate (issue cites 12f59105… at main 4a21144) was not recomputed here, because `git hash-object` was not permitted in this environment.

## 2. Fiscal extraction (Int. 905-A, Council Finance, prepared Oct 19, 2026; hearing Oct 22, 2026; page 1-2)

| Element | Value | Page |
| --- | --- | --- |
| Effective date of bill | One year after becoming law | 1 |
| Revenues | $0 (all years) | 1 |
| Expenditures | FY28 $128,000; FY29 $170,000; full impact FY29 $170,000 | 1 |
| Personal Services | $115,500 (one data analyst, incl. fringe) | 2 |
| OTPS | $55,000 (printing and mailing) | 2 |
| Component total | $170,500 vs. stated $170,000: $500 discrepancy, needs reconciliation | 2 |
| Source of funds | General Fund | 2 |
| OMB | Did not provide an estimate | 2 |
| One-time costs | None stated | n/a |
| Acquisition / rehabilitation capital | Excluded; the estimate covers HPD administration only | n/a |
| Qualified-entity periods | 20 days statement of interest; 70 days first offer; right of first refusal | 1 |

Zero cost must not be inferred for financing, predevelopment, rehabilitation, or tenant assistance. The estimate does not address them.

## 3. Clause-level crosswalk (candidate text; every row is a proposal pending review)

Action key: RETAIN / REPLACE / EXPAND / SEPARATE-AUTH (separate legal authority needed).

| # | Candidate location | Exact existing text (abridged) | Proposed treatment | Action | Source pinpoint | Fiscal effect | Responsible agency | Remaining legal question |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Header, §1, §26-2001 (lines 3, 9, 15) | "Amendments to Local Law Intro 902-A"; "amends Intro 902 COPA provisions" | Reconcile bill identity to Int. 905-A and code numbering once the passed text is authenticated. Keep the archived text and mark it superseded in a new version. | REPLACE (identifiers) | Fiscal stmt p.1 (Int. No. 905-A) | None | Council / counsel | Which Admin. Code sections did the passed bill assign? |
| 2 | §26-2002(a)(1)-(3) (lines 19-25) | HPD designates "TCAP-ready entities" as a special Qualified Entity category, including CLTs and tenant associations incorporated "as nonprofits or cooperative-formation entities" | Test each category against the certified-nonprofit / nonprofit-joint-venture requirement in 905-A. Treat the CLT land-only pathway separately. Do not create a category the bill does not allow. | REPLACE / SEPARATE-AUTH | Fiscal stmt p.1 summary | Possible HPD certification workload; not in estimate | HPD | Can a tenant-formation entity be certified under the passed text? |
| 3 | §26-2002(b) (lines 27-35) | Prior experience, binding conversion commitment, permanent affordability, "at least 40% Black and Latino membership" | Keep experience and affordability objectives. The membership threshold moves to row 8. | RETAIN (1-3), see row 8 (4) | n/a | None | HPD | Whether a binding commitment can be a certification condition |
| 4 | §26-2002(c)(1)-(4) (lines 37-45) | 60-day SOI "(vs. standard 45 days)"; 120-day offer "(vs. 90)"; extension to 180; ROFR 18 months "(vs. 12)" | The "standard" figures do not match the Council record: 20-day SOI, 70-day offer. Do not state comparisons against 45/90. Design financing service standards (HPD/lender response times, pre-approval) inside the 20/70 clocks. Any extension needs separate authority. | REPLACE / SEPARATE-AUTH | Fiscal stmt p.1 | Not in estimate | HPD, owner, lenders | Can the 20/70 periods be extended by rule or only by statute? ROFR duration in passed text is unverified. |
| 5 | §26-2002(d) (line 47) | Owner tax incentives, citing "A355-C/S1718-B" | State-law citation not verified; do not rely on it. | SEPARATE-AUTH | n/a | Revenue loss, unquantified | DOF / State | Is there tax-incentive authority at all? |
| 6 | §26-2003(a)-(b) (lines 51-71) | Tenants "must form" an association; binding commitment; 75% certification in 12 months; 10-year occupancy protection; democratic control by Year 3 | Keep objectives. Review: enforceability, voluntary participation (no tenant required to join or buy), permanent protection of non-purchasers (consistent with R1-R3 in `policy-research/redlines/PET_TCAP_R1_R4_20261026.md`), independent counsel for tenants, accessible governance. The "10 years" limit is shorter than the non-purchaser protection proposed in R1/R2. | EXPAND | Candidate lines 59-71 | HPD support staff and tenant services, not in estimate | HPD | Can HPD condition COPA preference on tenant-association formation? |
| 7 | §26-2003(c)-(d) (lines 73-89) | 60-day cure; HPD may appoint successor; TCAP Conversion Monitor | Retain. Add a tenant-initiated dispute path and outcome reporting. | RETAIN / EXPAND | n/a | New monitor staff, not in estimate | HPD | Authority to appoint a successor owner |
| 8 | §26-2005(a) and §26-2002(b)(4) (lines 35, 111-123) | "At least 40% Black and Latino membership"; "at least 50% of initial member equity distributions" to Black and Latino households | Obtain civil-rights counsel review before retaining. Evaluate lawful outreach and outcome monitoring as alternatives. Do not advance as drafted. | REPLACE (pending counsel) | n/a | None | HPD, Law Dept. | Is any race-based quota or distribution lawful here? |
| 9 | §26-2004(a)(1)-(3), (b) (lines 93-101) | DSS letter honoring CityFHEPS; "Transfer subsidy payments to the cooperative's account"; "80% carrying charge / 20% equity account" | Require stream-specific statutory, program and appropriation authority for each subsidy. Do not book rental assistance as equity capital by assumption. Keep voucher-continuity objective as benefit continuity for tenants. | SEPARATE-AUTH | n/a | Potentially large; none in estimate | DSS / HRA, HPD | Does program law allow diversion of vouchers to equity? |
| 10 | §26-2004(c)-(d) (lines 103-109) | Prioritize applications below 50% AMI; monitor 15% affordability cap | Retain as monitoring; fund through a separate appropriation. | RETAIN / SEPARATE-AUTH | n/a | Unquantified | DSS, HPD | Legal basis for priority |
| 11 | §26-2006 (lines 125-127) | Effective on enactment | The 905-A effective date is one year after becoming law. Align. | REPLACE | Fiscal stmt p.1 | Moves first fiscal year to FY28 | Council | Final effective date once signature is verified |

## 4. Required additions (not present in the candidate)

| Topic | Proposed treatment | Authority / funding | Agency |
| --- | --- | --- | --- |
| Rapid acquisition / predevelopment / rehabilitation | New commitments with defined turnaround, kept apart from the COPA clocks | Capital and appropriation authority required; none exists in 905-A | HPD, HDC |
| Independent tenant assistance | Funded technical assistance and independent counsel for tenants | Contract funding needed | HPD |
| Nonpurchaser safeguards | Carry R1-R3 into this chapter | Counsel review | HPD |
| Benefit continuity | Tenant-level continuity guarantee without equity diversion | Program law | DSS / HRA |
| Reserves | Operating and capital reserve standards | Funding source open | HPD |
| Outcome reporting | Annual metrics; align with HPD annual report required by 905-A | Within or beyond the $170,000 analyst? Unverified | HPD |

## 5. Task status for Issue #146

| Task | Result |
| --- | --- |
| Mayoral action, law number, effective dates, authenticated text | OPEN. Not verifiable from this checkout. |
| Fiscal PDF retrieved with provenance | DONE in part: checksum and page-linked extraction recorded above. $500 discrepancy open. |
| Exact editable baseline located | OPEN. Not found. Shallow clone. Only candidate exists. |
| Clause crosswalk | DRAFT above, on the candidate only. Re-run after baseline authentication. |
| Required additions | DRAFT above. |
| Advance to Verified | Only the fiscal figures above. All policy recommendations stay Proposed. |

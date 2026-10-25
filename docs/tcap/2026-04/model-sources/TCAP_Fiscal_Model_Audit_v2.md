# TCAP / PET FRAMEWORK — FISCAL MODEL AUDIT (v2)

**Prepared for:** NYC Mayor's Office Submission Review
**Prepared by:** Seth Foss, Housing Policy Researcher, Cooper Square Committee
**Audit Date:** April 3, 2026
**Status:** COMPREHENSIVE RECONCILIATION — All six critical inconsistencies resolved

______________________________________________________________________

## PURPOSE

This audit identifies and resolves six critical fiscal inconsistencies across the TCAP/PET Framework document suite. Each inconsistency is traced to its source documents, a defensible corrected figure is provided with citations, and a reconciled 10-year fiscal model follows at the end.

**Documents Reviewed:**

| Document                                     | Version/Date             | Abbreviation   |
| -------------------------------------------- | ------------------------ | -------------- |
| TCAP_Policy_Proposal_MASTER_v3.md            | v3.0, Dec 15, 2025       | **Master v3**  |
| TENANT CO-OP ACQUISITION PROGRAM Part I-III  | v3.0 FINAL, Dec 26, 2025 | **Part I-III** |
| PART_III_Fiscal_Analysis_Academic.md         | Deep research, 2026      | **Part III-A** |
| Rental_Ripoff_Testimony (Feb 2026)           | Feb 26, 2026             | **Testimony**  |
| PART_II-C_Equity_Intergenerational_Wealth.md | Deep research, 2026      | **Part II-C**  |
| PART_II-B_LECoop_Governance.md               | Deep research, 2026      | **Part II-B**  |

______________________________________________________________________

## ISSUE 1: EQUITY PER HOUSEHOLD INCONSISTENCY

### The Problem

Three mutually exclusive 10-year equity-per-household figures appear across the document suite:

| Figure          | Source Document                                 | Model Assumptions                                                                                           |
| --------------- | ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **$32,000/HH**  | Part I-III (§1 summary table); Master v3 (§1.4) | Phased 50/65/75 subsidy allocation; $5,800/yr cost structure                                                |
| **$66,500/HH**  | Testimony (§VI Table A); Part III-A (§3.5.3)    | Fixed 80/20 subsidy split; $21,600/yr subsidy; includes $8K initial stake + 20% credits + principal paydown |
| **$127,836/HH** | Part II-C (§2.9 year-by-year table)             | Fixed 20% subsidy + mortgage principal paydown at inflated rate                                             |

### Root Cause Analysis

**The $32,000 figure** comes from the earliest TCAP model (Master v3, December 2025), which uses a phased subsidy allocation schedule (50% → 65% → 75% equity) and a lower-resolution cost model ($5,800/yr per-capita cost). This model was superseded by the detailed Part III-A analysis.

**The $66,500 figure** comes from the thoroughly documented Part III-A model using a fixed 80/20 subsidy split (consistent with the statutory language in § 26-1803). It includes three equity components:

- $8,000 initial equity stake (down payment from redirected first-month subsidy + member savings)
- ~$48,264 cumulative from 20% monthly subsidy credits ($360/mo in Year 1, growing to $447/mo by Year 10)
- ~$10,184 from member's share of mortgage principal paydown

Part III-A provides year-by-year tables, sensitivity analysis (±7.3% variance band), and explicit data confidence ratings. This is the most rigorously documented figure.

**The $127,836 figure contains a computational error.** Part II-C calculates mortgage principal paydown as follows:

> "Annual payment: $51,576 … Principal portion (Year 1): $15,576 … Per-member principal (Year 1): $15,576 ÷ 25 = $623/member … Per-member annual (Year 1): $623 × 12 = $7,476"

This is incorrect. $15,576 is already the *annual* principal. Dividing by 25 members yields $623 per member **per year**, not per month. Multiplying by 12 again double-counts by a factor of 12. The correct per-member principal paydown in Year 1 is **$623**, not $7,476. This error inflates cumulative equity by approximately $70,000–$80,000 over ten years.

### Corrected Figure

**Defensible 10-year equity per household: ~$66,500 (±7.3%)**

This is the Part III-A figure, supported by:

- Detailed year-by-year projections with explicit assumptions
- Sensitivity analysis showing range of $61,742 (conservative) to $71,422 (optimistic)
- Consistent with the 80/20 split codified in proposed § 26-1803
- Consistent with Testimony Table A trajectory ($4,320 → $48,264 cumulative at Year 10)

**Benchmark comparison:** NYC HDFC limited-equity cooperatives show share values ranging from $85,000 to $500,000+ (Skybriz/Brick Underground, 2025), though these reflect unrestricted resale in some buildings. The Champlain Housing Trust's 25% equity-share model demonstrates the viability of shared-equity homeownership producing meaningful wealth over 10+ years (Lincoln Institute, 2023). The $66,500 figure—representing equity under a *limited*-equity resale formula in a subsidized building—is conservative and defensible relative to these benchmarks.

### Required Corrections

1. **Part I-III summary table**: Change "$32,000/household" to "$66,500/household" with footnote referencing Part III-A methodology
1. **Master v3 §1.4**: Update wealth generation table to use Part III-A figures
1. **Part II-C**: Correct the principal paydown calculation (remove ×12 error); recalculate cumulative equity to ~$66,500

______________________________________________________________________

## ISSUE 2: THE "$37.5 BILLION" SAVINGS CLAIM

### The Problem

The user identified a "$37.5 billion net public savings over ten years" claim attributed to the PET report. Upon thorough search of all available documents, **no document contains the figure "$37.5 billion."**

What exists instead:

| Figure               | Source                       | What It Represents                                         |
| -------------------- | ---------------------------- | ---------------------------------------------------------- |
| **$37,500/HH**       | Part I-III (multiple tables) | Per-household 10-year TCAP cost (one-time investment)      |
| **$3,751M ($3.75B)** | Testimony §VI 10-year table  | "Net savings" for 150 buildings, 38,700 HH                 |
| **$23.0B**           | Part I-III §1 summary        | Savings from full $5.2B/yr system conversion over 10 years |

### Root Cause Analysis

The "$37.5 billion" appears to be a misreading or conflation of **$37,500 per household** (a per-unit figure appearing dozens of times in Part I-III) with a system-level savings figure.

**However, the $3,751M ($3.75B) "net savings" figure in the Testimony is itself problematic.** The Testimony table reads:

| Category                     | Status Quo | TCAP    | Net Savings |
| ---------------------------- | ---------- | ------- | ----------- |
| Total 10-yr subsidy spending | $5,200M    | $1,449M | $3,751M     |

The $5,200M figure is **the annual systemwide subsidy budget** ($5.2B/year for all 895,000 households), NOT the 10-year cost of serving the 38,700 households that TCAP would convert. This is an apples-to-oranges comparison.

**Correct calculation for 150 buildings / 38,700 HH:**

- Status quo cost: 38,700 HH × $21,000/yr (CityFHEPS avg) × 10 years = **$8.127B**
- TCAP cost: 38,700 HH × $37,500/HH (one-time) = **$1.451B** (aligns with $1,449M)
- BUT: TCAP members also receive ongoing subsidy support of $21,600/yr for carrying charges and equity — the $37,500 figure only captures the initial investment, not ongoing subsidy flow

**More accurate comparison using Part III-A's per-household figures:**

- Status quo 10-year cost per HH: $210,000 ($21,000/yr × 10)
- TCAP 10-year cost per HH: $216,000 ($21,600/yr × 10)
- Difference: TCAP costs $6,000 MORE per household over 10 years, NOT less

The savings argument for TCAP is **not that it costs less in direct subsidy**, but that it:

1. Produces $66,500/HH in wealth (vs. $0 under status quo)
1. Eliminates future subsidy dependence (cooperatives become self-sustaining)
1. Avoids shelter cycling costs ($84,800/yr per family)
1. Generates societal externalities (reduced evictions, health improvements, educational outcomes)

### Corrected Figure

**There is no defensible "$37.5 billion savings" claim. The figure should be removed entirely.**

The defensible fiscal narrative is:

- **Direct subsidy cost**: TCAP costs ~3% more than CityFHEPS per household over 10 years ($216,000 vs $210,000)
- **Asset creation**: TCAP produces $66,500/HH in member equity (status quo produces $0)
- **Net public ROI**: For every $3.24 in TCAP subsidy, $1.00 in permanent household assets is created (Part III-A §3.6.3)
- **Shelter cost avoidance (for at-risk subset)**: If 15% of TCAP households would otherwise cycle through shelter, the avoidance savings are significant: 5,805 HH × $84,800/yr × 10 years = $4.92B — but this is a *conditional* savings, not a guaranteed one, and should be clearly labeled as such

### Required Corrections

1. **Remove** any claim of "$37.5 billion" savings
1. **Correct** the Testimony 10-year scaling table to use consistent denominators (same population for both columns)
1. **Reframe** the fiscal argument around asset creation ROI and conditional shelter-avoidance savings, not direct subsidy savings

______________________________________________________________________

## ISSUE 3: ROI RATIO INCONSISTENCY (3.4:1 vs 6.2:1 vs 2.9:1)

### The Problem

Three different ROI ratios appear:

| Ratio     | Source                | Definition                                                                         |
| --------- | --------------------- | ---------------------------------------------------------------------------------- |
| **6.2:1** | Testimony §VI         | "Full societal ROI" including externalities                                        |
| **3.4:1** | Testimony §VI         | "Direct financial ROI excluding externalities"                                     |
| **2.9:1** | Part I-III §1 summary | "For every dollar of public investment, society captures $2.90 in public benefits" |

Additionally, Part III-A uses a percentage metric: **31.7% asset creation per subsidy dollar** ($76,766 assets ÷ $241,993 subsidy).

### Root Cause Analysis

**The 6.2:1 ratio** is derived from the Testimony's 150-building scaling table:

$8.937B total societal benefit ÷ $1.449B TCAP investment = 6.17:1

This includes $2.8B in eviction prevention, $600M in health cost reduction, $800M in educational outcomes, and $400M in emergency services reduction — all speculative externality values based on academic literature.

**The 3.4:1 ratio** lacks clear derivation in the Testimony. It claims to be "direct financial ROI excluding externalities," but no calculation is shown.

Attempting to derive it: Direct financial benefit from the Testimony table = $3,751M net savings ÷ $1,449M = 2.59:1. Adding $1,236M in tenant wealth created: ($3,751M + $1,236M) ÷ $1,449M = 3.44:1. This appears to be the derivation — but as shown in Issue 2, the $3,751M savings figure is flawed.

**The 2.9:1 ratio** comes from a different model entirely (Part I-III, December 2025 version), using different cost assumptions ($5,800/yr per-capita status quo cost).

### Corrected Figures

Using only verified inputs from Part III-A:

**Direct Asset-Creation ROI (per household):**

- 10-year public investment: $241,993 (cumulative subsidy)
- 10-year assets created: $76,766 (member equity $66,582 + building equity $10,184)
- **Asset ROI: 31.7%** (or **0.32:1**)

This is not a traditional "ROI" in the sense that $1 invested returns $0.32 in tangible assets — but the remaining $0.68 provided housing (the same service status-quo subsidies provide for $0 in assets).

**Conditional Shelter-Avoidance ROI (for at-risk subset):**

If TCAP prevents shelter entry for even a fraction of members, the avoided costs dwarf the subsidy premium. For illustration:

- TCAP premium over status quo per HH: $6,000 over 10 years
- One year of family shelter avoided: $84,800
- If TCAP prevents even one shelter stay per household, the return on the premium alone is 14:1

**Societal ROI (6.2:1):** This ratio is only defensible if clearly labeled as including speculative externality valuations based on published academic literature (Desmond 2016, Maqbool et al. 2015, Buckner 2008). The individual externality estimates ($2.8B eviction prevention, $600M health, etc.) should cite specific studies and include confidence intervals.

### Required Corrections

1. **Drop the 3.4:1 figure** — its derivation relies on the flawed $3,751M savings number
1. **Retain the 6.2:1 figure** only with explicit "full societal ROI with externalities" label and study citations
1. **Use 31.7% asset creation ROI** as the primary direct fiscal metric — it is verifiable and conservative
1. **Replace the 2.9:1 figure** in Part I-III with updated calculations

______________________________________________________________________

## ISSUE 4: PER-UNIT COST PROPAGATION ($43K vs $150–250K)

### The Problem

| Figure                | Source                           | What It Represents                                           |
| --------------------- | -------------------------------- | ------------------------------------------------------------ |
| **$43,000–$43,500**   | Master v3 §3.2, §1.4             | "One-time conversion cost per unit"                          |
| **$52,500–$64,286**   | Master v3 §3.3 Scenarios A-B     | Scenario-specific per-unit costs (including some repairs)    |
| **$150,000–$250,000** | Fact-check document (correction) | Full conversion + rehabilitation cost per unit               |
| **$128,000–$215,000** | Perplexity synthesis             | One-time costs including rehabilitation                      |
| **$60,000/share**     | Part III-A §3.3.1                | Acquisition price per co-op share (non-luxury outer borough) |

### Root Cause Analysis

The **$43,000 figure** in Master v3 is constructed as:

| Component        | Amount      |
| ---------------- | ----------- |
| Down Payment     | $20,000     |
| Acquisition Loan | $23,500     |
| **Total**        | **$43,500** |

This covers only acquisition financing — it excludes rehabilitation, legal costs, TA costs, and capital reserves. Even Master v3's own scenarios show per-unit costs of $52,500 (Bronx) and $64,286 (Brooklyn) when repairs, legal fees, and tax lien payoffs are included.

**HPD's ANCP program** provides City Capital subsidies of **up to $200,000 per unit** for cooperative conversion of distressed occupied properties (HPD, ANCP Term Sheet). This is the closest real-world NYC benchmark for the type of conversion TCAP envisions.

**Part III-A** uses $60,000/unit acquisition price (pre-rehab), consistent with median per-unit prices for older non-luxury multifamily buildings. Adding rehabilitation: $60,000 acquisition + $50,000–$100,000 rehab = $110,000–$160,000 total.

### Corrected Figure

**Defensible per-unit conversion cost: $128,000–$200,000**

Breakdown:

| Component                    | Low Estimate | High Estimate |
| ---------------------------- | ------------ | ------------- |
| Acquisition (per-unit share) | $50,000      | $80,000       |
| Rehabilitation               | $50,000      | $80,000       |
| Legal, appraisal, title      | $3,000       | $5,000        |
| Technical assistance         | $5,000       | $10,000       |
| Capital reserves (initial)   | $5,000       | $10,000       |
| Contingency (10%)            | $11,300      | $18,500       |
| **Total per unit**           | **$124,300** | **$203,500**  |

Using midpoint: **~$165,000/unit** for a "moderate rehabilitation" conversion.

**Sources:** HPD ANCP term sheet (up to $200K/unit subsidy); Master v3 Scenario A ($52,500 for minimal rehab); Master v3 Scenario B ($64,286 with moderate repairs); NYC Comptroller ANCP audit (noted 81 of 113 buildings still awaiting conversion, indicating actual costs often exceed initial estimates).

### Impact on Other Figures

Using $165,000/unit instead of $43,000/unit:

- **150 buildings × 25 units**: $165K × 3,750 = **$618.75M** (vs. $161M at $43K)
- **Break-even payback** (simple): $165K ÷ $8,600/yr savings = **19.2 years** (vs. 5.0 years)
- **5-year citywide investment**: $618.75M (vs. Master v3's $7.5B, which used 150 × 25 × $43K = $161.25M — note: Master v3 actually says "$7.5B" which itself is an error; $161.25M ≠ $7.5B)

### Required Corrections

1. **Replace** $43,000 per-unit figure throughout Master v3 with $128,000–$200,000 range
1. **Recalculate** all scaling projections, break-even timelines, and investment totals
1. **Fix** the apparent calculation error in Master v3 §1.4 ("$7.5B" should be ~$161M at old rate or ~$619M at corrected rate)
1. **Use** HPD ANCP as the primary benchmark citation

______________________________________________________________________

## ISSUE 5: BREAK-EVEN INCONSISTENCY

### The Problem

At least five different break-even timelines appear:

| Timeline      | Source                            | Definition                                                            |
| ------------- | --------------------------------- | --------------------------------------------------------------------- |
| 2.9–3.7 years | Master v3 §3.3; Final Housing doc | Simple payback on conversion cost vs annual savings (using $43K cost) |
| 5.0 years     | Master v3 §1.4                    | $43,000 ÷ $8,600/yr savings                                           |
| 5.4 years     | Master v3 Scenario B              | 42-unit Brooklyn building                                             |
| Years 12–13   | Part III-A §3.7; Testimony §VI    | Cumulative assets = cumulative subsidy                                |
| Year 1        | Part I-III §12.3                  | "TCAP already cheaper" (using flawed cost comparison)                 |

### Root Cause Analysis

These measure fundamentally different things:

1. **Conversion payback (3.7–5.4 years):** One-time conversion cost ÷ annual operating cost savings vs status quo. This answers: "How long until the upfront investment is recouped by annual savings?" Uses the $43K figure — correcting to $165K makes this 19+ years.

1. **Asset = subsidy (Years 12–13):** When cumulative member equity + building equity equals cumulative public subsidy invested. This answers: "When have we created as much permanent wealth as we've spent?" This is the Part III-A definition and is well-documented.

1. **Year 1 break-even:** Uses the flawed cost comparison from Part I-III where TCAP's per-household cost ($37,500 one-time) is compared to status quo's annual cost ($5,800/yr). This is not a meaningful break-even calculation.

### Corrected Figures

**Two legitimate break-even metrics should be used, clearly labeled:**

**A. Conversion Investment Payback:**

Using corrected per-unit cost ($165,000) and the documented annual savings of $8,600/unit (Master v3 §3.1):

$165,000 ÷ $8,600 = **19.2 years** (simple payback)

However, this $8,600 annual savings figure itself uses the $32,800 status quo cost that includes shelter/eviction response costs ($7,400/yr) that not all voucher households would incur. Using only the direct subsidy comparison ($21,600 TCAP vs $21,000 CityFHEPS), TCAP costs MORE, so simple payback is never achieved through direct savings alone. The argument must shift to asset creation.

**B. Asset-Equals-Subsidy (Part III-A methodology):**

Part III-A documents this clearly:

- By Year 10: cumulative subsidy = $241,993; cumulative assets = $76,766 (32% of subsidy)
- Extrapolating: assets catch cumulative subsidy around **Years 12–13**
- This assumes continued cooperative operation and equity accumulation beyond Year 10

This is the more intellectually honest metric and should be the primary break-even figure used.

### Required Corrections

1. **Use Years 12–13** as the primary break-even figure throughout
1. **Clearly label** it as "asset-equals-subsidy" break-even
1. **Remove** the 5-year and 3.7-year simple payback claims, which rely on the $43K per-unit cost
1. **If a conversion payback metric is needed**, recalculate using corrected $165K/unit and clearly state assumptions

______________________________________________________________________

## ISSUE 6: STATUS QUO COST BASELINE VERIFICATION

### The Problem

Several per-program baseline costs are claimed. Verification results:

### Section 8 Housing Choice Voucher: $16,896/unit/year

**VERIFIED ✓**

HPD-administered HCV average monthly per-unit cost in November 2024: $1,408 (NYS Comptroller). $1,408 × 12 = **$16,896**. NYCHA-administered HCV: $1,466/month = $17,592/year.

Source: NYS Comptroller, "Section 8 Housing Choice Vouchers — Federal Funding and New York," 2024.

### CityFHEPS: $18,200–$21,154/unit/year

**VERIFIED ✓ (with nuance)**

Citizens Budget Commission (February 2025): CityFHEPS cost exceeds $1.1 billion for ~52,000 households = **~$21,154/yr average**.

However, CBC also found that CityFHEPS costs the city 27% more than shelter for typical single adults and 64% more for families over 5 years — meaning the subsidy vs. shelter comparison is more complex than presented.

IBO (January 2024): Provided analysis confirming per-voucher costs in the $18,000–$21,000 range depending on household composition.

Sources: CBC, "CityFHEPS Hits $1 Billion" (Feb 2025); IBO, "Understanding CityFHEPS" (Jan 2024).

### HASA: $33,144/unit/year

**NOT INDEPENDENTLY VERIFIED ⚠️**

Historical HASA per-unit data shows ~$24,000/unit in 2008–2009 (SHNNY Funding Guide). No publicly available 2024–2025 per-household cost data was found. The $33,144 figure ($2,762/month) aligns with CityFHEPS maximum payment standards for 1-BR units, suggesting it may be derived from maximum HASA enhanced rent levels rather than average actual cost.

Recommendation: Flag as "estimated based on maximum allowable rental assistance level" pending verification from DSS/HRA budget testimony.

### Family Shelter Per Diem: $84,800–$98,736/year

**PARTIALLY VERIFIED ✓ (figure depends on shelter type)**

DHS testimony to City Council, March 11, 2024: Non-emergency family shelter per diem rates of approximately **$186/day** for families = **$67,890/year**.

However, a higher rate of **$232/day** = **$84,680/year** has been cited for families with children in certain facility types (consistent with the $84,800 figure used in the Testimony and Part III-A).

The $98,736 figure ($270/day) may reflect full cost including wraparound services or asylum-seeker-specific shelter rates. The Comptroller's office documented combined per-diem rates of $332–$388/day for asylum-seeker shelters, which are significantly higher but represent a distinct population.

**Defensible range for traditional family shelter: $186–$232/day ($67,890–$84,680/year)**

Sources: DHS testimony to City Council Committee on General Welfare (March 11, 2024); NYC Comptroller, "Per Diem Hotel and Service Costs" (July 2024).

### Single Adult Shelter: $53,000/year

**VERIFIED ✓**

DHS non-emergency single adult per diem: approximately $145/day = $52,925/year ≈ $53,000.

### Summary of Baseline Verification

| Program               | Claimed         | Verified                                       | Status                  |
| --------------------- | --------------- | ---------------------------------------------- | ----------------------- |
| Section 8 HCV         | $16,896/yr      | $16,896/yr (HPD avg)                           | ✅ Verified             |
| CityFHEPS             | $18,200–$21,154 | ~$21,154 avg                                   | ✅ Verified             |
| HASA                  | $33,144/yr      | ~$24K (historical); $33K plausible at max rate | ⚠️ Unverified           |
| Family Shelter        | $84,800/yr      | $67,890–$84,680/yr                             | ✅ Verified (range)     |
| Family Shelter (high) | $98,736/yr      | Not verified for traditional shelter           | ⚠️ May include services |
| Single Adult Shelter  | $53,000/yr      | $52,925/yr                                     | ✅ Verified             |

______________________________________________________________________

## RECONCILED 10-YEAR FISCAL MODEL

Using ONLY verified and corrected figures, the following represents the defensible TCAP fiscal model for presentation to the Mayor's Office.

### Model Parameters

| Parameter                 | Value                           | Source                             | Confidence |
| ------------------------- | ------------------------------- | ---------------------------------- | ---------- |
| Annual subsidy per HH     | $21,600                         | CityFHEPS maximum standards        | 95%        |
| Subsidy split             | 80% carrying / 20% equity       | Proposed § 26-1803                 | Statutory  |
| Member income (start)     | $28,000                         | HUD ELI threshold for NYC          | 90%        |
| Income growth             | 1.5%/yr                         | Brookings, EPI                     | 85%        |
| Building cost inflation   | 2.5%/yr                         | RGB PIOC forecasts                 | 85%        |
| Carrying charge cap       | 15% of income                   | Proposed § 26-1809                 | Statutory  |
| Per-unit conversion cost  | $165,000 (midpoint)             | ANCP benchmarks, scenario analysis | 80%        |
| Units per cooperative     | 25                              | Model assumption                   | N/A        |
| Pilot scale               | 150 cooperatives, 3,750 members | Policy target                      | N/A        |
| Building acquisition cost | $1,500,000 (25-unit)            | Part III-A market data             | 85%        |
| Mortgage rate             | 4.0%, 30-year                   | Mid-2025 co-op terms               | 90%        |

### Per-Household 10-Year Projection

| Year | Member Income | Member Payment (15%) | Monthly Subsidy | Equity Credit (20%) | Cumulative Equity |
| ---- | ------------- | -------------------- | --------------- | ------------------- | ----------------- |
| 1    | $28,000       | $350/mo ($4,200/yr)  | $1,800/mo       | $360/mo             | $13,165           |
| 2    | $28,420       | $356/mo              | $1,800/mo       | $369/mo             | $18,473           |
| 3    | $28,846       | $361/mo              | $1,800/mo       | $378/mo             | $23,927           |
| 4    | $29,279       | $366/mo              | $1,800/mo       | $387/mo             | $29,532           |
| 5    | $29,718       | $372/mo              | $1,800/mo       | $397/mo             | $35,293           |
| 6    | $30,164       | $377/mo              | $1,800/mo       | $406/mo             | $41,212           |
| 7    | $30,616       | $383/mo              | $1,800/mo       | $416/mo             | $47,296           |
| 8    | $31,076       | $388/mo              | $1,800/mo       | $426/mo             | $53,549           |
| 9    | $31,542       | $394/mo              | $1,800/mo       | $436/mo             | $59,976           |
| 10   | $32,015       | $400/mo              | $1,800/mo       | $447/mo             | $66,582           |

Source: Part III-A §3.5.3 (verified year-by-year).

### Per-Household 10-Year Cost Comparison

| Metric                        | Status Quo (CityFHEPS) | TCAP        | Difference       |
| ----------------------------- | ---------------------- | ----------- | ---------------- |
| Annual subsidy                | $21,000                | $21,600     | +$600 (+3%)      |
| 10-year subsidy total         | $210,000               | $216,000    | +$6,000          |
| Member equity at Year 10      | $0                     | $66,582     | +$66,582         |
| Asset creation per subsidy $  | $0                     | $0.308      | 30.8% conversion |
| Permanent affordability       | 0 years                | 99+ years   | Permanent        |
| Break-even (assets = subsidy) | N/A                    | Years 12–13 | —                |

### 150-Cooperative Scaling Model (3,750 Members)

| Metric                            | Value                | Derivation                    |
| --------------------------------- | -------------------- | ----------------------------- |
| Total acquisition + rehab cost    | $618,750,000         | 3,750 units × $165,000        |
| 10-year aggregate subsidy         | $810,000,000         | 3,750 × $21,600 × 10          |
| Member equity generated (Year 10) | $249,682,500         | 3,750 × $66,582               |
| Mortgage principal paid down      | ~$38,190,000         | 150 buildings × $254,592 / 10 |
| Total asset creation              | ~$287,872,500        | Equity + principal            |
| **Asset creation rate**           | **35.5% of subsidy** | $287.9M ÷ $810M               |
| Status quo 10-yr cost (same HH)   | $787,500,000         | 3,750 × $21,000 × 10          |
| **TCAP premium over status quo**  | **$22,500,000**      | $810M - $787.5M               |
| **Premium per HH**                | **$6,000**           | Same as per-HH comparison     |

### Conditional Shelter-Avoidance Savings

| Scenario                     | Households at Risk | Annual Shelter Cost | 10-Year Savings |
| ---------------------------- | ------------------ | ------------------- | --------------- |
| 5% of members avoid shelter  | 188                | $84,800/family      | $159,424,000    |
| 10% of members avoid shelter | 375                | $84,800/family      | $318,000,000    |
| 15% of members avoid shelter | 563                | $84,800/family      | $477,424,000    |

Even at the conservative 5% scenario, shelter-avoidance savings ($159M) far exceed the TCAP premium over status quo ($22.5M) by a factor of 7:1.

### Corrected ROI Summary

| Metric                                 | Value  | Notes                                                       |
| -------------------------------------- | ------ | ----------------------------------------------------------- |
| Direct asset creation ROI              | 30.8%  | Member equity per subsidy dollar                            |
| Total asset creation ROI               | 35.5%  | Including building equity                                   |
| Shelter-avoidance ROI (10% scenario)   | 14.1:1 | $318M savings ÷ $22.5M premium                              |
| Full societal ROI (with externalities) | ~6.2:1 | Includes academic literature-based estimates; label clearly |

______________________________________________________________________

## SUMMARY OF ALL CORRECTIONS

| Issue                  | Original Claim       | Corrected Figure                                            | Action Required                                          |
| ---------------------- | -------------------- | ----------------------------------------------------------- | -------------------------------------------------------- |
| 1. Equity/HH           | $32,000 (Part I-III) | **$66,500 ±7.3%**                                           | Update Part I-III, Master v3; fix Part II-C math error   |
| 2. Net savings         | "$37.5B" / $3,751M   | **No net direct savings; TCAP costs 3% more**               | Remove savings claim; reframe as asset-creation ROI      |
| 3. ROI                 | 3.4:1 (direct)       | **30.8% asset creation; 6.2:1 societal**                    | Drop 3.4:1; clearly label 6.2:1 as externality-inclusive |
| 4. Per-unit cost       | $43,000              | **$128,000–$200,000 (midpoint $165,000)**                   | Update all tables; recalculate scaling projections       |
| 5. Break-even          | 5.0 years / 9 years  | **Years 12–13 (asset = subsidy)**                           | Use single consistent definition throughout              |
| 6. Status quo baseline | Various              | **Most verified; HASA unverified; shelter range $68K–$85K** | Add footnotes; flag HASA for independent verification    |

______________________________________________________________________

## POLICY INTEGRITY CHECK

### What Is Fact-Based

- CityFHEPS costs ~$21,000/yr per household (CBC 2025; IBO 2024)
- DHS family shelter costs $186–$232/day (DHS testimony March 2024)
- Section 8 HCV averages $16,896/yr in NYC (NYS Comptroller 2024)
- The 80/20 subsidy split produces ~$66,500 in member equity over 10 years under stated assumptions
- TCAP subsidy costs approximately 3% more per household than status quo CityFHEPS

### What Is Inferred or Modeled

- 1.5% annual income growth for members (based on Brookings, EPI research)
- 2.5% building cost inflation (based on RGB PIOC forecasts)
- $165,000 per-unit conversion cost (interpolated from ANCP benchmarks and scenario analysis)
- Years 12–13 break-even (extrapolated from 10-year model)

### Weak Assumptions

- Member tenure: Model assumes all members remain for full 10 years (real attrition will reduce average equity)
- Subsidy stability: Assumes $1,800/mo subsidy remains available for 10+ years (subject to policy change)
- Mortgage rate: 4.0% assumes credit union/CDFI partnerships; market rates may be higher
- The $8,600/yr "savings" figure in Master v3 includes $7,400 in averted shelter/eviction costs that are speculative

### Legal/Fiscal Risks

- CityFHEPS conversion to cooperative equity instruments requires new enabling legislation (proposed Local Laws A–D)
- Federal HUD approval may be needed if Section 8 vouchers are involved
- Per-unit conversion costs of $165K+ will require significant capital budget allocation beyond current HPD programs
- CBC finding that CityFHEPS costs more than shelter for some household types undermines the "redirect existing spending" narrative

### Areas Requiring Political/Administrative Buy-In

- HPD willingness to administer a new cooperative conversion program (14 FTE unit)
- DSS agreement to modify CityFHEPS payment mechanics for 80/20 split
- City Council passage of four coordinated local laws
- CDFI/credit union partnerships for below-market cooperative mortgage financing

______________________________________________________________________

## SOURCES

### Government Data (Primary)

- Citizens Budget Commission. (2025, Feb). "CityFHEPS Hits $1 Billion." https://cbcny.org/research/cityfheps-hits-1-billion
- NYC Independent Budget Office. (2024, Jan). "Understanding CityFHEPS." https://www.ibo.nyc.ny.us/iboreports/CityFHEPS_Jan2024.pdf
- NYS Comptroller. (2024). "Section 8 Housing Choice Vouchers — Federal Funding and New York." https://www.osc.ny.gov/reports/budget/fed-funding-ny/section-8-housing-choice-vouchers
- DHS. (2024, Mar 11). Testimony to NYC Council Committee on General Welfare. https://citymeetings.nyc/meetings/new-york-city-council/2024-03-11-1000-am-committee-on-general-welfare/
- NYC Comptroller. (2024, Jul). "Comparing Per Diem Hotel and Service Costs for Shelter." https://comptroller.nyc.gov/reports/comparing-per-diem-hotel-and-service-costs-for-shelter-for-asylum-seekers/
- HPD. ANCP Program Overview. https://www.nyc.gov/assets/hpd/downloads/pdfs/services/ancp-program-overview.pdf
- HPD. ANCP Term Sheet. https://www.nyc.gov/assets/hpd/downloads/pdfs/services/ancp-term-sheet.pdf
- NYC Comptroller. ANCP Audit. https://comptroller.nyc.gov/reports/audit-report-on-the-department-of-housing-preservation-and-developments-administration-of-the-affordable-neighborhood-co-operative-program/
- NYC Rent Guidelines Board. (2023). Price Index of Operating Costs. https://rentguidelinesboard.cityofnewyork.us/wp-content/uploads/2023/04/2023-PIOC.pdf
- HUD. FY 2026 Fair Market Rents. https://www.huduser.gov/portal/datasets/fmr.html
- NYC DSS. (2025). CityFHEPS Payment Standards (Form DSS-8r). https://www.nyc.gov/assets/hra/downloads/pdf/cityfheps-documents/DSS-8r-(E).pdf

### Academic / Research

- Desmond, M. (2016). *Evicted: Poverty and Profit in the American City*. Crown.
- Maqbool, N., Viveiros, J., & Ault, M. (2015). "The Impacts of Affordable Housing on Health." Center for Housing Policy.
- Buckner, J. C. (2008). "Understanding the Impact of Homelessness on Children." *American Behavioral Scientist*, 51(6), 721–736.
- Brookings Institution. (2016). "Job Advancement for Low-Wage Workers." https://www.brookings.edu/articles/encouraging-job-advancement-among-low-wage-workers-a-new-approach/
- Economic Policy Institute. "Strong Wage Growth for Low-Wage Workers." https://www.epi.org/publication/strong-wage-growth-for-low-wage-workers-bucks-the-historic-trend/
- Lincoln Institute of Land Policy. (2023). "Burlington Housing Affordability." https://www.lincolninst.edu/publications/articles/2023-10-burlington-housing-affordability-old-north-end/

### Cooperative Conversion Benchmarks

- D.C. Policy Center. "TOPA's Promise and Pitfalls." https://www.dcpolicycenter.org/publications/topas-promise-and-pitfalls-in-dc/
- Champlain Housing Trust (Burlington, VT). https://www.getahome.org/history-awards/
- AAFE. "3 East Village Buildings into Affordable Cooperatives." https://www.aafe.org/aafe-begins-to-transform-3-east-village-buildings-into-affordable-cooperatives/

______________________________________________________________________

*This audit was prepared for internal review prior to submission to the NYC Mayor's Office. All figures should be verified against original source data before inclusion in final policy documents.*

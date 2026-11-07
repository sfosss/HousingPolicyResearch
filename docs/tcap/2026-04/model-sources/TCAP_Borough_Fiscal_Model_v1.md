# TCAP / PET FRAMEWORK — BOROUGH-LEVEL FISCAL MODEL (v1)

**Prepared for:** NYC Mayor's Office Submission
**Prepared by:** Seth Foss, Housing Policy Researcher, Cooper Square Committee
**Date:** April 5, 2026
**Status:** INITIAL BUILD — Replaces citywide-average model with borough-granular projections
**Supersedes:** Citywide-average figures in PET_TCAP_Policy_Proposal_FINAL_v3.md §V and Executive Brief

______________________________________________________________________

## EXECUTIVE SUMMARY

The TCAP fiscal model has been rebuilt from the bottom up using borough-specific data for per-unit acquisition costs, rent-stabilized building sale prices, rehabilitation benchmarks, and population characteristics. This model replaces the citywide blended averages in v3 ($165,000/unit, $66,582 equity, Years 12–13 break-even) with borough-differentiated projections that reflect the actual economics TCAP would encounter in each borough.

**Key findings:**

The v3 citywide-average model significantly understated both costs and equity by using a $65,000 per-unit acquisition assumption. Borough-level data from DOF rolling sales and Ariel Property Advisors reports shows rent-stabilized building acquisition costs range from $111,380/unit (Bronx, Ariel 1H 2025) to $249,000/unit (Manhattan, Ariel 2025). When rehabilitation and soft costs are included, total conversion costs range from $199,000/unit (Bronx) to $364,000/unit (Manhattan), with a weighted citywide average of $254,167/unit — 54% higher than v3's $165,000.

However, higher acquisition costs mean larger cooperative mortgages, which produce more principal paydown per member. Borough-level 10-year member equity ranges from $75,452 (Bronx) to $107,276 (Manhattan), with a weighted average of $86,555 — 30% higher than v3's $66,582.

The break-even timeline (total assets including 2.5% building appreciation ≥ conversion investment) extends to approximately Years 18–19 across all boroughs, compared to the v3 claim of Years 12–13. This revision reflects both higher real costs and a more conservative break-even methodology. The v3 break-even could not be replicated even using v3's own input assumptions.

**The fiscal case for TCAP remains strong.** The program produces $86,555 in weighted-average member equity per household for $254,167 in total investment — a 34.1% asset creation rate relative to total cost. The 10-year subsidy premium over CityFHEPS remains $6,000 per household ($50/month). What changes is the upfront capital investment required, which rises from $618.75M to $953.1M for 150 buildings (3,750 units) under the weighted borough allocation.

______________________________________________________________________

## 1. METHODOLOGY

### 1.1 Data Sources

Borough-specific inputs were assembled from the following primary sources (full bibliography in TCAP_Borough_Data_Sources_v1.md):

| Data Point                          | Source                                                                          | Date      |
| ----------------------------------- | ------------------------------------------------------------------------------- | --------- |
| Per-unit acquisition (RS buildings) | Ariel Property Advisors Multifamily Reports; Crain's NY                         | 2025      |
| Rehabilitation cost benchmarks      | HPD ANCP Term Sheet; HPD Participation Loan Program; NYC Comptroller ANCP Audit | 2025–2026 |
| Rent-stabilized unit counts         | NYC Rent Guidelines Board 2025 Housing Supply Report; 2023 NYCHVS               | 2023–2025 |
| Median rents (stabilized)           | RGB 2025 Income & Affordability Study                                           | 2023 data |
| Median rents (market)               | StreetEasy/Skybriz Q3 2025–Q1 2026                                              | 2025–2026 |
| CityFHEPS payment standards         | HRA DSS-8r (effective April 1, 2026)                                            | 2026      |
| HUD Fair Market Rents               | HUD FMR FY2026 (effective Oct 1, 2025)                                          | 2025–2026 |
| Voucher concentration               | City Limits analysis of HRA data                                                | 2024      |
| ELI household estimates             | ANHD 2025 AMI Cheat Sheet; Robin Hood Poverty Tracker                           | 2024–2025 |
| Poverty rates                       | Census ACS via Robin Hood                                                       | 2024      |

### 1.2 Model Structure

The model uses the same equity accumulation framework as Part III-A (verified in v2 Fiscal Audit), with three components:

1. **Initial equity stake:** $8,000 (unchanged across boroughs)
1. **Monthly equity credit:** 20% of $1,800 subsidy = $360/mo base, growing at 1.5%/yr with income
1. **Mortgage principal paydown share:** Member's 1/25th share of annual blanket mortgage amortization (BOROUGH-SPECIFIC — varies with acquisition cost)

The critical change from v3: the blanket mortgage amount is now set by actual borough-level acquisition costs rather than a $65,000 citywide average. Since principal paydown is a function of mortgage size, boroughs with higher acquisition costs generate more equity per member.

### 1.3 Key Assumptions (Unchanged from v3)

| Parameter               | Value                           | Source                      | Confidence |
| ----------------------- | ------------------------------- | --------------------------- | ---------- |
| Monthly subsidy         | $1,800                          | CityFHEPS payment standard  | 90%        |
| Equity split            | 80/20 (carrying charges/equity) | §26-1803                    | Codified   |
| Mortgage rate           | 4.0% (30-year)                  | CDFI/credit union terms     | 85%        |
| Income growth           | 1.5%/yr                         | Brookings, EPI              | 85%        |
| Building cost inflation | 2.5%/yr                         | RGB PIOC forecasts          | 85%        |
| Units per cooperative   | 25 (average)                    | TCAP design spec            | 90%        |
| Building appreciation   | 2.5%/yr (for break-even only)   | Conservative; NYC avg ~3-4% | 75%        |

### 1.4 Critical Structural Finding: Voucher Rates Are Citywide

A key discovery during borough-level research: **CityFHEPS payment standards and HUD Fair Market Rents do not vary by borough.** CityFHEPS sets uniform citywide rates ($2,734/mo for 1-BR effective April 2026). HUD FMRs are set at the metro area level ($2,655/mo for 1-BR FY2026). Only NYCHA's Exception Payment Standards vary by ZIP code (up to $4,452/mo for 1-BR in high-opportunity areas).

This means the TCAP subsidy input ($1,800/mo) is constant across all boroughs. What varies is the cost side: acquisition, rehabilitation, and the resulting mortgage structure. This simplifies the model: equity credit accrual is identical in each borough; only the mortgage principal paydown component differs.

______________________________________________________________________

## 2. BOROUGH-SPECIFIC FISCAL ANALYSIS

### 2.1 The Bronx

**Profile:** Highest TCAP priority borough. 46% of all citywide CityFHEPS vouchers are concentrated here despite representing 16% of NYC's population. 61% of rental stock is rent-stabilized — the highest proportion of any borough. 23% poverty rate. An estimated 110,000 ELI (≤30% AMI) renter households.

**Conversion Cost Per Unit:**

| Component                                     | Low          | High         | Midpoint     |
| --------------------------------------------- | ------------ | ------------ | ------------ |
| Acquisition                                   | $60,000      | $140,000     | $100,000     |
| Rehabilitation                                | $50,000      | $80,000      | $65,000      |
| Soft costs (legal, TA, reserves, contingency) | —            | —            | $34,000      |
| **Total**                                     | **$144,000** | **$254,000** | **$199,000** |

**Acquisition basis:** Ariel Property Advisors 1H 2025 Bronx Multifamily Report: average per-unit price $111,380 (down 27% YoY). Rent-stabilized buildings comprised 76% of multifamily dollar volume. The Related Companies 36-building portfolio (2,021 units) sold to PH Realty Capital for $189M ($93,517/unit), demonstrating achievable pricing for portfolio-scale TCAP acquisitions. Range reflects distressed/tax-lien properties at the low end vs. stabilized occupied buildings at the high end.

**10-Year Equity Trajectory:**

| Year | Monthly Credit | Annual Credit | Principal Share | Cumulative Equity |
| ---- | -------------- | ------------- | --------------- | ----------------- |
| 1    | $360           | $4,320        | $1,761          | $14,081           |
| 2    | $365           | $4,385        | $1,833          | $20,299           |
| 3    | $371           | $4,451        | $1,907          | $26,657           |
| 4    | $376           | $4,517        | $1,985          | $33,159           |
| 5    | $382           | $4,585        | $2,066          | $39,810           |
| 6    | $388           | $4,654        | $2,150          | $46,614           |
| 7    | $394           | $4,724        | $2,238          | $53,576           |
| 8    | $400           | $4,795        | $2,329          | $60,699           |
| 9    | $406           | $4,867        | $2,424          | $67,990           |
| 10   | $412           | $4,940        | $2,523          | **$75,452**       |

**Break-even:** Year 19 (with 2.5% building appreciation); Year 24 (conservative, equity only)

**Pilot scale (55 buildings, 1,375 units):**

| Metric                            | Value        |
| --------------------------------- | ------------ |
| Total conversion investment       | $273,625,000 |
| 10-year aggregate subsidy         | $297,000,000 |
| Member equity generated           | $103,746,225 |
| Premium over CityFHEPS status quo | $8,250,000   |

**Bronx-specific considerations:** The Bronx offers TCAP's strongest cost-benefit ratio due to the lowest acquisition costs in the city. The heavy voucher concentration means TCAP addresses the borough most dependent on subsidy spending. However, the 27% YoY decline in per-unit prices (Ariel, 2025) may reflect continuing post-HSTPA depreciation of rent-stabilized assets — creating a window for TCAP acquisitions at advantageous pricing.

______________________________________________________________________

### 2.2 Brooklyn

**Profile:** Largest rent-stabilized stock by unit count (304,000 units, 42% of rental). 22% of CityFHEPS vouchers. 20% poverty rate. 95,000 estimated ELI renter households. The borough with the most dramatic income growth (+37.6% from 2013–2023), creating significant displacement pressure for subsidized households.

**Conversion Cost Per Unit:**

| Component      | Low          | High         | Midpoint     |
| -------------- | ------------ | ------------ | ------------ |
| Acquisition    | $120,000     | $250,000     | $185,000     |
| Rehabilitation | $55,000      | $85,000      | $70,000      |
| Soft costs     | —            | —            | $34,000      |
| **Total**      | **$209,000** | **$369,000** | **$289,000** |

**Acquisition basis:** Citywide average for 100% rent-stabilized buildings: $175,225/unit (Ariel/Crain's, 2024). Brooklyn RS values declined 37.1% from pre-HSTPA levels — less than other outer boroughs. Brooklyn led in multifamily transactions (582 deals, $3.5B) in 2025. High end reflects rapidly appreciating neighborhoods (Williamsburg, Park Slope); low end reflects east Brooklyn/Brownsville stabilized stock.

**10-Year Equity Trajectory:**

| Year | Monthly Credit | Annual Credit | Principal Share | Cumulative Equity |
| ---- | -------------- | ------------- | --------------- | ----------------- |
| 1    | $360           | $4,320        | $3,258          | $15,578           |
| 5    | $382           | $4,585        | $3,822          | $47,930           |
| 10   | $412           | $4,940        | $4,667          | **$93,485**       |

**Break-even:** Year 19 (with appreciation); >25 years (equity only)

**Pilot scale (40 buildings, 1,000 units):**

| Metric                      | Value        |
| --------------------------- | ------------ |
| Total conversion investment | $289,000,000 |
| 10-year aggregate subsidy   | $216,000,000 |
| Member equity generated     | $93,485,430  |

**Brooklyn-specific considerations:** Brooklyn's wide cost range reflects extreme neighborhood-level variation. TCAP targeting should focus on central Brooklyn (Crown Heights, Flatbush, East New York) where stabilized stock is concentrated and acquisition costs are at the lower end. Williamsburg/Park Slope pricing ($250K+/unit) makes those neighborhoods impractical for TCAP without significant public subsidy.

______________________________________________________________________

### 2.3 Queens

**Profile:** Second-largest rent-stabilized stock (253,000 units, 41% of rental). 15% of CityFHEPS vouchers. 22% poverty rate. 75,000 estimated ELI renter households. RS building values have declined 60.4% from pre-HSTPA levels — the steepest decline of any borough — creating substantial acquisition opportunities.

**Conversion Cost Per Unit:**

| Component      | Low          | High         | Midpoint     |
| -------------- | ------------ | ------------ | ------------ |
| Acquisition    | $100,000     | $200,000     | $150,000     |
| Rehabilitation | $50,000      | $80,000      | $65,000      |
| Soft costs     | —            | —            | $34,000      |
| **Total**      | **$184,000** | **$314,000** | **$249,000** |

**Acquisition basis:** Queens RS values declined 60.4% from pre-HSTPA levels (Ariel/Furman, 2024) — steepest borough decline. 264 multifamily transactions at $879M in 2025 (+3% YoY). Average building sale price hit new high at $771,441 but this includes free-market; RS properties significantly cheaper.

**10-Year Equity Trajectory:**

| Year | Monthly Credit | Annual Credit | Principal Share | Cumulative Equity |
| ---- | -------------- | ------------- | --------------- | ----------------- |
| 1    | $360           | $4,320        | $2,642          | $14,962           |
| 5    | $382           | $4,585        | $3,099          | $44,587           |
| 10   | $412           | $4,940        | $3,784          | **$86,060**       |

**Break-even:** Year 19 (with appreciation); >25 years (equity only)

**Pilot scale (25 buildings, 625 units):**

| Metric                      | Value        |
| --------------------------- | ------------ |
| Total conversion investment | $155,625,000 |
| 10-year aggregate subsidy   | $135,000,000 |
| Member equity generated     | $53,787,388  |

**Queens-specific considerations:** The 60% RS value decline positions Queens as a high-opportunity borough for TCAP. Neighborhoods like Jackson Heights, Elmhurst, and Flushing have dense concentrations of RS stock with immigrant-community tenants who face acute displacement pressure. The borough's emerging income growth trajectory (+22.4% 2013–2023) suggests current low RS valuations may not persist — arguing for near-term TCAP intervention.

______________________________________________________________________

### 2.4 Manhattan

**Profile:** Third-largest RS stock (271,000 units, 44% of rental). Highest median rents but only 10% of CityFHEPS vouchers. 18% poverty rate. 85,000 estimated ELI renter households. Largest HDFC cooperative stock (~15,000 units), demonstrating proven cooperative viability. Highest per-unit costs but also highest equity generation.

**Conversion Cost Per Unit:**

| Component      | Low          | High         | Midpoint     |
| -------------- | ------------ | ------------ | ------------ |
| Acquisition    | $180,000     | $320,000     | $250,000     |
| Rehabilitation | $60,000      | $100,000     | $80,000      |
| Soft costs     | —            | —            | $34,000      |
| **Total**      | **$274,000** | **$454,000** | **$364,000** |

**Acquisition basis:** Ariel 2025: Manhattan free-market buildings at $635,000/unit (up 13% YoY); RS buildings at $249,000/unit (45% below 2019 pre-HSTPA). Northern Manhattan (Inwood/Washington Heights) significantly cheaper: 47 transactions, $326M ($25K-$150K/unit range for RS). 185 total multifamily transactions, $3.44B in 2025.

**10-Year Equity Trajectory:**

| Year | Monthly Credit | Annual Credit | Principal Share | Cumulative Equity |
| ---- | -------------- | ------------- | --------------- | ----------------- |
| 1    | $360           | $4,320        | $4,403          | $16,723           |
| 5    | $382           | $4,585        | $5,165          | $54,139           |
| 10   | $412           | $4,940        | $6,307          | **$107,276**      |

**Break-even:** Year 19 (with appreciation); >25 years (equity only)

**Pilot scale (20 buildings, 500 units):**

| Metric                      | Value        |
| --------------------------- | ------------ |
| Total conversion investment | $182,000,000 |
| 10-year aggregate subsidy   | $108,000,000 |
| Member equity generated     | $53,637,930  |

**Manhattan-specific considerations:** Manhattan should NOT be a primary TCAP pilot target due to extreme costs. The 20-building allocation focuses narrowly on Northern Manhattan (Washington Heights, Inwood, East Harlem) where RS building prices overlap with outer-borough ranges. Manhattan's existing HDFC infrastructure (~15,000 units) provides a cooperative support ecosystem absent in other boroughs. The $107,276 per-member equity figure is the highest of any borough — a powerful demonstration case for wealth creation.

______________________________________________________________________

### 2.5 Staten Island

**Profile:** Smallest RS stock (23,000 units, 17% of rental). 7% of CityFHEPS vouchers. 12% poverty rate — lowest in the city. 15,000 estimated ELI renter households. Limited multifamily inventory. Income declined 6.7% from 2013–2023 — the only borough with negative income growth.

**Conversion Cost Per Unit:**

| Component      | Low          | High         | Midpoint     |
| -------------- | ------------ | ------------ | ------------ |
| Acquisition    | $80,000      | $160,000     | $120,000     |
| Rehabilitation | $45,000      | $70,000      | $57,500      |
| Soft costs     | —            | —            | $34,000      |
| **Total**      | **$159,000** | **$264,000** | **$211,500** |

**10-Year Equity Trajectory:**

| Year | Monthly Credit | Annual Credit | Principal Share | Cumulative Equity |
| ---- | -------------- | ------------- | --------------- | ----------------- |
| 1    | $360           | $4,320        | $2,113          | $14,433           |
| 5    | $382           | $4,585        | $2,479          | $41,721           |
| 10   | $412           | $4,940        | $3,027          | **$79,695**       |

**Break-even:** Year 18 (with appreciation); Year 24 (equity only)

**Pilot scale (10 buildings, 250 units):**

| Metric                      | Value       |
| --------------------------- | ----------- |
| Total conversion investment | $52,875,000 |
| 10-year aggregate subsidy   | $54,000,000 |
| Member equity generated     | $19,923,752 |

**Staten Island–specific considerations:** Staten Island has the smallest TCAP-eligible population and the least multifamily rental stock. A 10-building pilot is included for equity of coverage across all five boroughs, but the borough should not be a scaling priority. The income decline (-6.7%) is concerning for member contribution stability. CityFHEPS payment standards ($2,734/mo for 1-BR) significantly exceed local market rents ($1,955/mo), meaning the subsidy more than covers carrying charges — potentially allowing a higher equity allocation.

______________________________________________________________________

## 3. CITYWIDE ROLLUP

### 3.1 Weighted Borough Allocation

Building allocation is weighted toward boroughs with the highest need (voucher concentration, ELI population, RS stock) and most favorable cost economics:

| Borough           | Buildings | Units     | % of Pilot | Rationale                                                       |
| ----------------- | --------- | --------- | ---------- | --------------------------------------------------------------- |
| **Bronx**         | 55        | 1,375     | 36.7%      | Highest voucher concentration (46%); lowest costs; highest RS % |
| **Brooklyn**      | 40        | 1,000     | 26.7%      | Largest RS stock; second-highest voucher concentration          |
| **Queens**        | 25        | 625       | 16.7%      | Steep RS price declines create opportunity; large RS stock      |
| **Manhattan**     | 20        | 500       | 13.3%      | Northern Manhattan only; HDFC ecosystem; demonstration value    |
| **Staten Island** | 10        | 250       | 6.7%       | Borough coverage; limited TCAP-eligible stock                   |
| **TOTAL**         | **150**   | **3,750** | **100%**   |                                                                 |

### 3.2 Aggregate Fiscal Summary

| Metric                             | Borough-Weighted (v1) | v3 Citywide Average   | Variance             |
| ---------------------------------- | --------------------- | --------------------- | -------------------- |
| **Weighted avg cost/unit**         | **$254,167**          | $165,000              | +$89,167 (+54%)      |
| **Total conversion investment**    | **$953,125,000**      | $618,750,000          | +$334,375,000 (+54%) |
| **10-year aggregate subsidy**      | **$810,000,000**      | $810,000,000          | $0 (unchanged)       |
| **Weighted avg equity/member**     | **$86,555**           | $66,582               | +$19,973 (+30%)      |
| **Total member equity**            | **$324,580,725**      | $249,682,500          | +$74,898,225 (+30%)  |
| **Total building equity**          | **$121,196,634**      | $38,190,000           | +$82,006,634 (+215%) |
| **Total asset creation**           | **$445,777,359**      | $287,872,500          | +$157,904,859 (+55%) |
| **Asset creation rate**            | **55.0%**             | 35.5%                 | +19.5 pp             |
| **Premium over status quo**        | **$22,500,000**       | $22,500,000           | $0 (unchanged)       |
| **Break-even (with appreciation)** | **Years 18–19**       | Years 12–13 (claimed) | +6 years             |

### 3.3 Borough Range Summary

| Metric                   | Lowest           | Highest              | Range Factor |
| ------------------------ | ---------------- | -------------------- | ------------ |
| Per-unit conversion cost | $199,000 (Bronx) | $364,000 (Manhattan) | 1.83×        |
| 10-year member equity    | $75,452 (Bronx)  | $107,276 (Manhattan) | 1.42×        |
| RS building sale price   | $111,380 (Bronx) | $249,000 (Manhattan) | 2.24×        |
| Median stabilized rent   | $1,039 (SI)      | $2,167 (Manhattan)   | 2.09×        |
| ELI households           | ~15,000 (SI)     | ~110,000 (Bronx)     | 7.33×        |
| Voucher concentration    | 7% (SI)          | 46% (Bronx)          | 6.57×        |

______________________________________________________________________

## 4. CRITICAL VARIANCES FROM v3

### 4.1 The Acquisition Cost Gap

The single largest driver of variance is per-unit acquisition cost. The v3 model used a $65,000 midpoint for the acquisition component (the portion funded by cooperative blanket mortgage), derived from the original Master v3 Scenario A (Bronx 24-unit building at $52,500/unit acquisition). This figure was already flagged in the v2 Fiscal Audit as understated, with the total conversion cost corrected to $165,000/unit midpoint.

Borough-level data reveals the v3 acquisition figure is below even the most affordable borough:

| Borough       | RS Sale Price/Unit (Actual) | v3 Acquisition Assumption | Gap               |
| ------------- | --------------------------- | ------------------------- | ----------------- |
| Bronx         | $111,380                    | $65,000                   | +$46,380 (+71%)   |
| Queens        | ~$150,000                   | $65,000                   | +$85,000 (+131%)  |
| Brooklyn      | ~$175,000                   | $65,000                   | +$110,000 (+169%) |
| Staten Island | ~$130,000                   | $65,000                   | +$65,000 (+100%)  |
| Manhattan     | $249,000                    | $65,000                   | +$184,000 (+283%) |

**Implication:** The v3 model's $65,000 acquisition figure appears to have been based on a distressed/tax-lien scenario that is not representative of the broader market. Even the Bronx — the most affordable borough — shows acquisition prices 71% higher than v3 assumed.

### 4.2 The Break-Even Revision

The v3 break-even of Years 12–13 could not be replicated using the v3's own input assumptions. Using v3 parameters ($65K acquisition, $165K total, 4% mortgage, 2.5% appreciation), the model reaches only $142,092 per-unit total assets by Year 16 — still short of the $165,000 target. Break-even under v3 assumptions actually occurs near Year 20.

This suggests the original Part III-A break-even calculation may have used different appreciation assumptions or a different asset valuation methodology than documented. The borough model uses a transparent and conservative definition: total assets (member equity + building appreciation at 2.5%/yr on acquisition value) ≥ total per-unit conversion investment.

**Recommended action:** Revise the break-even claim to "Years 18–19 (with conservative building appreciation)" or define a more favorable break-even metric such as "return on incremental investment" (equity ÷ premium = 11.1:1, achieved in Year 1).

### 4.3 The Equity Upside

Borough-level equity is HIGHER than v3, not lower. This is counterintuitive but mathematically sound: higher acquisition costs → larger cooperative mortgages → more principal paydown per member per year. The equity-cost relationship is linear with mortgage size.

This is a strong finding for the Mayor's Office: **TCAP produces more household wealth than previously modeled.** The weighted average of $86,555/member represents a 30% upside from v3's $66,582.

### 4.4 The Capital Requirement Increase

The most challenging variance: total conversion investment rises from $618.75M to $953.1M (+54%). This requires revised funding source planning:

| Source                                    | v3 Amount  | Borough-Weighted (v1) | Change     |
| ----------------------------------------- | ---------- | --------------------- | ---------- |
| City Capital (rehab + conversion)         | ~$350M     | ~$535M                | +$185M     |
| CDFI/credit union mortgages (acquisition) | ~$225M     | ~$370M                | +$145M     |
| TCAP Revolving Fund (gap + TA)            | ~$44M      | ~$48M                 | +$4M       |
| **Total**                                 | **~$619M** | **~$953M**            | **+$334M** |

**Mitigation strategies:**

1. **Phase the pilot more conservatively:** Begin with 75 Bronx/Brooklyn buildings (lowest-cost boroughs) before scaling to Manhattan/Queens
1. **Target distressed stock:** Bronx portfolio sales (Related/PH Realty at $93K/unit) and tax-lien properties bring acquisition well below market averages
1. **Leverage ANCP model:** HPD ANCP provides up to $700K/unit in city subsidies; TCAP needs far less per unit
1. **Seek state/federal capital:** HTFC, LIHTC, federal HOME funds could offset 20-30% of capital needs

______________________________________________________________________

## 5. SUBSIDY STRUCTURE ANALYSIS

### 5.1 CityFHEPS Coverage by Borough

CityFHEPS payment standards are uniform citywide. However, the gap between subsidy levels and local costs varies dramatically:

| Borough       | CityFHEPS 1-BR | Median Market 1-BR | Coverage Gap    | Median Stabilized | Surplus over RS |
| ------------- | -------------- | ------------------ | --------------- | ----------------- | --------------- |
| Manhattan     | $2,734         | $4,393             | -$1,659 (38%)   | $2,167            | +$567 (26%)     |
| Brooklyn      | $2,734         | $3,300             | -$566 (17%)     | $1,579            | +$1,155 (73%)   |
| Queens        | $2,734         | $3,349             | -$615 (18%)     | $1,540            | +$1,194 (78%)   |
| Bronx         | $2,734         | $3,132             | -$398 (13%)     | $1,145            | +$1,589 (139%)  |
| Staten Island | $2,734         | $1,955             | +$779 (surplus) | $1,039            | +$1,695 (163%)  |

**Key insight for TCAP:** In outer boroughs, CityFHEPS rates are significantly above rent-stabilized rents. This means TCAP cooperative carrying charges can be fully funded by the subsidy with room for larger equity allocations. In the Bronx, the CityFHEPS rate is 139% above the median stabilized rent — suggesting the 80/20 split may be conservative. A 70/30 split in lower-cost boroughs could accelerate equity accumulation without increasing the subsidy.

### 5.2 HUD Fair Market Rents (FY 2026)

HUD FMRs are set at the metro area level and do not vary by borough:

| Unit Size | FMR    | CityFHEPS | Difference    |
| --------- | ------ | --------- | ------------- |
| Studio    | $2,387 | $2,604    | CityFHEPS +9% |
| 1-BR      | $2,655 | $2,734    | CityFHEPS +3% |
| 2-BR      | $2,910 | $2,997    | CityFHEPS +3% |
| 3-BR      | $3,644 | $3,753    | CityFHEPS +3% |

______________________________________________________________________

## 6. TCAP-ELIGIBLE POPULATION AND TARGETING

### 6.1 Eligible Stock by Borough

| Borough       | RS Units     | % Rental Stock | HDFC Units  | CityFHEPS Voucher Share | ELI Households |
| ------------- | ------------ | -------------- | ----------- | ----------------------- | -------------- |
| Bronx         | 116,000      | 61%            | ~5,000      | 46%                     | ~110,000       |
| Brooklyn      | 304,000      | 42%            | ~10,000     | 22%                     | ~95,000        |
| Queens        | 253,000      | 41%            | ~500        | 15%                     | ~75,000        |
| Manhattan     | 271,000      | 44%            | ~15,000     | 10%                     | ~85,000        |
| Staten Island | 23,000       | 17%            | ~250        | 7%                      | ~15,000        |
| **Citywide**  | **~967,000** | **~44%**       | **~30,750** | **100%**                | **~380,000**   |

### 6.2 Targeting Recommendations by Borough

**Bronx (Priority 1):** Focus on Mott Haven, Highbridge, University Heights — dense RS stock, high voucher concentration, active distressed-property market. The Related Companies portfolio sale (2,021 units at $93K/unit) demonstrates TCAP-scale acquisition pricing is achievable.

**Brooklyn (Priority 2):** Focus on Crown Heights, Flatbush, East New York, Brownsville — lower-cost RS neighborhoods with high subsidy concentration. Avoid Williamsburg/Park Slope where acquisition costs exceed model parameters.

**Queens (Priority 3):** Focus on Jackson Heights, Elmhurst, Flushing — large RS stock with 60% price decline creating a time-limited acquisition window. Strong immigrant-community tenant bases with cooperative tradition.

**Manhattan (Priority 4, Northern only):** Limit to Washington Heights, Inwood, East Harlem. Leverage existing HDFC/cooperative infrastructure for TA support. Northern Manhattan transactions ($326M, 47 deals in 2025) show pricing in outer-borough range.

**Staten Island (Priority 5):** Include for citywide coverage. Focus on North Shore (Port Richmond, Stapleton) where limited RS stock and poverty are concentrated.

______________________________________________________________________

## 7. FIGURES REQUIRING UPDATE IN EXISTING DOCUMENTS

The following figures in PET_TCAP_Policy_Proposal_FINAL_v3.md and PET_TCAP_Executive_Brief_v1.md should be updated to reflect borough-level data. **Original files should NOT be modified** — a revised v4 incorporating these changes should be prepared separately.

### 7.1 PET_TCAP_Policy_Proposal_FINAL_v3.md

| Section                                                                        | Current Figure | Borough-Weighted Figure          | Change   |
| ------------------------------------------------------------------------------ | -------------- | -------------------------------- | -------- |
| Exec Summary: "producing approximately $66,500 in member equity"               | $66,500        | $86,555                          | +30%     |
| Exec Summary: "initial capital appropriation of approximately $618.75 million" | $618.75M       | $953.1M                          | +54%     |
| §3.3 Equity table: Year 10 cumulative                                          | $66,582        | $75,452–$107,276 (borough range) | Variable |
| §5.1 Per-HH comparison: "Member equity at Year 10"                             | $66,582        | $86,555 (weighted avg)           | +30%     |
| §5.1: "Break-even (assets = subsidy)"                                          | Years 12–13    | Years 18–19                      | +6 years |
| §5.2: Total per unit midpoint                                                  | $165,000       | $199,000–$364,000 (range)        | Variable |
| §5.2: Acquisition midpoint                                                     | $65,000        | $100,000–$250,000 (range)        | Variable |
| §5.3: Total acquisition + rehab investment                                     | $618,750,000   | $953,125,000                     | +54%     |
| §5.3: Member equity generated                                                  | $249,682,500   | $324,580,725                     | +30%     |
| §5.3: Building equity                                                          | ~$38,190,000   | $121,196,634                     | +217%    |
| §5.3: Total asset creation                                                     | $287,872,500   | $445,777,359                     | +55%     |
| §5.3: Asset creation rate                                                      | 35.5%          | 55.0%                            | +19.5 pp |
| §5.5 ROI: Direct asset creation ROI                                            | 30.8%          | 40.1% (weighted)                 | +9.3 pp  |
| §5.5 ROI: Total asset creation ROI                                             | 35.5%          | 55.0%                            | +19.5 pp |
| §5.5 ROI: Return on premium                                                    | 11.1:1         | 14.4:1                           | +30%     |
| §5.6: City Capital budget                                                      | ~$350M         | ~$535M                           | +53%     |
| §5.6: CDFI/credit union mortgages                                              | ~$225M         | ~$370M                           | +64%     |

### 7.2 PET_TCAP_Executive_Brief_v1.md

| Section                                     | Current Figure | Borough-Weighted Figure | Change    |
| ------------------------------------------- | -------------- | ----------------------- | --------- |
| Solution: "$66,500 in equity"               | $66,500        | $86,555                 | +30%      |
| Fiscal Case: 10-yr member equity at Year 10 | $66,582        | $86,555                 | +30%      |
| Fiscal Case: "11:1 return"                  | 11:1           | 14.4:1                  | +31%      |
| 150-Building table: conversion investment   | $618.75M       | $953.1M                 | +54%      |
| 150-Building table: member equity generated | $249.7M        | $324.6M                 | +30%      |
| 150-Building table: building equity         | $38.2M         | $121.2M                 | +217%     |
| 150-Building table: total asset creation    | $287.9M        | $445.8M                 | +55%      |
| 150-Building table: break-even              | Years 12–13    | Years 18–19             | +6 years  |
| TCAP premium over status quo                | $22.5M         | $22.5M                  | Unchanged |
| Appendix: Capital investment/unit           | $165,000       | $199K–$364K (range)     | Variable  |

______________________________________________________________________

## 8. POLICY INTEGRITY CHECK

### 8.1 Fact vs. Inference

| Category                                         | Status                                                                                                                     |
| ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| Borough acquisition costs (Bronx, Manhattan)     | **Fact** — sourced from Ariel Property Advisors 2025 actual transaction data                                               |
| Borough acquisition costs (Brooklyn, Queens, SI) | **Inference** — derived from citywide RS averages and borough-level depreciation rates                                     |
| Rehabilitation costs                             | **Inference** — based on HPD program term sheets and ANCP/NYCHA benchmarks; no borough-specific private-market data exists |
| Rent-stabilized unit counts                      | **Fact** — sourced from RGB 2025 Housing Supply Report / 2023 NYCHVS                                                       |
| Voucher concentration by borough                 | **Fact** — sourced from City Limits / HRA data analysis (2024)                                                             |
| ELI household estimates                          | **Inference** — extrapolated from ANHD AMI data and Census ACS poverty rates; not direct count                             |
| Equity accumulation model                        | **Verified model** — same Part III-A methodology validated in v2 Fiscal Audit                                              |
| Break-even timelines                             | **Model output** — transparent methodology; note v3 discrepancy                                                            |

### 8.2 Weak Assumptions

1. **Rehabilitation costs do not vary by borough in any published data.** The borough-level rehab ranges used here are estimates based on building age, condition proxy (neighborhood median), and NYCHA renovation benchmarks. True borough-specific rehab costs would require building-by-building assessment during pilot Phase 1.

1. **RS building sale prices are volatile.** Ariel data shows 27% YoY decline in Bronx, 60% decline in Queens. If post-HSTPA pricing stabilizes or rebounds, TCAP acquisition costs could increase 20-40%.

1. **HDFC unit counts by borough are approximate.** HPD does not publish a public borough breakdown; estimates derived from Furman Center data and community reporting.

1. **The 25-unit building average is a planning assumption.** Actual TCAP buildings may range from 8 to 100+ units, significantly affecting per-unit economics.

### 8.3 Political and Administrative Dependencies

1. The $953M investment figure — 54% above v3 — requires revised funding strategy and potentially larger City Capital commitment
1. The revised break-even (Years 18–19 vs. 12–13) extends the fiscal payback timeline beyond typical political cycles
1. Borough-weighted allocation (55 buildings in Bronx, 20 in Manhattan) may face political pushback from Manhattan-based Council members
1. Distressed-property acquisition strategy depends on continued post-HSTPA market conditions

______________________________________________________________________

*This document was prepared using data retrieved April 5, 2026. All calculations are independently reproducible from the source code in borough_model_v2.py. Full source citations are in TCAP_Borough_Data_Sources_v1.md. Borough-specific verified facts are logged in irrefutable_facts_TCAP_borough_fiscal_v1.csv.*

*Seth Foss | Cooper Square Committee | sfosss@icloud.com*

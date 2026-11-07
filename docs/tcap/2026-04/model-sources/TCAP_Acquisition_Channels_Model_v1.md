# TCAP / PET FRAMEWORK — THREE-CHANNEL ACQUISITION COST MODEL (v1)

**Prepared for:** NYC Mayor's Office Submission
**Prepared by:** Seth Foss, Housing Policy Researcher, Cooper Square Committee
**Date:** April 5, 2026
**Status:** INITIAL BUILD — Replaces single-channel acquisition in Borough Fiscal Model v1
**Supersedes:** Acquisition cost assumptions in TCAP_Borough_Fiscal_Model_v1.md and PET_TCAP_Policy_Proposal_FINAL_v3.md §V

______________________________________________________________________

## EXECUTIVE SUMMARY

This model rebuilds the TCAP acquisition cost structure using three distinct acquisition channels, each with different per-unit costs, risk profiles, and volume capacities. The critical methodological correction from v1: all Channel 1 (market) data is derived from **whole-building multifamily transaction records** (NYC DOF rolling sales, building classes C0–C9 and D0–D9, representing entire apartment buildings), cross-referenced against the RGB 2025 Mortgage Survey Report and Ariel Property Advisors borough reports. Individual apartment/condo unit sales are excluded.

**Three Channels:**

1. **Market-Rate Whole-Building Purchases** (50% of acquisitions): Rent-stabilized buildings purchased at current post-HSTPA market prices. Per-unit cost: $112,023 (Bronx) to $249,000 (Manhattan).

1. **Foreclosure/Auction Acquisitions** (20% of acquisitions): Buildings acquired through tax lien sales, mortgage foreclosure auctions, and Third Party Transfer pipeline. Documented discounts of 40–59% from market. Per-unit cost: $67,214 (Bronx) to $149,400 (Manhattan).

1. **Penalty-Leveraged Acquisitions** (30% of acquisitions): Buildings where accumulated HPD/DOB civil penalty exposure under NYC Admin Code §27-2115 (as amended by Local Law 71 of 2023) approaches or exceeds building value. The city offers penalty forgiveness in exchange for below-market building transfer. Per-unit cost: $33,607 (Bronx) to $74,700 (Manhattan).

**Key Findings:**

The three-channel blended acquisition model reduces the total TCAP program investment from $953.1M (v1 single-channel) to $798.6M — a savings of $154.5M (16.2%). Weighted per-unit conversion cost drops from $254,167 to $212,969. However, lower acquisition costs produce smaller cooperative mortgages, which means less equity from principal paydown. Weighted 10-year member equity declines from $86,555 to $74,264 (14.2% reduction). Break-even extends from Years 18–19 to Years 23–27.

**The fiscal case shifts from "higher equity per household" to "lower total capital at risk."** The three-channel model requires $154.5M less in public investment while still producing $74,264 in weighted member equity — a 34.9% asset creation rate on the smaller investment base. The city also gains enforcement cost savings ($326,500+ per 10-year cycle per distressed building), eliminates penalty collection futility (historically ~4% collection rate), and converts permanently noncompliant buildings into functional cooperatives.

______________________________________________________________________

## 1. METHODOLOGY

### 1.1 Critical Correction: Whole-Building vs. Individual Unit Sales

The v1 Borough Fiscal Model used per-unit prices from Ariel Property Advisors and RGB reports. While Ariel and RGB data track whole-building multifamily transactions, this model adds direct validation from the NYC Department of Finance rolling sales dataset, filtering specifically for building classes C0–C9 (walk-up apartments) and D0–D9 (elevator apartments). These building class codes represent entire residential buildings, excluding condominiums (class R) and individual cooperative apartment sales.

**DOF Rolling Sales Validation (12-month rolling data, sales > $100K, 5+ residential units):**

| Borough       | Transactions | Total Volume        | Total Units | All-MF $/Unit | RS $/Unit (RGB/Ariel) |
| ------------- | ------------ | ------------------- | ----------- | ------------- | --------------------- |
| Manhattan     | 374          | $3,979,576,045      | 16,586      | $239,936      | $249,000              |
| Bronx         | 273          | $3,115,942,489      | 10,080      | $309,121      | $112,023              |
| Brooklyn      | 447          | $2,241,620,124      | 6,292       | $356,265      | $190,000 (est.)       |
| Queens        | 198          | $770,378,671        | 3,954       | $194,835      | $145,000 (est.)       |
| Staten Island | 12           | $23,892,000         | 136         | $175,676      | $120,000 (est.)       |
| **Citywide**  | **1,304**    | **$10,131,409,329** | **37,048**  | **$273,467**  | **$175,225**          |

**Source:** NYC Open Data API, DOF Rolling Sales dataset (usep-8jbt), queried April 5, 2026. RS per-unit costs from RGB 2025 Mortgage Survey Report (Bronx, Citywide) and Ariel Property Advisors 2025 Annual Report (Manhattan).

**Note on Bronx DOF All-MF figure ($309K):** This is inflated by inclusion of new-construction elevator buildings and subsidized affordable housing transactions. The RGB 2025 Mortgage Survey Report, which specifically tracks buildings with rent-stabilized units, shows Bronx 100% RS buildings at $112,023/unit. This is the correct TCAP-relevant figure.

### 1.2 Data Sources

| Data Point                              | Source                                           | Date                          | Confidence |
| --------------------------------------- | ------------------------------------------------ | ----------------------------- | ---------- |
| Whole-building per-unit (all MF)        | NYC DOF Rolling Sales via Open Data API          | April 2026 (rolling 12-month) | HIGH       |
| RS building per-unit (Bronx)            | RGB 2025 Mortgage Survey Report                  | April 2025 (2024 sales data)  | HIGH       |
| RS building per-unit (Manhattan)        | Ariel Property Advisors 2025 Annual              | March 2026 (2025 data)        | HIGH       |
| RS building per-unit (citywide 100% RS) | RGB 2025 Mortgage Survey Report                  | April 2025                    | HIGH       |
| Foreclosure discount range              | PropertyShark, Bisnow, Crain's, Multifamily Dive | 2024–2025                     | MEDIUM     |
| Tax lien sale data                      | Rosenberg & Estis; NYC DOF                       | 2025                          | MEDIUM     |
| HPD violation penalties (LL71)          | NYC Admin Code §27-2115; HPD Penalties & Fees    | 2023 (effective)              | HIGH       |
| Worst Landlords violation data          | NYC Public Advocate Watchlist                    | 2024–2025                     | HIGH       |
| ECB collection rates                    | NYC Comptroller Audit                            | 2008 (most recent available)  | MEDIUM-LOW |
| HPD enforcement budget                  | NYC Council Budget Analysis FY2025               | 2024                          | MEDIUM     |
| Rehabilitation benchmarks               | HPD ANCP/Participation Loan Term Sheets          | 2025–2026                     | HIGH       |

### 1.3 Channel Mix Rationale

The blended acquisition model uses: **50% Market / 20% Foreclosure / 30% Penalty-Leveraged**.

**Volume feasibility:**

- Channel 1 (Market): ~1,188 whole-building multifamily deals closed citywide in 2025 (Ariel). TCAP targeting 75 buildings over 5 years = ~15/year, representing 1.3% of annual market volume. Feasible.
- Channel 2 (Foreclosure): 1,588 first-time foreclosure filings in 2025 (PropertyShark) + 1,355 multifamily parcels in city tax lien trusts. TCAP targeting 30 buildings over 5 years = ~6/year. Feasible.
- Channel 3 (Penalty-Leveraged): Estimated 200–400 buildings where cumulative penalty exposure approaches or exceeds building value. TCAP targeting 45 buildings over 5 years = ~9/year. Feasible but requires new administrative mechanism.

**5-year acquisition pipeline: 75 market + 30 foreclosure + 45 penalty = 150 buildings ✓**

### 1.4 Key Assumptions (Unchanged from v1 except as noted)

| Parameter                   | Value                           | Source                            | Confidence     |
| --------------------------- | ------------------------------- | --------------------------------- | -------------- |
| Monthly subsidy             | $1,800                          | CityFHEPS payment standard        | 90%            |
| Equity split                | 80/20 (carrying charges/equity) | §26-1803                          | Codified       |
| Mortgage rate               | 4.0% (30-year)                  | CDFI/credit union terms           | 85%            |
| Mortgage LTV                | 90% of acquisition cost         | Standard co-op terms              | 85%            |
| Income growth               | 1.5%/yr                         | Brookings, EPI                    | 85%            |
| Building cost inflation     | 2.5%/yr                         | RGB PIOC forecasts                | 85%            |
| Units per cooperative       | 25 (average)                    | TCAP design spec                  | 90%            |
| Building appreciation       | 2.5%/yr (for break-even only)   | Conservative; NYC avg ~3–4%       | 75%            |
| **Channel 2 discount**      | **40% from Channel 1**          | **Documented range 44–59%**       | **MEDIUM**     |
| **Channel 3 discount**      | **70% from Channel 1**          | **Modeled settlement structure**  | **LOW-MEDIUM** |
| **Channel 3 rehab premium** | **+38% over standard rehab**    | **Distressed building condition** | **MEDIUM**     |

______________________________________________________________________

## 2. CHANNEL 1: MARKET-RATE WHOLE-BUILDING PURCHASES

### 2.1 Per-Unit Acquisition Costs by Borough

| Borough                | RS $/Unit    | Source                                 | Confidence | HSTPA Decline (2019–2024) |
| ---------------------- | ------------ | -------------------------------------- | ---------- | ------------------------- |
| Bronx                  | $112,023     | RGB 2025 MSR (100% RS)                 | HIGH       | -58.5%                    |
| Brooklyn               | $190,000     | Est. from RGB citywide + HSTPA pattern | MEDIUM     | -37.1%                    |
| Manhattan              | $249,000     | Ariel Property Advisors 2025           | HIGH       | -47.4%                    |
| Queens                 | $145,000     | Est. from RGB citywide + HSTPA pattern | MEDIUM     | -60.4%                    |
| Staten Island          | $120,000     | Estimated: limited data                | LOW        | N/A                       |
| **Citywide (100% RS)** | **$175,225** | **RGB 2025 MSR**                       | **HIGH**   | **—**                     |

### 2.2 Market Context

The Housing Stability and Tenant Protection Act (HSTPA) of 2019 fundamentally restructured rent-stabilized building economics by eliminating vacancy bonuses, limiting MCI recoveries, and capping IAI rent increases. From 2019 to 2024, inflation-adjusted RS building sale prices declined 37–60% by borough (RGB 2025 MSR). RS buildings now trade at gross rent multiples of 4–6.5× (vs. 14–18× pre-HSTPA) and represent just 20% of multifamily dollar volume despite comprising 47% of transactions (Ariel 2025).

For TCAP, this represents a structural acquisition opportunity. RS buildings are trading at historically depressed valuations with compressed operating margins. Portfolio-scale acquisitions — like the Related Companies 36-building, 2,021-unit Bronx portfolio sold for $189M ($93,517/unit) — demonstrate that institutional-scale purchasing achieves further per-unit discounts.

### 2.3 Volume and Transaction Data

In 2025, NYC recorded 1,188 multifamily transactions totaling $8.9B (Ariel). Borough breakdown:

| Borough            | 2025 Transactions | 2025 Volume | YoY Trans Δ | YoY Volume Δ |
| ------------------ | ----------------- | ----------- | ----------- | ------------ |
| Manhattan          | 185               | $3.4B       | -2%         | -1%          |
| Brooklyn           | 582               | $3.5B       | +7%         | -3%          |
| Bronx              | 110               | $801M       | +21%        | +66%         |
| Queens             | 264               | $879M       | +4%         | +3%          |
| Northern Manhattan | 47                | $326M       | -28%        | -54%         |

______________________________________________________________________

## 3. CHANNEL 2: FORECLOSURE/AUCTION ACQUISITIONS

### 3.1 Acquisition Mechanism

Channel 2 aggregates three sub-channels for discounted multifamily building acquisitions:

**3.1.1 Mortgage Foreclosure Auctions**
In 2025, PropertyShark recorded 1,588 first-time foreclosure filings citywide (up 8% YoY), with Queens leading at 587 filings (37% of citywide), followed by Brooklyn (460), Manhattan (208, a record since 2010), and Bronx (up 35% YoY). Documented discounts from prior market values range from 44% to 97%, with large RS portfolios typically selling at 44–59% discounts. The Flagstar Bank foreclosure of 5,100+ rent-stabilized units (auction expected 2026) and A&E Real Estate's 31-property, 3,500-unit portfolio default demonstrate that distressed RS inventory is growing.

**3.1.2 NYC Tax Lien Sales**
As of 2025, the city's tax lien trusts hold 7,270 liens including 1,355 on multifamily parcels. Tax liens are sold at approximately 72 cents on the dollar. The 2024 Home Preservation and Debt Resolution Reform Act introduced the Easy Exit Program and expanded payment plans, but for buildings that remain delinquent, the lien sale process creates a pathway to acquisition at below-market costs.

**3.1.3 Third Party Transfer (TPT) Program**
TPT has been frozen since 2019 but is being reauthorized under the Housing Rescue and Resident Protection Act (introduced January 2025). Since inception, TPT stabilized ~520 buildings (~6,000 homes). Buildings qualify when tax lien-to-market-value ratios exceed 25% and significant HPD violations exist. If reauthorized, TPT could provide a direct pipeline for TCAP acquisitions of the most distressed buildings.

### 3.2 Per-Unit Acquisition Costs (40% Discount from Channel 1)

| Borough       | Channel 1 | Channel 2 (40% discount) | Discount Basis                                |
| ------------- | --------- | ------------------------ | --------------------------------------------- |
| Bronx         | $112,023  | $67,214                  | Documented: 44–59% discounts on RS portfolios |
| Brooklyn      | $190,000  | $114,000                 | Conservative end of 44–59% range              |
| Manhattan     | $249,000  | $149,400                 | Conservative end of 44–59% range              |
| Queens        | $145,000  | $87,000                  | Conservative end of 44–59% range              |
| Staten Island | $120,000  | $72,000                  | Conservative end of 44–59% range              |

**Note:** The 40% discount is conservative. Documented cases include a 29-unit Manhattan building at 97% discount from 2016 price, Inwood portfolio at 44%, Northern Manhattan 28-property portfolio at ~55%, and Harlem building at 59% below 2016 purchase price. TCAP would systematically target the 40–50% discount range, avoiding the deeply distressed end where hidden liabilities may exist.

______________________________________________________________________

## 4. CHANNEL 3: PENALTY-LEVERAGED ACQUISITIONS

### 4.1 The Leverage Mechanism

Channel 3 represents the most innovative acquisition pathway. It uses the city's existing but underenforced civil penalty authority as bargaining leverage to acquire the worst-maintained multifamily buildings at steep discounts.

**The mechanism works as follows:**

1. **Identify target buildings:** HPD violations data + Public Advocate Worst Landlords Watchlist + AEP list → buildings with large backlogs of overdue Class B/C violations.
1. **Calculate penalty exposure:** Under NYC Admin Code §27-2115 (as amended by Local Law 71 of 2023), daily civil penalties for overdue violations accumulate at $25–$150/day per violation depending on class and building size. For buildings with hundreds of overdue violations, annual penalty exposure can exceed building value within months.
1. **Negotiate settlement:** City offers landlord a choice — pay the full penalty exposure (which is uncollectable anyway, given the ~4% historical collection rate) OR transfer the building to the city/TCAP cooperative at 30% of market value, with the city forgiving 85% of accumulated penalties. The landlord avoids catastrophic penalty liability and exits a losing asset; the city acquires the building at a fraction of market cost.
1. **Rehabilitate and convert:** Building enters TCAP cooperative structure. Direct city-managed rehabilitation replaces the failed enforcement cycling model.

### 4.2 Penalty Schedule (Local Law 71 of 2023)

| Violation Class                    | Base Penalty | Daily Penalty (>5 units) | Annual Accumulation (per violation) |
| ---------------------------------- | ------------ | ------------------------ | ----------------------------------- |
| Class A (Non-hazardous)            | $50–$150     | $25/day                  | $9,125                              |
| Class B (Hazardous)                | $75–$500     | $25–$125/day             | $9,125–$45,625                      |
| Class C (Immediately hazardous)    | $50–$150     | $50–$125/day             | $18,250–$45,625                     |
| Heat/Hot Water (initial)           | $350–$1,250  | Per occurrence           | Varies                              |
| Heat/Hot Water (repeat, same year) | $500–$1,500  | Per occurrence           | Varies                              |

### 4.3 Representative Case Study

**620 E. 178th Street, Bronx** (Barry Singer, #1 Worst Landlord 2024)

| Metric                              | Value                                 |
| ----------------------------------- | ------------------------------------- |
| Units                               | 47                                    |
| Open HPD violations                 | 706                                   |
| Est. violation mix                  | 30% Class C, 50% Class B, 20% Class A |
| Daily penalty accumulation          | $56,480                               |
| Annual penalty accumulation         | $20,615,200                           |
| Building market value (RS rate)     | $5,265,081 (47 × $112,023)            |
| Penalty-to-value ratio (1 year)     | 3.9×                                  |
| Months until penalties exceed value | 3.1                                   |

**Settlement model:**

| Component                               | Amount                                                             |
| --------------------------------------- | ------------------------------------------------------------------ |
| Building transfer price (30% of market) | $1,579,524                                                         |
| Per-unit acquisition cost               | $33,607                                                            |
| City forgives 85% of annual penalties   | $17,523,920                                                        |
| Landlord outcome                        | Exits building with no penalty liability                           |
| City outcome                            | Acquires building at 70% discount + eliminates enforcement cycling |

### 4.4 Estimated Target Universe

| Category                                          | Estimated Buildings | Source                                   |
| ------------------------------------------------- | ------------------- | ---------------------------------------- |
| Public Advocate Worst Landlords Watchlist         | ~400                | NYC Public Advocate 2024–2025            |
| Alternative Enforcement Program (AEP) active      | ~250                | HPD AEP Building List                    |
| 7A Administrator buildings                        | ~100–200            | HPD (estimated)                          |
| Buildings with >100 open violations               | ~500–800            | NYC Open Data HPD violations (estimated) |
| **Buildings where penalties likely exceed value** | **~200–400**        | **Cross-referenced estimate**            |
| Estimated total units in target universe          | ~10,000–20,000      | Avg 30–50 units/building                 |

**Borough distribution:** Bronx and Brooklyn predominate. Bronx properties show highest violation concentrations with lowest property values, creating the largest penalty-to-value ratios and the strongest acquisition leverage.

### 4.5 Enforcement Cost Savings

Beyond acquisition discount, Channel 3 eliminates the failed enforcement cycling model:

| Cost Category                         | Annual Cost (per building) | 10-Year Cost Avoided  |
| ------------------------------------- | -------------------------- | --------------------- |
| HPD inspection cycling                | $15,000–$32,650            | $150,000–$326,500     |
| Emergency Repair Program (ERP)        | $25,000                    | $250,000              |
| Housing Court costs                   | $10,000                    | $100,000              |
| ECB/OATH administrative costs         | $5,000                     | $50,000               |
| **Total enforcement cycling avoided** | **$55,000–$72,650**        | **$550,000–$726,500** |

**Additional downstream savings:** Each displacement prevented avoids $49,640–$139,795/year in shelter costs per family (DHS: $136–$383/night). For a 47-unit building preventing even 10 displacements, annual shelter cost avoidance = $496,400–$1,397,950.

### 4.6 Per-Unit Acquisition Costs (70% Discount from Channel 1)

| Borough       | Channel 1 | Channel 3 (70% discount) | Rationale                                       |
| ------------- | --------- | ------------------------ | ----------------------------------------------- |
| Bronx         | $112,023  | $33,607                  | Highest violation density, lowest values        |
| Brooklyn      | $190,000  | $57,000                  | High violation density, moderate values         |
| Manhattan     | $249,000  | $74,700                  | Lower violation density but very high penalties |
| Queens        | $145,000  | $43,500                  | Moderate violation density                      |
| Staten Island | $120,000  | $36,000                  | Limited data; proxy estimate                    |

### 4.7 Channel 3 Rehabilitation Premium

Buildings acquired through Channel 3 are by definition the most physically deteriorated. Rehabilitation costs are modeled at 38% above standard (Channels 1–2):

| Borough       | Standard Rehab (Ch1/2) | Distressed Rehab (Ch3) | Premium |
| ------------- | ---------------------- | ---------------------- | ------- |
| Bronx         | $65,000                | $90,000                | +38%    |
| Brooklyn      | $65,000                | $90,000                | +38%    |
| Manhattan     | $75,000                | $100,000               | +33%    |
| Queens        | $60,000                | $85,000                | +42%    |
| Staten Island | $55,000                | $80,000                | +45%    |

### 4.8 Legal and Policy Requirements

Channel 3 is the most legally novel pathway. To operationalize it, the following would be needed:

1. **Administrative mechanism:** HPD or a designated agency needs authority to offer structured penalty-for-transfer settlements. This could be done under existing OATH/ECB settlement authority or may require local legislation.
1. **Penalty assessment accuracy:** Requires systematic calculation of accumulated penalty exposure per building from HPD violations data. NYC Open Data makes this feasible.
1. **Fair value determination:** Independent appraisal to establish market value; transfer price set as a percentage of appraised value.
1. **COPA alignment (if reauthorized):** The Community Opportunity to Purchase Act, if revived, provides a complementary legal pathway — AEP buildings become "Covered Properties" eligible for community entity first-purchase rights with municipal fee waivers.
1. **TPT integration:** If the Housing Rescue and Resident Protection Act passes, TPT provides an existing administrative channel for distressed building transfer to qualified entities.

______________________________________________________________________

## 5. BLENDED ACQUISITION COST MODEL

### 5.1 Blended Per-Unit Acquisition by Borough

Channel mix: 50% Market / 20% Foreclosure / 30% Penalty-Leveraged

| Borough       | Ch1 (50%) | Ch2 (20%) | Ch3 (30%) | Blended Acquisition |
| ------------- | --------- | --------- | --------- | ------------------- |
| Bronx         | $56,012   | $13,443   | $10,082   | **$79,536**         |
| Brooklyn      | $95,000   | $22,800   | $17,100   | **$134,900**        |
| Manhattan     | $124,500  | $29,880   | $22,410   | **$176,790**        |
| Queens        | $72,500   | $17,400   | $13,050   | **$102,950**        |
| Staten Island | $60,000   | $14,400   | $10,800   | **$85,200**         |

### 5.2 Total Per-Unit Conversion Cost (Blended)

Rehabilitation and soft costs weighted by channel mix (70% standard for Ch1/2, 30% distressed for Ch3):

| Borough          | Blended Acq  | Rehab (weighted) | Soft (weighted) | **Total Conversion** |
| ---------------- | ------------ | ---------------- | --------------- | -------------------- |
| Bronx            | $79,536      | $72,500          | $35,200         | **$187,236**         |
| Brooklyn         | $134,900     | $72,500          | $37,200         | **$244,600**         |
| Manhattan        | $176,790     | $82,500          | $41,200         | **$300,490**         |
| Queens           | $102,950     | $67,500          | $35,200         | **$205,650**         |
| Staten Island    | $85,200      | $62,500          | $33,200         | **$180,900**         |
| **Wtd Citywide** | **$104,889** | —                | —               | **$212,969**         |

### 5.3 Total Program Investment (150 Buildings, 3,750 Units)

| Borough       | Buildings | Units     | $/Unit       | Total Investment |
| ------------- | --------- | --------- | ------------ | ---------------- |
| Bronx         | 69        | 1,725     | $187,236     | $322,982,100     |
| Brooklyn      | 30        | 750       | $244,600     | $183,450,000     |
| Manhattan     | 15        | 375       | $300,490     | $112,683,750     |
| Queens        | 27        | 675       | $205,650     | $138,813,750     |
| Staten Island | 9         | 225       | $180,900     | $40,702,500      |
| **TOTAL**     | **150**   | **3,750** | **$212,969** | **$798,632,100** |

______________________________________________________________________

## 6. EQUITY TRAJECTORY AND BREAK-EVEN

### 6.1 10-Year Member Equity by Borough

| Borough          | Year 1  | Year 5  | Year 10     |
| ---------------- | ------- | ------- | ----------- |
| Bronx            | $13,581 | $37,096 | **$69,423** |
| Brooklyn         | $14,458 | $41,855 | **$79,994** |
| Manhattan        | $15,122 | $45,457 | **$87,993** |
| Queens           | $13,952 | $39,109 | **$73,893** |
| Staten Island    | $13,670 | $37,583 | **$70,504** |
| **Wtd Citywide** | —       | —       | **$74,264** |

### 6.2 Break-Even Analysis (Assets ≥ Investment with 2.5% Appreciation)

| Borough       | Break-Even Year | Notes                   |
| ------------- | --------------- | ----------------------- |
| Staten Island | Year 23         | Lowest conversion cost  |
| Bronx         | Year 24         | Lowest acquisition cost |
| Queens        | Year 24         |                         |
| Brooklyn      | Year 25         |                         |
| Manhattan     | Year 27         | Highest conversion cost |

### 6.3 Equity Trade-Off Explanation

The three-channel model produces **less equity per household** than v1 because lower blended acquisition costs → smaller cooperative mortgages → less principal paydown per member. The equity credit component ($360/month base, growing at 1.5%/year) is fixed and does not change with acquisition price — only the mortgage principal paydown varies.

This creates a clear trade-off for policymakers:

| Metric                   | v1 (Single Channel) | v2 (Three Channel) | Change                     |
| ------------------------ | ------------------- | ------------------ | -------------------------- |
| Total investment         | $953,125,000        | $798,632,100       | **-$154,492,900 (-16.2%)** |
| Per-unit conversion cost | $254,167            | $212,969           | **-$41,198 (-16.2%)**      |
| 10-year equity per HH    | $86,555             | $74,264            | **-$12,291 (-14.2%)**      |
| Asset creation rate      | 34.1% (v1 revised)  | 34.9%              | +0.8 ppt                   |
| Break-even               | Years 18–19         | Years 23–27        | +5–8 years                 |
| Subsidy premium          | $22,500,000         | $22,500,000        | No change                  |

**Recommendation:** The three-channel model is superior for the Mayor's Office pitch because:

1. **$154.5M less capital at risk** — easier to fund and politically defensible
1. **Asset creation rate is equivalent** (34.9% vs. 34.1%) — same efficiency on a smaller base
1. **Enforcement cost savings** of $550K–$726K per distressed building (10-year) are additive
1. **Shelter cost avoidance** of $496K–$1.4M/year per building with prevented displacements
1. **Penalty leverage is politically compelling** — the city currently collects ~4% of imposed penalties. Converting uncollectable penalties into building acquisitions turns a fiscal black hole into productive assets
1. **Equity shortfall is remediable** — increasing the equity split from 20% to 25%, or adding $75/month to the subsidy, would close the $12,291 gap

______________________________________________________________________

## 7. KEY FIGURES REQUIRING UPDATES IN EXISTING DOCUMENTS

The following figures in PET_TCAP_Policy_Proposal_FINAL_v3.md and the Executive Brief need updating if the three-channel model is adopted:

| Document            | Section              | Current Value      | New Value                              | Notes                                            |
| ------------------- | -------------------- | ------------------ | -------------------------------------- | ------------------------------------------------ |
| FINAL v3            | §V Budget            | $165,000/unit      | $212,969/unit (or $187,236 Bronx-only) | Was already superseded by v1 Borough at $254,167 |
| FINAL v3            | §V Budget            | $618,750,000 total | $798,632,100                           | Down from v1's $953.1M                           |
| FINAL v3            | §V Equity            | $66,582/HH         | $74,264/HH                             | Down from v1's $86,555                           |
| FINAL v3            | §V Break-even        | "Years 12–13"      | "Years 23–27"                          | Was already revised to 18–19 in v1               |
| Executive Brief     | Key metrics          | Various            | Align with above                       |                                                  |
| Legislative package | §26-1803 assumptions | As above           | As above                               | May affect equity formula parameters             |

______________________________________________________________________

## 8. CHANGES REQUIRING APPROVAL

The following facts contradict values in the v1 Borough Fiscal Model. Per irrefutable facts protocol, these require Accept/Deny/Modify before integration.

| Change ID  | Fact Changed                                | v1 Value          | Three-Channel Value            | Rationale                                                                             |
| ---------- | ------------------------------------------- | ----------------- | ------------------------------ | ------------------------------------------------------------------------------------- |
| ACQ-CHG001 | Blended per-unit acquisition (Bronx)        | $100,000          | $79,536                        | Three-channel blend: 50% market ($112K) + 20% foreclosure ($67K) + 30% penalty ($34K) |
| ACQ-CHG002 | Blended per-unit acquisition (citywide wt.) | $156,000 (est.)   | $104,889                       | Reduces acquisition component by ~33%                                                 |
| ACQ-CHG003 | Total per-unit conversion (Bronx)           | $199,000          | $187,236                       | Lower acquisition partially offset by higher weighted rehab                           |
| ACQ-CHG004 | Total per-unit conversion (citywide wt.)    | $254,167          | $212,969                       | -16.2% from v1                                                                        |
| ACQ-CHG005 | Total program investment (150 bldgs)        | $953,125,000      | $798,632,100                   | -$154.5M (-16.2%)                                                                     |
| ACQ-CHG006 | 10-year equity per HH (Bronx)               | $75,452           | $69,423                        | Smaller mortgage → less principal paydown                                             |
| ACQ-CHG007 | 10-year equity per HH (citywide wt.)        | $86,555           | $74,264                        | -14.2%; trade-off for lower capital requirement                                       |
| ACQ-CHG008 | Break-even (years)                          | 18–19             | 23–27                          | Extended by lower equity accumulation rate                                            |
| ACQ-CHG009 | Acquisition channels                        | 1 (market only)   | 3 (market/foreclosure/penalty) | New structural feature of model                                                       |
| ACQ-CHG010 | Foreclosure discount assumption             | N/A (not modeled) | 40%                            | Conservative end of documented 44–59% range                                           |
| ACQ-CHG011 | Penalty-leverage discount assumption        | N/A (not modeled) | 70%                            | Based on penalty-to-value analysis                                                    |

______________________________________________________________________

## 9. POLICY INTEGRITY CHECK

### 9.1 Fact-Based vs. Inferred

| Category                                        | Status                                                                                       |
| ----------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Channel 1 per-unit costs (Bronx, Manhattan)     | **Fact-based** — RGB MSR 2025, Ariel 2025, DOF rolling sales                                 |
| Channel 1 per-unit costs (Brooklyn, Queens, SI) | **Inferred** — estimated from citywide average + HSTPA decline patterns                      |
| Channel 2 discount (40%)                        | **Conservative inference** — documented range is 44–59%, model uses low end                  |
| Channel 3 discount (70%)                        | **Modeled** — based on penalty accumulation analysis, no direct precedent for this mechanism |
| Channel 3 target universe (200–400 buildings)   | **Rough estimate** — cross-referenced from Worst Landlords, AEP, and violation data          |
| Rehabilitation cost differential (Ch3 +38%)     | **Inferred** — based on HPD ANCP experience with distressed buildings                        |
| ECB collection rate (~4%)                       | **Dated fact** — Comptroller audit from 2008; current rate unknown                           |
| Enforcement cost per building ($55K–$73K/yr)    | **Estimated** — derived from HPD budget / inspection volume                                  |

### 9.2 Weak Assumptions

1. **Channel 3 legal mechanism does not currently exist in codified form.** The penalty-leverage settlement structure is modeled as a policy proposal, not an existing program. It would require either administrative rulemaking or local legislation.
1. **ECB collection rate data is from 2008.** The Comptroller has not published a more recent audit. If collection rates have improved significantly, the penalty leverage argument weakens.
1. **Brooklyn, Queens, and Staten Island RS per-unit costs are estimates.** The RGB Mortgage Survey publishes a Bronx and citywide figure but not borough-by-borough for all five boroughs.
1. **Channel 3 rehabilitation premium (38%) is estimated.** Actual costs for worst-condition buildings may be higher; HPD ANCP data shows capital subsidy limits up to $700,000/unit for the most distressed projects.

### 9.3 Legal and Fiscal Risks

1. **Takings clause challenge:** Channel 3 must be carefully structured to avoid Fifth Amendment challenges. The settlement must be genuinely voluntary — the penalty exposure creates leverage, but the transfer must remain the landlord's choice.
1. **COPA dependency:** If COPA is not reauthorized, Channel 3 loses one potential legal pathway (though OATH/ECB settlement authority may suffice independently).
1. **TPT reauthorization uncertainty:** Channel 2 partially depends on TPT revival. If the Housing Rescue and Resident Protection Act fails, foreclosure/auction acquisition volume may be lower.
1. **Capital market conditions:** The 4.0% mortgage rate assumption may be optimistic. Current multifamily mortgage rates are 6.73% (RGB MSR 2025). CDFI/community lending rates are lower but may not reach 4.0% for all projects.

### 9.4 Areas Requiring Political/Administrative Buy-In

1. Mayor's Office must endorse three-channel strategy (especially Channel 3)
1. HPD must establish penalty-leverage administrative mechanism
1. City Council must support COPA reauthorization for Channel 3 legal pathway
1. DOF must improve penalty assessment infrastructure
1. OMB must approve $798.6M capital commitment (down from $953.1M)
1. HRA must maintain CityFHEPS payment standards at $1,800/month minimum

______________________________________________________________________

*This model was prepared using publicly available data from NYC government sources, academic research institutions, and commercial real estate analytics firms. All assumptions are disclosed. No statistics were invented. Where data gaps exist, the gap is identified and the estimation methodology is transparent.*

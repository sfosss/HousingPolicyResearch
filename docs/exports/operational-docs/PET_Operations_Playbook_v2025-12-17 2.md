# Public Equity Transfer (PET) Framework

## Program Operations Playbook – v2025-12-17

______________________________________________________________________

## Overview

This playbook specifies the operational workflows for PET implementation, mapping PET household intake, underwriting, equity-share execution, payment handling, and exit/default scenarios onto existing NYC DSS/HPD infrastructure. It is intended for HPD/HRA ops managers, DSS case workers, credit-union underwriters, and Right-to-Counsel providers.

______________________________________________________________________

## 1. Intake & Eligibility Screening

### 1.1 Entry Points

PET participants enter through existing DSS homelessness-prevention and rental-assistance channels:

1. **Homebase intake:** Households at risk of eviction visit nearest Homebase office (25 locations across 5 boroughs). Homebase staff assess emergency rental needs and may refer eligible households to PET pilot if:

   - Household income 0–100% AMI (modifiable by policy).
   - Household willing to transition from rental assistance to cooperative/CLT ownership.
   - Building cohort is enrolled in active PET pilot.

1. **CityFHEPS intake:** HRA case managers working with households on CityFHEPS (city rental-assistance voucher) identify PET-eligible candidates after 6–12 months of stable rental payment history.

1. **Right-to-Counsel referral:** OCJ legal-services providers counsel tenants facing eviction; if building is in PET cohort and tenant is interested, OCJ refers to HPD PET enrollment.

### 1.2 PET Eligibility Criteria

| Criterion                 | Standard                                                                                                          | Notes                                                                                         |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **Income**                | ≤ 100% AMI (or policy-set ceiling) by HUD 2024 NYC Metro FMR tables                                               | Household must provide paystubs, SSA, or program benefits documentation                       |
| **Credit history**        | No eviction judgment in past 3 years; no active delinquency on rent/utilities                                     | TIL/ANCP precedent: can overlook prior rental-payment issues if circumstances have stabilized |
| **Occupancy**             | Existing tenant in rental unit or candidate for new PET-enabled cooperative unit                                  | For new conversions, household must express written intent to participate                     |
| **Consent**               | Signed consent form acknowledging Article XI restrictions, federal-subsidy volatility, and equity-share mechanics | Provide in tenant's preferred language; Right-to-Counsel review optional but encouraged       |
| **Household composition** | Any size (1+ persons); immediate family members on lease/deed permitted                                           | Succession rights must be documented at intake (emergency contact, beneficiary designation)   |

### 1.3 Intake Documentation

Homebase or HRA case manager completes:

1. **PET Intake Form** (standardized template; linked in playbook appendix):

   - Household ID, members, DOB.
   - Current income (all sources), benefits received.
   - Current rent and subsidy (if applicable).
   - Building/cohort identifier.
   - Household preference: cooperative ownership vs. CLT leasehold.

1. **Income Verification Packet:**

   - Prior 2 months of paystubs (or SSA letter, SNAP notice).
   - Tax return (prior year).
   - Lease showing current rent.

1. **Consent & Disclosure Form** (PET-specific; see appendix):

   - Acknowledges low-income ownership restrictions (Article XI in perpetuity).
   - Lists potential risks: federal subsidy cuts, special assessments, cooperative governance obligations.
   - Defines equity-share accrual mechanics and vesting schedule.
   - Signature of all household members age 18+; Right-to-Counsel provider (if engaged) also signs.

### 1.4 Triage & Screening Decision

**Process:**

1. HRA/Homebase case manager inputs household data into **PET Eligibility Dashboard** (Notion or Excel template; auto-calc against income bands).
1. Dashboard flags: income-qualifying (Y/N), credit-acceptable (Y/N), building cohort active (Y/N).
1. If all flags = Y: household moves to **Underwriting.**
1. If any flag = N: household is counseled on next steps (rental assistance, legal services, etc.) but not enrolled in PET.

**Timeline:** 5–10 business days from intake to screening decision.

______________________________________________________________________

## 2. Underwriting & Building Assignment

### 2.1 Credit & Underwriting Review

**Owner:** HPD PET Credit & Underwriting Team (or delegated credit union).

**Inputs:**

- PET Intake Form + income verification.
- Credit report (pulled by credit union or HPD-authorized third party).
- Rental history (via background check service or landlord contact).

**Assessment:**

| Factor                          | Standard                                                            | Risk Mitigation                                                                 |
| ------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **FICO score**                  | No minimum required by PET policy; consider case-by-case if \<580   | Credit counseling; co-signer or guarantor; higher initial subsidy share         |
| **Prior eviction judgment**     | None in prior 3 years                                               | If 3+ years past, document circumstance (job loss, illness) and stability since |
| **Current delinquency**         | None on active rent or utilities                                    | Must resolve prior to equity-share vesting                                      |
| **Debt-to-income**              | Target ≤ 43% after PET subsidy; acceptable up to 50% in pilot phase | Design subsidy to bring tenant below 30% rent burden if possible                |
| **Employment/income stability** | Documented income source for prior 6 months                         | Self-employment, gig work acceptable if tax returns or bank statements provided |

**Underwriting Decision:** Approve, Approve with Conditions, or Decline.

**Timeline:** 10–15 business days.

### 2.2 Building Cohort Assignment

**Process:**

Once household is underwriting-approved, HPD PET Operations matches household to available cooperative or CLT unit in an active pilot cohort:

1. **Cohort inventory:** HPD maintains list of PET-active buildings/portfolios (TIL, HDFC, warehoused, or new conversions).
1. **Unit availability:** For each building, track occupied, vacant, pending-rehab units.
1. **Tenant preference:** Household may list neighborhood/building preferences; assignment is best-effort but subject to PET cohort availability.
1. **Building readiness:** Only buildings with completed governance training (tenant boards, bylaws) and operational readiness are open to new PET assignments.

**Timeline:** 5–10 business days for matching; may extend if preferred neighborhoods unavailable.

______________________________________________________________________

## 3. Equity-Share Agreement & Legal Execution

### 3.1 Equity-Share Agreement Preparation

**Owner:** Right-to-Counsel provider (or HPD legal) + credit union.

**Process:**

1. **Customize PET equity-share agreement** (template in appendix) with:

   - Household ID, income level, and subsidy allocation.
   - Building legal description, cooperative/CLT entity name.
   - Initial rent charge and PET equity-share accrual rate (e.g., $50/month into equity pool).
   - Vesting schedule (e.g., 5-year cliff or year-over-year linear vesting).
   - Default scenarios and remedies.
   - Succession rights and exit procedures.

1. **Credit union underwriting addendum** (if credit union is lender):

   - Loan terms (rate, amortization, security interest in equity share).
   - Underwriting conditions and approval terms.
   - Subordination of credit-union lien to city equity-share interest (if applicable).

1. **Right-to-Counsel legal review:**

   - OCJ-contracted attorney reviews PET agreement for Article XI compliance, ADA/504 protections, and disclosure adequacy.
   - Attorney meets with household (in person or video) to explain equity mechanics, risks, and alternatives (remaining in rental assistance).
   - Attorney signs-off confirming household understanding and consent.

**Timeline:** 10–15 business days.

### 3.2 Household Signing Session

**Process:**

1. Household meets with HPD PET enrollment staff + Right-to-Counsel attorney + credit-union representative (if applicable).
1. All documents reviewed in household's preferred language (via interpreter if needed).
1. Household signs:
   - PET Consent & Disclosure Form.
   - Equity-share agreement.
   - Cooperative bylaws (if transitioning to coop; or CLT ground lease if CLT model).
   - Credit-union loan document (if applicable).
   - Authorization for HPD to set up automatic rent/subsidy payments.
1. Originals retained by HPD; copies to household, Right-to-Counsel, cooperative/CLT entity, and credit union.

**Timeline:** 1–2 hours. Schedule in advance to allow adequate explanation time.

______________________________________________________________________

## 4. Payment Flows & Subsidy Administration

### 4.1 Rent & Equity-Share Payment Architecture

**Monthly Cash Flow (Illustrative Example):**

| Item                                          | Amount               | Payer                                 | Payee                  |
| --------------------------------------------- | -------------------- | ------------------------------------- | ---------------------- |
| **Rent/Maintenance Charge** (4-person family) | $1,200               | City (HRA) + Household                | Coop/CLT               |
| **City subsidy payment**                      | $840 (70% of charge) | HRA CityFHEPS                         | Coop/CLT               |
| **Household cash payment**                    | $360 (30% of charge) | Tenant (personal funds)               | Coop/CLT               |
| **PET Equity Accrual**                        | $75/month            | HPD (from redirected CityFHEPS funds) | Household Equity Pool  |
| **Total public commitment**                   | $915/month           | City budget (HRA + HPD)               | Coop/CLT + Equity Pool |

**Design principle:** Redirect a portion of HRA's existing CityFHEPS payment into HPD's equity-investment account; this portion accrues to household equity share, not paid directly to landlord.

### 4.2 HRA Payment Operations

**Owner:** HRA Accounts Payable & Rental Assistance Division.

**Process:**

1. **Setup:** HRA receives signed PET equity-share agreement from HPD. HRA creates household record in its billing system with:

   - Cooperative/CLT payee entity and bank account (direct deposit).
   - **Split payment routing:** 70% to landlord; 30% to HPD equity-investment account (separate account number).
   - PET identifier flag (for monthly reporting).

1. **Monthly payment:**

   - HRA generates HRA-household subsidy payment (standard CityFHEPS process).
   - System automatically splits payment: 70% → Coop bank account; 30% → HPD equity account.
   - Both transfers clear within 5 business days.

1. **Household responsibility:**

   - Household pays 30% rent share (or negotiated percentage) from personal funds; mails check or arranges auto-pay to coop.
   - Coop verifies receipt and reports delinquency to HPD PET if household payment is >5 days late.

1. **Reporting:**

   - HRA generates monthly PET payment dashboard (counts of households, total outlay split, delinquencies).
   - HRA coordinates with HPD on subsidy adjustments (e.g., if household income drops below eligibility) or terminations (e.g., household moves out).

**Timeline:** Ongoing; begins after equity-share agreement is executed and cooperative/CLT entity is set up.

### 4.3 HPD Equity Account Management

**Owner:** HPD Asset & Property Management Division (or delegated credit union).

**Process:**

1. **Equity account setup:**

   - HPD opens dedicated **PET Household Equity Sub-Account** for each household (nested within building/cooperative equity-pool account).
   - Account tracks:
     - Monthly accrual ($50–100/month, or negotiated amount).
     - Cumulative equity balance.
     - Interest earned (if any).
     - Withdrawals or transfers (to co-op down payment, special assessment, etc.).

1. **Account administration:**

   - HPD (or delegated credit union) receives monthly HRA equity-split payment and deposits into household sub-account.
   - HPD generates quarterly household statement (mailed or emailed) showing:
     - Beginning balance.
     - Accrual this quarter.
     - Ending balance.
     - Projected balance at vesting (e.g., year 5 or 10).
   - HPD maintains master ledger of all household equity accounts and building-level equity pools.

1. **Restrictions & withdrawal rules:**

   - Household **cannot withdraw** equity share during active occupancy (locked for wealth-building).
   - Household **can use** equity for:
     - Initial down payment on cooperative share purchase (if/when vesting complete).
     - Special assessments or building emergency costs (if cooperative approves; must repay or reduce future accrual).
   - Upon household exit or default, equity share disposition follows equity-share agreement (see Section 5 below).

**Timeline:** Ongoing monthly; quarterly statements.

### 4.4 Subsidy Adjustment Triggers

**Event:** Household income change, household size change, change in federal subsidy, or cooperative rent increase.

**Process:**

1. **Annual recertification:** HRA/Homebase conducts annual income verification (standard DSS process). If income changes >10%, HRA recalculates subsidy.

1. **Subsidy adjustment:** If recertification shows:

   - Income increased: HRA reduces subsidy proportionally; HPD may adjust equity-accrual rate (policy decision).
   - Income decreased: HRA increases subsidy; HPD may increase equity-accrual rate.
   - Household becomes ineligible (>100% AMI): HRA terminates PET subsidy; household transitions to market rent or other assistance.

1. **Cooperative rent increase:** If coop votes to increase maintenance charge (e.g., due to capital project), HRA is notified. HRA recalculates subsidy based on new rent; may request HPD coverage analysis (can equity subsidy be funded from current budget?).

1. **Federal subsidy cut:** If HUD cuts Section 8 or CityFHEPS appropriation, HRA notifies HPD. HPD may:

   - Reduce equity-accrual rate to preserve basic subsidy for rent.
   - Tap PET Emergency Reserve Fund (if funded) to backfill.
   - Terminate new PET enrollments and prioritize existing participants.

**Timeline:** Annual recertification window (typically October–December); emergency adjustments as needed.

______________________________________________________________________

## 5. Default, Exit, & Succession

### 5.1 Rent Delinquency Protocol

**Event:** Household fails to pay 30% rent share for >5 days or >2 months in any 12-month period.

**Process:**

1. **Early warning (5–15 days late):**

   - Coop notifies household via email/phone; offers payment plan or hardship application.
   - Coop notifies HPD PET Coordinator; HPD reaches out to household via case manager.

1. **Intermediate escalation (15–30 days late):**

   - Coop may assess late fee (per cooperative bylaws; typically 1–2% of rent).
   - HPD and household meet to assess hardship (job loss, health emergency, etc.).
   - If eligible, household may apply for emergency rental assistance (existing HRA emergency fund) to catch up.
   - HPD may pause equity accrual (halt new contributions) but does not claw back existing balance.

1. **Formal default (>30 days late or >2 months in 12 months):**

   - Coop issues **default notice** (per cooperative bylaws and PET equity-share agreement).
   - HPD is copied on all notices.
   - Right-to-Counsel is automatically notified; OCJ attorney contacts household to explore remedies (negotiate payment plan, review eligibility for additional benefits, etc.).

1. **Eviction/exit:**

   - If household does not cure default within 30 days of notice, coop may proceed with legal eviction (subject to state/city eviction law and Right-to-Counsel defense).
   - HPD suspends equity accrual as of default date.
   - Upon eviction/exit, household's accumulated equity balance follows **exit terms** (see Section 5.3 below).

**Timeline:** 5–60 days from late payment to eviction commencement (subject to state law forbearance periods).

### 5.2 Building Default Scenario

**Event:** Cooperative building defaults on debt (e.g., fails to service HPD-issued equity-pool credit line or mortgage).

**Process:**

1. **Building-level trigger:** Coop DSCR drops below 1.0, or coop misses loan payment to HPD or private lender.

1. **HPD intervention:**

   - HPD PET Credit team notifies coop board immediately.
   - HPD conducts building financial audit (operations, reserves, rent roll).
   - HPD offers options: emergency cash-flow support (if available), special assessment (residents contribute), building refinancing, or orderly liquidation.

1. **Household impact:**

   - All household rent payments continue (required to avoid eviction).
   - Household equity-accrual may be suspended pending building stabilization.
   - Households are informed of building distress via Right-to-Counsel and case manager.
   - If building forecloses, households have right to first bid (per CLT or cooperative bylaws, if in place).

1. **Recovery pathway:** HPD works with building board and residents to restructure debt, pursue operational efficiencies, or facilitate transfer to stronger cooperative/CLT entity.

**Timeline:** Weeks to months depending on severity.

### 5.3 Exit & Equity Disposition

**Event:** Household voluntarily exits (moves out) or is evicted for default/non-payment.

**Equity disposition rules** (policy to be finalized; options listed):

| Scenario                                                | Equity Disposition                                                                                                                                                                                                                                                                        | Notes                                                                                                                                         |
| ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **Voluntary exit, household income still ≤100% AMI**    | Household buys equity share (pays from savings or borrowed funds); remains in coop as owner-occupant. Or: Household receives equity balance in cash (as onetime payout) and exits coop. Or: Equity balance is transferred to new rental-assistance household (cooperative/HPD agreement). | Households should be counseled to prefer owner option if possible (builds permanent housing stability).                                       |
| **Voluntary exit, household income >100% AMI**          | Household exits cooperative (income no longer PET-eligible). Equity balance paid to household in cash as buyout; no further connection to coop.                                                                                                                                           | Equity buildup should create pathway to homeownership even outside PET coop.                                                                  |
| **Eviction for non-payment (household in default)**     | Household forfeits accumulated equity balance. Balance remains in cooperative equity pool (offsets future tenant's subsidy or rebuilds coop reserve).                                                                                                                                     | Harsh but incentivizes payment; household is offered Right-to-Counsel representation to explore alternatives (payment plan, hardship waiver). |
| **Household death (with succession rights documented)** | Equity balance + cooperative share transferred to designated beneficiary (spouse, child, parent) per succession-rights documentation filed at intake. Beneficiary must qualify as low-income member to retain share; otherwise equity is liquidated.                                      | Article XI succession rules and PET agreement must be aligned; see Section 3.2 above.                                                         |

### 5.4 Equity Share Buyout & Cashing Out

**Scenario:** Household reaches equity-vesting milestone (e.g., year 5) and is offered opportunity to purchase full cooperative share.

**Process:**

1. **Appraisal & buyout price:** Cooperative board appraises PET household's share equity and cooperative market value; sets buyout price (typically below market, per Article XI low-income pricing).
1. **Financing options:**
   - Household uses accumulated PET equity as down payment.
   - Household borrows remainder from credit union (PET-affiliated lender) or other lender; or negotiates seller financing with cooperative.
1. **Buyout execution:**
   - Household and cooperative execute share-purchase agreement (per cooperative bylaws).
   - Household becomes full member-owner; no longer receives city subsidy (but may still be Section 8 or CityFHEPS eligible if income-qualified).
   - HPD is released from equity obligations; can redeploy subsidy to new PET household.

**Timeline:** 1–3 months from appraisal to closing.

### 5.5 Right-to-Counsel Access Throughout

**Principle:** Right-to-Counsel coverage extends to all PET households from intake through exit.

**Integration:**

- OCJ attorney is present at equity-share agreement signing (Section 3.2).
- OCJ attorney is automatically contacted upon rent delinquency >15 days (Section 5.1).
- OCJ attorney counsels household on equity disposition options at exit (Section 5.3).
- OCJ attorney can represent household in any dispute with cooperative board (e.g., special assessment, eviction, equity accounting).

**Funding:** PET implementation budget must allocate 2–3% of redirected subsidies to OCJ for PET-specific legal services.

______________________________________________________________________

## 6. Building Governance & Cooperative Operations

### 6.1 Cooperative Board Composition & Training

**Requirement:** Any building converting to PET-enabled cooperative (or CLT with member governance) must establish or strengthen resident governance.

**Process:**

1. **Board formation (or expansion):** Tenant association becomes cooperative board (if not already). New buildings: residents elect board from membership.

1. **Board size:** Target 5–7 member board; at least 50% must be active PET households (ensures equity-investment voice).

1. **Training:** Before building transitions to PET, all board members complete:

   - **Cooperative governance basics** (2–4 hours): roles, responsibilities, fiduciary duties, meeting procedures.
   - **PET-specific training** (2–4 hours): equity accrual mechanics, subsidy administration, member communication.
   - **Financial management** (4–8 hours): budget, reserve planning, debt service, internal controls.

   Training is provided by HPD-contracted nonprofit (e.g., UHAB, ANCP administrator, or credit union partner).

1. **Board recertification:** Annually, board confirms fiduciary competency; any new members are trained before seating.

**Timeline:** 6–12 weeks from tenant association to board readiness.

### 6.2 Member Meetings & Communication

**Requirement:** Cooperative must hold quarterly member meetings (at minimum).

**Agenda items (PET-relevant):**

- Rent/maintenance charge updates and financial performance.
- Equity-pool status (aggregate balance, accrual rate, member education).
- Special assessments or capital projects affecting equity shares.
- Member disputes or defaults (anonymized; confidentiality rules apply).

**Transparency:**

- Cooperative board provides monthly financial statements to HPD PET team.
- HPD posts (anonymized) building-level equity-pool data in quarterly PET dashboard for policy analysis.

______________________________________________________________________

## 7. Compliance & Reporting

### 7.1 HPD PET Reporting Dashboard

**Purpose:** Monthly tracking of PET program performance, fiscal impact, and equity outcomes.

**Metrics:**

- Number of active PET households (by building, by borough, by income band).
- Total city equity investment (redirected subsidy outlay).
- Aggregate household equity-pool balance (cumulative accrual).
- Rent delinquency rate (>5 days, >15 days, >30 days).
- Eviction/exit count and reason.
- Equity disposition (household buys share, cashes out, forfeits, inherits).
- Disaggregated by race/ethnicity, family size, borough (to track equity outcomes).

**Frequency:** Monthly; aggregated quarterly and annually for public reporting.

**Owner:** HPD PET Operations (coordination with HRA, credit unions, Right-to-Counsel providers).

### 7.2 Annual PET Civil-Rights Compliance Report

**Purpose:** Document racial equity, fair housing, and ADA/504 compliance.

**Contents:**

- Household demographic breakdown: race, ethnicity, family composition, disability status, language access.
- Equity outcomes: median equity accrual, median household net worth impact, foreclosure/eviction disparities.
- Civil-rights incidents: SOI discrimination complaints, Title VI disparate-impact concerns, ADA/504 accommodations granted.
- Corrective actions taken (if any disparities identified).

**Frequency:** Annually; submitted to NYC Comptroller, NYC Public Advocate, civil-rights organizations for public review.

**Owner:** HPD + designated civil-rights review team.

______________________________________________________________________

## 8. Appendix: Templates & Tools

| Template                                       | Purpose                                                                      | Location                               |
| ---------------------------------------------- | ---------------------------------------------------------------------------- | -------------------------------------- |
| **PET Intake Form**                            | Household data collection; eligibility screening                             | \[Link to HPD shared drive\]           |
| **PET Consent & Disclosure**                   | Household consent; risks & restrictions disclosure                           | \[Link to HPD shared drive\]           |
| **PET Equity-Share Agreement**                 | Legal framework for equity accrual, vesting, default, exit                   | \[Link to HPD shared drive\]           |
| **Cooperative Bylaws (PET-enabled)**           | Model bylaws incorporating PET equity, member governance, dispute resolution | \[Link to HPD shared drive\]           |
| **CLT Ground Lease (PET-enabled)**             | Model ground lease for CLT model; equity ownership on leasehold              | \[Link to HPD shared drive\]           |
| **Credit Union Loan Agreement (PET)**          | Credit union mortgage/LOC terms for cooperative/CLT PET buildings            | \[Link to credit union partner drive\] |
| **Equity-Share Agreement (Succession Rights)** | Successor-in-interest documentation; beneficiary designation                 | \[Link to HPD shared drive\]           |
| **PET Payment Routing Setup (HRA)**            | HRA billing system configuration for split CityFHEPS payments                | \[Link to HRA operations drive\]       |
| **PET Eligibility Dashboard**                  | Notion or Excel; auto-calc income banding and underwriting flags             | \[Link to HPD shared drive\]           |
| **Monthly Equity Account Statement**           | Household statement template; balance, accrual, projections                  | \[Link to HPD shared drive\]           |
| **Building Financial Audit (HPD)**             | Cooperative balance-sheet analysis; DSCR, default risk                       | \[Link to HPD credit team drive\]      |
| **Right-to-Counsel Referral Form**             | OCJ intake form for PET households; case tracking                            | \[Link to OCJ drive\]                  |

______________________________________________________________________

## 9. Glossary

- **Equity accrual:** Monthly amount of redirected subsidy deposited into household equity account (builds resident ownership stake).
- **DSCR:** Debt-service coverage ratio; cooperative's ability to service debt from operating income.
- **Article XI:** NY PHFL provision requiring HDFC cooperatives to maintain low-income purpose in perpetuity.
- **CLT:** Community land trust; holds land; residents lease ground and own building/equity.
- **Right-to-Counsel:** NYC program providing free legal representation to low-income tenants in housing matters.
- **SOI:** Source of income; NYC law prohibiting landlord/broker discrimination based on use of government rental assistance.
- **PET:** Public Equity Transfer; framework converting rental subsidies into resident equity investment.

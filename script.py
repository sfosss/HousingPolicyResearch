# FACT-CHECK AND FEASIBILITY ANALYSIS

# Data verification based on web search results
fact_check_results = {
    "VERIFIED_DATA": {
        "Section 8 Voucher Amounts (NYC 2024-2025)": {
            "Studio": "$2,646-$2,762",
            "1-BR": "$2,762-$2,762",
            "2-BR": "$3,058",
            "3-BR": "$3,811",
            "Source": "NYCHA Payment Standards 2024-2025",
            "Status": "✓ VERIFIED",
        },
        "CityFHEPS Costs": {
            "Daily Cost": "$54.79",
            "Annual Cost per Household": "$20,000",
            "FY2024 Total": "$819.4M",
            "FY2025 Projected": "$1.1B+",
            "Source": "Citizens Budget Commission Feb 2025",
            "Status": "✓ VERIFIED",
        },
        "Shelter Costs (FY2024)": {
            "Family Shelter Per Day": "$270.51",
            "City Share Family": "$123.36/day",
            "Single Adult Per Day": "$143.90",
            "City Share Single": "$132.50/day",
            "Annual Family Cost": "$67,000",
            "Source": "NYC DHS, Citizens Budget Commission",
            "Status": "✓ VERIFIED",
        },
        "Income Limits NYC (2024)": {
            "Family of 4 - 50% AMI": "$77,650",
            "Family of 4 - ELI 30% AMI": "$46,600",
            "Source": "HUD Income Limits NY Metro 2024",
            "Status": "✓ VERIFIED",
        },
    },
    "DATA_REQUIRING_ADJUSTMENT": {
        "Homeownership Rates": {
            "Original_Claim": "27% Black, 17% Latino, 44% White",
            "Verification_Status": "Data from NYU Furman Center 2021-2022 reports",
            "Adjustment_Needed": "Add date qualifier: '(2021-2022 data)'",
            "Status": "⚠ REQUIRES DATE QUALIFIER",
        },
        "Annual Subsidy Spending": {
            "Original_Claim": "$5 billion annually",
            "Breakdown_Found": {
                "CityFHEPS": "$1.1B (FY2025)",
                "NYCHA Section 8": "~$2.5B estimated",
                "HPD HCV": "~$600M estimated",
                "Other Programs": "~$800M estimated",
            },
            "Verification_Status": "Total plausible but not single verified source",
            "Adjustment": "Cite: 'Over $5B across all programs (CityFHEPS, Section 8, HPD vouchers)'",
            "Status": "⚠ REQUIRES COMPONENT BREAKDOWN",
        },
        "Shelter Cost Figure": {
            "Original_Claim": "$62,000 per family annually",
            "Updated_Data": "$98,736/year (based on $270.51/day × 365)",
            "City_Share": "$45,016/year (based on $123.36/day × 365)",
            "Adjustment": "Use $45,000 city share OR $99,000 total cost",
            "Status": "⚠ REQUIRES UPDATE",
        },
    },
    "HDFC_COOPERATIVE_DATA": {
        "Code_Violations": {
            "Claim": "HDFC cooperatives show 60% fewer violations",
            "Evidence_Found": "UHAB reports distressed HDFCs struggle with violations",
            "Reality": "Well-managed HDFCs perform better, distressed ones worse",
            "Adjustment": "Qualify: 'Well-managed HDFCs maintain lower violation rates'",
            "Status": "⚠ REQUIRES QUALIFICATION",
        },
        "Housing_Violations_2024": {
            "Total_Violations": "895,457 (FY2024)",
            "Increase": "24% year-over-year",
            "Source": "NYC Mayor's Management Report, City Limits",
            "Status": "✓ VERIFIED",
        },
    },
    "COST_MODEL_ADJUSTMENTS": {
        "Annual_Status_Quo_Cost": {
            "Original": "$32,800/unit",
            "Components_Verified": {
                "Voucher": "$20,000-$24,000 (depending on unit size)",
                "Eviction_Prevention": "$5,000-$7,400 plausible",
                "Admin": "$1,800-$2,000 plausible",
            },
            "Adjusted": "$28,000-$35,000 range more accurate",
            "Status": "⚠ USE RANGE",
        },
        "TCAP_Model_Cost": {
            "Original": "$26,200/unit",
            "Adjustment": "Reduced subsidy $18,000 + TA $1,200 + admin $1,200 = $20,400",
            "Plus": "Eviction reduction savings $2,500",
            "Net": "$22,900/unit annual",
            "Status": "⚠ RECALCULATE",
        },
    },
    "ROI_FEASIBILITY": {
        "10_Year_Savings": {
            "Original_Claim": "$1.33B",
            "Recalculation": "Based on $5,100/unit annual savings × 2,000 units × 10 years",
            "Result": "$102M savings (more conservative)",
            "Additional": "+$31M shelter +$14M eviction = $147M total benefits",
            "Adjusted_ROI": "~2.5:1 instead of 4.6:1",
            "Status": "⚠ MAJOR REVISION NEEDED",
        },
        "Acquisition_Costs": {
            "Original": "$43,000/unit",
            "Plausibility": "Reasonable for down payment + repairs + legal",
            "Verification": "Comparable to CDC acquisition financing",
            "Status": "✓ REASONABLE",
        },
    },
}

# Print summary
print("=" * 70)
print("FACT-CHECK & FEASIBILITY ANALYSIS SUMMARY")
print("=" * 70)
print("\n✓ VERIFIED DATA (Use as-is with citations):")
print("  - Section 8 voucher payment standards")
print("  - CityFHEPS costs and program spending")
print("  - Shelter system costs (per diem and annual)")
print("  - Income limits and AMI calculations")
print("  - Housing violations data\n")

print("⚠ DATA REQUIRING ADJUSTMENT:")
print("  - Homeownership gap statistics (add date qualifier)")
print("  - $5B annual subsidy claim (needs breakdown)")
print("  - $62K shelter cost (update to $45K city share or $99K total)")
print("  - HDFC violation rates (needs qualification)")
print("  - Annual cost per unit ranges (use $28K-$35K range)")
print("\n")

print("🚨 CRITICAL REVISIONS NEEDED:")
print("  - 10-year savings: REDUCE from $1.33B to $102M-$147M")
print("  - ROI: REDUCE from 4.6:1 to 2.5:1")
print("  - Annual savings per unit: REDUCE from $6,600 to $5,100")
print("\n")

print("=" * 70)
print("FEASIBILITY ASSESSMENT")
print("=" * 70)
print("\n✓ LEGALLY FEASIBLE:")
print("  - NYC can create new cooperative classifications")
print("  - Subsidy redirection possible with HUD waivers")
print("  - TOPA exists in DC as precedent")
print("  - State cooperative law provides framework\n")

print("✓ FINANCIALLY VIABLE (with adjustments):")
print("  - Positive ROI maintained (2.5:1 still strong)")
print("  - Acquisition costs reasonable")
print("  - Revolving fund model sound")
print("  - Break-even extended to Year 9-10 (vs Year 7)\n")

print("⚠ IMPLEMENTATION CHALLENGES:")
print("  - HUD waiver approval uncertain")
print("  - Landlord opposition likely significant")
print("  - Technical assistance capacity limited")
print("  - Tenant organizing time-intensive\n")

print("=" * 70)
print("RECOMMENDATION: Proceed with REVISED NUMBERS")
print("=" * 70)
print("\nThe program remains viable but projections must be")
print("adjusted to reflect realistic cost comparisons and")
print("conservative savings estimates. Core concept sound.")

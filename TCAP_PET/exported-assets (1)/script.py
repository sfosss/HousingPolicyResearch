import json
import os
from datetime import datetime
import csv

# Create a project structure and generate key deliverables

# 1. Create a comprehensive task list for Notion/Trello
tasks = [
    {
        "Section": "I. Baseline Research",
        "Task": "Complete NYC Agency Architecture Mapping (HPD, HRA, NYCHA, HUD alignment)",
        "Owner": "Policy Analyst",
        "Due": "Week 1",
        "Status": "In Progress",
        "Artifact": "Agency Map + Budget Flow Chart",
    },
    {
        "Section": "I. Baseline Research",
        "Task": "Conduct Literature Grid: Public Equity Transfer + Tenant Ownership Models",
        "Owner": "Research Team",
        "Due": "Week 1-2",
        "Status": "In Progress",
        "Artifact": "Annotated Bibliography (APA 7)",
    },
    {
        "Section": "I. Baseline Research",
        "Task": "Extract Financial Baseline: Current Subsidy Spending & ROI",
        "Owner": "CFO Analyst",
        "Due": "Week 2",
        "Status": "Queued",
        "Artifact": "Budget Snapshot (3-yr trend)",
    },
    {
        "Section": "II. Drafting",
        "Task": "Draft v1 Master Policy Report (20-30pp) with Alternatives",
        "Owner": "Lead Policy Writer",
        "Due": "Week 3-4",
        "Status": "Queued",
        "Artifact": "Master_Policy_Report_v1_YYYYMMDD.docx",
    },
    {
        "Section": "II. Drafting",
        "Task": "Build ROI Model Template (Excel: PACT vs. CLT vs. Ownership Hybrid)",
        "Owner": "Financial Analyst",
        "Due": "Week 3",
        "Status": "Queued",
        "Artifact": "ROI_Model_Comparison_v1.xlsx",
    },
    {
        "Section": "II. Drafting",
        "Task": "Create Stakeholder Briefing Memo (2pp, CFO + Legal review)",
        "Owner": "Communications",
        "Due": "Week 4",
        "Status": "Queued",
        "Artifact": "Briefing_Memo_v1_YYYYMMDD.docx",
    },
    {
        "Section": "II. Drafting",
        "Task": "Draft 1-Pager Executive Summary",
        "Owner": "Lead Policy Writer",
        "Due": "Week 4",
        "Status": "Queued",
        "Artifact": "1Pager_Summary_v1_YYYYMMDD.docx",
    },
    {
        "Section": "III. Validation",
        "Task": "Legal Review: Title VI/IX/504/ADA/HSTPA Compliance",
        "Owner": "Civil Rights Attorney",
        "Due": "Week 7-8",
        "Status": "Queued",
        "Artifact": "Legal_Risk_Memo.docx",
    },
    {
        "Section": "III. Validation",
        "Task": "Stakeholder Interviews (HPD, NYCHA, HRA, Credit Union Coalition)",
        "Owner": "Policy Analyst",
        "Due": "Week 7-9",
        "Status": "Queued",
        "Artifact": "Interview_Summary_Notes.docx",
    },
    {
        "Section": "III. Validation",
        "Task": "Finalize ROI Model with Real Budget Data (FOIL requests)",
        "Owner": "Financial Analyst",
        "Due": "Week 8",
        "Status": "Queued",
        "Artifact": "ROI_Model_Final_v2.xlsx",
    },
    {
        "Section": "IV. Finalization",
        "Task": "Approval + Version Control (v1->v_final)",
        "Owner": "Municipal CFO",
        "Due": "Week 10-11",
        "Status": "Queued",
        "Artifact": "All Docs v_final in Archive/",
    },
    {
        "Section": "IV. Finalization",
        "Task": "Generate Slide Deck (15-20pp for mayoral/council briefing)",
        "Owner": "Communications",
        "Due": "Week 11",
        "Status": "Queued",
        "Artifact": "Briefing_Deck_Final_YYYYMMDD.pptx",
    },
    {
        "Section": "IV. Finalization",
        "Task": "Publish Deliverables Packet (PDF + Web Summary)",
        "Owner": "Communications",
        "Due": "Week 12",
        "Status": "Queued",
        "Artifact": "NYC_Housing_Subsidy_Reform_Packet_Final_YYYYMMDD.pdf",
    },
]

# Write tasks CSV
csv_filename = "NYC_Housing_Subsidy_Ops_Tasks_Workplan.csv"
with open(csv_filename, "w", newline="") as csvfile:
    fieldnames = ["Section", "Task", "Owner", "Due", "Status", "Artifact"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(tasks)

print(f"✓ Created: {csv_filename}")
print(f"  Total tasks: {len(tasks)}")

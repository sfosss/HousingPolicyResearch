# TCAP Housing Subsidy Reform — Interactive Task Dashboard

## Automated Task Management, Risk Radar & Version Control System

**Version:** 0.1\
**Generated:** 2025-12-14\
**Status:** ✅ READY FOR DEPLOYMENT

______________________________________________________________________

## 🎯 System Overview

The **TCAP Interactive Task Dashboard** is a **scripted automation system** that:

1. **Reads/Writes CSV Task Data** — Syncs bidirectionally with your task file
1. **Visualizes Dependencies** — Maps task blocking relationships across 8 project phases
1. **Tracks Risk Radar** — Real-time heat map of legal/fiscal/operational risks
1. **Maintains Version History** — Captures snapshots with timestamps and audit trails
1. **Generates Automated Reports** — Status, risk, overdue task alerts
1. **Enables Scheduling** — Cron-based daily/weekly/monthly automation

______________________________________________________________________

## 📦 Deliverables

### Core Files

| File                                       | Purpose                          | Format      |
| ------------------------------------------ | -------------------------------- | ----------- |
| `tcap_task_automation.py`                  | Main automation engine           | Python 3.8+ |
| `tcap_automation.sh`                       | Orchestration & scheduling       | Bash script |
| `TCAP_Task_Status_Risk_Tracking.csv`       | Task status + risk export        | CSV         |
| `TCAP_Version_History_Audit_Log.txt`       | Version control + escalation log | Text        |
| `NYC_Housing_Subsidy_Ops_Tasks_Notion.csv` | Master task file (update me)     | CSV         |

### Supporting Config

| File                                   | Purpose                  |
| -------------------------------------- | ------------------------ |
| `tcap_cron_setup.txt`                  | Cron scheduling examples |
| `TCAP_Interactive_Dashboard_README.md` | This file                |

______________________________________________________________________

## 🚀 Quick Start

### 1. Install & Initialize

```bash
# Copy all files to your project directory
cp tcap_*.py tcap_*.sh *.csv *.txt ./your-project/
cd your-project

# Make shell script executable
chmod +x tcap_automation.sh

# Verify Python installation
python3 --version  # Requires 3.8+
```

### 2. Generate Your First Report

```bash
# Generate comprehensive status report
python3 tcap_task_automation.py report

# View risk assessment
python3 tcap_task_automation.py risk

# Check dependency graph
python3 tcap_task_automation.py dependencies
```

### 3. Update a Task Status

```bash
# Update TASK_001 to "In Progress"
python3 tcap_task_automation.py update --task-id 1 --status "In Progress"

# CSV is automatically updated with timestamp
```

### 4. Schedule Automation

```bash
# Add to your crontab (edit with: crontab -e)
0 6 * * 1-5 /path/to/tcap_automation.sh daily
0 9 * * 1 /path/to/tcap_automation.sh weekly
0 8 1 * * /path/to/tcap_automation.sh monthly
```

______________________________________________________________________

## 📊 System Features

### A. Dependency Visualization

**How it works:**

- Analyzes all 20 tasks across 8 project phases
- Maps blocker relationships based on section ordering
- Identifies critical path (tasks with most dependencies)
- Exports CSV with blocker counts per task

**Example Output:**

```
TASK_000: Set scope guardrails
  Status: Not Started
  Blockers: 19 (all downstream tasks)
  Critical Path Rank: 1 (highest priority)
  Action: CRITICAL - Activate parallel workstreams

TASK_017: Produce 1-pager summary
  Status: Not Started
  Blockers: 15 (must complete Intake→QA phases first)
  Critical Path Rank: 2
  Action: BLOCKED - Depends on v1 drafting
```

**File Generated:** `TCAP_Task_Status_Risk_Tracking.csv`

### B. Risk Radar Heat Map

**Scoring Method:**

- **Legal Risk:** Flags tasks with "legal", "title", "aida", "504", "procurement"

  - Weight: Not Started = ×3, In Progress = ×2, Complete = ×0
  - Current Score: 6/60 (10% - LOW)

- **Fiscal Risk:** Flags tasks with "budget", "mou", "cfo", "funding", "roi"

  - Current Score: 18/60 (30% - CRITICAL)
  - Top Risks: TASK_001 (KPIs), TASK_004 (Funding), TASK_006 (Draft v1)

- **Operational Risk:** Flags tasks with "automation", "version", "process"

  - Current Score: 3/60 (5% - LOW)
  - Mitigated by parallel execution of Version Control phase

**Escalation Triggers:**

- Fiscal Risk ≥ 15: Escalate to Municipal CFO
- Legal Risk ≥ 10: Escalate to Civil-Rights Attorney
- Overdue + High Blocker Count: Escalate to Program Manager

**File Generated:** `TCAP_Version_History_Audit_Log.txt`

### C. Version History & Audit Trail

**What's Tracked:**

- Task count, status breakdown, completion %
- Risk scores at each snapshot
- Content hash (MD5) for integrity verification
- Timestamp and description for each version

**Snapshots:**

- Automatic when system initializes
- Manual when you run: `python3 tcap_task_automation.py snapshot "Your description"`
- Preserves last 5 snapshots in memory; older ones archived

**Example:**

```
🔍 VERSION 0.1 - BASELINE (2025-12-14T21:58:00.555554)
  ✅ INITIALIZED
  Task Count: 20
  Status: 19 Not Started, 0 In Progress, 1 Complete
  Legal Risk: 6/60 | Fiscal Risk: 18/60 | Operational Risk: 3/60
  Actions: Loaded CSV, inferred dependencies, assessed risks
```

**Naming Convention (Ops Manual):**

```
Housing_Subsidy_Reform_MASTER_v[VERSION]_[YYYYMMDD].docx
Example: Housing_Subsidy_Reform_MASTER_v0.1_20251214.docx
```

______________________________________________________________________

## 🔧 Command Reference

### Python Automation Engine

```bash
# View status report (with overdue tasks)
python3 tcap_task_automation.py report

# Output: TCAP_Status_Report.txt
#   - Status breakdown (Not Started / In Progress / Complete)
#   - Risk assessment (Legal/Fiscal/Operational scores)
#   - Overdue tasks list with days overdue
#   - Critical path summary

# View risk heat map
python3 tcap_task_automation.py risk

# Output: Terminal display
#   - Risk scores by category
#   - Flagged tasks per risk type
#   - Top 3 escalation actions

# View dependency graph
python3 tcap_task_automation.py dependencies

# Output: Terminal display
#   - Tasks with most blockers
#   - Section-by-section dependency chain
#   - Parallel vs. sequential phases

# Update task status & sync to CSV
python3 tcap_task_automation.py update --task-id 1 --status "In Progress"

# Output: 
#   ✅ Updated TASK_001: Not Started → In Progress
#   (CSV automatically updated with timestamp)
```

### Bash Orchestration

```bash
# Generate daily reports
./tcap_automation.sh daily

# Output:
#   ✅ Loaded 20 tasks
#   ✅ Status report generated: TCAP_Status_Report.txt
#   ✅ Risk assessment complete
#   📁 Task backup created: backups/TCAP_Tasks_v20251214_215900.csv

# Run weekly comprehensive review
./tcap_automation.sh weekly

# Output: Includes daily + overdue task summary + risk escalations

# Create monthly archive
./tcap_automation.sh monthly

# Output: Includes all weekly reports + compressed tar.gz backup
```

______________________________________________________________________

## 📈 Risk Radar Interpretation

### Current Status (v0.1)

| Risk Type       | Score | Status      | Escalation                                        |
| --------------- | ----- | ----------- | ------------------------------------------------- |
| **Legal**       | 6/60  | 🟢 LOW      | Monitor Title IV/IX/ADA/504 review (TASK_008)     |
| **Fiscal**      | 18/60 | 🔴 CRITICAL | Activate CFO review on funding streams (TASK_004) |
| **Operational** | 3/60  | 🟢 LOW      | On track — automation proceeding                  |

### Critical Tasks (Require Immediate Action)

**Priority 1 — BLOCKER:**

- **TASK_001**: Refine core research question (Policy Analyst)
  - Due: 2025-09-22 (83 days OVERDUE)
  - Impact: Blocks all Research, Drafting, Decision phases
  - Action: **ESCALATE TO PROGRAM MANAGER NOW**

**Priority 2 — FISCAL GATE:**

- **TASK_004**: Identify funding streams (Municipal CFO)
  - Due: 2025-10-01 (74 days OVERDUE)
  - Impact: Required for Decision phase
  - Action: **SCHEDULE CFO MEETING WITH HRA/HPD**

**Priority 3 — LEGAL GATE:**

- **TASK_008**: Legal feasibility crosswalk (Civil-Rights Attorney)
  - Due: 2025-10-11 (OVERDUE)
  - Impact: Procurement constraints, Title compliance
  - Action: **ASSIGN ATTORNEY + BRIEF ON FRAMEWORK**

______________________________________________________________________

## 🔗 Dependency Phases

### Phase I: Intake/Triage (Entry Point)

- **TASK_000**: Set scope guardrails
- **TASK_001**: Refine research question ← **BLOCKER FOR ALL DOWNSTREAM**

### Phase II: Research (Precursor)

- **TASK_003**: Map programs (blocked by TASK_001)
- **TASK_004**: Identify funding (blocked by TASK_001)
- **TASK_005**: Assemble models (blocked by TASK_001)

### Phase III: Drafting (Knowledge Intensive)

- **TASK_006**: Draft v1 (blocked by TASK_003, 004)
- **TASK_007**: Equity analysis (blocked by Research phase)
- **TASK_008**: Legal feasibility (blocked by Research phase)

### Phase IV: Decision (Choice Point)

- **TASK_010**: List mechanisms (blocked by Drafting phase)
- **TASK_011**: Select CU model (blocked by Drafting phase)

### Phase V: QA (Validation)

- **TASK_012**: Fact check claims (blocked by Drafting phase)
- **TASK_013**: Resolve flags (blocked by TASK_012)

### Phase VI: Automation (Technical — CAN RUN IN PARALLEL)

- **TASK_014**: Generate shells ✅ In Progress
- No blockers — proceed independently

### Phase VII: Version Control (Housekeeping — CAN RUN IN PARALLEL)

- **TASK_015**: File naming ✅ Ready
- **TASK_016**: Works cited ✅ Ready

### Phase VIII: Deliverables (Outputs)

- **TASK_017**: 1-pager (blocked by all prior phases)
- **TASK_018**: Briefing memo (blocked by all prior phases)
- **TASK_019**: Slide deck (blocked by all prior phases)
- **TASK_020**: Appendices (blocked by all prior phases)

______________________________________________________________________

## 📋 Weekly Checklist (Ops Manual Pattern)

**Every Monday, 9 AM:**

- [ ] Run `./tcap_automation.sh weekly`
- [ ] Review risk radar scores (email summary to stakeholders)
- [ ] Check TASK_001 & TASK_004 status (escalate if still "Not Started")
- [ ] Update any completed tasks: `python3 tcap_task_automation.py update --task-id X --status Complete`
- [ ] Archive previous week's reports to `/archive/` folder
- [ ] Create new version snapshot if major changes: `python3 tcap_task_automation.py snapshot "Weekly review — TASK_X moved to In Progress"`

**Monthly (1st of month):**

- [ ] Run `./tcap_automation.sh monthly`
- [ ] Export CSV & archive to external backup (see cron config)
- [ ] Update master document version: `Housing_Subsidy_Reform_MASTER_v0.2_YYYYMMDD.docx`
- [ ] Reset APA audit checklist for next review cycle

______________________________________________________________________

## 🛠️ Customization

### Add New Tasks

Edit `NYC_Housing_Subsidy_Ops_Tasks_Notion.csv`:

```csv
New Task Name,Section,Owner Persona,Status,Due Date,Frequency,Trigger,Artifact,Notes
```

Then re-run:

```bash
python3 tcap_task_automation.py report
```

System will automatically recalculate dependencies.

### Change Risk Thresholds

Edit `tcap_task_automation.py`, line ~100:

```python
risk_keywords = {
    "legal": ["legal", "title", "aida", "504", "procurement", "attorney"],
    "fiscal": ["budget", "mou", "cfo", "funding", "streams", "roi"],
    "operational": ["automation", "version", "process", "naming", "audit"]
}
```

### Modify Cron Schedule

Edit `tcap_cron_setup.txt` and update `crontab -e`:

```bash
# Example: Run reports twice daily
0 6 * * * /path/to/tcap_automation.sh daily
0 18 * * * /path/to/tcap_automation.sh daily
```

______________________________________________________________________

## 🔍 Troubleshooting

**Problem:** `python3: command not found`

- **Solution:** Install Python 3.8+. On macOS: `brew install python3`

**Problem:** `Permission denied: tcap_automation.sh`

- **Solution:** `chmod +x tcap_automation.sh`

**Problem:** CSV file not updating after `update` command

- **Solution:** Check file permissions: `ls -la NYC_Housing_Subsidy_Ops_Tasks_Notion.csv`

**Problem:** Risk scores seem wrong

- **Solution:** Check task text for keywords. Add debug flag: `python3 tcap_task_automation.py risk --debug`

______________________________________________________________________

## 📞 Support & Integration

### Sync with Notion (Optional)

Once you migrate to Notion:

1. Use Notion API to fetch tasks into CSV
1. Run automation pipeline
1. Sync results back to Notion via API

**Script Template:**

```bash
# notion_sync.py
from notion_client import Client
import csv

notion = Client(auth=os.environ["NOTION_TOKEN"])
# Query database → export to CSV
# Run tcap_task_automation.py
# Query results → update Notion
```

### Email Alerts

Add to cron:

```bash
0 6 * * 1-5 /path/to/tcap_automation.sh daily | mail -s "TCAP Daily Report" team@example.com
```

### Dashboard Integration

Export CSV to Metabase/Tableau/Power BI:

```bash
python3 tcap_task_automation.py report  # → TCAP_Status_Report.txt
cat TCAP_Task_Status_Risk_Tracking.csv | curl -X POST http://localhost:3000/api/data
```

______________________________________________________________________

## 📚 Appendix: Ops Manual Integration

This system implements these patterns from your **NYC Housing Subsidy Ops Manual:**

| Pattern                    | Usage                                        |
| -------------------------- | -------------------------------------------- |
| **Context Manager**        | Maintains project scope (NYC-only, 8 phases) |
| **Question Refinement**    | Tracks TASK_001 (measurable KPIs)            |
| **Fact Check List**        | TASK_002 & TASK_012 (APA audit)              |
| **Recipe**                 | Phase-by-phase dependency sequencing         |
| **Template**               | Version naming (MASTER_v\[N\]\_YYYYMMDD)     |
| **Alternative Approaches** | TASK_010 (policy mechanism comparison)       |
| **Persona**                | Owner assignment (CFO, Attorney, Analyst)    |
| **Output Automater**       | This system (CSV exports + scripts)          |

______________________________________________________________________

## ✅ Next Steps

1. **Copy all files** to your project directory
1. **Run baseline report**: `python3 tcap_task_automation.py report`
1. **Review risk escalations** in `TCAP_Version_History_Audit_Log.txt`
1. **Assign TASK_001 & TASK_004** to unblock dependent phases
1. **Set up cron** (see `tcap_cron_setup.txt`)
1. **Update CSV weekly** as work progresses
1. **Archive versions** using ops manual naming convention

______________________________________________________________________

**Questions?** Review `TCAP_Version_History_Audit_Log.txt` for detailed analysis and mitigation actions.

**Ready to deploy?** Run: `./tcap_automation.sh daily`

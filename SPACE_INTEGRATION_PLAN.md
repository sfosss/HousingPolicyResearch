# Housing Policy Research Tools - Space Integration Plan

**Status:** Implementation Ready\
**Objective:** Integrate Raycast extension components into NYC Housing Subsidy Reform operational framework\
**Pattern:** Context Manager + Recipe + Output Automater

______________________________________________________________________

## 1 | CONTEXT & SCOPE

### Research Operations Frame

**Focus:** NYC housing subsidy policy reform via Public Equity Transfer Framework\
**Tools:** Raycast CLI extension for automated research, drafting, and source management\
**Scale:** Three commands (BillSweep, DraftSection, AddSource)\
**Budget:** Reuse existing agency infrastructure (HPD, HRA, NYCHA)\
**Deliverables:** Evidence-based policy memos, briefing decks, ROI models

### Scope Alignment

✅ **In Scope:**

- Legislation tracking (NYC, NY State, Federal)
- AI-assisted policy document drafting
- Research source inventory management
- Integration with housing subsidy policy domain

✅ **Integration Points:**

- TCAP task automation (Phase III: Validation)
- Capstone research workflow (Phase II: Drafting)
- Notion database for source tracking
- Git-based version control for drafts

______________________________________________________________________

## 2 | ROLES & PERSONAS

### Municipal Policy Analyst (You)

**Responsibilities:**

- Run BillSweep to monitor legislative changes
- Trigger DraftSection for policy memo sections
- Manage sources via AddSource command
- Review generated content for accuracy
- Integrate findings into final briefing memos

**Tools Access:**

- Raycast CLI extension
- Local Notion instance for sources
- Git for version control
- Backend API (assistant service)

### Technical Architect (Support)

**Responsibilities:**

- Maintain backend API endpoints
- Monitor Raycast extension performance
- Support preference configuration
- Handle integration issues

**Tools Access:**

- Backend API server
- API monitoring/logging
- Raycast configuration management

______________________________________________________________________

## 3 | IMPLEMENTATION WORKFLOW

### Phase 1: Setup (Week 1)

**Week 1 Tasks:**

```
[ ] 1.1 Install Node.js 18+ and npm
[ ] 1.2 Create package.json in project root
[ ] 1.3 Run npm install (install @raycast/api, React, dependencies)
[ ] 1.4 Create tsconfig.json for TypeScript compilation
[ ] 1.5 Create raycast.manifest.json with command definitions
[ ] 1.6 Verify file structure:
        src/commands/
          ├── BillSweep.tsx
          ├── DraftSection.tsx
          └── AddSource.tsx
        src/utils/
          └── api.ts
[ ] 1.7 Run npm run build (verify compilation)
[ ] 1.8 Document backend API endpoint requirements
```

**Deliverable:** Compiled extension ready for loading into Raycast

### Phase 2: Configuration (Week 1)

**Configuration Tasks:**

```
[ ] 2.1 Set up Raycast preferences
     - Assistant Backend URL (required)
     - API Timeout (optional, default 30000ms)

[ ] 2.2 Configure backend API endpoints
     - POST /sweep_bills
     - POST /generate_section
     - POST /add_source

[ ] 2.3 Set up local development environment
     npm run dev  (development mode with auto-reload)

[ ] 2.4 Load extension into Raycast
     Cmd + Shift + A → "Load Extension" → Select directory

[ ] 2.5 Test all three commands with mock data
```

**Deliverable:** Extension loaded and tested in Raycast

### Phase 3: Integration (Week 2-3)

**Integration Tasks:**

```
[ ] 3.1 Map bill sweep results to policy tracking
     - NYC bills → Subsidy policy context
     - NY State bills → Broader housing framework
     - Federal bills → National policy trends

[ ] 3.2 Connect DraftSection to policy memo workflow
     - Section: "Executive Summary" (housing subsidy ROI)
     - Section: "Key Findings" (equity impact analysis)
     - Section: "Recommendations" (implementation roadmap)

[ ] 3.3 Integrate AddSource with Notion database
     - Create Notion schema for sources
     - Tag sources by:
       * Policy area (subsidies, equity, tenure)
       * Jurisdiction (NYC, NY, Federal)
       * Type (report, statute, research)

[ ] 3.4 Create automated task checklist
     - Weekly bill sweeps (Mondays)
     - Monthly draft reviews
     - Source inventory updates

[ ] 3.5 Document integration patterns
     - How to use BillSweep for policy scanning
     - How to use DraftSection in memo workflow
     - How to manage sources via AddSource
```

**Deliverable:** Fully integrated into housing policy research workflow

### Phase 4: Automation (Week 3)

**Automation Tasks:**

```
[ ] 4.1 Create task automation scripts
     - sweep_bills.sh (weekly legislative scan)
     - draft_memo_section.sh (on-demand drafting)
     - manage_sources.sh (source inventory)

[ ] 4.2 Set up Notion integration
     - Source table with metadata
     - Task tracking for drafts
     - Bill tracking dashboard

[ ] 4.3 Create CSV output automater
     - Bills found (date, jurisdiction, status)
     - Drafts generated (section, tokens used, timestamp)
     - Sources added (title, url, tags, date added)

[ ] 4.4 Document automation workflows
     - Manual trigger procedures
     - Scheduled execution (if applicable)
     - Error handling and recovery
```

**Deliverable:** Automated research operations checklist

### Phase 5: Documentation & QA (Week 4)

**Documentation Tasks:**

```
[ ] 5.1 Create operational runbooks
     - "How to sweep bills" (step-by-step)
     - "How to generate a policy memo section"
     - "How to add and manage sources"

[ ] 5.2 Create troubleshooting guide
     - Common errors and fixes
     - Backend connectivity issues
     - API timeout handling

[ ] 5.3 Create training materials
     - Raycast keyboard shortcuts
     - Extension preferences guide
     - Command-by-command tutorial

[ ] 5.4 Quality assurance verification
     - Test each command 3x with real data
     - Verify error handling
     - Confirm output quality

[ ] 5.5 Get stakeholder sign-off
     - Review output quality
     - Confirm workflow integration
     - Approve for production use
```

**Deliverable:** Production-ready extension with operational documentation

______________________________________________________________________

## 4 | DETAILED RECIPES

### Recipe 1: Run Bill Sweep

**Goal:** Monitor new legislation across jurisdictions\
**Time:** 5 minutes per execution\
**Frequency:** Weekly (Mondays recommended)

**Step-by-step:**

```
STEP 1: Open Raycast (Cmd + Space)
STEP 2: Type "Sweep Bills"
STEP 3: Select the command
STEP 4: Check jurisdictions:
        ✓ NYC
        ✓ New York State
        (Optional: ✓ Federal)
STEP 5: Set "Search Since" date (e.g., 7 days ago)
STEP 6: Click "Sweep Bills"
STEP 7: Wait for results (5-30 seconds)
STEP 8: Review bills in detail view
STEP 9: Copy relevant bills to Notion database
STEP 10: Close Raycast (Esc)

OUTPUT: Array of bills with:
  - Title
  - Jurisdiction
  - Status
  - Last Action date
  - Summary (optional)
  - URL (optional)

NOT: Store results in CSV for weekly tracking
```

**Automation Hook:**

```bash
#!/bin/bash
# sweep_bills_weekly.sh
# Runs bill sweep every Monday at 9am

echo "Running weekly bill sweep..."
raycast sweep-bills --jurisdictions NYC,NY --since "7 days ago"
echo "Results exported to bills_$(date +%Y%m%d).csv"
```

### Recipe 2: Generate Policy Memo Section

**Goal:** Create draft policy memo sections with AI assistance\
**Time:** 2-5 minutes per section\
**Frequency:** As needed during drafting phase

**Step-by-step:**

```
STEP 1: Open Raycast (Cmd + Space)
STEP 2: Type "Generate Draft"
STEP 3: Select "Generate Draft Section" command
STEP 4: Enter Section Name (required)
        Examples:
        - "Executive Summary"
        - "Key Findings"
        - "Recommendations"
        - "Implementation Roadmap"
STEP 5: Enter Prompt (required)
        Example:
        "Summarize NYC housing subsidy reform findings from attached research, 
         focusing on ROI implications and equity outcomes. Target: 500 words."
STEP 6: Click "Generate Draft"
STEP 7: Wait for generation (10-60 seconds)
STEP 8: Review generated markdown in detail view
STEP 9: Copy/paste into policy memo document
STEP 10: Refine and edit as needed
STEP 11: Close Raycast (Esc)

OUTPUT: Markdown text with:
  - Section content
  - Metadata (tokens used, model, timestamp)
  - Ready for copy-paste into final document

NOTE: Output is draft only - human review required
```

**Automation Hook:**

```bash
#!/bin/bash
# draft_memo_section.sh
# Generates policy memo sections on demand

SECTION="$1"  # e.g., "Executive Summary"
PROMPT="$2"   # Detailed prompt

echo "Generating $SECTION draft..."
raycast generate-section --section "$SECTION" --prompt "$PROMPT"
echo "Draft generated - open memo document for refinement"
```

### Recipe 3: Add Research Source

**Goal:** Manage research source inventory\
**Time:** 1-2 minutes per source\
**Frequency:** As sources are discovered

**Step-by-step:**

```
STEP 1: Open Raycast (Cmd + Space)
STEP 2: Type "Add Source"
STEP 3: Select "Add Source" command
STEP 4: Enter Source Title (required)
        Example: "NYC Housing Preservation Database"
STEP 5: Enter URL (required)
        Format: https://example.com/resource
STEP 6: Enter Notes (optional)
        Example: "Key data on subsidy program outcomes, 
                  2015-2024 time series available"
STEP 7: Click "Add Source"
STEP 8: Confirm success notification
STEP 9: Source is now in Notion database
STEP 10: Close Raycast (Esc)

OUTPUT: Source stored with:
  - Title
  - URL (validated)
  - Notes
  - Timestamp
  - Source ID (for references)

INTEGRATION: Auto-tags source in Notion database
```

**Automation Hook:**

```bash
#!/bin/bash
# add_sources_batch.sh
# Batch add multiple sources from CSV

while IFS=',' read -r TITLE URL NOTES; do
  echo "Adding source: $TITLE"
  raycast add-source --title "$TITLE" --url "$URL" --notes "$NOTES"
done < sources.csv

echo "Batch source addition complete"
```

______________________________________________________________________

## 5 | OUTPUT AUTOMATION

### CSV Task List Generator

**Purpose:** Export Raycast operations to Notion/Trello task list

**Output Format:**

```csv
Task,Command,Owner,Due Date,Status,Priority,Artifact,Notes
Weekly Bill Sweep,sweep-bills,Policy Analyst,2025-01-06,TODO,HIGH,bills_20250106.csv,Monitor NYC/NY legislation
Draft Executive Summary,generate-section,Policy Analyst,2025-01-10,IN_PROGRESS,HIGH,memo_v1.md,Use bill sweep results as context
Add Housing Database Source,add-source,Policy Analyst,2025-01-06,DONE,MEDIUM,sources.csv,Key 2015-2024 data
Review Generated Section,Manual Review,Policy Analyst,2025-01-11,TODO,HIGH,memo_v1_reviewed.md,Edit and refine AI output
Finalize Memo,Manual Refinement,Policy Analyst,2025-01-15,TODO,HIGH,memo_final.docx,Integrate all sections
```

**Generation Script:**

```bash
#!/bin/bash
# generate_task_list.sh
# Creates task list from Raycast operations

echo "Task,Command,Owner,Due Date,Status,Priority,Artifact,Notes" > tasks.csv

# Bill sweep task
echo "Weekly Bill Sweep,sweep-bills,Policy Analyst,$(date -d '7 days' +%Y-%m-%d),TODO,HIGH,bills_$(date +%Y%m%d).csv,Monitor NYC/NY/Federal legislation" >> tasks.csv

# Draft task
echo "Draft Policy Memo Sections,generate-section,Policy Analyst,$(date -d '14 days' +%Y-%m-%d),TODO,HIGH,memo_v1.md,Use AI-assisted drafting" >> tasks.csv

# Source management task
echo "Maintain Source Inventory,add-source,Policy Analyst,ONGOING,IN_PROGRESS,MEDIUM,sources.csv,Add sources as discovered" >> tasks.csv

echo "Task list generated: tasks.csv"
```

### Fact Check List Automation

**Purpose:** Verify claims and sources in generated content

**Template:**

```
Claim: [From generated memo section]
Source: [Cited source or data point]
Verification Method: [Search, calculation, interview]
Status: [VERIFIED, NEEDS REVIEW, UNVERIFIED]
Notes: [Evidence or explanation]

Example:
Claim: NYC housing subsidy spending has increased 15% since 2020
Source: NYC HPD budget reports 2020-2024
Verification: Cross-check with municipal budget database
Status: NEEDS_REVIEW
Notes: Confirm inflation adjustment applied
```

______________________________________________________________________

## 6 | PATTERN INTEGRATION MATRIX

| Pattern                    | Trigger                                | Action                                | Artifact                      |
| -------------------------- | -------------------------------------- | ------------------------------------- | ----------------------------- |
| **Context Manager**        | Scope drift in policy focus            | Restate housing subsidy constraints   | SPACE_INTEGRATION_PLAN.md     |
| **Question Refinement**    | Ambiguous research direction           | Rewrite measurable policy outcomes    | Research questions doc        |
| **Fact Check List**        | Claims in generated memo               | Generate verification checklist       | fact_check\_\[date\].csv      |
| **Recipe**                 | Multi-step Raycast workflow            | Output full command sequence          | sweep_bills.sh, draft_memo.sh |
| **Template**               | Policy memo output format              | Apply standard memo structure         | memo_template.md              |
| **Alternative Approaches** | Design choice (bill tracking method)   | Compare ≥2 filtering/sorting options  | alternatives_comparison.md    |
| **Persona**                | Policy analyst role                    | Adopt municipal CFO constraints       | Policy analyst runbook        |
| **Output Automater**       | ≥2 repeatable steps (bill sweep → CSV) | Emit sweep_bills_weekly.sh            | task_automation.sh            |
| **Flipped Interaction**    | Missing backend config                 | Ask 3 clarifying Qs before proceeding | setup_checklist.md            |

______________________________________________________________________

## 7 | WORKFLOW EXECUTION

### Standard Workflow Loop

```
1. INTAKE (Monday)
   → Run BillSweep for NYC, NY, Federal jurisdictions
   → Export results to CSV (bills_[date].csv)
   → Review bills for housing subsidy relevance
   → Tag relevant bills in Notion

2. RESEARCH (Tue-Wed)
   → Add new sources as discovered (AddSource)
   → Tag sources by policy area
   → Store URLs and summaries in Notion database

3. DRAFTING (Wed-Thu)
   → Use DraftSection to generate memo sections
   → Input: Bill sweep results + source summaries
   → Output: Draft memo with Executive Summary, Key Findings
   → Manual refinement of AI output

4. VALIDATION (Thu-Fri)
   → Fact-check generated claims
   → Cross-reference with source documents
   → Update memo with verified information
   → Prepare final briefing memo

5. APPROVAL (Friday EOD)
   → Stakeholder review of final memo
   → Incorporate feedback
   → Export to DOCX/PDF for distribution
   → Archive in Git with version tag
```

### Escalation Gates

```
GATE 1: Bill Sweep Results
  IF no relevant bills → Continue monitoring
  IF relevant bills found → Proceed to Research

GATE 2: Source Quality
  IF sources are academic/government → Use as-is
  IF sources are advocacy → Note bias in memo
  IF missing critical sources → Manual research task

GATE 3: Generated Content Quality
  IF accuracy > 90% → Proceed to Validation
  IF accuracy < 90% → Return to DraftSection with refined prompt
  IF scope issue → Question Refinement pattern

GATE 4: Fact Check
  IF all claims verified → Proceed to Approval
  IF claims need revision → Update generated content
  IF claims unverifiable → Flag for stakeholder review

GATE 5: Final Approval
  IF approved → Export and archive
  IF revision needed → Return to Drafting
  IF reject → Question Refinement for next iteration
```

______________________________________________________________________

## 8 | INTEGRATION CHECKLIST

### Phase 1: Installation

- [ ] Node.js 18+ installed
- [ ] npm dependencies installed (`npm install`)
- [ ] Build successful (`npm run build`)
- [ ] TypeScript validated (`npm run typecheck`)
- [ ] Extension loads in Raycast without errors

### Phase 2: Configuration

- [ ] Backend API URL configured in Raycast preferences
- [ ] API timeout set (recommended: 30000ms)
- [ ] All three commands visible in Raycast search
- [ ] Test command executes successfully

### Phase 3: Integration

- [ ] BillSweep results map to policy tracking
- [ ] DraftSection output integrates with memo template
- [ ] AddSource connects to Notion database
- [ ] CSV export automater working
- [ ] Task tracking updated after each operation

### Phase 4: Operations

- [ ] Weekly bill sweep scheduled
- [ ] Memo drafting workflow documented
- [ ] Source inventory system live
- [ ] Error handling procedures established
- [ ] Team trained on Raycast commands

### Phase 5: Quality Assurance

- [ ] 100+ hour operational testing complete
- [ ] Error rates \< 2%
- [ ] User satisfaction > 90%
- [ ] Documentation comprehensive
- [ ] Ready for production use

______________________________________________________________________

## 9 | RISK MITIGATION

| Risk                             | Impact               | Mitigation                           | Owner   |
| -------------------------------- | -------------------- | ------------------------------------ | ------- |
| Backend API unavailable          | Can't run commands   | Fallback to manual research          | Tech    |
| Generated content inaccurate     | Policy errors        | Fact-check all claims                | Analyst |
| Bill surge (legislative session) | Workflow overwhelmed | Increase sweep frequency, automation | Analyst |
| Source URL broken                | Research interrupted | Maintain source inventory in Notion  | Analyst |
| Preference misconfiguration      | Extension fails      | Clear documentation + validation     | Tech    |

______________________________________________________________________

## 10 | SUCCESS METRICS

### Operational Metrics

- **Bill Sweep:** 3+ bills identified per week (NYC/NY focus)
- **Draft Quality:** 85%+ of generated sections usable without revision
- **Source Management:** 50+ sources tracked by Q1 2025
- **Productivity:** 3x faster memo drafting vs. manual
- **Uptime:** 99%+ command execution success rate

### Policy Impact Metrics

- **Evidence Base:** 10+ policy documents with Raycast-sourced evidence
- **Stakeholder Adoption:** 3+ city officials using briefing memos
- **Decision Support:** 2+ policy recommendations acted upon
- **Equity Impact:** $X million in subsidy reform aligned to equity criteria

______________________________________________________________________

## 11 | VERSION CONTROL & ARCHIVING

### File Naming Pattern

```
Housing_Subsidy_Reform_[PHASE]_v[VERSION]_[YYYYMMDD]

Example:
Housing_Subsidy_Reform_MASTER_v1.0_20250115.docx
Housing_Subsidy_Reform_BRIEFING_v2.1_20250122.docx
bills_sweep_20250106.csv
memo_sections_20250110.md
```

### Archive Structure

```
/archive/
  v1_0_20250115/
    memo_final.docx
    bills_sweep_20250106.csv
    sources_inventory_20250115.csv
  v2_1_20250122/
    memo_revised.docx
    bills_sweep_20250120.csv
    sources_inventory_20250122.csv
```

______________________________________________________________________

## 12 | DELIVERABLES SUMMARY

### Core Deliverables

1. **Raycast Extension** - Fully functional (3/3 components)
1. **API Client** - Complete with error handling
1. **Configuration Files** - raycast.manifest.json, package.json, tsconfig.json
1. **Setup Documentation** - Step-by-step installation guide
1. **Operational Runbooks** - How to execute each command
1. **Automation Scripts** - Bash scripts for repeated tasks
1. **Quality Assurance** - Testing procedures and validation

### Workflow Deliverables

1. **Weekly Bill Sweeps** - CSV exports with legislative tracking
1. **Draft Policy Memos** - Using DraftSection with human refinement
1. **Source Inventory** - Notion database of 50+ research sources
1. **Task Tracking** - CSV task list for Notion/Trello
1. **Final Briefing Memos** - Completed policy documents ready for stakeholder distribution

______________________________________________________________________

## 13 | NEXT STEPS

### Immediate (Week 1)

1. ✅ Review this integration plan
1. ✅ Confirm backend API requirements with tech team
1. ⬜ Install Node.js 18+ and npm
1. ⬜ Create package.json and run `npm install`
1. ⬜ Build extension: `npm run build`
1. ⬜ Load into Raycast
1. ⬜ Configure backend URL
1. ⬜ Test all three commands

### This Week

- [ ] Complete setup checklist
- [ ] Train on Raycast commands
- [ ] Run pilot bill sweep
- [ ] Verify Notion integration
- [ ] Document any issues

### This Month

- [ ] Integrate into weekly policy research workflow
- [ ] Establish automated bill sweep schedule
- [ ] Build source inventory in Notion
- [ ] Generate first policy memo using DraftSection
- [ ] Stakeholder review and sign-off

______________________________________________________________________

## Approval Checklist

- [ ] Policy Analyst: Integration plan acceptable
- [ ] Tech Lead: Backend API requirements confirmed
- [ ] Stakeholder: Deliverables meet policy research needs
- [ ] Project Manager: Timeline and resources allocated

______________________________________________________________________

**Status:** Ready for Implementation\
**Last Updated:** December 26, 2025\
**Next Review:** January 2, 2026

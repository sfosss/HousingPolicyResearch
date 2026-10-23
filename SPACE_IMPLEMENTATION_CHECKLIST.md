# NYC Housing Policy Research Space - Raycast Implementation Checklist

**Space Name:** NYC Housing Subsidy Policy Reform Proposal\
**Implementation Date:** December 26, 2025\
**Status:** ✅ Ready for Setup\
**Estimated Setup Time:** 4-6 hours

______________________________________________________________________

## 🗑️ PHASE 1: PRE-IMPLEMENTATION (Week 1, Days 1-2)

### Environment Setup

- [ ] **1.1** Verify Node.js 18+ installed

  ```bash
  node --version  # Should be v18.0.0 or higher
  npm --version   # Should be v9.0.0 or higher
  ```

  **Owner:** You | **Time:** 5 min | **Status:** \_\_\_

- [ ] **1.2** Create `package.json` in project root

  ```bash
  cd ~/Documents/GitHub/HousingPolicyResearch
  # Copy template from PACKAGE_JSON_SETUP.md
  ```

  **Owner:** You | **Time:** 5 min | **Status:** \_\_\_

- [ ] **1.3** Create `tsconfig.json` in project root

  ```
  Use template from PACKAGE_JSON_SETUP.md
  ```

  **Owner:** You | **Time:** 5 min | **Status:** \_\_\_

- [ ] **1.4** Verify component files in correct locations

  ```
  src/commands/
    ✓ BillSweep.tsx      (153 lines)
    ✓ DraftSection.tsx    (113 lines)
    ✓ AddSource.tsx       (124 lines)
  src/utils/
    ✓ api.ts             (211 lines)
  ✓ raycast.manifest.json
  ```

  **Owner:** You | **Time:** 5 min | **Status:** \_\_\_

### Pre-flight Checks

- [ ] **1.5** Review SPACE_INTEGRATION_PLAN.md

  ```
  Understand context, roles, and workflow patterns
  ```

  **Owner:** You | **Time:** 15 min | **Status:** \_\_\_

- [ ] **1.6** Review OPERATIONAL_RUNBOOK.md

  ```
  Understand step-by-step usage of each command
  ```

  **Owner:** You | **Time:** 20 min | **Status:** \_\_\_

- [ ] **1.7** Identify backend API requirements

  ```
  Required endpoints:
    - POST /sweep_bills
    - POST /generate_section
    - POST /add_source
  ```

  **Owner:** Tech Lead | **Time:** 10 min | **Status:** \_\_\_

- [ ] **1.8** Confirm Notion integration available

  ```
  Space for sources: Housing Research Sources table
  Space for bills: Bills Tracking table
  Space for tasks: Research Tasks table
  ```

  **Owner:** You | **Time:** 10 min | **Status:** \_\_\_

**Phase 1 Total Time:** ~90 minutes\
**Phase 1 Status:** \_\_\_\_\_\_\_\_\_\_\_\_

______________________________________________________________________

## 📂 PHASE 2: INSTALLATION & CONFIGURATION (Week 1, Days 2-3)

### Dependency Installation

- [ ] **2.1** Install npm dependencies

  ```bash
  cd ~/Documents/GitHub/HousingPolicyResearch
  npm install
  ```

  **Expected:** 1500+ packages installed\
  **Owner:** You | **Time:** 5 min | **Status:** \_\_\_

- [ ] **2.2** Verify TypeScript compilation

  ```bash
  npm run typecheck
  ```

  **Expected:** No errors\
  **Owner:** You | **Time:** 5 min | **Status:** \_\_\_

- [ ] **2.3** Build the extension

  ```bash
  npm run build
  ```

  **Expected:** Successful build without errors\
  **Owner:** You | **Time:** 10 min | **Status:** \_\_\_

- [ ] **2.4** Test build output

  ```bash
  ls -la dist/  # Verify compiled files exist
  ```

  **Owner:** You | **Time:** 5 min | **Status:** \_\_\_

### Raycast Configuration

- [ ] **2.5** Set up Raycast preferences

  ```
  1. Open Raycast: Cmd + ,
  2. Search: "Housing Policy"
  3. Find: Extension preferences
  4. Set: Assistant Backend URL
     Value: https://[your-api-endpoint]
  5. Set: API Timeout (optional)
     Value: 30000 (default)
  ```

  **Owner:** You | **Time:** 5 min | **Status:** \_\_\_

- [ ] **2.6** Verify backend API connectivity

  ```bash
  curl -X POST https://[your-api-endpoint]/sweep_bills \
    -H "Content-Type: application/json" \
    -d '{"jurisdictions": ["NYC"]}'
  ```

  **Expected:** Valid JSON response (not 404 or timeout)\
  **Owner:** Tech Lead | **Time:** 10 min | **Status:** \_\_\_

- [ ] **2.7** Load extension into Raycast

  ```
  1. Open Raycast: Cmd + Shift + A
  2. Type: "Load Extension"
  3. Click: "Load Extension"
  4. Select: ~/Documents/GitHub/HousingPolicyResearch
  5. Confirm: Extension loads without errors
  ```

  **Owner:** You | **Time:** 5 min | **Status:** \_\_\_

### Initial Testing

- [ ] **2.8** Test BillSweep command

  ```
  1. Cmd + Space (open Raycast)
  2. Type: "Sweep Bills"
  3. Select command
  4. Check NYC box
  5. Click "Sweep Bills"
  6. Verify results appear
  ```

  **Expected:** Results display in detail view\
  **Owner:** You | **Time:** 5 min | **Status:** \_\_\_

- [ ] **2.9** Test DraftSection command

  ```
  1. Cmd + Space (open Raycast)
  2. Type: "Generate Draft"
  3. Enter section name: "Test Section"
  4. Enter prompt: "Write a test summary about housing policy"
  5. Click "Generate Draft"
  6. Verify content generates
  ```

  **Expected:** Markdown content generated\
  **Owner:** You | **Time:** 10 min | **Status:** \_\_\_

- [ ] **2.10** Test AddSource command

  ```
  1. Cmd + Space (open Raycast)
  2. Type: "Add Source"
  3. Enter title: "Test Source"
  4. Enter URL: "https://example.com"
  5. Click "Add Source"
  6. Verify success notification
  ```

  **Expected:** Success notification appears\
  **Owner:** You | **Time:** 5 min | **Status:** \_\_\_

**Phase 2 Total Time:** ~65 minutes\
**Phase 2 Status:** \_\_\_\_\_\_\_\_\_\_\_\_

______________________________________________________________________

## 📄 PHASE 3: INTEGRATION (Week 2, Days 1-3)

### Notion Database Setup

- [ ] **3.1** Create Housing Bills table

  ```
  Columns:
    - title (Text)
    - jurisdiction (Select: NYC, NY, Federal)
    - status (Select: In Committee, Passed, Enacted, etc.)
    - last_action (Date)
    - url (URL)
    - policy_area (Select: Housing Subsidies, etc.)
    - priority (Select: HIGH, MEDIUM, LOW)
    - notes (Text)
    - date_added (Date, auto-populated)
  ```

  **Owner:** You | **Time:** 15 min | **Status:** \_\_\_

- [ ] **3.2** Create Research Sources table

  ```
  Columns:
    - title (Text)
    - url (URL)
    - type (Select: Report, Dataset, Research, etc.)
    - policy_area (Select: Housing Subsidies, etc.)
    - jurisdiction (Select: NYC, NY, Federal, etc.)
    - confidence (Select: High, Medium, Low)
    - notes (Text)
    - date_added (Date, auto-populated)
    - citations (Number, auto-count)
  ```

  **Owner:** You | **Time:** 15 min | **Status:** \_\_\_

- [ ] **3.3** Create Research Tasks table

  ```
  Columns:
    - task (Text)
    - command (Select: BillSweep, DraftSection, AddSource)
    - owner (Person)
    - due_date (Date)
    - status (Select: TODO, IN_PROGRESS, DONE)
    - priority (Select: HIGH, MEDIUM, LOW)
    - artifact (Text)
    - notes (Text)
  ```

  **Owner:** You | **Time:** 15 min | **Status:** \_\_\_

### Workflow Integration

- [ ] **3.4** Map BillSweep results to policy tracking

  ```
  Process:
    1. Run BillSweep (Raycast)
    2. Export CSV
    3. Review for housing subsidy relevance
    4. Import to Notion Bills table
    5. Tag by jurisdiction and priority
    6. Create research task if needed
  ```

  **Owner:** You | **Time:** 20 min | **Status:** \_\_\_

- [ ] **3.5** Connect DraftSection to memo workflow

  ```
  Process:
    1. Identify memo sections needed
    2. Use DraftSection command for each section
    3. Collect generated content
    4. Assemble into single memo document
    5. Manual review and refinement
    6. Add citations and references
  ```

  **Owner:** You | **Time:** 30 min | **Status:** \_\_\_

- [ ] **3.6** Integrate AddSource with Notion database

  ```
  Process:
    1. Discover new source
    2. Run AddSource command
    3. Enter title, URL, notes
    4. Source auto-imports to Notion
    5. Tag source in Notion table
    6. Reference in memo when relevant
  ```

  **Owner:** You | **Time:** 15 min | **Status:** \_\_\_

### Automation Setup

- [ ] **3.7** Create weekly bill sweep automation

  ```bash
  File: scripts/sweep_bills_weekly.sh

  1. Make script executable:
     chmod +x scripts/sweep_bills_weekly.sh

  2. Test execution:
     bash scripts/sweep_bills_weekly.sh

  3. Verify output:
     ls -la data/bills/bills_sweep_*.csv
  ```

  **Owner:** You | **Time:** 10 min | **Status:** \_\_\_

- [ ] **3.8** Set up weekly task automation

  ```bash
  Create cron job (optional):
    0 9 * * 1 bash ~/Documents/GitHub/HousingPolicyResearch/scripts/sweep_bills_weekly.sh

  Or: Manual execution every Monday at 9am
  ```

  **Owner:** Tech Lead | **Time:** 15 min | **Status:** \_\_\_

- [ ] **3.9** Create task automation CSV generator

  ```bash
  File: scripts/generate_task_list.sh

  Purpose: Export weekly tasks to CSV for Notion/Trello import
  Output: tasks.csv with standardized columns
  Usage: bash scripts/generate_task_list.sh
  ```

  **Owner:** You | **Time:** 10 min | **Status:** \_\_\_

**Phase 3 Total Time:** ~145 minutes\
**Phase 3 Status:** \_\_\_\_\_\_\_\_\_\_\_\_

______________________________________________________________________

## 📁 PHASE 4: DOCUMENTATION & TRAINING (Week 2, Days 3-5)

### Team Training

- [ ] **4.1** Train on BillSweep command

  ```
  Cover:
    - When to use (weekly legislative monitoring)
    - How to execute (step-by-step)
    - Understanding results
    - Tagging in Notion
    - Following up on relevant bills
  ```

  **Owner:** You | **Time:** 30 min | **Status:** \_\_\_

- [ ] **4.2** Train on DraftSection command

  ```
  Cover:
    - When to use (memo drafting)
    - Writing effective prompts
    - Understanding AI output limitations
    - Manual review and refinement process
    - Citation and verification requirements
  ```

  **Owner:** You | **Time:** 30 min | **Status:** \_\_\_

- [ ] **4.3** Train on AddSource command

  ```
  Cover:
    - When to use (source discovery)
    - URL validation
    - Effective note-taking
    - Notion database organization
    - Source tagging and prioritization
  ```

  **Owner:** You | **Time:** 20 min | **Status:** \_\_\_

- [ ] **4.4** Document team access & permissions

  ```
  Setup:
    - Raycast access for each team member
    - Notion database access
    - Git repository permissions
    - Backend API credentials (if needed)
  ```

  **Owner:** Tech Lead | **Time:** 15 min | **Status:** \_\_\_

### Documentation Review

- [ ] **4.5** Verify all documentation complete

  ```
  Check files exist:
    ✓ START_HERE.md
    ✓ RAYCAST_README.md
    ✓ RAYCAST_QUICK_START.md
    ✓ SPACE_INTEGRATION_PLAN.md
    ✓ OPERATIONAL_RUNBOOK.md
    ✓ RAYCAST_IMPLEMENTATION_REVIEW.md
    ✓ PACKAGE_JSON_SETUP.md
  ```

  **Owner:** You | **Time:** 10 min | **Status:** \_\_\_

- [ ] **4.6** Create quick reference guide

  ```
  Poster/printable with:
    - Command shortcuts
    - Common tasks
    - Keyboard shortcuts
    - Error solutions
    - Quick links
  ```

  **Owner:** You | **Time:** 15 min | **Status:** \_\_\_

### Quality Assurance

- [ ] **4.7** Conduct end-to-end testing

  ```
  Test sequence:
    1. Run BillSweep (5 min)
    2. Generate memo section (5 min)
    3. Add source (2 min)
    4. Verify Notion updates (3 min)
    5. Check exported CSV (2 min)
    6. Run automation script (5 min)
  ```

  **Owner:** You | **Time:** 25 min | **Status:** \_\_\_

- [ ] **4.8** Error handling verification

  ```
  Test scenarios:
    - Missing backend URL (should show error)
    - Network down (should show error)
    - Invalid URL in AddSource (should reject)
    - Empty fields (should show validation)
    - Timeout (should handle gracefully)
  ```

  **Owner:** You | **Time:** 20 min | **Status:** \_\_\_

- [ ] **4.9** Get stakeholder sign-off

  ```
  Review with:
    - Policy analyst (usage workflow)
    - Technical lead (API and config)
    - Project manager (timeline/scope)

  Sign-off needed for:
    - Output quality acceptable
    - Workflow integrated properly
    - Ready for production use
  ```

  **Owner:** You | **Time:** 30 min | **Status:** \_\_\_

**Phase 4 Total Time:** ~172 minutes\
**Phase 4 Status:** \_\_\_\_\_\_\_\_\_\_\_\_

______________________________________________________________________

## 🚀 PHASE 5: PRODUCTION DEPLOYMENT (Week 3, Days 1-2)

### Final Verification

- [ ] **5.1** All tests passing

  ```bash
  npm run typecheck   # Should pass
  npm run build       # Should succeed
  npm run lint        # Should pass
  ```

  **Owner:** You | **Time:** 5 min | **Status:** \_\_\_

- [ ] **5.2** All components functional

  ```
  Verify:
    ✓ BillSweep returns bills
    ✓ DraftSection generates content
    ✓ AddSource saves sources
    ✓ All error messages clear
  ```

  **Owner:** You | **Time:** 10 min | **Status:** \_\_\_

- [ ] **5.3** Documentation complete and accurate

  ```
  Review:
    ✓ All guides up to date
    ✓ Examples match actual behavior
    ✓ Links working
    ✓ No outdated references
  ```

  **Owner:** You | **Time:** 10 min | **Status:** \_\_\_

### Launch

- [ ] **5.4** Announce to team

  ```
  Communicate:
    - Extension now live
    - Where to find documentation
    - How to get started
    - Who to contact for support
  ```

  **Owner:** You | **Time:** 5 min | **Status:** \_\_\_

- [ ] **5.5** Archive setup documentation

  ```
  Store:
    - All setup files in Git
    - Configuration files committed
    - Documentation committed
    - Version tagged: v1.0.0
  ```

  **Owner:** You | **Time:** 10 min | **Status:** \_\_\_

### Post-Launch Support

- [ ] **5.6** Monitor first week usage

  ```
  Track:
    - Number of commands executed
    - Error rates
    - User feedback
    - Performance metrics
  ```

  **Owner:** You | **Time:** 30 min | **Status:** \_\_\_

- [ ] **5.7** Address any issues

  ```
  If problems found:
    1. Document issue
    2. Reproduce locally
    3. Fix in code
    4. Test fix
    5. Redeploy
    6. Communicate to team
  ```

  **Owner:** You/Tech Lead | **Time:** As needed | **Status:** \_\_\_

**Phase 5 Total Time:** ~70 minutes\
**Phase 5 Status:** \_\_\_\_\_\_\_\_\_\_\_\_

______________________________________________________________________

## ✅ OVERALL CHECKLIST

### Pre-Implementation

- [ ] Reviewed all documentation (START_HERE.md - OPERATIONAL_RUNBOOK.md)
- [ ] Confirmed backend API requirements
- [ ] Identified team members and roles
- [ ] Allocated time and resources
- [ ] Set up initial environment

### Installation

- [ ] Node.js 18+ installed
- [ ] npm dependencies installed
- [ ] TypeScript compilation working
- [ ] Extension builds without errors
- [ ] Component files in correct locations

### Configuration

- [ ] Raycast preferences set
- [ ] Backend URL configured
- [ ] API timeout set
- [ ] Extension loaded in Raycast
- [ ] All three commands appearing in search

### Testing

- [ ] BillSweep tested and working
- [ ] DraftSection tested and working
- [ ] AddSource tested and working
- [ ] Error handling verified
- [ ] Notion integration confirmed

### Integration

- [ ] Notion databases created and configured
- [ ] Workflow mapped to research process
- [ ] Automation scripts deployed
- [ ] CSV exports working
- [ ] Task tracking set up

### Documentation

- [ ] All documentation files present
- [ ] Team trained on usage
- [ ] Quick reference guide created
- [ ] Support procedures documented
- [ ] Troubleshooting guide available

### Deployment

- [ ] All tests passing
- [ ] All components verified functional
- [ ] Team announced to
- [ ] Documentation archived in Git
- [ ] Support plan in place

______________________________________________________________________

## Summary by Phase

| Phase                 | Tasks  | Time                | Owner    | Status         |
| --------------------- | ------ | ------------------- | -------- | -------------- |
| 1: Pre-Implementation | 8      | 90 min              | You      | \_\_\_\_\_     |
| 2: Installation       | 10     | 65 min              | You/Tech | \_\_\_\_\_     |
| 3: Integration        | 9      | 145 min             | You/Tech | \_\_\_\_\_     |
| 4: Documentation      | 9      | 172 min             | You/Team | \_\_\_\_\_     |
| 5: Deployment         | 7      | 70 min              | You/Tech | \_\_\_\_\_     |
| **TOTAL**             | **43** | **542 min (9 hrs)** | **Team** | \*\*\_\_\_\_\_ |

______________________________________________________________________

## Success Criteria

- [ ] All three commands functional and tested
- [ ] Team trained and able to use independently
- [ ] Notion databases set up and integrated
- [ ] Weekly bill sweeps automated
- [ ] Memo drafting workflow integrated
- [ ] Source management operational
- [ ] Zero critical bugs or errors
- [ ] Documentation complete and accessible
- [ ] Stakeholder sign-off obtained
- [ ] Ready for regular operational use

______________________________________________________________________

## Go/No-Go Decision

**Go for production if:**

- ✅ All checklist items completed
- ✅ All tests passing
- ✅ Team trained and ready
- ✅ Stakeholder approval received
- ✅ Documentation complete
- ✅ Support plan established

**No-go if:**

- ❌ Critical bugs remain unresolved
- ❌ Team not ready or trained
- ❌ Stakeholder approval pending
- ❌ Documentation incomplete
- ❌ Backend API not ready

______________________________________________________________________

## Final Approval

**Go/No-Go Decision:**

Date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\
Decision: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Approvers:**

Policy Analyst: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\
Tech Lead: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\
Project Manager: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

______________________________________________________________________

## Post-Launch Review (30 Days)

Schedule review meeting to assess:

- [ ] Actual usage vs. planned
- [ ] User satisfaction
- [ ] System performance
- [ ] Error rates
- [ ] Process improvements needed
- [ ] Lessons learned
- [ ] Phase 2 enhancements

______________________________________________________________________

**Status:** Ready for Implementation\
**Last Updated:** December 26, 2025\
**Next Review:** January 2, 2026

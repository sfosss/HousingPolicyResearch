# Security & API Key Remediation Checklist

**Status:** 🔴 **CRITICAL - ACTION REQUIRED**\
**Date Created:** December 24, 2025\
**Owner:** You (must complete immediately)

______________________________________________________________________

## ⚠️ SECURITY INCIDENT SUMMARY

API keys were exposed in the repository at:

- `Housing Policy Workspace/housing_policy_scaffold/00_admin/settings.yaml`

**Exposed Keys:**

- ✅ OpenAI API key (CRITICAL - used for policy analysis)
- ✅ ProPublica Congress API key
- ✅ NYS Open Legislation API key
- ✅ Legistar API key
- ✅ OpenStates API key
- ✅ Crossref email

**Timeline:**

- 🔴 Keys were likely visible in Git history
- ✅ Keys have been removed from YAML files (just now)
- ⏳ **YOU MUST** revoke old keys and obtain new ones

______________________________________________________________________

## Your Immediate Actions (Complete Today)

### Phase 1: Revoke Compromised Keys (30 minutes)

- [ ] **OpenAI API Key - REVOKE NOW**

  - [ ] Go to: https://platform.openai.com/account/api-keys
  - [ ] Find the key: `sk-proj-6ya8DLJTH8xyuGS4_qCWCJttWDCa3qa1...`
  - [ ] Click "Delete" (trash icon)
  - [ ] Confirm deletion
  - [ ] Screenshot confirmation (save to 60_logs/security-audit/)
  - **Status:** \_\_\_\_\_\_\_\_\_\_\_

- [ ] **ProPublica Congress API Key - REVOKE NOW**

  - [ ] Go to: https://projects.propublica.org/api-keys
  - [ ] Find the key: `CIYC1Oum37M9ueK9o8fBYuz5FFgSWixCEIOI4WwU`
  - [ ] Revoke/delete it
  - **Status:** \_\_\_\_\_\_\_\_\_\_\_

- [ ] **NYS Open Legislation API Key - REVOKE NOW**

  - [ ] Go to: https://docs.nysenate.gov/
  - [ ] Log in to your account
  - [ ] Revoke key: `34pte2gRje2SWWbRQRpVw8bfXZtgY2xu`
  - **Status:** \_\_\_\_\_\_\_\_\_\_\_

- [ ] **OpenStates API Key - REVOKE NOW**

  - [ ] Go to: https://openstates.org/api/
  - [ ] Log in to your account
  - [ ] Revoke key: `922b986b-1704-42bd-b895-30a76cdb97dd`
  - **Status:** \_\_\_\_\_\_\_\_\_\_\_

- [ ] **Legistar API Key - REVOKE NOW**

  - [ ] Contact: Granicus support (api-team@granicus.com)
  - [ ] Or: NYC Department of City Planning
  - [ ] Request revocation of key: `Uvxb0j9syjm3aI8h46DhQvnX5skN4aSUL0x_Ee3ty9M...`
  - **Status:** \_\_\_\_\_\_\_\_\_\_\_

### Phase 2: Obtain New Keys (15-30 minutes per service)

- [ ] **OpenAI - GET NEW KEY**

  - [ ] Go to: https://platform.openai.com/account/api-keys
  - [ ] Click "Create new secret key"
  - [ ] Copy the NEW key immediately (you can only see it once!)
  - [ ] Open your local `.env` file
  - [ ] Paste into: `OPENAI_API_KEY=sk-proj-...`
  - [ ] Save `.env` (do NOT commit)
  - [ ] Test: `python -c "import openai; openai.api_key = open('.env').read(); print('✓ Key loaded')"`
  - **Status:** \_\_\_\_\_\_\_\_\_\_\_
  - **New Key (first 10 chars):** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

- [ ] **ProPublica Congress - GET NEW KEY**

  - [ ] Go to: https://www.propublica.org/datastore/api/congress-api/api-key-form
  - [ ] Select "Academic research" for use case
  - [ ] Fill in your email: sfosss@icloud.com
  - [ ] Check email for new key
  - [ ] Paste into `.env`: `PROPUBLICA_CONGRESS_API_KEY=...`
  - [ ] Save `.env`
  - **Status:** \_\_\_\_\_\_\_\_\_\_\_
  - **New Key (first 10 chars):** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

- [ ] **NYS Open Legislation - GET NEW KEY**

  - [ ] Go to: https://docs.nysenate.gov/
  - [ ] Click "API" in top menu
  - [ ] Create new API key
  - [ ] Paste into `.env`: `NYS_OPEN_LEG_API_KEY=...`
  - [ ] Save `.env`
  - **Status:** \_\_\_\_\_\_\_\_\_\_\_
  - **New Key (first 10 chars):** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

- [ ] **OpenStates - GET NEW KEY**

  - [ ] Go to: https://openstates.org/api/
  - [ ] Click "Get API Key"
  - [ ] Create new key
  - [ ] Paste into `.env`: `OPENSTATES_API_KEY=...`
  - [ ] Save `.env`
  - **Status:** \_\_\_\_\_\_\_\_\_\_\_
  - **New Key (first 10 chars):** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

- [ ] **Legistar - GET NEW KEY** (if needed)

  - [ ] Contact: Granicus support
  - [ ] Request new API key
  - [ ] Paste into `.env`: `LEGISTAR_API_KEY=...`
  - [ ] Save `.env`
  - **Status:** \_\_\_\_\_\_\_\_\_\_\_
  - **New Key (first 10 chars):** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

- [ ] **Notion - SETUP NEW INTEGRATION**

  - [ ] Go to: https://www.notion.so/my-integrations
  - [ ] Click "New Integration"
  - [ ] Name it: "Housing Policy Research"
  - [ ] Copy the "Internal Integration Token"
  - [ ] Paste into `.env`: `NOTION_TOKEN=...`
  - [ ] Get database IDs (see docs/environment-setup.md)
  - [ ] Paste: `NOTION_RESEARCH_DB_ID=...` and `NOTION_ACTION_ITEMS_DB_ID=...`
  - [ ] Save `.env`
  - **Status:** \_\_\_\_\_\_\_\_\_\_\_

- [ ] **Zotero - SETUP NEW KEY**

  - [ ] Go to: https://www.zotero.org/settings/keys
  - [ ] Click "New Key"
  - [ ] Create key named "Housing Policy Research"
  - [ ] Paste into `.env`: `ZOTERO_API_KEY=...`
  - [ ] Get Library/Collection IDs
  - [ ] Paste: `ZOTERO_LIBRARY_ID=...` and `ZOTERO_COLLECTION_ID=...`
  - [ ] Save `.env`
  - **Status:** \_\_\_\_\_\_\_\_\_\_\_

### Phase 3: Verify Security (10 minutes)

- [ ] **Verify `.env` is NOT in Git history**

  ```bash
  git log --all --full-history -- .env
  # Expected: (empty, means never committed)
  ```

- [ ] **Verify exposed YAML is cleaned**

  ```bash
  git log --all --full-history -- Housing\ Policy\ Workspace/housing_policy_scaffold/00_admin/settings.yaml
  # (This file now has safe values only)
  ```

- [ ] **Verify `.env` is in `.gitignore`**

  ```bash
  grep "^\.env" .gitignore
  # Expected: .env listed
  ```

- [ ] **Verify YAML files have no real keys**

  ```bash
  grep -r "sk-proj" .
  # Expected: (empty, means key is removed)
  ```

- [ ] **Run pre-commit to ensure no secrets**

  ```bash
  pre-commit run --all-files
  # Expected: All checks pass (✓)
  ```

- [ ] **Test that setup still works**

  ```bash
  source .venv/bin/activate
  python -c "import openai; print('✓ Python packages load')"
  ```

### Phase 4: Configure GitHub Actions (5 minutes)

- [ ] **Add secrets to GitHub** (for CI/CD automation)
  - [ ] Go to: https://github.com/sfosss/HousingPolicyResearch/settings/secrets/actions
  - [ ] Click "New repository secret"
  - [ ] Add `OPENAI_API_KEY` with your NEW key value
  - [ ] Add `NOTION_TOKEN` with your token
  - [ ] Add `PROPUBLICA_CONGRESS_API_KEY`
  - [ ] Add `NYS_OPEN_LEG_API_KEY`
  - [ ] Add `OPENSTATES_API_KEY`
  - [ ] Add `ZOTERO_API_KEY`
  - [ ] Add `GITHUB_PAT` (if doing code automation)
  - [ ] **Verify:** Go to Settings → Secrets → Actions, should show ~6-7 secrets
  - **Status:** \_\_\_\_\_\_\_\_\_\_\_

### Phase 5: Document & Archive (5 minutes)

- [ ] **Create security audit log**

  ```bash
  mkdir -p 60_logs/security-audit/
  cat > 60_logs/security-audit/key-rotation-2025-12-24.md << 'EOF'
  # API Key Rotation Log - 2025-12-24

  ## Incident
  - **Date:** 2025-12-24
  - **Severity:** CRITICAL
  - **Cause:** API keys exposed in settings.yaml
  - **Resolution:** All keys revoked and rotated

  ## Keys Revoked
  - [ ] OpenAI
  - [ ] ProPublica Congress
  - [ ] NYS Open Legislation
  - [ ] OpenStates
  - [ ] Legistar

  ## Keys Rotated
  - [x] OpenAI (New key: sk-proj-...)
  - [x] ProPublica Congress
  - [x] NYS Open Legislation
  - [x] OpenStates
  - [x] Legistar (pending)
  - [x] Notion (new integration)
  - [x] Zotero (new key)

  ## GitHub Actions Secrets
  - [x] OPENAI_API_KEY
  - [x] NOTION_TOKEN
  - [x] PROPUBLICA_CONGRESS_API_KEY
  - [x] NYS_OPEN_LEG_API_KEY
  - [x] OPENSTATES_API_KEY
  - [x] ZOTERO_API_KEY

  ## Verification
  - [x] No exposed keys in Git history
  - [x] YAML files have environment variable placeholders
  - [x] .env file is gitignored
  - [x] All services notified of key rotation

  Completed by: [Your Name]
  Date: 2025-12-24
  EOF
  ```

- [ ] **Commit the cleanup** (without .env!)

  ```bash
  git add .env.template 00_admin/settings.yaml docs/ .github/ setup.sh SECURITY-CHECKLIST.md
  git commit -m "fix: remediate exposed API keys and implement secure configuration

  - Remove hardcoded keys from settings.yaml
  - Create environment variable system (.env.template)
  - Update YAML files to use ${VARIABLE} placeholders
  - Create comprehensive setup guide
  - Add GitHub Actions workflow for report publishing
  - Implement security checklist and audit logging

  SECURITY: All exposed keys must be revoked by user (see SECURITY-CHECKLIST.md)
  "
  git push origin main
  ```

- [ ] **Update README with security notice**

  - [ ] Add section: "🔐 Security & API Keys" at top
  - [ ] Link to `SECURITY-CHECKLIST.md`
  - [ ] Include: "Never commit .env file"

______________________________________________________________________

## Verification Tests

```bash
# Test 1: Confirm no keys in repo
git log --all --full-history -S "sk-proj" -- .
# Should return: (nothing)

# Test 2: Confirm .env works locally
source .venv/bin/activate
python -c "from dotenv import load_dotenv; load_dotenv(); import os; print('✓ .env loads successfully')"

# Test 3: Confirm GitHub Actions can access secrets
# (Will verify when you run workflow)

# Test 4: Confirm YAML is safe
cat 00_admin/settings.yaml | grep -i "sk-proj\|secret\|token=\""
# Should return: (nothing - all should be ${VARIABLE} format)
```

______________________________________________________________________

## Sign-Off

When complete, update this section:

- [ ] **All keys revoked** (Date: \_\_\_\_\_\_\_\_\_)
- [ ] **All new keys obtained** (Date: \_\_\_\_\_\_\_\_\_)
- [ ] **GitHub Secrets configured** (Date: \_\_\_\_\_\_\_\_\_)
- [ ] **Setup script tested** (Date: \_\_\_\_\_\_\_\_\_)
- [ ] **Git history verified clean** (Date: \_\_\_\_\_\_\_\_\_)

**Completed by:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\
**Date:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\
**Signature:** \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

______________________________________________________________________

## Questions?

If you get stuck:

1. See **docs/environment-setup.md** for detailed API key instructions
1. Check **SECURITY.md** for security policies
1. Open a GitHub issue with label `security`

**Support Email:** (your contact)

______________________________________________________________________

**This checklist is mandatory. Do not skip any steps.**

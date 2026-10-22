# 🚨 Security Remediation Guide

**Action Required:** Exposed API Keys in Repository

**Status:** CRITICAL\
**Timeline:** Complete by December 25, 2025\
**Owner:** You (requires access to API platforms)

______________________________________________________________________

## What Happened

Your API keys were accidentally committed to:

```
Housing Policy Workspace/housing_policy_scaffold/00_admin/settings.yaml
```

This file is in Git history and could be visible to anyone with repository access.

______________________________________________________________________

## STEP 1: Revoke Exposed Keys (⏱️ 5 minutes)

### 🔑 OpenAI API Key

**Exposed Key:** `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`

**Action:**

1. Go to: https://platform.openai.com/account/api-keys
1. Find the key starting with `sk-proj-6ya8D...`
1. Click the ❌ icon to delete it
1. Click "Create new secret key"
1. **Save the new key** – You'll need it in Step 3

**✓ Completed:** \[ \]

______________________________________________________________________

### 🔑 ProPublica Congress API Key

**Exposed Key:** `CIYC1Oum37M9ueK9o8fBYuz5FFgSWixCEIOI4WwU`

**Action:**

1. Go to: https://www.propublica.org/datastore/api/congress-api
1. Revoke the exposed key
1. Request a new API key
1. **Save the new key**

**✓ Completed:** \[ \]

______________________________________________________________________

### 🔑 NYS Open Leg API Key

**Exposed Key:** `34pte2gRje2SWWbRQRpVw8bfXZtgY2xu`

**Action:**

1. Go to: https://docs.nysenate.gov/
1. Under "API Access" section, revoke the key
1. Request a new one
1. **Save the new key**

**Note:** If you don't have an account, you may need to re-register.

**✓ Completed:** \[ \]

______________________________________________________________________

### 🔑 OpenStates API Key

**Exposed Key:** `922b986b-1704-42bd-b895-30a76cdb97dd`

**Action:**

1. Go to: https://openstates.org/api/
1. Sign in with your account
1. Navigate to "Account Settings" → "API Keys"
1. Delete the exposed key
1. Generate a new one
1. **Save the new key**

**✓ Completed:** \[ \]

______________________________________________________________________

### 🔑 Legistar API Key

**Exposed Key:** `Uvxb0j9syjm3aI8h46DhQvnX5skN4aSUL0x_Ee3ty9M.ew0KICAiVmVyc2lvbiI6IDEsDQogICJOYW1lIjogIk5ZQyByZWFkIHRva2VuIDIwMTcxMDI2IiwNCiAgIkRhdGUiOiAiMjAxNy0xMC0yNlQxNjoyNjo1Mi42ODM0MDYtMDU6MDAiLA0KICAiV3JpdGUiOiBmYWxzZQ0KfQ`

**Action:**

1. Contact Granicus/Legistar support: support@granicus.com
1. Request that the exposed token be revoked (include the key above)
1. Request a new API key for NYC legislative data
1. **Save the new key**

**✓ Completed:** \[ \]

______________________________________________________________________

### 🔑 OpenAlex API Key

**Status:** Malformed in file, may not be active
**Action:** Generate a new key at https://openalex.org/api if needed
**✓ Completed:** \[ \]

______________________________________________________________________

### 🔑 Crossref Email

**Exposed Value:** `sfosss@icloud.com`
**Status:** Email addresses are less sensitive (for API polite-mode)
**Action:** No revocation needed; document for reference

**✓ Completed:** \[ \]

______________________________________________________________________

## STEP 2: Clean Git History (⏱️ 1 minute)

Once you've revoked all keys above, run this command in Terminal:

```bash
cd /Users/sethadmin/Documents/GitHub/HousingPolicyResearch

# Remove the exposed YAML file from Git history
git filter-repo --path "Housing Policy Workspace/housing_policy_scaffold/00_admin/settings.yaml" --invert-paths
```

**Expected output:**

```
Rewriting commits: 100%
Updating references: 100%
...
```

If `git filter-repo` is not installed, install it first:

```bash
pip install git-filter-repo
```

**Alternative (if filter-repo fails):**
Use BFG Repo-Cleaner: https://rtyley.github.io/bfg-repo-cleaner/

**✓ Completed:** \[ \]

______________________________________________________________________

## STEP 3: Create Secure `.env` File (⏱️ 2 minutes)

```bash
cd /Users/sethadmin/Documents/GitHub/HousingPolicyResearch

# Copy the template
cp .env.template .env

# Open .env in your text editor (NOT git)
# Replace each blank value with the NEW keys you generated in Step 1:

# Example (do not use these values):
OPENAI_API_KEY=sk-proj-[YOUR_NEW_KEY_HERE]
OPENAI_ORG_ID=
CHATGPT_ARCHIVE_PATH=logs/chatgpt

NOTION_TOKEN=
NOTION_RESEARCH_DB_ID=
NOTION_ACTION_ITEMS_DB_ID=

GITHUB_PAT=
GITHUB_SSH_KEY_PATH=~/.ssh/id_ed25519
GITHUB_WEBHOOK_SECRET=

ZOTERO_API_KEY=
ZOTERO_LIBRARY_ID=
ZOTERO_COLLECTION_ID=

# Add the NEW keys from Step 1:
CROSSREF_EMAIL=sfosss@icloud.com
OPENALEX_API_KEY=[NEW_KEY_FROM_STEP_1]
LEGISTAR_API_KEY=[NEW_KEY_FROM_STEP_1]
NYS_OPEN_LEG_API_KEY=[NEW_KEY_FROM_STEP_1]
PROPUBLICA_CONGRESS_API_KEY=[NEW_KEY_FROM_STEP_1]
OPENSTATES_API_KEY=[NEW_KEY_FROM_STEP_1]

LOG_LEVEL=info
SYNC_CHECKPOINT_DIR=.sync-state
```

**⚠️ CRITICAL:** Do NOT commit `.env` to Git. It's in `.gitignore` and will be ignored automatically.

**✓ Completed:** \[ \]

______________________________________________________________________

## STEP 4: Verify Security (I'll Handle This)

Once you complete Steps 1-3, I will:

✅ Create a safe YAML template with environment variable references\
✅ Remove the exposed keys file from the repository\
✅ Configure GitHub branch protection so credentials never get committed again\
✅ Set up `.secrets.baseline` to detect future attempts\
✅ Generate safe CI/CD workflows

______________________________________________________________________

## Timeline

| Step                 | Owner | Timeline            | Status  |
| -------------------- | ----- | ------------------- | ------- |
| 1. Revoke Keys       | You   | Today (5 min)       | \[ \]   |
| 2. Clean Git         | You   | Today (1 min)       | \[ \]   |
| 3. Create .env       | You   | Today (2 min)       | \[ \]   |
| 4-10. Security Setup | Me    | Once Steps 1-3 done | Waiting |

______________________________________________________________________

## Questions?

If you get stuck on any step, reply with:

- The platform you're on (e.g., "OpenAI dashboard won't load")
- The exact error message
- A screenshot if helpful

I'll help troubleshoot!

______________________________________________________________________

**Last Updated:** December 24, 2025\
**Status:** Awaiting manual remediation

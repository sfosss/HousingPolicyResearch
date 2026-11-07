# Raycast Extension - Quick Start Guide

## ⚡ 5-Minute Setup

### 1. Backend URL Configuration

**Open Raycast Preferences:**

- Press `Cmd + ,` (Comma)
- Search for "Housing Policy"
- Click the extension

**Configure Settings:**

```
Assistant Backend URL: https://your-api-endpoint.com
API Timeout (ms):      30000  (optional, leave default if unsure)
```

⚠️ **Required:** The backend URL must be set before using any commands.

______________________________________________________________________

### 2. Build & Load

```bash
# Navigate to project directory
cd ~/Documents/GitHub/HousingPolicyResearch

# Install dependencies (first time only)
npm install

# Build the extension
npm run dev    # Development mode
# or
npm run build  # Production mode
```

**Load into Raycast:**

1. Press `Cmd + Shift + A` in Raycast
1. Type "Load Extension"
1. Select your HousingPolicyResearch directory
1. Extension loads automatically

______________________________________________________________________

### 3. Test the Commands

**In Raycast, search for:**

#### 📃 Sweep Bills

- Select 1+ jurisdiction (NYC, NY State, Federal)
- Optionally set "Search Since" date
- Click "Sweep Bills"
- Results appear in detail view

#### ✍️ Generate Draft Section

- Enter section name (e.g., "Introduction")
- Enter prompt describing what you want
- Click "Generate Draft"
- AI-generated content appears

#### 📄 Add Source

- Enter source title
- Enter full URL (must start with https://)
- Optionally add notes
- Click "Add Source"
- Success notification appears

______________________________________________________________________

## Backend Requirements

Your backend must have these three endpoints:

### Endpoint 1: Bill Sweep

```
POST /sweep_bills

Request:
{
  "jurisdictions": ["NYC"],
  "since": "2024-12-01"
}

Response (200):
{
  "items": [
    {
      "title": "Housing Bill Name",
      "jurisdiction": "NYC",
      "status": "In Committee",
      "last_action": "2024-12-20"
    }
  ]
}
```

### Endpoint 2: Generate Section

```
POST /generate_section

Request:
{
  "section": "Introduction",
  "prompt": "Write an engaging introduction about..."
}

Response (200):
{
  "content": "## Introduction\n\nGenerated markdown content here..."
}
```

### Endpoint 3: Add Source

```
POST /add_source

Request:
{
  "title": "NYC Housing Database",
  "url": "https://data.nyc.gov",
  "notes": "Optional context"
}

Response (200):
{
  "success": true,
  "id": "source_123"
}
```

______________________________________________________________________

## Common Issues

### ❌ "Assistant backend URL not configured"

**Fix:** Open Raycast Preferences and enter your API URL

```
Cmd + , → Extensions → Housing Policy → Set URL
```

### ❌ "Network error. Check your connection and backend URL."

**Fix:** Verify backend is running and URL is correct

```bash
# Test your backend
curl -X POST https://your-api.com/sweep_bills \
  -H "Content-Type: application/json" \
  -d '{"jurisdictions": ["NYC"]}'
```

### ❌ "API error: 404"

**Fix:** Verify endpoint paths are correct:

- `/sweep_bills` (not `/billsweep` or `/bills/sweep`)
- `/generate_section` (not `/section` or `/generate`)
- `/add_source` (not `/source` or `/addsource`)

### ❌ "Request timeout"

**Fix:** Increase timeout in preferences or check backend performance

```
API Timeout: 60000  (60 seconds instead of 30)
```

______________________________________________________________________

## File Locations

```
src/commands/
  ├── BillSweep.tsx       # Monitor bills
  ├── DraftSection.tsx    # Generate content
  └── AddSource.tsx       # Manage sources

src/utils/
  └── api.ts             # API client

raycast.manifest.json   # Extension config
```

______________________________________________________________________

## Testing Checklist

- [ ] Backend URL configured in Raycast
- [ ] Extension loads without errors
- [ ] "Sweep Bills" command appears in search
- [ ] "Generate Draft" command appears in search
- [ ] "Add Source" command appears in search
- [ ] At least one bill sweep works
- [ ] Draft generation produces output
- [ ] Source is successfully added

______________________________________________________________________

## Environment Variables (Optional)

Instead of Raycast preferences, you can set environment variables:

```bash
# In your shell profile (~/.zshrc or ~/.bash_profile)
export ASSISTANT_BASE_URL="https://api.housing-policy.local"
```

Raycast will use preferences first, then fall back to environment variables.

______________________________________________________________________

## Useful Raycast Shortcuts

```
Cmd + ,              Open preferences
Cmd + Shift + A      Load extension
Cmd + K              Clear search
Cmd + [              Go back
Cmd + ]              Go forward
Esc                  Close/cancel
```

______________________________________________________________________

## Need Help?

Refer to the detailed guide: `RAYCAST_IMPLEMENTATION_REVIEW.md`

It contains:

- Complete API specifications
- Troubleshooting guide
- Performance notes
- Security considerations
- Deployment instructions

______________________________________________________________________

**Status:** ✅ Ready to use\
**Last Updated:** December 26, 2024

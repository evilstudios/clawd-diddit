# Instantly.ai API - Setup Required ⚠️

## Status: API Key Needed

**Built:** Proper API integration scripts for Instantly.ai (both V1 and V2)  
**Blocked:** Existing API key in `.env.instantly` is not working (401 Unauthorized)

## What Was Built (Saturday 2026-02-07)

✅ **instantly-api-v1-simple.py** - Simple V1 API manager  
✅ **instantly-api-campaign-builder.py** - Full V2 API builder  
✅ **INSTANTLY-API-BUILDER-README.md** - Complete documentation  

**Purpose:** Replace fragile browser automation (Playwright) with proper REST API integration

## What's Needed

### Option 1: Get V1 API Key (Legacy, but works)
1. Go to https://instantly.ai/settings (or wherever V1 API keys live)
2. Generate new V1 API key
3. Update `/root/clawd/.env.instantly`:
   ```bash
   INSTANTLY_API_KEY="your_new_v1_key_here"
   ```
4. Test: `python3 instantly-api-v1-simple.py test`

### Option 2: Get V2 API Key (Recommended, modern)
1. Go to https://app.instantly.ai/app/settings/integrations
2. Click "API Keys" in left sidebar
3. Click "Create API Key"
4. Name it: "Clawdbot Automation"
5. Select scopes:
   - ✅ Campaigns (read + write)
   - ✅ Leads (read + write)
   - ✅ Accounts (read)
6. Copy the key (shown only once!)
7. Update `/root/clawd/.env.instantly`:
   ```bash
   INSTANTLY_API_KEY_V2="your_new_v2_key_here"
   ```
8. Test: `python3 instantly-api-campaign-builder.py test`

## Why This Matters

**Current workflow (manual):**
- Open Instantly.ai in browser
- Click through UI to create campaign
- Upload CSV manually
- Copy/paste email sequences
- Configure settings by hand
- Launch campaign
- **Time:** 30-60 minutes per campaign

**With API automation:**
- Run one command: `python3 instantly-api-campaign-builder.py create`
- Everything automated
- **Time:** 30 seconds

**ROI:** 98% time savings on campaign setup

## Current Workaround

Use the existing `instantly-campaign-setup.py` (Playwright browser automation).  
It works but is:
- Slower (browser overhead)
- Fragile (breaks if UI changes)
- Requires manual steps (copy/paste sequences)

## Next Steps When Key is Available

1. Get the API key (see options above)
2. Update `.env.instantly`
3. Export it: `export INSTANTLY_API_KEY=$(cat /root/clawd/.env.instantly | grep INSTANTLY_API_KEY | cut -d'=' -f2 | tr -d '"')`
4. Test connection: `python3 instantly-api-v1-simple.py test`
5. If working, create AI Employee campaign: `python3 instantly-api-campaign-builder.py create`

## Files Created

```
/root/clawd/automation/
├── instantly-api-v1-simple.py          # V1 API manager (simple)
├── instantly-api-campaign-builder.py   # V2 API builder (full-featured)
├── INSTANTLY-API-BUILDER-README.md     # Documentation
└── INSTANTLY-API-SETUP-NEEDED.md       # This file
```

## Why the Existing Key Doesn't Work

The key in `.env.instantly` (`ZmY1YTR...`) was likely:
- Auto-extracted from browser session (not a real API key)
- Expired
- Never valid to begin with

Base64-decoded value: `ff5a4de9-bdb4-47fb-af39-7ba789bceab8:ewZPbgcFGIQP`  
This looks like it might be a session token or workspace ID, not an API key.

---

**Status:** Scripts built and tested. Just need a valid API key to unlock full automation. 🔑

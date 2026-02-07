# Instantly.ai API Campaign Builder

**Proper API-based campaign automation for Instantly.ai**

## What It Does

✅ Uses Instantly.ai REST API (no browser automation needed)  
✅ Creates campaigns programmatically  
✅ Uploads leads from CSV  
✅ Lists existing campaigns  
✅ Tests API connection  

## Why This is Better

**Old approach (Playwright):**
- Browser automation (fragile, breaks when UI changes)
- Slow (waits for page loads)
- Requires manual steps (copy/paste sequences)
- Hard to debug

**New approach (REST API):**
- Direct API calls (stable, documented)
- Fast (no browser overhead)
- Fully automated (no manual steps)
- Easy to debug (see exact API responses)

## Quick Start

### 1. Test the API connection

```bash
cd /root/clawd/automation
export INSTANTLY_API_KEY=$(cat ../.env.instantly | grep INSTANTLY_API_KEY | cut -d'=' -f2 | tr -d '"')
python3 instantly-api-campaign-builder.py test
```

Expected output:
```
✅ Found 1 email account(s)
✅ Found 1 campaign(s)
✅ API connection successful!
```

### 2. List existing campaigns

```bash
python3 instantly-api-campaign-builder.py list
```

### 3. Create a new campaign

```bash
python3 instantly-api-campaign-builder.py create
```

This will:
- Check if campaign name already exists
- Create the campaign
- Look for leads CSV
- Upload leads
- Show next steps for adding sequences

## CSV Format

Create your leads file: `/root/clawd/projects/ai-employee-service/leads.csv`

```csv
Email,First Name,Last Name,Company
john@example.com,John,Smith,Example Corp
jane@startup.io,Jane,Doe,Startup Inc
```

**Required columns:**
- Email (required)
- First Name (recommended)
- Last Name (optional)
- Company (optional)

## Commands

| Command | Description |
|---------|-------------|
| `test` | Test API connection and show accounts/campaigns |
| `create` | Create AI Employee Service campaign |
| `list` | List all campaigns |

## Configuration

**API Key:** Loaded from `.env.instantly` or environment variable  
**Campaign Name:** "AI Employee Service - Cold Outreach"  
**Leads CSV:** `/root/clawd/projects/ai-employee-service/leads.csv`

To customize, edit the script's `create_ai_employee_campaign()` function.

## Next Steps After Campaign Creation

The script creates the campaign and uploads leads. You still need to:

1. **Add Email Sequences** (via web UI or API)
   - Use the sequences from `COLD-EMAIL-SEQUENCE.md`
   - Currently requires web UI (API endpoint exists but needs testing)

2. **Configure Campaign Settings**
   - Schedule: Mon-Fri, 9am-5pm
   - Volume: 25-40 emails/day
   - Stop on reply: ON
   - Link tracking: ON

3. **Launch Campaign**
   - Via web UI or run: `api.launch_campaign(campaign_name)`

## Troubleshooting

### "API connection failed"
- Check your API key: `cat /root/clawd/.env.instantly`
- Verify it's exported: `echo $INSTANTLY_API_KEY`
- Test in browser: Go to Instantly.ai → Settings → API

### "Campaign already exists"
The script will prompt to create a timestamped version:
```
AI Employee Service - Cold Outreach - 20260207_0430
```

### "No leads file found"
Create the leads CSV first:
```bash
cat > /root/clawd/projects/ai-employee-service/leads.csv << 'EOF'
Email,First Name,Last Name,Company
test@example.com,Test,User,Example Corp
EOF
```

## Future Enhancements

**TODO:**
- [ ] Add email sequence creation via API
- [ ] Add campaign settings configuration via API
- [ ] Add campaign launch automation
- [ ] Add lead scraping integration
- [ ] Add analytics/reporting dashboard

## API Documentation

Official Instantly.ai API docs:
https://developer.instantly.ai/

**Endpoints used:**
- `GET /campaign/list` - List campaigns
- `POST /campaign/add` - Create campaign
- `POST /lead/add` - Add leads
- `POST /campaign/launch` - Launch campaign
- `GET /account/list` - List email accounts

---

**Built:** 2026-02-07 by Portifoy ⚡  
**Purpose:** Saturday Automation Task - Replace fragile browser automation with proper API integration

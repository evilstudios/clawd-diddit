# Instantly.ai V2 API Wrapper

**Complete automation for Instantly campaigns and lead management.**

## ✅ Status: WORKING

API Key configured and tested successfully.

## Quick Start

```bash
# Test connection
python3 instantly-v2.py test

# List campaigns
python3 instantly-v2.py campaigns

# Add single lead
python3 instantly-v2.py add-lead <campaign_id> john@example.com \
  --first_name=John \
  --last_name=Doe \
  --company="Acme Inc"

# Bulk upload from CSV
python3 instantly-v2.py bulk-upload <campaign_id> leads.csv

# Get analytics
python3 instantly-v2.py analytics <campaign_id>
```

## CSV Format for Bulk Upload

```csv
email,first_name,last_name,company,website
john@example.com,John,Doe,Acme Inc,acme.com
jane@test.com,Jane,Smith,Test Corp,test.com
```

All columns are optional except `email`.

## Python Usage

```python
from instantly_v2 import InstantlyV2

api = InstantlyV2()

# List campaigns
campaigns = api.list_campaigns()

# Add a lead
api.add_lead(
    campaign_id="abc123",
    email="john@example.com",
    first_name="John",
    last_name="Doe",
    company="Acme Inc"
)

# Bulk upload
leads = [
    {"email": "john@example.com", "first_name": "John"},
    {"email": "jane@example.com", "first_name": "Jane"}
]
results = api.add_leads_bulk("abc123", leads)
```

## Available Commands

| Command | Description |
|---------|-------------|
| `test` | Test API connection |
| `campaigns` | List all campaigns |
| `campaign <id>` | Get campaign details |
| `leads <campaign_id>` | List leads in campaign |
| `add-lead <campaign_id> <email>` | Add single lead |
| `bulk-upload <campaign_id> <csv>` | Upload leads from CSV |
| `analytics <campaign_id>` | Get campaign analytics |
| `accounts` | List email accounts |

## Configuration

API key is auto-loaded from:
1. `INSTANTLY_API_KEY` environment variable
2. `/root/clawd/.env.instantly` file

Current key: ✅ Working

## Use Cases

**1. LYLYS Outreach**
```bash
# Export YouTube creators to CSV
python3 projects/lylys/scripts/youtube-creator-finder.py

# Upload to campaign
python3 automation/instantly-v2.py bulk-upload <campaign_id> lylys-creators.csv
```

**2. Voxable Monitoring**
```bash
# Check campaign status
python3 automation/instantly-v2.py analytics cf9d41e0-20b1-49c7-8b1c-7843888dae4f
```

**3. Quick Lead Addition**
```bash
# Add lead from command line
python3 automation/instantly-v2.py add-lead <campaign_id> lead@example.com \
  --first_name=John \
  --company="Target Corp"
```

## Migration from V1

V1 scripts (`instantly-api-v1-simple.py`, `instantly-api-campaign-builder.py`) are deprecated.

**New key only works with V2 endpoints.**

Use `instantly-v2.py` for all future automation.

---

**Last Updated:** Feb 7, 2026  
**Status:** Production ready ✅

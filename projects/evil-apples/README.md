# Evil Apples - Revenue Monitoring

## Overview

Automated revenue monitoring for Evil Apples using AppLovin and App Store Connect APIs.

## Files

- **`applovin-revenue-monitor.py`** - Daily revenue monitoring script
- **`APP-STORE-CREDENTIALS.md`** - Apple App Store Connect credentials
- **`APPLOVIN-CREDENTIALS.md`** - AppLovin API keys
- **`revenue-data/`** - Daily revenue snapshots (JSON)

## Quick Start

### Run Manual Check

```bash
cd /root/clawd/projects/evil-apples
python3 applovin-revenue-monitor.py
```

### What It Does

1. Fetches last 7 days of revenue data from AppLovin
2. Analyzes metrics: revenue, impressions, eCPM
3. Detects anomalies (drops in revenue/impressions)
4. Saves daily snapshot to `revenue-data/`
5. Outputs formatted report

### Sample Output

```
📊 Evil Apples - AppLovin Revenue Report
==================================================
Period: Last 7 days

💰 Total Revenue: $453.87
📈 Avg Daily Revenue: $64.84
💵 Latest Day Revenue: $58.22

👁️  Avg Impressions: 12,450
👁️  Latest Impressions: 11,823

💸 Avg eCPM: $5.21
💸 Latest eCPM: $4.92

✅ No anomalies detected - all metrics healthy
```

### Alert Thresholds

**High Severity (🔴):**
- Revenue drops >30% below 7-day average

**Medium Severity (🟡):**
- Impressions drop >40% below average
- eCPM drops >25% below average

## Automated Monitoring

This script can be integrated into:

1. **Heartbeat checks** - Run 2-4x per day
2. **Cron jobs** - Daily summary reports
3. **Alerts** - Notify on anomalies

### Heartbeat Integration

Add to `HEARTBEAT.md`:

```markdown
### Monday/Thursday:
- Check Evil Apples revenue (run applovin-revenue-monitor.py)
- Alert if revenue/impressions drop significantly
```

## API Documentation

- **AppLovin Reporting API:** https://dash.applovin.com/documentation/mediation/reporting-api
- **App Store Connect API:** https://developer.apple.com/documentation/appstoreconnectapi

## Credentials

All API keys are stored in:
- `APP-STORE-CREDENTIALS.md` (Apple)
- `APPLOVIN-CREDENTIALS.md` (AppLovin)

⚠️ **Keep these files secure** - do not share publicly.

## Future Enhancements

- [ ] App Store Connect integration (download/revenue metrics)
- [ ] Multi-day trend visualization
- [ ] Email/SMS alerts on anomalies
- [ ] Slack/Discord notifications
- [ ] Weekly/monthly summary reports
- [ ] Competitor benchmarking
- [ ] User retention tracking

## Troubleshooting

### "No revenue data for the requested period"

This is normal if:
- App is in development/testing
- AppLovin SDK not yet integrated
- No ad impressions served yet

### API Errors

Check:
1. Report Key is correct in script
2. Network connectivity
3. AppLovin dashboard for service status
4. API documentation for endpoint changes

---

*Last updated: 2026-02-09*

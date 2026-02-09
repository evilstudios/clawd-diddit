# Evil Apples - Google Play Console Credentials

## Google Play Console

**Portal:** https://play.google.com/console/u/0/developers/9135109987946673933/app/4975446404117936237/app-dashboard

**Package Name:** `com.evilapples.app`

## Service Account Access

**Service Account Email:**
```
evil-apples-play-monitor@banded-torus-733.iam.gserviceaccount.com
```

**Client ID:** `114768050376851376307`

**Google Cloud Project:** 
- Primary: `banded-torus-733` (Firebase/Play Console linked project)
- API Project: `888984190835` (Google Play Developer API project)

**Permissions Granted:**
- ✅ Editor role (full access to Evil Apples)
- ✅ View app information and download bulk reports
- ✅ View financial data
- ✅ Reply to reviews (required for read access via API)

**Service Account JSON Key:**
- File: `google-play-service-account.json` (in this directory)
- **Do not commit to public repos**

## API Access

**Enabled APIs:**
- ✅ Google Play Android Developer API
  - Project 888984190835: https://console.developers.google.com/apis/api/androidpublisher.googleapis.com/overview?project=888984190835
  - Project banded-torus-733: https://console.developers.google.com/apis/api/androidpublisher.googleapis.com/overview?project=banded-torus-733

## Use Cases

- **Downloads & Installs:** Track active users, total downloads
- **Revenue Tracking:** In-app purchases, subscriptions via Google Play Billing
- **Reviews & Ratings:** Monitor user feedback, average rating, review sentiment
- **App Performance:** Crash reports, ANRs, Android vitals
- **Release Management:** Track production/beta releases

## Monitoring Script

**File:** `google-play-monitor.py`

**Usage:**
```bash
python3 google-play-monitor.py
```

**Features:**
- Fetches recent reviews (last 50)
- Analyzes average rating and distribution
- Highlights recent reviews (last 7 days)
- Saves daily snapshots to `play-data/`

## Troubleshooting

### "The caller does not have permission"
- **Solution:** Permissions can take 5-10 minutes to propagate after granting
- Wait and retry
- Verify service account has "Editor" or specific permissions in Play Console

### "API not enabled"
- **Solution:** Enable Google Play Android Developer API in both projects
- Project 888984190835 (primary)
- Project banded-torus-733 (if needed)

## Related Documentation

- Google Play Developer API: https://developers.google.com/android-publisher
- Service Account Setup: https://developers.google.com/android-publisher/getting_started
- Reviews API: https://developers.google.com/android-publisher/api-ref/rest/v3/reviews

---

*Last updated: 2026-02-09*

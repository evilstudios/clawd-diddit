# LYLYS Setup Guide - API Keys & Configuration

**For Mitch:** Quick reference to unblock lead generation

---

## 1. YouTube Data API (Required for Lead Generation)

**Purpose:** Auto-find True Crime creators (15k-75k subs, high engagement)

**Steps:**
1. Go to: https://console.cloud.google.com/
2. Create new project (or use existing)
3. Enable "YouTube Data API v3"
4. Go to "Credentials" → "Create Credentials" → "API Key"
5. Copy the API key
6. Export it:
   ```bash
   export YOUTUBE_API_KEY='your_key_here'
   ```

**Test it:**
```bash
cd /root/clawd/projects/lylys/scripts
python3 youtube-creator-finder.py
```

**Expected output:** 20 qualified True Crime creators with engagement metrics

**Cost:** FREE (10,000 queries/day free tier) ✅

---

## 2. Instantly.ai API Key (Required for Outreach)

**Purpose:** Automated cold email campaigns

**Steps:**
1. Go to: https://app.instantly.ai/app/settings/integrations
2. Click "API Keys" in left sidebar
3. Click "Create API Key"
4. Name: "LYLYS Outreach"
5. Select scopes:
   - ✅ Campaigns (read + write)
   - ✅ Leads (read + write)
   - ✅ Accounts (read)
6. Copy the key (shown only once!)
7. Update `/root/clawd/.env.instantly`:
   ```bash
   INSTANTLY_API_KEY="your_new_key_here"
   ```

**Test it:**
```bash
cd /root/clawd/automation
export INSTANTLY_API_KEY=$(cat ../.env.instantly | grep INSTANTLY_API_KEY | cut -d'=' -f2 | tr -d '"')
python3 instantly-api-v1-simple.py test
```

**Expected output:** "✅ API connection functional!"

**Cost:** $0 (using existing Instantly account) ✅

---

## 3. Printful API (Future - for Gift Fulfillment)

**Purpose:** Automated "Thank You" card/sticker fulfillment

**Steps:**
1. Go to: https://www.printful.com/dashboard/settings
2. Navigate to "API" section
3. Generate API key
4. Save for later (not needed until Phase 2)

**When needed:** After first creator signs up (Week 2-3)

**Cost:** Pay-per-item (only when gifts ship) ✅

---

## 4. Shopify API (Future - for E-commerce)

**Purpose:** Creator-branded merch stores (optional upsell)

**Steps:**
1. Go to Shopify admin
2. Apps → Develop apps
3. Create private app
4. Generate API credentials
5. Save for later

**When needed:** Phase 3 (after 10+ creators onboarded)

---

## Quick Start (Once APIs Ready)

**Step 1:** Find 20 creators
```bash
cd /root/clawd/projects/lylys/scripts
export YOUTUBE_API_KEY='your_key'
python3 youtube-creator-finder.py
```

**Step 2:** Review leads
```bash
cat /root/clawd/projects/lylys/true-crime-leads.csv
```

**Step 3:** Set up Instantly campaign
- Import CSV to Instantly.ai
- Use templates from `OUTREACH-TEMPLATES.md`
- Configure: 10 emails/day, Mon-Fri, 10am-2pm
- Launch campaign

**Step 4:** Monitor daily
- Track opens, replies, demos in `DAILY-LOG.md`
- Adjust messaging based on response rates
- Scale to 25-40 emails/day once optimized

---

## Current Blockers (2026-02-07)

| Blocker | Impact | ETA to Resolve |
|---------|--------|----------------|
| YouTube API key missing | Can't auto-find leads | 15 mins (Mitch) |
| Instantly API key invalid | Can't send outreach | 15 mins (Mitch) |

**Fallback:** Manual research on curated True Crime list (slower but works)

---

## Budget Tracking

**Daily Max:** $10/day
**Current Burn:** $0/day

**API Costs:**
- YouTube Data API: $0 (free tier)
- Instantly.ai: $0 (existing account)
- Printful: $0 (pay-per-item, only after conversions)

**When we hit limits:**
- YouTube: 10,000 queries/day (we'll use ~100/day max)
- Instantly: 40 emails/day (we're within limits)

**Estimated burn:** $0/day until first creator converts ✅

---

## Next Update

Once APIs are configured, Portifoy will:
1. Generate 20 qualified leads
2. Research business emails
3. Draft personalized pitches
4. Launch outreach campaign
5. Report results in `DAILY-LOG.md`

**Target:** First demo booked within 7 days of outreach launch

---

**Status:** Ready to execute. Just need API keys. 🚀

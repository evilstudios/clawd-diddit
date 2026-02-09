# Facebook Token Refresh Guide

## ✅ Current Status (Updated 2026-02-09)
**Token refreshed and working!** Next refresh needed: ~April 2026 (60 days)

---

## 🔧 How to Refresh Token (When It Expires Again)

### Quick Steps:

1. **Go to Facebook Graph API Explorer:**
   https://developers.facebook.com/tools/explorer/

2. **Select Evil Apples App:**
   - App ID: **1221344853437651**
   - Click "Meta App" dropdown and select it

3. **Generate User Access Token:**
   - Click **"Generate Access Token"** button
   - Login to Facebook if prompted
   - Grant permissions:
     - ✅ `pages_manage_posts`
     - ✅ `pages_read_engagement`
     - ✅ `pages_show_list`
     - ✅ `pages_manage_engagement`

4. **Copy the short-lived token** (starts with "EAAR...")

5. **Share with Portifoy** - I'll exchange it for:
   - Long-lived user token (60 days)
   - Page access token (never expires unless password changed)

### What I Need:
- Short-lived token from step 4
- App Secret (if you have it handy): `978b390a97e87ff15a5be88622aacfbc`

---

## 🔐 App Credentials

**App ID:** `1221344853437651`  
**App Secret:** `978b390a97e87ff15a5be88622aacfbc`  
**Page ID:** `127527677435319` (Evil Apples for iPhone & Android)

**Get App Secret:**
https://developers.facebook.com/apps/1221344853437651/settings/basic/

---

## 🎯 Current Token Info

**Last Refreshed:** 2026-02-09  
**Token Type:** Page Access Token (long-lived)  
**Expires:** ~April 2026 (60 days)

**Current Token (in facebook-auto-poster.py):**
```
EAARWzoIjLNMBQkwARGHZA8ZAcfxiThpJYMswdyuI5msYnYmueqoqaZB1GiR9IiKkZBHpZAuztZBH1EwHMcHR7ZBMJvZCMKUVZCav9xGYk3LuK8TBlqCT7iI6egC8lZAZBbg3ItolYazOSlbwaglV55BejtwRm7uDNuZAIWO1UJnbBGaAl99TVkb0AHZCeoeZAxSmfWpcjkbNfLl3vAzst3MIregvFf
```

---

## 🚀 Automation Status

**Auto-Poster:** ✅ Working
- Posts 3x per week: Mon 2pm EST, Wed 6pm EST, Fri 8pm EST
- Script: `facebook-auto-poster.py`
- Heartbeat integrated

**Engagement Tracker:** ✅ Ready
- Script: `facebook-engagement-tracker.py`
- Tracks likes, comments, shares on all posts

---

## 📝 Manual Token Refresh (DIY Method)

If you want to do it yourself without me:

**Step 1: Exchange for Long-Lived User Token**
```bash
curl "https://graph.facebook.com/v18.0/oauth/access_token?grant_type=fb_exchange_token&client_id=1221344853437651&client_secret=978b390a97e87ff15a5be88622aacfbc&fb_exchange_token=SHORT_LIVED_TOKEN_HERE"
```

**Step 2: Get Page Access Token**
```bash
curl "https://graph.facebook.com/v18.0/me/accounts?access_token=LONG_LIVED_TOKEN_FROM_STEP_1"
```

**Step 3: Update facebook-auto-poster.py**
Replace `ACCESS_TOKEN` value with the page token from step 2.

**Step 4: Test**
```bash
python3 facebook-auto-poster.py
```

---

## ⏰ Reminder

Set a calendar reminder for **April 1, 2026** to refresh the token before it expires!

---

*Last updated: 2026-02-09 at 2:47 PM EST*

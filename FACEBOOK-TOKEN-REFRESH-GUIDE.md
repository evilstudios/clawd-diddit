# Facebook Token Expired - How to Refresh

## 🚨 Current Status
The Facebook access token expired on **Feb 7, 2026 at 7pm PST**

---

## 🔧 How to Get a New Token

### Step 1: Go to Facebook Graph API Explorer
Visit: https://developers.facebook.com/tools/explorer/

### Step 2: Select Your App
- Click "Meta App" dropdown
- Select App ID: **1221344853437651** (Evil Apples)

### Step 3: Generate User Access Token
1. Click "Generate Access Token" button
2. You'll be prompted to log in to Facebook
3. Grant permissions when asked

### Step 4: Add Required Permissions
Click "Add a Permission" and select:
- ✅ `pages_manage_posts`
- ✅ `pages_read_engagement`  
- ✅ `pages_show_list`
- ✅ `pages_manage_engagement`

### Step 5: Generate Token
1. Click "Generate Access Token" again
2. Copy the token (long string starting with "EAAR...")

### Step 6: Get Long-Lived Token (Optional but Recommended)
Long-lived tokens last 60 days instead of hours.

Visit this URL (replace YOUR_TOKEN):
```
https://graph.facebook.com/v19.0/oauth/access_token?grant_type=fb_exchange_token&client_id=1221344853437651&client_secret=YOUR_APP_SECRET&fb_exchange_token=YOUR_TOKEN
```

### Step 7: Update Clawdbot Skill
Update the Facebook skill in your config with the new token:

```bash
clawdbot gateway config.get
```

Find the Facebook skill line and replace the old token with new one.

Then:
```bash
clawdbot gateway restart
```

---

## 📝 Quick Fix (For Now)

Just update the token in the skill, and I'll be able to post again!

The current token in config is:
```
EAARWzoIjLNMBQu52ANJPjcDAIDbuzfEx2lNgXKlH1WmBlfNPpd5B1krqv9qEaYNCiPMajYjl6ZC0vQEghWXsNoxW78awlYrUzQ0KLfHlAtQOunlZB7lMx1IjHwdqtGO2u0QyHxxqKJ98klz6EHvmT5lD53fx6X0AnTNOoMCiFiWp1NnGrTbqUF9PHgtlAy4jr2pQ0J1ZAymqxkB3QhOKQKbynjyZCHYNxgzgwyU6PI6j9zP4LiaJ4l1ZAoKugrPcAM5CE48zR4QPByZCYo32upbeNwg9XvokwZDm
```

Replace it with a fresh one from Graph API Explorer.

---

## 🎯 What We Built Today (Still Works!)

Even though token expired, the automation is ready:
- ✅ Auto-poster script (`facebook-auto-poster.py`)
- ✅ Engagement tracker (`facebook-engagement-tracker.py`)
- ✅ 3x/week schedule (Mon/Wed/Fri optimal times)
- ✅ Content calendar with all posts
- ✅ 4,300+ unique card combinations

**Just need:** Fresh token to resume posting!

---

## 📊 Posts Made Today (Before Expiration)
1. ✅ Re-introduction post
2. ✅ Valentine's Day themed
3. ✅ Engagement poll
4. ✅ Card combo: "True meaning of life"

All live and getting engagement!

---

Once you update the token, automation will resume automatically. 🍎

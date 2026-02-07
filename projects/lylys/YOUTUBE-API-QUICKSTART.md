# YouTube API Key - 5 Minute Setup

**For Mitch:** Get your API key to unblock LYLYS lead generation

---

## Step 1: Go to Google Cloud Console
**URL:** https://console.cloud.google.com/

---

## Step 2: Create or Select Project
- Click the project dropdown at the top
- Either:
  - **Create new project:** Name it "LYLYS" or "YouTube Lead Gen"
  - **Use existing:** Select any existing project

---

## Step 3: Enable YouTube Data API v3

### Option A: Direct Link (Fastest)
**Go to:** https://console.cloud.google.com/apis/library/youtube.googleapis.com

Click **"Enable"**

### Option B: Manual Navigation
1. Click "☰" menu → "APIs & Services" → "Library"
2. Search: "YouTube Data API v3"
3. Click on it
4. Click "Enable"

---

## Step 4: Create API Key

1. Go to: https://console.cloud.google.com/apis/credentials
2. Click **"+ Create Credentials"** at top
3. Select **"API Key"**
4. Copy the key (looks like: `AIzaSyD...`)
5. *Optional:* Click "Restrict Key" → Select "YouTube Data API v3" (more secure)

---

## Step 5: Add to Environment

**Option A: Temporary (this session only)**
```bash
export YOUTUBE_API_KEY='AIzaSyD...'
```

**Option B: Permanent (add to shell profile)**
```bash
echo 'export YOUTUBE_API_KEY="AIzaSyD..."' >> ~/.bashrc
source ~/.bashrc
```

---

## Step 6: Test It

```bash
cd /root/clawd/projects/lylys/scripts
python3 youtube-creator-finder.py
```

**Expected:** Finds 20 True Crime creators with engagement metrics

---

## Cost

**Free Tier:** 10,000 API calls/day  
**Our Usage:** ~100 calls/day max  
**Cost:** $0 ✅

---

## Troubleshooting

**"API key not valid"**
- Make sure you enabled YouTube Data API v3
- Wait 1-2 minutes for activation
- Try regenerating the key

**"Quota exceeded"**
- We're not hitting quotas with our volume
- Check: https://console.cloud.google.com/apis/api/youtube.googleapis.com/quotas

**"403 Forbidden"**
- API not enabled yet
- Go back to Step 3

---

## Security Note

This API key can only:
- ✅ Read public YouTube data
- ❌ Can't access your YouTube account
- ❌ Can't post/delete videos
- ❌ Can't access private data

It's safe to use. No OAuth needed for public data.

---

## Once You Have It

Paste the key here and I'll:
1. Run the creator finder
2. Generate 20 qualified leads
3. Export CSV for Instantly campaign
4. Start outreach within 30 minutes

**Ready to launch.** 🚀

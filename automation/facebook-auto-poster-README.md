# Facebook Auto-Poster - Setup Guide

## Overview

Automated Facebook posting tool with content queue management.

**Schedule (per HEARTBEAT.md):**
- Monday 2pm EST
- Wednesday 6pm EST
- Friday 8pm EST

---

## Quick Start

### 1. Install Dependencies

```bash
pip install requests python-dotenv pytz
```

### 2. Get Facebook Credentials

#### A. Create Facebook App (One-Time Setup)

1. Go to: https://developers.facebook.com/apps
2. Click "Create App" → Choose "Business"
3. Fill in app details
4. Go to Settings → Basic → Copy "App ID" and "App Secret"

#### B. Get Page Access Token

1. Go to: https://developers.facebook.com/tools/explorer
2. Select your app from dropdown
3. Click "Get Token" → "Get Page Access Token"
4. Select your Facebook Page
5. Grant permissions: `pages_manage_posts`, `pages_read_engagement`
6. Copy the token (starts with `EAA...`)

**Important:** For long-lived token (doesn't expire):
```bash
curl -X GET "https://graph.facebook.com/v18.0/oauth/access_token?grant_type=fb_exchange_token&client_id=YOUR_APP_ID&client_secret=YOUR_APP_SECRET&fb_exchange_token=YOUR_SHORT_LIVED_TOKEN"
```

#### C. Get Page ID

1. Go to your Facebook Page
2. Click "About"
3. Scroll to "Page ID" (or find in URL)

### 3. Configure Environment Variables

Create `.env` file in `/root/clawd/automation/`:

```bash
FB_PAGE_ACCESS_TOKEN=your_long_lived_page_access_token
FB_PAGE_ID=your_page_id
FB_GROUP_ID=your_group_id  # Optional
```

**Security:** Add `.env` to `.gitignore`!

---

## Usage

### Post Directly

```bash
# Simple text post
python3 facebook-auto-poster.py --post "Your message here"

# Post with link
python3 facebook-auto-poster.py --post "Check this out!" --link "https://example.com"

# Post with image
python3 facebook-auto-poster.py --post "Look at this!" --image "/path/to/image.jpg"
```

### Use Content Queue

```bash
# View queue
python3 facebook-auto-poster.py --list

# Post next item from queue
python3 facebook-auto-poster.py --schedule

# Add to queue
python3 facebook-auto-poster.py --add "New post message" --link "https://example.com"
```

### Post to Group

```bash
# Post to group instead of page
python3 facebook-auto-poster.py --post "Group message" --group
```

---

## Automation Setup

### Option 1: Cron Job (Scheduled Posts)

Edit crontab:
```bash
crontab -e
```

Add scheduled posts:
```bash
# Monday 2pm EST (14:00 EST = 19:00 UTC)
0 19 * * 1 cd /root/clawd/automation && python3 facebook-auto-poster.py --schedule

# Wednesday 6pm EST (18:00 EST = 23:00 UTC)
0 23 * * 3 cd /root/clawd/automation && python3 facebook-auto-poster.py --schedule

# Friday 8pm EST (20:00 EST = 01:00 UTC next day)
0 1 * * 6 cd /root/clawd/automation && python3 facebook-auto-poster.py --schedule
```

### Option 2: Clawdbot Cron

Use Clawdbot's built-in cron system:

```bash
# Add Monday 2pm EST post
clawdbot cron add --schedule "0 14 * * 1" --tz "America/New_York" --text "Run Facebook auto-poster"

# Similar for Wednesday and Friday
```

### Option 3: Manual (Heartbeat-Triggered)

In `HEARTBEAT.md`, the heartbeat system already checks:
- Mon 2pm EST
- Wed 6pm EST
- Fri 8pm EST

Just run manually when heartbeat fires.

---

## Content Queue Management

### Queue File Format

`facebook-content-queue.json`:

```json
{
  "posts": [
    {
      "id": 1,
      "message": "Your post text here",
      "link": "https://example.com",
      "image": "/path/to/image.jpg",
      "posted": false,
      "posted_at": null
    },
    {
      "id": 2,
      "message": "Another post",
      "link": null,
      "image": null,
      "posted": true,
      "posted_at": "2026-02-10T14:00:00-05:00"
    }
  ]
}
```

### Managing Queue

```bash
# View queue status
python3 facebook-auto-poster.py --list

# Add post to queue
python3 facebook-auto-poster.py --add "Message" --link "URL"

# Post next item
python3 facebook-auto-poster.py --schedule

# Use custom queue file
python3 facebook-auto-poster.py --queue "/path/to/custom-queue.json" --schedule
```

---

## Content Ideas (Pre-Loaded Examples)

The script creates a default queue with sample posts. Customize for your business:

**Business Tips:**
- "💡 Tip: Focus on high-leverage activities today."
- "🚀 What's one thing you shipped this week?"
- "📊 Revenue > Vanity metrics. Focus on what moves the needle."

**Product Promotions:**
- "🎉 New feature alert: [Feature name] is now live!"
- "💰 Limited offer: Get 20% off for the next 24 hours"

**Engagement:**
- "🤔 Quick poll: What's your biggest challenge right now?"
- "🔥 Share your wins below! We want to celebrate with you."

**Educational:**
- "📚 Today's tip: [Quick actionable advice]"
- "🎯 Case study: How [Customer] achieved [Result]"

---

## Troubleshooting

### "Error: FB_PAGE_ACCESS_TOKEN not set"

**Solution:** Create `.env` file with credentials (see Setup step 3)

### "Invalid OAuth access token"

**Solution:** Token expired. Generate new long-lived token (see Setup step 2B)

### "Permissions error"

**Solution:** Re-grant permissions in Graph API Explorer:
- `pages_manage_posts`
- `pages_read_engagement`

### "Post failed: Rate limited"

**Solution:** Facebook limits posting frequency. Wait 30-60 minutes between posts.

### Image upload fails

**Solution:** 
- Check image path is correct
- Ensure image is < 8MB
- Use JPG or PNG format

---

## Best Practices

### Posting Frequency
✅ **Good:** 3-5 posts per week  
❌ **Bad:** 10+ posts per day (looks spammy)

### Content Mix
- 40% Educational (tips, how-tos)
- 30% Promotional (product, offers)
- 30% Engagement (questions, polls)

### Timing
- **Best times:** Mon-Fri 1-4pm EST
- **Worst times:** Late night, early morning
- **Test your audience:** Track engagement by time

### Avoid
- ❌ All-caps messages (looks like spam)
- ❌ Too many emojis (1-3 max)
- ❌ External links in every post (Facebook deprioritizes)
- ❌ Controversial topics (politics, religion)

---

## Analytics & Tracking

### Check Post Performance

```bash
# Get post insights (requires additional permissions)
curl -X GET "https://graph.facebook.com/v18.0/{POST_ID}/insights?metric=post_impressions,post_engaged_users&access_token={ACCESS_TOKEN}"
```

### What to Track
- Reach (how many people saw it)
- Engagement (likes, comments, shares)
- Link clicks (if you included a link)
- Best-performing content types

### Optimize
- Double down on high-engagement content
- Test different posting times
- A/B test headlines/copy
- Use insights to refine your queue

---

## Security Notes

⚠️ **Important:**
- Never commit `.env` to git
- Use long-lived tokens (60 days+)
- Store tokens securely
- Rotate tokens periodically
- Don't share tokens publicly

**Add to `.gitignore`:**
```
.env
*-queue.json
facebook-credentials.txt
```

---

## Advanced: Multiple Pages/Accounts

To manage multiple pages, create separate `.env` files:

```bash
# Page 1
python3 facebook-auto-poster.py --post "Message" --env .env.page1

# Page 2  
python3 facebook-auto-poster.py --post "Message" --env .env.page2
```

Or use different queue files per page:

```bash
python3 facebook-auto-poster.py --schedule --queue page1-queue.json
python3 facebook-auto-poster.py --schedule --queue page2-queue.json
```

---

## Support

**Facebook Graph API Docs:** https://developers.facebook.com/docs/graph-api  
**Page Publishing:** https://developers.facebook.com/docs/pages/publishing  
**Troubleshooting:** https://developers.facebook.com/support

---

**Status:** Ready to use. Just add credentials and start posting! 🚀

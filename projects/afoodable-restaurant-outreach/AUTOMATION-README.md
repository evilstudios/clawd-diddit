# Afoodable Social Media Automation

**Status**: Ready to configure  
**Platform Support**: Facebook, Twitter/X, LinkedIn, Instagram  
**Content Library**: 20+ templates across 4 platforms

---

## 🎯 What This Does

Automatically posts social media content for Afoodable across multiple platforms with:
- **Smart content rotation** (prevents repetition)
- **Category-based templates** (stat_shock, case_study, quick_tip, etc.)
- **Landing page integration** (auto-inserts URLs)
- **Posting history tracking** (JSON logs)
- **Dry-run mode** (test before going live)

---

## 📦 Files

### Core Tools
- `afoodable-content-library.py` - 20+ content templates organized by platform
- `facebook-auto-poster.py` - Facebook Page auto-poster
- `twitter-auto-poster.py` - Twitter/X auto-poster (supports threads)
- `preview-content.py` - Browse and preview all templates
- `setup-schedule.sh` - One-command cron setup

### Documentation
- `AUTOMATION-README.md` - This file
- `social-media-content-week.md` - Original content calendar
- `email-sequences.md` - Cold email templates

---

## 🚀 Quick Start

### 1. Preview Content Library

```bash
# See what's available
python3 afoodable-content-library.py

# Preview specific platform
python3 preview-content.py --platform facebook_linkedin

# Preview random samples
python3 preview-content.py --random 3
```

### 2. Test in Dry-Run Mode

```bash
# Test Facebook poster (no actual posting)
DRY_RUN=true python3 facebook-auto-poster.py

# Test Twitter poster
DRY_RUN=true python3 twitter-auto-poster.py
```

### 3. Configure Credentials

#### Facebook
```bash
export FACEBOOK_PAGE_ID="your_page_id"
export FACEBOOK_PAGE_ACCESS_TOKEN="your_access_token"
```

**Get Facebook credentials:**
1. Go to https://developers.facebook.com/
2. Create an app
3. Add "Facebook Login" product
4. Get Page Access Token from Graph API Explorer
5. Grant `pages_manage_posts` and `pages_read_engagement` permissions

#### Twitter/X
```bash
export TWITTER_API_KEY="your_api_key"
export TWITTER_API_SECRET="your_api_secret"
export TWITTER_ACCESS_TOKEN="your_access_token"
export TWITTER_ACCESS_SECRET="your_access_secret"
```

**Get Twitter credentials:**
1. Go to https://developer.twitter.com/
2. Create a new app
3. Enable OAuth 1.0a with Read & Write permissions
4. Generate keys in "Keys and tokens" section

### 4. Test Live Posting

```bash
# Post to Facebook (LIVE)
python3 facebook-auto-poster.py

# Post to Twitter (LIVE)
python3 twitter-auto-poster.py
```

### 5. Set Up Automation

```bash
# Schedule daily posts (2x Facebook, 2x Twitter)
./setup-schedule.sh
```

**Default schedule:**
- Facebook: 10 AM & 6 PM EST
- Twitter: 11 AM & 5 PM EST

---

## 📊 Content Library Stats

| Platform | Templates | Categories |
|----------|-----------|------------|
| Facebook/LinkedIn | 5 posts | stat_shock, quick_tip, case_study, problem_solution, sustainability_angle |
| Twitter/X | 6 tweets/threads | case_study_thread, stat_shock, quick_tip, problem, sustainability, objection_handler |
| LinkedIn Long | 2 posts | human_story, industry_insight |
| Instagram | 3 posts | stat_visual, before_after, how_it_works |

**Total**: 20+ content templates

---

## 🧪 Testing & Validation

### Dry Run (Recommended First)

```bash
# Test without posting
DRY_RUN=true python3 facebook-auto-poster.py
DRY_RUN=true python3 twitter-auto-poster.py
```

**What dry-run shows:**
- Selected category
- Full post content
- Image suggestions (for manual creation)
- Hashtags
- Simulated post ID

### Live Test

```bash
# Post one time to each platform
python3 facebook-auto-poster.py  # Posts to Facebook
python3 twitter-auto-poster.py   # Posts to Twitter
```

### Check History

```bash
# View posting history
cat facebook-post-history.json
cat twitter-post-history.json
```

---

## 🔄 Smart Content Rotation

### How It Works

1. **Tracks recent posts** (last 5-10 depending on platform)
2. **Avoids repetition** (won't reuse recent categories)
3. **Resets when needed** (if all categories recently used)
4. **Random selection** (from available pool)

### Example Flow

```
Day 1: Posts "stat_shock" (marked as recent)
Day 2: Won't use "stat_shock", selects "quick_tip"
Day 3: Won't use "stat_shock" or "quick_tip", selects "case_study"
...
Day 6: All categories used, resets and starts over
```

### History Files

- `facebook-post-history.json` - Last 50 Facebook posts
- `twitter-post-history.json` - Last 100 Twitter posts

**Format:**
```json
[
  {
    "timestamp": "2026-02-12T10:00:00",
    "category": "stat_shock",
    "post_id": "123456789",
    "content_preview": "The average restaurant throws away..."
  }
]
```

---

## ⏰ Automation Schedule

### Recommended Posting Times

**Facebook**:
- 10:00 AM EST (catch morning browsing)
- 6:00 PM EST (evening engagement)

**Twitter**:
- 11:00 AM EST (lunch break scrolling)
- 5:00 PM EST (commute time)

### Setup with Cron

```bash
# Edit crontab
crontab -e

# Add these lines:
0 10 * * * cd /path/to/afoodable-restaurant-outreach && python3 facebook-auto-poster.py >> facebook-auto.log 2>&1
0 18 * * * cd /path/to/afoodable-restaurant-outreach && python3 facebook-auto-poster.py >> facebook-auto.log 2>&1
0 11 * * * cd /path/to/afoodable-restaurant-outreach && python3 twitter-auto-poster.py >> twitter-auto.log 2>&1
0 17 * * * cd /path/to/afoodable-restaurant-outreach && python3 twitter-auto-poster.py >> twitter-auto.log 2>&1
```

**Or use the setup script:**
```bash
./setup-schedule.sh
```

---

## 📝 Customizing Content

### Edit Existing Templates

```python
# Edit afoodable-content-library.py
CONTENT_LIBRARY = {
    "facebook_linkedin": [
        {
            "category": "your_new_category",
            "copy": "Your post content here...",
            "hashtags": "#YourHashtags",
            "image_suggestion": "Description of image"
        }
    ]
}
```

### Add New Categories

1. Add to `CONTENT_LIBRARY` dict
2. Follow existing format
3. Use `{LANDING_PAGE}` placeholder for URLs
4. Test with dry-run mode

### Update Landing Page URL

```python
# In afoodable-content-library.py
LANDING_PAGE_URL = "https://your-new-url.com"
```

---

## 🖼️ Image Creation

Each template includes `image_suggestion` field. Create these manually using:

**Tools**:
- Canva (free, easy)
- Figma (pro-level)
- Adobe Express (quick)

**Recommended sizes**:
- Facebook: 1200×630 (link previews)
- Twitter: 1200×675 (cards)
- Instagram: 1080×1080 (square posts)

**Brand colors** (from Afoodable):
- Primary: Food waste red/orange tones
- Secondary: Money green
- Accent: Earth tones (sustainability)

---

## 🔍 Monitoring & Analytics

### Check Logs

```bash
# View posting logs
tail -f facebook-auto.log
tail -f twitter-auto.log
```

### Track Performance

**Manually check**:
- Facebook Insights (engagement, reach, clicks)
- Twitter Analytics (impressions, engagements)
- URL shortener stats (if using bit.ly, etc.)

**Metrics to track**:
- Engagement rate (likes, comments, shares)
- Click-through rate (to landing page)
- Follower growth
- Best-performing categories

### Optimize Based on Data

1. **Week 1**: Post all categories equally
2. **Week 2-4**: Track which perform best
3. **Month 2+**: Double down on winners
4. **Update library**: Remove low-performers, add more of what works

---

## 🚨 Troubleshooting

### "No content available in library"
- Check `afoodable-content-library.py` exists
- Verify `CONTENT_LIBRARY` dict has content
- Run: `python3 afoodable-content-library.py` to verify

### "Facebook credentials not configured"
- Set `FACEBOOK_PAGE_ID` and `FACEBOOK_PAGE_ACCESS_TOKEN`
- Get credentials from Facebook Developer Console
- Test with dry-run first

### "Twitter API integration not yet implemented"
- Install tweepy: `pip3 install tweepy`
- Uncomment Twitter API code in `twitter-auto-poster.py`
- Set all 4 Twitter environment variables

### Posts repeating too often
- Increase `MAX_HISTORY` in poster script
- Add more content templates to library
- Adjust `get_recent_categories()` limit

### Dry-run mode stuck
- Unset `DRY_RUN`: `unset DRY_RUN`
- Or set to false: `export DRY_RUN=false`

---

## 📈 Next Steps

### Immediate
1. ✅ Content library built (20+ templates)
2. ✅ Auto-posters coded
3. [ ] Get Facebook credentials
4. [ ] Get Twitter credentials
5. [ ] Test in dry-run mode
6. [ ] Post live test
7. [ ] Set up cron automation

### Week 1
- [ ] Create images for top 10 posts
- [ ] Monitor engagement
- [ ] Respond to comments
- [ ] Track landing page clicks

### Month 1
- [ ] Add 10 more content templates
- [ ] A/B test different CTAs
- [ ] Cross-post best performers
- [ ] Build email list from engaged followers

---

## 🎯 Expected Results

**Week 1** (4 posts/day = 28 posts/week):
- 500-1,000 total reach
- 50-100 engagements
- 10-20 landing page clicks

**Month 1** (120 posts):
- 5,000-10,000 total reach
- 500-1,000 engagements
- 100-200 landing page clicks
- 10-20 email signups

**Month 3** (360 posts):
- 20,000-50,000 total reach
- 2,000-5,000 engagements
- 500-1,000 landing page clicks
- 50-100 email signups
- 5-10 restaurant demos booked

---

## 💡 Pro Tips

1. **Post consistently** - Automation ensures you never miss a day
2. **Engage manually** - Respond to comments within 1 hour
3. **Test timing** - Try different posting times, track best performance
4. **Use video** - Add Instagram Reels (most content templates work as voiceovers)
5. **Cross-promote** - Share Twitter threads on LinkedIn, Facebook posts on Instagram
6. **Track competitors** - See what other food waste platforms post
7. **User-generated content** - Ask early customers for testimonials/photos

---

## 📞 Support

**Documentation**:
- Original content calendar: `social-media-content-week.md`
- Email sequences: `email-sequences.md`

**Questions**:
- Check code comments in `.py` files
- Review dry-run output for debugging
- Test changes incrementally

---

**Status**: System ready! Just needs API credentials to go live. 🚀

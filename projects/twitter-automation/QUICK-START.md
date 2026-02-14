# Twitter Automation - Quick Start Guide

## 📍 You Are Here

A complete Twitter automation system with **28 pre-written tweets** across 5 categories.

## ⚡ 60-Second Setup

### 1. Fix Twitter Permissions (REQUIRED)

Your app needs **Read & Write** permissions:

1. Go to https://developer.twitter.com/en/portal/dashboard
2. Find your app (Consumer Key: `qnuZrAAs...`)
3. Settings → User authentication settings
4. Change to **"Read and Write"**
5. Regenerate Access Token & Secret
6. Update `auto-tweet.py` with new tokens

**See `SETUP-PERMISSIONS.md` for detailed steps**

### 2. Test It Works

```bash
cd projects/twitter-automation

# Preview what tweets exist
python3 preview-tweets.py --count

# Test with dry-run (safe, won't post)
python3 auto-tweet.py --dry-run

# Post one tweet
python3 auto-tweet.py
```

### 3. Set Up Automation

```bash
# Install 2x daily auto-posting (9 AM & 6 PM EST)
./setup-schedule.sh

# View what's scheduled
crontab -l

# Check logs later
tail -f auto-tweet.log
```

## 🎯 What You Have

### Tools
- `auto-tweet.py` - Smart posting bot (never repeats recent tweets)
- `twitter-poster.py` - Low-level API wrapper
- `preview-tweets.py` - Browse all templates
- `setup-schedule.sh` - One-command scheduling

### Content (28 tweets)
- **Evil Apples** (7) - Game promotion & engagement
- **WellPlate AI** (5) - Nutrition tracking features
- **MoltFoundry** (5) - AI agent platform positioning
- **Tech Insights** (6) - Indie dev wisdom
- **Engagement** (5) - Questions & discussion

### Features
✅ Smart duplicate prevention  
✅ Tweet history tracking  
✅ Category-based posting  
✅ Dry-run testing  
✅ Automated scheduling  
✅ Full logging  

## 🎮 Commands

```bash
# Post random tweet
python3 auto-tweet.py

# Post from specific category
python3 auto-tweet.py --category evil_apples

# Preview without posting
python3 auto-tweet.py --dry-run

# Browse all templates
python3 preview-tweets.py

# See 5 random examples
python3 preview-tweets.py --random 5

# View template counts
python3 preview-tweets.py --count
```

## 📊 Monitor Performance

After automation is running:

```bash
# Check what's been posted
cat tweet_history.json | jq '.tweets[-5:]'

# View recent logs
tail -20 auto-tweet.log

# Check authentication
python3 twitter-poster.py me
```

## ⚙️ Customize

Edit `auto-tweet.py` to:

1. **Add tweets**: Append to any category in `TWEET_TEMPLATES`
2. **New category**: Create new key in `TWEET_TEMPLATES` dict
3. **Change schedule**: Edit times in `setup-schedule.sh`
4. **Adjust frequency**: Modify cron schedule

## 🚨 Current Status

✅ **Ready**: Code, templates, tools all working  
⚠️ **Blocked**: Need Read & Write permissions (5-min fix)  
⏳ **Next**: Fix permissions → test → schedule → launch  

## 💡 Pro Tips

1. **Start manual** - Post 5-10 tweets manually before automating
2. **Monitor early** - Check logs daily for first week
3. **Engage back** - Reply to responses for better reach
4. **Refresh content** - Update templates monthly
5. **Track metrics** - Note which categories perform best

## 🎯 Success Looks Like

After setup:
- 2 tweets posted automatically per day
- Never repeats recent content
- Rotates across all categories
- Logs every action
- Zero manual work required

## 📚 Full Documentation

- `USAGE.md` - Detailed usage guide
- `README.md` - API wrapper docs
- `status.md` - Project status & roadmap
- `SETUP-PERMISSIONS.md` - Permission setup

## 🆘 Troubleshooting

**"Forbidden" error when posting?**  
→ Need Read & Write permissions (see step 1)

**Tweets repeating?**  
→ Delete `tweet_history.json` or add more templates

**Cron not running?**  
→ Check `crontab -l` and verify log file path

**Want to stop automation?**  
→ Run `crontab -e` and delete auto-tweet lines

---

**Built**: Twitter automation system with smart templates  
**Status**: Ready (pending permission fix)  
**Time to launch**: ~5 minutes  

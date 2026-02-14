# Twitter Auto-Posting Bot - Quick Start

Simple, smart Twitter automation that posts engaging content about your products.

## 🚀 Quick Test

Post a random tweet right now:
```bash
cd projects/twitter-automation
python3 auto-tweet.py
```

## 🎯 Features

✅ **Smart content rotation** - Never repeats recent tweets  
✅ **5 content categories** - Evil Apples, WellPlate AI, MoltFoundry, tech insights, engagement  
✅ **Tweet history tracking** - Avoids duplicates  
✅ **Dry run mode** - Test before posting  
✅ **Easy scheduling** - One command setup  

## 📋 Usage

### Post a random tweet
```bash
python3 auto-tweet.py
```

### Post from specific category
```bash
python3 auto-tweet.py --category evil_apples
python3 auto-tweet.py --category tech_insights
python3 auto-tweet.py --category engagement
```

### Test without posting (dry run)
```bash
python3 auto-tweet.py --dry-run
python3 auto-tweet.py --category evil_apples --dry-run
```

### List all categories
```bash
python3 auto-tweet.py --list-categories
```

## ⏰ Automated Scheduling

Set up automatic posting (2x daily):
```bash
./setup-schedule.sh
```

This adds cron jobs for:
- **Morning**: 9:00 AM EST
- **Evening**: 6:00 PM EST

View the schedule:
```bash
crontab -l
```

View logs:
```bash
tail -f auto-tweet.log
```

Remove schedule:
```bash
crontab -e  # Delete the auto-tweet.py lines
```

## 📝 Content Categories

### evil_apples
Tweets about Evil Apples game, encouraging downloads and engagement

### wellplate_ai
WellPlate AI nutrition tracking features and benefits

### molt_foundry
MoltFoundry AI agent platform positioning

### tech_insights
General tech wisdom, indie dev motivation, building in public

### engagement
Questions and prompts to encourage replies and discussion

## 🎨 Customization

Edit `auto-tweet.py` to:
1. Add new tweet templates to `TWEET_TEMPLATES`
2. Create new categories
3. Adjust posting frequency
4. Modify scheduling times

## 📊 Tweet History

All posted tweets are tracked in `tweet_history.json`:
- Prevents duplicate posts
- Records tweet IDs and timestamps
- Keeps last 100 tweets

## 🔧 Manual Control

The underlying Twitter poster tool (`twitter-poster.py`) supports:
- Manual tweet posting
- Tweet deletion
- Timeline viewing
- User info lookup

See `README.md` for full API documentation.

## 💡 Tips

1. **Test first**: Always run with `--dry-run` to see what will be posted
2. **Monitor logs**: Check `auto-tweet.log` regularly when using cron
3. **Vary content**: Mix categories to keep your feed diverse
4. **Engage back**: Auto-posting works best when you also reply to engagement
5. **Update templates**: Refresh tweet templates periodically to keep content fresh

## 🚨 Important

- Tweets are posted immediately (no undo)
- Cron schedule uses UTC timezone internally
- History file tracks last 100 tweets
- Rate limits: Twitter allows ~300 tweets per 3 hours

## 🎯 Next Steps

1. Test with dry run: `python3 auto-tweet.py --dry-run`
2. Post a few manual tweets to verify
3. Set up automated schedule: `./setup-schedule.sh`
4. Monitor for first few days
5. Customize templates as needed

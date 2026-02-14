# Quick Command Reference

## 💰 You Have: $25 in Credits
**Status**: Can post for years at 4x daily  
**Recommendation**: Upgrade to 4x daily now!

---

## 🚀 Post Tweets

```bash
cd projects/twitter-automation

# Smart post (best choice)
python3 auto-tweet-v2.py

# Specific content type
python3 auto-tweet-v2.py --category evil_apples
python3 auto-tweet-v2.py --category engagement
python3 auto-tweet-v2.py --category molt_foundry
python3 auto-tweet-v2.py --category wellplate_ai
python3 auto-tweet-v2.py --category time_based

# Test first (doesn't actually post)
python3 auto-tweet-v2.py --dry-run
```

---

## 💰 Check Credits

```bash
# Full status
python3 credit-monitor.py

# Quick test (exit code 0 = can post)
python3 credit-monitor.py --test-post

# JSON output
python3 credit-monitor.py --json
```

---

## 📊 View Your Tweets

```bash
# Recent tweets
python3 twitter-poster.py recent --max-results 10

# Account info
python3 twitter-poster.py me

# Manual post
python3 twitter-poster.py post --text "Your tweet here"
```

---

## 😈 Evil Apples Content

```bash
# Generate one combo
python3 evil-apples-generator.py

# Generate multiple
python3 evil-apples-generator.py --count 5

# Twitter-ready format
python3 evil-apples-generator.py --twitter-format

# Get JSON
python3 evil-apples-generator.py --json
```

---

## 🧵 Post Threads

```bash
# From command line
python3 thread-poster.py --tweets \
  "First tweet" \
  "Second tweet" \
  "Third tweet"

# From file
python3 thread-poster.py --file thread.txt

# Dry run first
python3 thread-poster.py --file thread.txt --dry-run
```

---

## 📸 Upload Media

```bash
# Upload image
python3 media-uploader.py image.jpg

# With alt text (accessibility)
python3 media-uploader.py image.jpg --alt-text "Description"

# Multiple images
python3 media-uploader.py img1.jpg img2.jpg img3.jpg

# Get media ID for posting
python3 media-uploader.py logo.png --json
```

---

## 📈 Analytics

```bash
# Last 7 days
python3 engagement-tracker.py

# Last 30 days
python3 engagement-tracker.py --days 30

# Save to history
python3 engagement-tracker.py --save

# JSON output
python3 engagement-tracker.py --json
```

---

## 🔍 Browse Templates

```bash
# Count templates
python3 preview-tweets.py --count

# Show all
python3 preview-tweets.py

# Specific category
python3 preview-tweets.py --category evil_apples

# Random samples
python3 preview-tweets.py --random 10
```

---

## ⏰ Set Up Automation

```bash
# Enhanced setup (multiple frequency options)
./setup-schedule-enhanced.sh

# Choose:
#   1) 2x daily (conservative)
#   2) 4x daily ⭐ RECOMMENDED with $25
#   3) 6x daily (active)
#   4) 8x daily (aggressive)
```

---

## 🛠️ Manage Cron Jobs

```bash
# View current schedule
crontab -l

# Edit schedule
crontab -e

# Remove all auto-tweet jobs
crontab -l | grep -v auto-tweet | crontab -

# View logs
tail -f auto-tweet.log

# Follow logs live
tail -f auto-tweet.log | grep -E "Posted|Failed|Error"
```

---

## 🔥 Quick Actions

### Post Right Now
```bash
cd projects/twitter-automation && python3 auto-tweet-v2.py
```

### Check Everything
```bash
cd projects/twitter-automation
python3 credit-monitor.py
python3 twitter-poster.py recent --max-results 5
```

### Emergency Stop
```bash
crontab -r  # Removes ALL cron jobs (be careful!)
# or
crontab -e  # Then delete just auto-tweet lines
```

### Full Status
```bash
echo "=== Credits ===" && python3 credit-monitor.py --test-post
echo "=== Recent Tweets ===" && python3 twitter-poster.py recent --max-results 3
echo "=== Cron Jobs ===" && crontab -l | grep auto-tweet
```

---

## 🎯 Recommended Daily Workflow

### Morning Check
```bash
cd projects/twitter-automation
python3 credit-monitor.py --test-post
python3 twitter-poster.py recent --max-results 5
```

### Manual Post
```bash
# Post one tweet
python3 auto-tweet-v2.py

# Check it posted
python3 twitter-poster.py recent --max-results 5
```

### Weekly Review
```bash
# Get engagement stats
python3 engagement-tracker.py --days 7 --save

# Review logs
tail -50 auto-tweet.log
```

---

## 💡 Pro Tips

### Test Before Committing
```bash
python3 auto-tweet-v2.py --dry-run  # See what would post
python3 thread-poster.py --file thread.txt --dry-run
```

### Batch Post Evil Apples
```bash
for i in {1..3}; do
  python3 auto-tweet-v2.py --category evil_apples
  sleep 300  # 5 min between posts
done
```

### Check History
```bash
cat tweet_history.json | jq '.tweets[-10:]'  # Last 10 tweets
cat tweet_history.json | jq '.tweets | length'  # Total count
```

### Monitor Engagement
```bash
watch -n 60 'python3 twitter-poster.py recent --max-results 5'
```

---

## 🆘 Troubleshooting

### Can't Post?
```bash
python3 credit-monitor.py  # Check credits
python3 twitter-poster.py me  # Check auth
```

### Import Errors?
```bash
pip3 install requests-oauthlib
```

### Permission Denied?
```bash
chmod +x *.py
```

### Cron Not Working?
```bash
# Test command manually first
cd /root/clawd/projects/twitter-automation
python3 auto-tweet-v2.py

# Check logs
tail -f auto-tweet.log

# Verify cron
crontab -l
```

---

## 📱 URLs

- **Dashboard**: https://developer.twitter.com/en/portal/dashboard
- **Your Profile**: https://twitter.com/moltfoundry
- **Latest Tweets**: Check tweet_history.json or run recent command

---

## ⚡ One-Liners

```bash
# Quick post
cd ~/clawd/projects/twitter-automation && python3 auto-tweet-v2.py

# Status check
cd ~/clawd/projects/twitter-automation && python3 credit-monitor.py && python3 twitter-poster.py recent --max-results 3

# Enable 4x daily
cd ~/clawd/projects/twitter-automation && ./setup-schedule-enhanced.sh

# View what's posted
cd ~/clawd/projects/twitter-automation && cat tweet_history.json | jq '.tweets[-5:] | .[] | .text'
```

---

**Quick Access**: Bookmark this file for daily use!

**Location**: `/root/clawd/projects/twitter-automation/`

**All commands assume you're in the project directory**

# Twitter API Credits Guide

## ✅ You Have Credits!

Your bot just posted successfully, which means credits are available.

## 📊 Understanding Twitter API Credits

### Free Tier (What You Have)
- **Cost**: $0/month
- **Tweet Posts**: 1,500/month
- **Tweet Reads**: 10,000/month  
- **Resets**: Monthly (check dashboard for exact date)

### Credit Consumption
- **1 post = 1 credit**
- **Reading tweets = uses separate quota**
- **Rate limits**: Additional per 15-min windows

## 💰 Where to Get More Credits

### Option 1: Wait for Monthly Reset
- **Free**: Credits reset every month
- **Check**: https://developer.twitter.com/en/portal/dashboard
- **Usage tab**: Shows credits used and reset date

### Option 2: Upgrade Plan

Go to: https://developer.twitter.com/en/portal/products

**Basic ($100/month)**:
- 3,000 tweet posts/month
- 10,000 tweet reads/month
- Better rate limits
- Good for: Small bots, testing

**Pro ($5,000/month)**:
- 50,000 tweet posts/month
- 100,000 tweet reads/month
- Premium support
- Good for: Production apps, high volume

## 📈 Monitor Your Usage

### Check Credits Before Posting
```bash
cd projects/twitter-automation
python3 credit-monitor.py
```

### Quick Credit Test
```bash
python3 credit-monitor.py --test-post
```

### Add to Your Automation
```bash
# In cron, before posting:
python3 credit-monitor.py --test-post && python3 auto-tweet-v2.py || echo "Out of credits"
```

## 🎯 Credit Management Strategy

### For 2x Daily Posts (Your Setup)
- **Usage**: 2 posts/day × 30 days = 60 posts/month
- **Free tier**: 1,500/month
- **You're fine**: Only using 4% of quota

### Conservative Approach
```bash
# Post only if credits available
if python3 credit-monitor.py --test-post > /dev/null 2>&1; then
    python3 auto-tweet-v2.py
else
    echo "Skipping - out of credits"
fi
```

## 📊 Current Status

Run this to check:
```bash
python3 credit-monitor.py
```

Output shows:
- ✅ Credits available (can post)
- ❌ Credits depleted (need to wait or upgrade)
- 📈 Rate limit status

## 🚨 What If Credits Run Out?

### You'll See:
```
❌ Out of API credits
Detail: Your enrolled account does not have any credits to fulfill this request.
```

### Solutions:
1. **Wait** - Reset happens monthly (check dashboard)
2. **Upgrade** - Basic plan for $100/month
3. **Optimize** - Reduce posting frequency

### Emergency Posting (Manual)
- Post directly on Twitter.com
- No API credits needed
- Bot resumes when credits reset

## 💡 Best Practices

### Track Usage
```bash
# Weekly check
python3 credit-monitor.py > credit-log.txt
date >> credit-log.txt
```

### Smart Scheduling
- 2x daily = safe for free tier
- 4x daily = still well under limit
- 50+ daily = monitor closely

### Error Handling
Your bot already handles credit errors gracefully:
- Logs the error
- Exits cleanly
- No data loss
- Resumes when credits available

## 🔍 Debugging Credit Issues

### Check Dashboard
https://developer.twitter.com/en/portal/dashboard
- **Products & usage** tab
- View monthly breakdown
- See reset date

### Common Issues

**"Credits depleted" but should have some?**
- Check you're looking at right app
- Multiple apps share account quota
- Old test requests count too

**Credits reset but still failing?**
- Wait 5-10 minutes after reset
- Try credit-monitor.py to verify
- Check for Twitter API status issues

**Rate limit vs Credits?**
- **Rate limit**: 15-min windows (auto-resets)
- **Credits**: Monthly quota (needs reset/upgrade)
- Different error messages

## 📅 Your Bot's Efficiency

**Current Setup**:
- Posts: 2/day
- Monthly: ~60 tweets
- Free tier: 1,500 tweets
- **Usage**: 4% of quota
- **Buffer**: 1,440 tweets spare

**You're golden!** Your automation uses <5% of free tier.

## 🎯 When to Upgrade

Upgrade to Basic if:
- [ ] Want to post 4+ times daily
- [ ] Need more reliability
- [ ] Testing lots of features
- [ ] Building production service

Stay Free if:
- [x] 2x daily is enough (you)
- [x] Personal/side project use
- [x] 60 posts/month is plenty

## 🚀 You're All Set

✅ Bot is live and working
✅ Credits available
✅ 4% usage on free tier
✅ Monitoring tool ready
✅ 1,440 tweets buffer

No action needed - you're running efficiently on the free tier!

---

**Quick Command Reference**:
```bash
# Check credits
python3 credit-monitor.py

# Test posting ability
python3 credit-monitor.py --test-post

# Post tweet (uses 1 credit)
python3 auto-tweet-v2.py

# View usage history
# → Go to https://developer.twitter.com/en/portal/dashboard
```

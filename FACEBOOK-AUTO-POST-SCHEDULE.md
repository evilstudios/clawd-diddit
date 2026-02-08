# Evil Apples Facebook Auto-Posting Schedule

## 🎯 Strategy: 3x Per Week at Optimal Times

**Goal:** Consistent engagement without overwhelming followers  
**Content:** Random Evil Apples card combos (Prompt + 2 Answers + Vote CTA)

---

## 📅 Posting Schedule

### Monday - 2pm EST (7pm UTC)
- **Why:** Start of work week, lunch break scrolling
- **Command:** `python3 /root/clawd/facebook-auto-poster.py`
- **Audience:** Working professionals on break

### Wednesday - 6pm EST (11pm UTC)  
- **Why:** Mid-week, evening engagement peak
- **Command:** `python3 /root/clawd/facebook-auto-poster.py`
- **Audience:** Evening scrollers, dinner time

### Friday - 8pm EST (1am UTC Saturday)
- **Why:** Weekend starts, party/game night planning
- **Command:** `python3 /root/clawd/facebook-auto-poster.py`
- **Audience:** Weekend planners, social activity peak

---

## 🤖 Automation Options

### Option 1: Clawdbot Heartbeat (Current)
I'll post automatically during heartbeats on these days/times.

**Setup:** Add to HEARTBEAT.md check:
```markdown
### Monday 7pm UTC / Wednesday 11pm UTC / Friday 1am UTC:
- Run facebook-auto-poster.py
- Post Evil Apples card combo
```

### Option 2: System Cron (Manual Setup)
Add to your system crontab:
```bash
# Evil Apples Facebook Posts (3x per week)
0 19 * * 1 cd /root/clawd && python3 facebook-auto-poster.py  # Monday 2pm EST
0 23 * * 3 cd /root/clawd && python3 facebook-auto-poster.py  # Wednesday 6pm EST
0 1 * * 6 cd /root/clawd && python3 facebook-auto-poster.py   # Saturday 1am UTC (Friday 8pm EST)
```

To add:
```bash
crontab -e
# Paste the lines above
```

### Option 3: Manual Trigger
Run anytime:
```bash
python3 /root/clawd/facebook-auto-poster.py
```

---

## 📊 Content Rotation

**Total Prompts:** 86  
**Total Answers:** 50  
**Possible Combinations:** 4,300 unique posts

**At 3 posts/week:** 28+ years of unique content before repeating!

---

## 🎯 Post Format (Automated)

Every post includes:
- ✅ Random prompt card
- ✅ Two random answer options (A/B)
- ✅ Vote CTA ("Drop A or B in the comments")
- ✅ Download link (evilapples.com)
- ✅ Hashtags (#EvilApples #CardGame #DarkHumor #GameNight #VoteNow)

---

## 📈 Success Metrics (Track Weekly)

Monitor via `facebook-engagement-tracker.py`:
- Engagement rate per post
- Comments (A/B votes)
- Shares
- Link clicks to evilapples.com

**Goal:** 
- Week 1: 0.5% engagement rate
- Month 1: 1% engagement rate
- Month 3: 2%+ engagement rate

---

## 🔧 Testing & Adjustments

### If Engagement is Low:
- Try different posting times
- Increase to 4-5x per week
- Add images (card graphics)

### If Engagement is High:
- Boost best-performing posts ($10-20)
- Create themed weeks (Valentine's, Halloween, etc.)
- Add Stories resharing

---

## 🚀 Quick Start

**Post Right Now:**
```bash
cd /root/clawd
python3 facebook-auto-poster.py
```

**Check Recent Posts:**
```bash
python3 facebook-engagement-tracker.py
```

---

## 📝 Current Status

- ✅ Auto-poster script created
- ✅ Card database loaded (86 prompts, 50 answers)
- ✅ Facebook API connected
- ⏳ Schedule: Will post during heartbeats on Mon/Wed/Fri
- 📊 Tracking: Run engagement tracker anytime

---

**Next Actions:**
1. I'll automatically post 3x/week during heartbeats
2. Monitor engagement after each post
3. Adjust timing based on performance
4. Report weekly stats

**Status:** Automation live! 🍎🚀

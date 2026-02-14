# Voxable Campaign - LIVE Status

**Campaign ID**: `cf9d41e0-20b1-49c7-8b1c-7843888dae4f`  
**Campaign Name**: "Voxable Home Service Prospects"  
**Status**: ✅ ACTIVE (Status: 1)  
**Last Updated**: 2026-02-11 13:09 UTC  

---

## ✅ Campaign Configuration

### Schedule
- **Days**: Monday-Friday
- **Hours**: 9:00 AM - 5:00 PM
- **Timezone**: America/Detroit (EST)
- **Daily Limit**: 25 emails/day
- **Created**: 2026-02-03

### Email Sequence (3 Emails)

#### Email 1: Day 1 (Initial Outreach)
**Subject**: `{{firstName}}, quick question about {{company}}'s customer support`

**Key Points**:
- Problem: Team getting slammed with calls
- 3 bad solutions (hiring, voicemail, chatbots)
- 4th option: AI voice agents
- Social proof: 40% → 0% missed calls
- CTA: 5-min demo

#### Email 2: Day 4 (Follow-up)
**Subject**: `Re: {{firstName}}, quick question about {{companyName}}'s customer support`

**Key Points**:
- Clarification: Not a chatbot, real voice AI
- Stats: 90% can't tell it's AI
- Pricing: $500-1,500/mo vs $3K+ for human
- CTA: Quick chat

#### Email 3: Day 5 (Breakup)
**Subject**: `Last note - AI for {{companyName}}`

**Key Points**:
- Final pitch: Short and direct
- Pain points recap
- Calendly link: https://calendly.com/supermassive/15min
- P.S.: Check back Q3 if not now

### Settings
- ✅ **Stop on reply**: TRUE (important!)
- ✅ **Link tracking**: Enabled
- ✅ **Open tracking**: Enabled
- ✅ **First email text only**: TRUE (better deliverability)
- ✅ **Unsubscribe header**: Included
- ❌ **Stop on auto-reply**: FALSE
- ❌ **Bounce protect**: FALSE (disabled)

### Sender Email
- **From**: lauren@valuereach.co

---

## 📊 Performance Metrics

**Note**: API v2 doesn't expose analytics endpoint yet. Need to:
1. Check Instantly.ai dashboard manually
2. Use webhooks for real-time updates
3. Export data periodically

### Expected Performance (Based on Setup)
- **Daily sends**: 25 emails
- **Total leads**: Unknown (need to check dashboard)
- **Campaign duration**: ~9 days (if 230 leads ÷ 25/day)

---

## 🎯 Monitoring Plan

### What I Can Track via API
- ✅ Campaign status (active/paused)
- ✅ Campaign configuration
- ✅ Email sequence content
- ✅ Sending schedule

### What Needs Dashboard Access
- ⏳ Emails sent count
- ⏳ Open rate
- ⏳ Click rate
- ⏳ Reply rate
- ⏳ Lead list size

### Workarounds
1. **Manual checks**: Log into Instantly.ai dashboard
2. **Webhooks**: Set up reply notifications
3. **Email forwarding**: Forward replies to monitoring system

---

## 🔧 API Access Confirmed

**Base URL**: `https://api.instantly.ai/api/v2/`  
**Auth**: Bearer token (configured ✅)  

**Working Endpoints**:
- ✅ `GET /campaigns` - List all campaigns
- ✅ Campaign details retrieved

**Not Available in V2**:
- ❌ Analytics/stats endpoint
- ❌ Lead list endpoint (different path)
- ❌ Real-time activity feed

---

## 📋 Next Steps

### Immediate Actions
1. [ ] Check Instantly.ai dashboard for current stats
2. [ ] Verify lead count (should be ~230)
3. [ ] Monitor for first replies (within 24-48 hours)
4. [ ] Set up email forwarding for replies

### Response Handling
When replies come in:
- Check inbox: lauren@valuereach.co
- Use response templates from LAUNCH-STATUS.md
- Book demos via Calendly: https://calendly.com/supermassive/15min

### Weekly Review
- [ ] Monday: Check weekend activity
- [ ] Wednesday: Mid-week review
- [ ] Friday: Week summary, plan next week

---

## 🚨 Campaign Health Check

### Green Flags ✅
- Campaign is ACTIVE
- Sequence is complete (3 emails)
- Schedule configured (M-F, 9-5)
- Stop on reply enabled
- Tracking enabled
- Professional sender email

### Yellow Flags ⚠️
- Daily limit: 25/day (could be higher)
- No analytics via API (need dashboard access)
- First email text-only (good for deliverability but limits formatting)

### Red Flags ❌
- None detected!

---

## 💡 Optimization Ideas

### Increase Send Volume
- Current: 25/day = ~9 days for 230 leads
- Could increase to 40/day = ~6 days
- Recommendation: Start conservative, scale up if deliverability is good

### A/B Testing
- Currently using single variant per email
- Could add subject line variants
- Test different CTAs

### Timing Optimization
- Current: 9 AM - 5 PM EST
- Could test: 8 AM - 6 PM (broader window)
- Or: 7 AM - 3 PM (catch early birds)

---

## 📞 Contact Info Being Used

**Phone**: 267-550-0466  
**Calendar**: https://calendly.com/supermassive/15min  
**Sender**: lauren@valuereach.co  

---

## ✅ Status Summary

**Campaign**: ✅ LIVE & CONFIGURED  
**API Access**: ✅ CONNECTED  
**Monitoring**: ⏳ MANUAL (dashboard needed for stats)  
**Response Handling**: ✅ READY  

**The campaign is running!** Just need dashboard access for detailed metrics.

---

**Last API Check**: 2026-02-12 13:47 UTC  
**Next Check**: Monitor inbox for replies  
**Action Required**: Check Instantly.ai dashboard for real-time stats

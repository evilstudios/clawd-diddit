# Afoodable - 3-Email Cold Sequence for Instantly.ai

**Campaign:** Afoodable Restaurant Outreach  
**Target:** 200 independent restaurants (Philly/NYC/DC metro)  
**Goal:** 10-15 demo calls from 200 sends  
**Created:** 2026-02-13

---

## Campaign Settings (Instantly.ai)

**Daily Limit:** 25 emails/day  
**Stop on Reply:** TRUE  
**Stop on Auto-Reply:** FALSE  
**Open Tracking:** TRUE  
**Link Tracking:** TRUE  
**First Email Text-Only:** TRUE (better deliverability)  
**Timezone:** America/New_York (EST)  
**Send Window:** Mon-Fri, 8 AM - 6 PM  

---

## Email 1 - Day 1 (The Question)

### Subject Line Options (A/B Test):
1. `{{firstName}}, quick question about {{restaurantName}}'s end-of-day food`
2. `What happens to your unsold food at {{restaurantName}}?`
3. `{{firstName}}, are you throwing away money at close?`

### Body:

```
Hi {{firstName}},

Quick question:

What happens to the food you can't sell at the end of the day at {{restaurantName}}?

Most restaurants throw it away—which means you're paying twice: once to make it, and again to dispose of it.

We built Afoodable to help restaurants turn that waste into revenue instead.

**One bakery recovered $1,200/month** from items they used to throw away.

Would it make sense to chat for 5 minutes about how this could work for {{restaurantName}}?

Best,
Mitch

P.S. We only make money when you recover money. Zero upfront cost.
```

**Personalization Variables:**
- `{{firstName}}` - Owner/manager first name
- `{{restaurantName}}` - Restaurant name

**Fallback Values:**
- `{{firstName}}` → "there" (if name missing)
- `{{restaurantName}}` → "your restaurant" (if name missing)

---

## Email 2 - Day 4 (The Math)

### Subject Line Options (A/B Test):
1. `Re: {{firstName}}, quick question about {{restaurantName}}'s end-of-day food`
2. `The real cost of throwing away food`
3. `{{restaurantName}} - following up on waste → revenue`

### Body:

```
Hi {{firstName}},

Following up on my last note.

Here's the math most restaurant owners don't want to think about:

If you throw away just $50 worth of food per day:
→ $350/week
→ $1,500/month  
→ $18,000/year in lost revenue

Afoodable helps you recover that by:

✅ Listing surplus items (end-of-day, overproduction)  
✅ Connecting with local buyers automatically  
✅ Handling ordering & pickup (zero manual work)  
✅ Tracking waste reduction (ESG reporting included)

You're already making the food. Why not get paid for it?

Are you open to a 5-minute call to see if this fits {{restaurantName}}?

Best,
Mitch

Book a time: https://calendly.com/supermassive/15min
or just reply with a good day this week.
```

---

## Email 3 - Day 7 (The Breakup)

### Subject Line Options (A/B Test):
1. `Should I take {{restaurantName}} off my list?`
2. `Last note, {{firstName}}`
3. `Closing the loop`

### Body:

```
Hi {{firstName}},

I haven't heard back, so I'm guessing turning waste into revenue isn't a priority for {{restaurantName}} right now.

I'll take you off my follow-up list so I don't clutter your inbox.

But if you ever get tired of watching food (and money) go into the trash, feel free to reach out anytime.

Wishing you the best with {{restaurantName}}.

Best,
Mitch

P.S. We're still in early rollout, so spots are limited. If you change your mind, just reply.
```

---

## Instantly.ai Import Format

### CSV Column Headers:
```
firstName,restaurantName,email,restaurantType,city,website
```

### Example Row:
```
Maria,Café Luna,maria@cafeluna.com,Café,Philadelphia,cafeluna.com
```

---

## Response Templates (Quick Copy-Paste)

### ✅ Positive Reply ("Tell me more")

```
Great! Here's my calendar: https://calendly.com/supermassive/15min

Pick a time that works for you, and I'll walk you through:
- How the marketplace works
- Success stories from similar restaurants
- Setup process (takes ~10 minutes)

Looking forward to it!

Best,
Mitch
```

---

### ✅ Neutral Reply ("What's the pricing?")

```
Good question! Pricing is simple:

**Option 1 (Most Popular):** 15% commission per sale
- Zero upfront cost
- You only pay when you recover money
- Most restaurants start here

**Option 2:** $49-149/month + 5-10% commission
- Lower per-transaction fee
- Better for high-volume

Most restaurants start with Option 1 since there's no risk.

Want to hop on a quick call to discuss what works best for {{restaurantName}}?

https://calendly.com/supermassive/15min

Best,
Mitch
```

---

### ❌ Negative Reply ("Not interested")

```
No worries at all, {{firstName}}! Appreciate you letting me know.

Mind if I check back in 6 months in case things change?

Either way, best of luck with {{restaurantName}}!

Best,
Mitch
```

---

### ⏸️ Busy Reply ("Too busy right now")

```
Totally understand—I know how crazy restaurant operations can be.

If things calm down or this becomes a priority, feel free to reach out anytime: mitch@supermassive.co

In the meantime, here's a quick tip: [Insert 1 free resource about reducing food waste]

Best,
Mitch
```

---

## Expected Performance (Based on 200 Sends)

### Conservative Estimate:
- **Open Rate:** 40-50% (80-100 opens)
- **Reply Rate:** 10% (20 replies)
- **Positive Replies:** 50% of replies (10 interested)
- **Demos Booked:** 50% of positive (5 calls)
- **Signups:** 40% of demos (2 paying customers)

### Optimistic Estimate:
- **Open Rate:** 50-60% (100-120 opens)
- **Reply Rate:** 15% (30 replies)
- **Positive Replies:** 60% of replies (18 interested)
- **Demos Booked:** 60% of positive (10-11 calls)
- **Signups:** 50% of demos (5-6 paying customers)

---

## A/B Testing Plan

### Week 1: Test Subject Lines
Run all 3 variants for Email 1, measure open rates:
- Variant A: "{{firstName}}, quick question..."
- Variant B: "What happens to your unsold food..."
- Variant C: "{{firstName}}, are you throwing away money..."

**Winner becomes default for Week 2+**

### Week 2: Test CTA in Email 2
- Variant A: "Are you open to a 5-minute call?"
- Variant B: "Book a time: [Calendly link]"
- Variant C: "Just reply with a good day this week"

**Measure: Which gets most positive replies?**

---

## Red Flags & Fixes

### 🚩 Open Rate < 35%
**Problem:** Subject lines or sender reputation  
**Fix:** 
- Test new subject lines (less salesy)
- Warm up sender domain
- Check spam score (mail-tester.com)

### 🚩 Reply Rate < 8%
**Problem:** Email content or CTA  
**Fix:**
- Shorten Email 1 (make it punchier)
- Simplify the value prop (focus on $$$)
- Make CTA more specific

### 🚩 High Negative Replies
**Problem:** Wrong audience or tone  
**Fix:**
- Refine lead targeting (smaller restaurants?)
- Soften language (less aggressive)
- Lead with sustainability, not just money

---

## Timeline to First Customers

**Week 1 (Days 1-7):**
- Send 125 emails (25/day × 5 days)
- Expected: 50-60 opens, 10-15 replies, 5-8 positive

**Week 2 (Days 8-14):**
- Complete 200 sends
- Book 5-10 demo calls
- Expected: 2-3 signed customers

**Week 3 (Days 15-21):**
- Follow up with demo prospects
- Onboard first customers
- Document success stories

---

## Next Steps

1. ✅ **Review sequences** - Approve copy/tone
2. ✅ **Import leads to Instantly** - Upload Manus CSV
3. ✅ **Set up campaign** - Configure settings above
4. ✅ **Warm up sender** - Send 5-10 test emails first
5. ✅ **Launch** - Start 25/day sends
6. ✅ **Monitor daily** - Check replies, adjust as needed

---

## Files Needed

- ✅ Lead list CSV from Manus (200 restaurants)
- ✅ Calendly link (https://calendly.com/supermassive/15min)
- ✅ Sender email configured in Instantly.ai
- ✅ Response templates (above)

---

**Status:** READY TO LAUNCH  
**Created:** 2026-02-13  
**Campaign ID:** (Add after Instantly.ai setup)

---

**Questions? Changes? Let me know and I'll adjust!** 🚀

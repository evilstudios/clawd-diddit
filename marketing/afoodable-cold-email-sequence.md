# Afoodable Cold Email Sequence

## Campaign Overview
- **Platform:** Instantly.ai
- **Target:** Fast casual restaurants, bakeries, cafés, ghost kitchens
- **Goal:** Book discovery calls → onboard pilot locations
- **Sequence:** 4 emails over 10 days

---

## Email 1: Direct Question (Day 0)

**Subject:** Quick question about end-of-day food

**Body:**
```
Hi {{first_name}},

Quick question: Does {{business_name}} throw away food at the end of the day?

Most restaurants do. One bakery we work with was tossing ~$40/day in unsold items.

We built Afoodable to help them sell it instead—recovered $1,200 last month.

Worth a 10-minute call?

Best,
[Your Name]
Afoodable
```

**Why This Works:**
- Opens with a yes/no question (high engagement)
- Shows immediate dollar impact
- Low-friction ask (10 min)

---

## Email 2: Social Proof (Day 3)

**Subject:** Re: Quick question about end-of-day food

**Body:**
```
{{first_name}},

Following up in case this got buried.

We're working with a few local restaurants/bakeries who were throwing away $500-2,000/month in unsold inventory.

Afoodable lists their surplus food to local buyers, nonprofits, and consumers—so they get paid instead of paying for disposal.

No upfront cost. We only make money when you recover revenue.

Here's a 2-min explainer: [link]

Open to a quick chat?

Best,
[Your Name]
```

**Why This Works:**
- Reinforces revenue recovery
- Removes risk ("no upfront cost")
- Provides resource for research

---

## Email 3: Specificity (Day 6)

**Subject:** Recovering {{amount}}/month for {{business_type}}

**Body:**
```
Hi {{first_name}},

I've been tracking trends in {{city}} and noticed that most {{business_type}} locations discard ~$800-1,500/month in surplus food.

That's $10k-18k/year you've already paid to produce.

Afoodable helps recover 60-80% of that by listing surplus to local buyers before it hits the trash.

- No setup fees
- 15-20% commission only on recovered sales
- Plug into your existing POS workflow

Worth exploring for {{business_name}}?

Best,
[Your Name]
Afoodable
```

**Why This Works:**
- Personalized to business type and location
- Shows annualized cost (bigger number = more pain)
- Clear commission structure

---

## Email 4: Breakup / Last Attempt (Day 10)

**Subject:** Should I close your file?

**Body:**
```
{{first_name}},

I'll take the hint and stop bugging you :)

Before I do—just want to confirm: are you already handling surplus food in a way that works for you? Or is this just not a priority right now?

Either way, no hard feelings. If things change, you know where to find me.

Best,
[Your Name]
Afoodable

P.S. — If you know another {{business_type}} owner who'd benefit, I'd love an intro.
```

**Why This Works:**
- "Permission to close" often gets replies
- Opens door to referrals
- Low-pressure, respectful tone

---

## Campaign Settings (Instantly.ai)

- **Daily Send Limit:** 50/day per inbox (warm sending)
- **Follow-up Intervals:** Day 0 → Day 3 → Day 6 → Day 10
- **Stop on Reply:** Yes
- **Stop on Open + No Reply After Email 2:** Optional (saves sends)
- **Personalization Fields Required:**
  - `{{first_name}}`
  - `{{business_name}}`
  - `{{business_type}}` (e.g., "bakery", "café", "fast casual")
  - `{{city}}`
  - `{{amount}}` (estimated monthly waste: $800-$1,500 range)

---

## Lead List Requirements

**Minimum Data:**
- First name
- Business name
- Email
- Business type
- City

**Scraping Source:**
- Google Maps → "bakery", "fast casual", "café" + city filters
- Tools: Apify, Outscraper, or Instant Data Scraper

---

## Success Metrics

**Week 1 Target:**
- 250 emails sent
- 20%+ open rate
- 5%+ reply rate
- 3-5 discovery calls booked

**Conversion Goal:**
- 10-20% of calls → pilot signup
- Target: First 10 restaurants onboarded by end of month

---

## Next Steps

1. ✅ Sequence written
2. ⏳ Scrape lead list (Google Maps)
3. ⏳ Upload to Instantly.ai
4. ⏳ Configure campaign
5. ⏳ Launch + monitor replies

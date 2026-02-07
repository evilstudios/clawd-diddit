# Afoodable Monday Launch - Final Checklist

**Target:** 50 Philadelphia restaurants  
**Launch:** Monday morning, Feb 10  
**First emails:** Monday 10am EST

---

## Sunday Tasks (4 hours total)

### Task 1: Build Lead List (2-3 hours)

**Option A: Automated (If scraper works on your machine)**
```bash
cd /root/clawd
python3 automation/google-maps-scraper.py \
  --city "Philadelphia, PA" \
  --query "bakery" \
  --query "cafe" \
  --query "fast casual restaurant" \
  --max-per-query 20 \
  --output-csv philly-restaurants.csv
```

**Option B: Manual (Fallback - 2 hours)**
- Follow `MANUAL-LEAD-BUILD-GUIDE.md`
- Google Maps manual collection
- Target: 50 restaurants minimum

**Output:** `philly-restaurants.csv` with 50-75 leads

---

### Task 2: Find Emails (1 hour)

**Automated:**
```bash
python3 automation/email-finder.py \
  --input projects/afoodable-restaurant-outreach/philly-restaurants.csv \
  --output projects/afoodable-restaurant-outreach/philly-ready.csv
```

**Manual (if needed):**
- Check each website contact page
- Try common patterns (info@, contact@, hello@)
- Use Hunter.io for verification

**Target:** 30-40 emails found (60%+ coverage)

---

### Task 3: Clean & Review CSV (30 min)

Open `philly-ready.csv` and:
- [ ] Remove obvious chains (Starbucks, Dunkin')
- [ ] Remove fine dining (wrong target)
- [ ] Verify at least 30 have emails
- [ ] Check for duplicates
- [ ] Add any notes/personalizations

**Final target:** 30-50 high-quality leads with emails

---

## Monday Morning Tasks (30 min)

### Task 4: Create Instantly Campaign

1. Log into Instantly.ai
2. Click "Create Campaign"
3. Name: "Afoodable - Philadelphia - Feb 2026"

**Settings:**
- Daily limit: 25 emails
- Schedule: Mon-Fri, 10am-4pm EST
- Stop on reply: ✅ Yes
- First email as text: ✅ Yes

---

### Task 5: Set Up Email Sequence

**Email 1 (Day 0) - The Question**

```
Subject: Quick question about {{company}}

Hi {{firstName}},

Quick question: Do you throw away food at the end of the day?

Most restaurants do. Bakeries especially.

We built Afoodable to turn that waste into revenue — no upfront cost, just a small cut when you recover a sale.

Worth a 5-minute call to see if it fits?

Best,
Mitch
```

**Delay:** 3 days

---

**Email 2 (Day 3) - The Math**

```
Subject: Re: Quick question about {{company}}

Hi {{firstName}},

Following up on my note about food waste recovery.

The math is simple:
• You're already making the food
• It's getting thrown away anyway  
• We help you sell it before closing time

You keep 80-90% of the recovery. We take a small commission.

One bakery client recovered $1,200 last month from items they were discarding.

5-minute chat to see if it fits your operation?

Best,
Mitch
```

**Delay:** 4 days

---

**Email 3 (Day 7) - Last Note**

```
Subject: Last note - Afoodable for {{company}}

Hi {{firstName}},

Last note on this.

If you're throwing away $50-200/day in unsold inventory, we should talk.

If not a priority right now, no worries — I'll check back in a few months.

Here's my calendar if you want to explore it: [Your Calendly Link]

Best,
Mitch

P.S. Even 5% recovery adds up to real profit over time.
```

---

### Task 6: Upload Leads

**Via Web UI:**
1. Click "Import Leads"
2. Upload `philly-ready.csv`
3. Map columns:
   - Email → Email
   - Restaurant Name → Company (or First Name)
   - Phone → Custom Variable
   - Website → Custom Variable

**Via API:**
```bash
python3 automation/instantly-v2.py bulk-upload \
  <campaign_id> \
  projects/afoodable-restaurant-outreach/philly-ready.csv
```

---

### Task 7: Final Review & Launch

**Pre-flight checklist:**
- [ ] 30+ leads with emails uploaded
- [ ] Email sequence configured (3 emails, proper delays)
- [ ] Sending schedule set (25/day, Mon-Fri, 10am-4pm)
- [ ] "Stop on reply" enabled
- [ ] Calendly link added to breakup email
- [ ] Preview first email (check personalization)

**Launch:**
- Click "Start Campaign"
- First emails send Monday 10am

---

## Week 1 Monitoring

### Daily Checks:
- **Monday 2pm:** Verify first batch sent (check Instantly dashboard)
- **Tuesday 10am:** Check for first opens/clicks
- **Wednesday:** Look for first replies
- **Thursday:** Respond to any interested leads
- **Friday:** Week 1 summary

### Track These Metrics:
- Emails sent: ___ / 50
- Open rate: ___%
- Reply rate: ___%
- Interested responses: ___
- Demos booked: ___

**Goal:** 5-8 interested responses in Week 1

---

## Response Handling

### "Interested" / "Tell me more"
→ Book 15-min call
→ Explain setup (10 min, then automated)
→ Show dashboard demo
→ Close or follow up

### "How much does it cost?"
→ "No upfront cost - we take 10-15% when you recover a sale"
→ "You only pay when you're already making money"

### "Sounds complicated"
→ "10-minute setup, then fully automated"
→ "We handle everything - you just set end-of-day pickup times"

### "Not interested" / No response
→ Tag in CRM
→ Follow up in 3 months

---

## Success Criteria

### Week 1 Goals:
- [ ] 50 emails sent
- [ ] 40%+ open rate
- [ ] 10%+ reply rate
- [ ] 3-6 interested responses
- [ ] 1-2 demos booked

### Month 1 Goals:
- [ ] 150 emails sent (3 sequences complete)
- [ ] 8-12 interested restaurants
- [ ] 4-6 demos completed
- [ ] **2-4 paying customers**

---

## Files You Need

**Lead Generation:**
- `philly-restaurants.csv` (raw)
- `philly-ready.csv` (with emails)

**Campaign Assets:**
- `email-sequences.md` (full templates)
- `READY-TO-LAUNCH.md` (overview)

**Tools:**
- `google-maps-scraper.py`
- `email-finder.py`
- `instantly-v2.py`

---

## Timeline

**Sunday:**
- 9am-12pm: Build/clean lead list
- 12pm-1pm: Find emails
- 1pm-2pm: Review and finalize

**Monday:**
- 9am-9:30am: Create Instantly campaign
- 9:30am-10am: Upload leads, launch
- 10am: First emails send
- Throughout week: Monitor and respond

---

## Quick Troubleshooting

**"Scraper didn't work"**
→ Use manual method (MANUAL-LEAD-BUILD-GUIDE.md)

**"Not enough emails found"**
→ That's OK - 30 with emails is enough to start
→ Focus on quality over quantity

**"How do I get campaign ID for API upload?"**
→ Create campaign in web UI first
→ Campaign ID is in the URL

**"What if nobody responds?"**
→ Week 1 is early
→ Most replies come Days 3-7
→ Patience - campaigns take 2-3 weeks to mature

---

**Status:** Everything ready. Just need to execute Sunday/Monday.

**Expected outcome:** 2-4 Afoodable customers by end of February.

**Let's go!** 🚀

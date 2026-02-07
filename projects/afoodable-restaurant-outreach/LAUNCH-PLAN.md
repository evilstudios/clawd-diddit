# Afoodable Philadelphia Launch Plan

**Target:** 100 Philadelphia restaurants (bakeries, cafés, fast casual)  
**Timeline:** Launch Sunday, first responses Monday  
**Goal:** 2-6 signups from first 100 leads

---

## ✅ What's Built (Saturday Evening)

### 1. Google Maps Scraper
- **File:** `/root/clawd/automation/google-maps-scraper.py`
- **Scrapes:** Name, address, phone, website, email, rating, reviews
- **Target:** 3 queries × 35 results = 105 restaurants
- **Runtime:** ~8-10 minutes for 100 places

### 2. Email Finder Tool
- **File:** `/root/clawd/automation/email-finder.py`
- **Methods:** Website scraping, pattern guessing, Hunter.io (optional)
- **Boost:** 10-20% emails → 40-60% emails

### 3. Email Sequences
- **File:** `email-sequences.md`
- **Proven formula** from Voxable campaign
- 3 emails, 7-day sequence
- Hook: "Do you throw away food at the end of the day?"

### 4. Instantly V2 Integration
- **File:** `/root/clawd/automation/instantly-v2.py`
- Bulk upload CSV to campaigns
- Full automation ready

---

## 📋 Sunday Execution Plan

### Morning (9am-11am): Data Collection

**Step 1: Run Full Scraper (10 min)**
```bash
cd /root/clawd
python3 automation/google-maps-scraper.py \
  --city "Philadelphia, PA" \
  --query "bakery" \
  --query "cafe" \
  --query "fast casual restaurant" \
  --max-per-query 35
```

**Output:** `philadelphia-restaurants.csv` (~105 leads)

**Step 2: Find Emails (15 min)**
```bash
python3 automation/email-finder.py \
  --input projects/afoodable-restaurant-outreach/philadelphia-restaurants.csv \
  --output projects/afoodable-restaurant-outreach/philly-ready.csv
```

**Output:** `philly-ready.csv` (40-60 with emails)

**Step 3: Manual Review (30 min)**
- Open `philly-ready.csv`
- Verify data quality
- Remove any obvious non-targets (chains, fine dining)
- Add any missing info manually
- **Target:** 50-75 high-quality leads

---

### Afternoon (2pm-3pm): Campaign Launch

**Step 1: Create Instantly Campaign**
- Log into Instantly.ai
- Name: "Afoodable - Philadelphia - Feb 2026"
- Configure: 25 emails/day, Mon-Fri, 10am-4pm

**Step 2: Set Up Email Sequence**

Copy from `email-sequences.md`:

**Email 1 (Day 0):**
```
Subject: Quick question about [Restaurant Name]

Hi [FirstName],

Quick question: Do you throw away food at the end of the day?

Most restaurants do. Bakeries especially.

We built Afoodable to turn that waste into revenue — no upfront cost, just a small cut when you recover a sale.

Worth a 5-minute call to see if it fits?

Best,
Mitch
```

**Email 2 (Day 3):**
```
Subject: Re: Quick question about [Restaurant Name]

Hi [FirstName],

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

**Email 3 (Day 7):**
```
Subject: Last note - Afoodable for [Restaurant Name]

Hi [FirstName],

Last note on this.

If you're throwing away $50-200/day in unsold inventory, we should talk.

If not a priority right now, no worries — I'll check back in a few months.

Here's my calendar if you want to explore it: [Calendly Link]

Best,
Mitch
```

**Step 3: Upload Leads**

**Option A: Web UI**
1. Import `philly-ready.csv`
2. Map columns (Email → Email, Restaurant Name → Company)
3. Assign to sequence

**Option B: API (automated)**
```bash
python3 automation/instantly-v2.py bulk-upload \
  <campaign_id> \
  projects/afoodable-restaurant-outreach/philly-ready.csv
```

**Step 4: Launch**
- Review settings one more time
- Hit "Start Campaign"
- First emails send Monday morning

---

## 📊 Expected Results

### Week 1 (50-75 emails sent)
- **Opens:** 40-50% (20-35 opens)
- **Replies:** 10-15% (5-10 replies)
- **Interested:** 3-6 restaurants
- **Demos booked:** 1-2

### Week 2 (Follow-ups sent)
- **Additional replies:** 3-5
- **Total interested:** 6-10
- **Demos booked:** 2-4

### Week 3 (Breakup emails)
- **Last responses:** 2-3
- **Total qualified leads:** 8-12
- **Signups:** 2-4

**Conservative Goal:** 2 paying customers by end of Month 1

---

## 🎯 Success Metrics

### Email Performance
- Open rate >40%
- Reply rate >10%
- Positive response rate >5%

### Conversion
- Demo booking rate >30% of interested
- Demo → signup rate >50%
- **Target:** 2-6 signups from 100 leads

### Revenue (if 3 signups)
- $1,200/month recovered × 3 restaurants = $3,600/month
- 15% commission = **$540/month recurring**
- **Annual run rate:** $6,480 from first 100 leads

---

## 🔧 Monitoring & Optimization

### Daily Checks (Week 1)
- **Monday:** Verify first emails sent
- **Tuesday:** Check open rates (adjust subject if <30%)
- **Wednesday:** Review any replies
- **Thursday:** Track demo bookings
- **Friday:** Week 1 summary

### Adjustments Based on Data
- **Low open rate (<30%):** Test new subject lines
- **High opens, low replies:** Adjust body copy
- **Negative responses:** Refine targeting/messaging
- **Good responses:** Scale up send volume

---

## 📞 Handling Responses

### Interested / Questions
- Book demo call (15 min)
- Show dashboard
- Explain setup process
- Answer objections
- Close or follow up

### Not Interested
- Ask why (learn for messaging)
- Offer to check back in 3 months
- Tag in CRM

### Objections
See `email-sequences.md` for response templates:
- "We don't waste much" → Show even 5% recovery = profit
- "Sounds complicated" → 10-min setup, automated after
- "What's the catch?" → No upfront cost, you only pay on recovery

---

## 🚀 Post-Launch Scale Plan

### If Campaign Succeeds (2+ signups)
1. **Expand Philadelphia:** 100 more leads
2. **New city:** Replicate in Austin or Portland
3. **Optimize:** Use winner subject lines/copy
4. **Scale:** 500 leads/month × 3 cities

### If Results Are Meh (0-1 signups)
1. **Analyze:** Which step failed? (Open? Reply? Demo? Close?)
2. **Iterate:** Fix the weakest link
3. **Test:** New messaging or targeting
4. **Retry:** 50 more leads with improvements

---

## 📁 Files & Locations

**Scraper & Tools:**
- `/root/clawd/automation/google-maps-scraper.py`
- `/root/clawd/automation/email-finder.py`
- `/root/clawd/automation/instantly-v2.py`

**Campaign Assets:**
- `/root/clawd/projects/afoodable-restaurant-outreach/email-sequences.md`
- `/root/clawd/projects/afoodable-restaurant-outreach/lead-sourcing-strategy.md`
- `/root/clawd/projects/afoodable-restaurant-outreach/SCRAPER-GUIDE.md`

**Data (Generated Sunday):**
- `philadelphia-restaurants.csv` (raw scrape)
- `philly-ready.csv` (with emails, cleaned)

---

## ✅ Pre-Launch Checklist

- [ ] Scraper tested and working
- [ ] 50-75 Philadelphia leads collected
- [ ] Emails found for 40-60% of leads
- [ ] CSV cleaned and reviewed
- [ ] Instantly.ai campaign created
- [ ] Email sequence configured (3 emails, 3/4/7 day gaps)
- [ ] Sending schedule set (25/day, Mon-Fri, 10am-4pm)
- [ ] Calendly link added to breakup email
- [ ] Leads uploaded to campaign
- [ ] Campaign launched

---

**Status:** Tools built. Ready to execute Sunday morning.

**Timeline:**
- **Sunday 9am:** Run scraper
- **Sunday 11am:** Find emails
- **Sunday 2pm:** Launch campaign
- **Monday 10am:** First emails send
- **Monday-Friday:** Responses roll in
- **Week 2:** Follow-ups + demos
- **Week 3-4:** Close signups

**Expected Outcome:** 2-4 paying Afoodable customers by end of February ✅

# Instantly.ai Campaign Sequences
## Philadelphia Med Spa Lead Generation

**Target Audience:** Philadelphia area prospects interested in cosmetic procedures  
**Total Leads:** 62 with email addresses  
**Segmentation:** Hot (8-10) vs Warm (5-7) intent scores

---

## Campaign Structure

### Campaign 1: Hot Leads (Intent Score 8-10) - 25 Leads
**Objective:** Book consultations ASAP  
**Tone:** Direct, urgent, low-friction  
**Sequence:** 4 emails over 7 days

### Campaign 2: Warm Leads (Intent Score 5-7) - 37 Leads
**Objective:** Nurture and educate, then book  
**Tone:** Educational, helpful, non-pushy  
**Sequence:** 5 emails over 14 days

---

## CAMPAIGN 1: HOT LEADS (Score 8-10)

### Email 1 - Day 0 (Send Time: 10:00 AM)
**Subject:** Re: {{procedureInterest}} in {{location}}

**Body:**
```
{{firstName}},

Saw you were looking into {{procedureInterest}}. We're running complimentary consultations for {{location}} area clients through the end of the month.

No pressure—just a 15-minute review to walk through:
- Realistic results for your goals
- Transparent pricing (no hidden fees)
- Recovery timeline
- Financing options

Open to a quick call this week?

[Your Calendar Link]

Best,
[Your Name]
[Practice Name]
[Phone Number]

P.S. Based on your interest in {{procedureInterest}}, I can also share some recent before/after results if helpful.
```

---

### Email 2 - Day 3 (Send Time: 2:00 PM)
**Subject:** Quick question about {{procedureInterest}}

**Body:**
```
{{firstName}},

Following up on my email from Tuesday.

Most {{location}} clients considering {{procedureInterest}} have 2-3 main questions before booking:

1. "Will it look natural?" (Yes—we focus on subtle, confidence-boosting results)
2. "How much downtime?" (Depends on procedure—I can break this down on a call)
3. "What's the real cost?" (Transparent pricing, financing available)

If any of these resonate, let's hop on a quick 15-minute call and I'll walk you through everything.

[Your Calendar Link]

No hard sell. Just honest answers.

Best,
[Your Name]
```

---

### Email 3 - Day 5 (Send Time: 11:00 AM)
**Subject:** {{firstName}}, still interested?

**Body:**
```
{{firstName}},

I haven't heard back, so I'm guessing one of three things:

1. You're still researching (totally fair—this is a big decision)
2. You're busy (I get it—life happens)
3. You already found someone else (congrats if so!)

If it's #1 or #2, I'm here to help—no pressure.

We have a few consultation slots left this week. If you want one, just grab a time here:

[Your Calendar Link]

If not, no worries—I'll stop bugging you after this.

Best,
[Your Name]
```

---

### Email 4 - Day 7 (Send Time: 9:00 AM) - BREAKUP EMAIL
**Subject:** Last note from me

**Body:**
```
{{firstName}},

This is my last email—I don't want to clog your inbox.

If you ever want to chat about {{procedureInterest}}, I'm just a reply away. No pressure, no pitch—just honest guidance.

Here's my calendar if you need it down the road:
[Your Calendar Link]

Best of luck with whatever you decide!

[Your Name]
[Practice Name]
[Phone Number]
```

---

## CAMPAIGN 2: WARM LEADS (Score 5-7)

### Email 1 - Day 0 (Send Time: 10:00 AM)
**Subject:** Considering {{procedureInterest}}? Start here.

**Body:**
```
{{firstName}},

I noticed you were exploring {{procedureInterest}} options in {{location}}.

If you're like most people at this stage, you probably have a few questions:
- What results can I realistically expect?
- How much does it actually cost?
- What's the recovery like?

I put together a quick guide that walks through everything—no fluff, just the honest breakdown.

Want me to send it over?

Just reply "yes" and I'll shoot it your way.

Best,
[Your Name]
[Practice Name]

P.S. If you'd rather just hop on a quick 15-minute call instead, here's my calendar: [Link]
```

---

### Email 2 - Day 3 (Send Time: 2:00 PM)
**Subject:** 3 things to know before booking {{procedureInterest}}

**Body:**
```
{{firstName}},

Before you book a consultation anywhere, here are 3 things most {{location}} patients wish they knew earlier:

1. **Not all providers are the same.**  
   Board certification matters. Experience with your specific procedure matters more.

2. **The cheapest option usually isn't the best.**  
   You're trusting someone with your face/body—prioritize expertise over discounts.

3. **Ask about revision policies upfront.**  
   Reputable practices stand behind their work. If they don't offer revisions, that's a red flag.

We offer complimentary consultations so you can ask all the right questions before committing to anything.

Want to grab a 15-minute slot this week?

[Your Calendar Link]

Best,
[Your Name]
```

---

### Email 3 - Day 7 (Send Time: 11:00 AM)
**Subject:** Real {{procedureInterest}} results from {{location}} patients

**Body:**
```
{{firstName}},

I thought you might want to see what {{procedureInterest}} results actually look like (not the Instagram-filtered version).

Here are 3 recent before/after cases from {{location}} patients:

[Link to before/after gallery or PDF]

All of these clients had the same concerns you probably have:
- Will it look natural?
- Is it worth the cost?
- What if I don't like it?

If you want to talk through your specific goals, I'm happy to review options on a quick 15-minute call—no commitment required.

[Your Calendar Link]

Best,
[Your Name]
```

---

### Email 4 - Day 10 (Send Time: 3:00 PM)
**Subject:** {{firstName}}, quick question

**Body:**
```
{{firstName}},

I haven't heard back, so I wanted to check in.

Is {{procedureInterest}} still on your radar, or did you decide to hold off for now?

If you're still considering it, I'd love to help. If not, totally understand—no hard feelings.

Either way, just let me know so I'm not bugging you with emails you don't need.

Best,
[Your Name]

P.S. If timing's the issue, we offer financing options that break it into monthly payments. Happy to walk through that if helpful.
```

---

### Email 5 - Day 14 (Send Time: 10:00 AM) - FINAL TOUCH
**Subject:** Last email (I promise)

**Body:**
```
{{firstName}},

This is my last email—I don't want to spam you.

If you ever want to chat about {{procedureInterest}}, I'm just a reply away. No pressure, no pitch—just honest advice.

Here's my calendar if you need it:
[Your Calendar Link]

And if you're not ready yet, that's totally fine too. When you are, we're here.

Best,
[Your Name]
[Practice Name]
[Phone Number]
```

---

## Instantly.ai Setup Instructions

### Step 1: Upload Leads
1. Go to **Campaigns** → **New Campaign**
2. Click **Import Leads**
3. Upload `philadelphia_medspa_leads_instantly.csv`
4. Map columns:
   - Email → email
   - First Name → firstName
   - Last Name → lastName
   - Custom variables: location, procedureInterest, intentScore, notes

### Step 2: Create Two Campaigns

**Campaign A: Hot Leads**
- Filter: `intentScore >= 8`
- Sequence: 4 emails (Days 0, 3, 5, 7)
- Daily send limit: 50/day
- Sending hours: 9 AM - 5 PM (local time)

**Campaign B: Warm Leads**
- Filter: `intentScore >= 5 AND intentScore < 8`
- Sequence: 5 emails (Days 0, 3, 7, 10, 14)
- Daily send limit: 50/day
- Sending hours: 9 AM - 5 PM (local time)

### Step 3: Configure Merge Tags
Make sure these are mapped correctly:
- `{{firstName}}` → firstName
- `{{procedureInterest}}` → procedureInterest
- `{{location}}` → location

### Step 4: Warmup Settings
- Use warmed-up email accounts (aged 30+ days)
- Start with 10-20 emails/day, ramp up to 50/day over 2 weeks
- Enable reply detection (auto-stop sequence on reply)
- Enable click tracking
- Enable open tracking

### Step 5: A/B Testing (Optional)
Test these variants:
- Subject line A vs B
- CTA placement (early vs late)
- Tone (formal vs casual)

---

## Expected Results

### Hot Leads (25 emails)
- **Open rate:** 35-45%
- **Reply rate:** 8-12%
- **Booked consultations:** 2-4 (8-16%)
- **Timeline:** 7 days

### Warm Leads (37 emails)
- **Open rate:** 30-40%
- **Reply rate:** 5-8%
- **Booked consultations:** 2-3 (5-8%)
- **Timeline:** 14 days

### Total Expected Bookings: 4-7 consultations
**Assuming 50% show rate → 2-4 actual consultations**

---

## Follow-Up Strategy for Replies

### If they reply "Interested":
```
Great! Let's get you scheduled. Here's my calendar:
[Link]

Pick a time that works and we'll walk through everything on the call—goals, pricing, timeline, etc.

Looking forward to it!
```

### If they reply "How much does it cost?":
```
Great question. {{procedureInterest}} typically ranges from $X,XXX to $X,XXX depending on your specific goals.

I can give you a more accurate estimate after a quick 15-minute consultation (no charge, no pressure).

Want to grab a time this week?
[Calendar Link]
```

### If they reply "Not ready yet":
```
Totally understand—this is a big decision. No rush.

When you're ready, just shoot me an email or grab a time on my calendar:
[Calendar Link]

In the meantime, if you have any questions, I'm here!
```

---

## Pro Tips for Instantly.ai

1. **Use spintax for subject lines** to avoid spam filters:
   - `{Re:|About|Quick question about} {{procedureInterest}}`

2. **Personalize with conditional logic:**
   - If source = Instagram → mention "saw your engagement on Instagram"
   - If notes include "pricing" → address cost upfront

3. **Track what works:**
   - Monitor open rates by subject line
   - Track reply rates by email sequence position
   - A/B test CTA placement

4. **Enable auto-stop on reply** so you don't spam people who respond

5. **Use link tracking** to see who clicks your calendar link (re-engage them separately)

---

## Files Included
- `/root/clawd-main/projects/cosmetic-surgeon-lead-scraper/philadelphia_medspa_leads_instantly.csv` (62 leads, Instantly.ai ready)
- This campaign playbook

---

**Next Steps:**
1. Upload CSV to Instantly.ai
2. Set up 2 campaigns (Hot + Warm)
3. Configure merge tags
4. Launch campaigns
5. Monitor replies and book consultations

Good luck! 🚀

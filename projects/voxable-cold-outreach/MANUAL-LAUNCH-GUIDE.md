# Voxable Campaign - Manual Launch Guide

**Time to Complete:** 15 minutes  
**Date:** Friday, February 6, 2026

---

## Step 1: Prepare Your Leads CSV (2 minutes)

You'll need a CSV file with these columns:
```
email,firstName,lastName,company,website
```

**Option A: Use Sample Template**
Create a file called `voxable-leads.csv` with this format:

```csv
email,firstName,lastName,company,website
john@example.com,John,Smith,Acme Corp,acme.com
jane@example.com,Jane,Doe,Tech Inc,techinc.com
```

**Option B: If you already have your leads:**
- Make sure the CSV has those exact column headers
- Save it as `voxable-leads.csv`

---

## Step 2: Log Into Instantly.ai (1 minute)

1. Go to: https://app.instantly.ai
2. Log in with your credentials
3. You should see your dashboard

---

## Step 3: Create New Campaign (2 minutes)

1. Click **"Campaigns"** in the left sidebar
2. Click **"+ New Campaign"** (top right)
3. Campaign Settings:
   - **Name:** `Voxable - AI Voice Agent Outreach`
   - **Daily Limit:** 40 emails per day
   - **Sending Schedule:** 
     - Monday-Friday
     - 9:00 AM - 5:00 PM (your timezone)
   - **Timezone:** Select your timezone
4. Click **"Continue"** or **"Next"**

---

## Step 4: Upload Leads (2 minutes)

1. You'll see **"Add Leads"** or **"Upload CSV"**
2. Click **"Upload CSV"**
3. Select your `voxable-leads.csv` file
4. Map columns:
   - Email → email
   - First Name → firstName
   - Last Name → lastName
   - Company → company
   - Website → website
5. Click **"Import"** or **"Upload"**
6. Verify lead count (should show ~230 leads)

---

## Step 5: Add Email Sequences (5 minutes)

You'll create 3 emails (Initial + 2 Follow-ups).

### **Email 1: Initial Outreach** (Wait: 0 days)

**Subject Line Options (Instantly will A/B test these):**
```
{{firstName}}, quick question about {{company}}'s customer support
AI voice agents for {{company}}?
How {{company}} handles after-hours calls
```

**Email Body:**
```
Hi {{firstName}},

I noticed {{company}} is growing fast, and I'm guessing your team is getting slammed with customer calls.

Most teams handle this by:
1. Hiring more reps (expensive)
2. Letting calls go to voicemail (bad experience)
3. Using chatbots (frustrating for customers)

There's a fourth option: AI voice agents that actually sound human.

They handle:
- After-hours calls
- Overflow during busy times
- Simple questions (so your team can focus on complex issues)

**Real use case:** One of our clients went from 40% missed calls to 0% in 30 days.

Interested in a 5-min demo?

Best,
Mitch
```

---

### **Email 2: Follow-Up #1** (Wait: 3 days after Email 1)

**Subject Line:**
```
Re: {{firstName}}, quick question about {{company}}'s customer support
```

**Email Body:**
```
Hi {{firstName}},

Following up on my email from Tuesday.

Just to clarify – this isn't a chatbot. It's a voice AI that:
- Answers calls like a real person
- Handles FAQs, scheduling, and routing
- Works 24/7 (no breaks, no sick days)

**Quick stats:**
- 90% of callers can't tell it's AI
- $500-$1,500/month (vs $3,000+/month for a human)
- Set up in 48 hours

Worth a quick chat?

Best,
Mitch
```

---

### **Email 3: Follow-Up #2** (Wait: 4 days after Email 2)

**Subject Line:**
```
Last note - AI for {{company}}
```

**Email Body:**
```
Hi {{firstName}},

I'll keep this short.

If you're dealing with:
- Missed calls hurting revenue
- Long hold times frustrating customers
- Support costs eating your margins

We should talk.

15-minute demo, zero pressure.

Here's my calendar: [YOUR CALENDLY LINK]

Best,
Mitch

P.S. If this isn't a priority right now, just let me know and I'll check back in Q3.
```

---

## Step 6: Configure Campaign Settings (2 minutes)

Before launching, verify these settings:

**Sending Settings:**
- ✅ Daily limit: 40 emails/day
- ✅ Schedule: Mon-Fri, 9am-5pm
- ✅ Timezone: Correct
- ✅ Stop on reply: YES (important!)

**Tracking:**
- ✅ Track opens: YES
- ✅ Track clicks: YES
- ✅ Track replies: YES

**Unsubscribe:**
- ✅ Include unsubscribe link: YES (legal requirement)

---

## Step 7: Preview & Test (1 minute)

1. Click **"Preview"** to see how emails look
2. Send a test email to yourself
3. Check:
   - Variables populate correctly ({{firstName}}, etc.)
   - Links work
   - Formatting looks good
   - Unsubscribe link present

---

## Step 8: LAUNCH! (1 minute)

1. Click **"Launch Campaign"** or **"Start Sending"**
2. Confirm launch
3. **🎉 You're live!**

---

## What Happens Next

### First 24 Hours:
- Instantly will start sending (up to 40 emails)
- Opens/clicks tracked in real-time
- Replies will come to your connected email

### First Week:
- Monitor reply rate (target: 5-10%)
- Check open rate (target: 40-60%)
- Adjust subject lines if needed

### Expected Results (30 days):
- **230 leads contacted**
- **~12-20 replies** (5-10% reply rate)
- **~3-5 meetings booked** (assuming 25% of replies convert)

---

## Monitoring Dashboard

Log into Instantly.ai daily to check:
- **Sends:** How many emails went out today
- **Opens:** Who opened (see companies)
- **Clicks:** Who clicked links
- **Replies:** New conversations (respond within 2 hours!)

---

## Responding to Replies

### Positive Reply (Interested):
```
Great! Here's my calendar: [CALENDLY LINK]

Pick a time that works for you, and I'll walk you through a live demo.

Looking forward to it!
```

### Neutral Reply (Want more info):
```
Happy to share more details.

Quick question: What's your biggest support challenge right now?
- Missed calls?
- Long hold times?
- After-hours coverage?

That'll help me tailor the demo to your specific needs.
```

### Negative Reply (Not interested):
```
No worries! If anything changes, feel free to reach out.

Quick question before I go: Is this not a priority, or just not the right time?
```

---

## Troubleshooting

**Emails not sending?**
- Check email account is connected in Instantly
- Verify warmup is complete (if new account)
- Check daily limit hasn't been hit

**Low open rates (<30%)?**
- Try different subject lines
- Check spam score (Instantly has a tool)
- Verify leads have valid emails

**No replies after 1 week?**
- Normal! Give it 2-3 weeks
- Try adding a 4th follow-up email
- Consider calling high-value leads

---

## Post-Launch Checklist

After launching, do these:

✅ Set calendar reminder to check Instantly daily  
✅ Prepare Calendly link for booking demos  
✅ Draft response templates (save time)  
✅ Set up CRM to track leads (HubSpot, Pipedrive, etc.)  
✅ Create demo script/slides  

---

## Next Steps

Once campaign is live:

1. **Monitor for 48 hours** - See initial response
2. **Respond to replies FAST** - Within 2 hours if possible
3. **Book meetings** - Use Calendly to schedule demos
4. **Track results** - Document what works

---

## Need Help?

If you hit any snags:
- Instantly.ai support: support@instantly.ai
- Or just ping me and I'll troubleshoot with you

---

**Let's get this launched! 🚀**

You've got everything you need above. Should take ~15 minutes start to finish.

Let me know when you're live!

- Portifoy ⚡🦗

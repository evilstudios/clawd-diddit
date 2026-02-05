# Voxable Cold Outreach Automation

Complete toolkit for launching and managing Voxable cold email campaigns via Instantly.ai

## 🚀 Quick Start

### 1. Get Your Instantly.ai API Key
1. Log into Instantly.ai
2. Go to Settings → API
3. Copy your API key
4. Set environment variable:
```bash
export INSTANTLY_API_KEY="your_api_key_here"
```

### 2. Prepare Your Lead List

**CSV Format (recommended):**
```csv
email,first_name,last_name,company_name,phone,website
john@example.com,John,Doe,Doe Plumbing,555-1234,doeplumbing.com
```

**Required fields:**
- `email` - Lead email address
- `first_name` - First name for personalization
- `company_name` - Company name for personalization

**Optional fields:**
- `last_name` - Last name
- `phone` - Phone number
- `website` - Company website
- Any custom fields you want

**JSON Format (alternative):**
```json
{
  "leads": [
    {
      "email": "john@example.com",
      "first_name": "John",
      "company_name": "Doe Plumbing"
    }
  ]
}
```

### 3. Launch Campaign

**Dry run first (preview only):**
```bash
./automation/instantly-campaign-launcher.py \
  --leads leads/voxable-prospects.csv \
  --dry-run
```

**Launch for real:**
```bash
./automation/instantly-campaign-launcher.py \
  --leads leads/voxable-prospects.csv \
  --campaign-name "Voxable - Local Service - Feb 2025"
```

**The script will:**
✅ Create campaign in Instantly.ai
✅ Upload all leads
✅ Show you the email sequences to configure
✅ Provide setup checklist

### 4. Configure in Instantly.ai Dashboard

After running the launcher, go to Instantly.ai and:

1. **Add Email Sequences** (copy from script output):
   - Email 1 (Day 1): Missed calls hook
   - Email 2 (Day 3): Value prop + hiring trap
   - Email 3 (Day 7): Breakup email

2. **Configure Sending Schedule:**
   - Days: Monday-Friday
   - Hours: 9am-5pm (recipient timezone)
   - Max emails/day: 30-40
   - Delays: 2-5 minutes between sends

3. **Set Auto-Stop Rules:**
   - ✅ Stop if lead replies
   - ✅ Stop if lead clicks + opens
   - ✅ Stop after sequence ends

4. **Start Small:**
   - Test with 10-20 leads first
   - Monitor deliverability
   - Scale up once confirmed working

### 5. Monitor Performance

**View dashboard:**
```bash
./automation/voxable-lead-tracker.py \
  --campaign "Voxable - Local Service - Feb 2025" \
  --dashboard
```

**Export replies to CSV:**
```bash
./automation/voxable-lead-tracker.py \
  --campaign "Voxable - Local Service - Feb 2025" \
  --export-replies replies.csv
```

**Daily digest:**
```bash
./automation/voxable-lead-tracker.py \
  --campaign "Voxable - Local Service - Feb 2025" \
  --daily-digest
```

---

## 📊 Expected Performance

### Good Results (230 leads):
- **Open Rate:** 40-50%
- **Reply Rate:** 5-8%
- **Positive Replies:** 8-12 leads
- **Demos Booked:** 4-8 demos
- **Expected Conversions:** 1-3 customers

### Great Results (230 leads):
- **Open Rate:** 50-60%+
- **Reply Rate:** 10-15%
- **Positive Replies:** 15-23 leads
- **Demos Booked:** 8-15 demos
- **Expected Conversions:** 3-7 customers

---

## 📝 Email Sequences

### Email 1 - Day 1: "Missed Call" Hook
**Subject:** Quick question about missed calls at {{company_name}}

Hits the pain point immediately - local businesses lose 20-30% of calls when busy.

**Call to Action:**
- 5-minute call to discuss
- Try the AI: 267-550-0466

### Email 2 - Day 3: "Hiring Trap"
**Subject:** Scaling {{company_name}} without the extra payroll

Addresses the "can't afford a receptionist" objection.

**Call to Action:**
- 2-minute demo
- Book a time to chat

### Email 3 - Day 7: "Breakup"
**Subject:** Should I take you off my list, {{first_name}}?

Low-pressure exit that keeps the door open.

**Call to Action:**
- Link to demo
- Option to reply anytime

---

## 🎯 Response Handling

### Positive Reply ("Tell me more")
**Template:**
```
Great! Two quick ways to see it in action:

1. Call our AI right now: 267-550-0466 (experience what your customers would)
2. Book a 5-min demo: [Calendar link]

Which works better for you?
```

### Pricing Question
**Template:**
```
Good question! The investment is significantly less than hiring a part-time 
receptionist (typically $300-600/month depending on your volume).

Most clients see ROI in the first month from the leads they would've otherwise lost.

Want to hop on a quick call to discuss {{company_name}}'s specific setup? [Book here]
```

### "Not Interested"
**Template:**
```
No worries at all, {{first_name}}! Appreciate you letting me know.

Mind if I check back in 3-6 months in case things change?

Either way, best of luck with {{company_name}}!
```

### "Too Busy Right Now"
**Template:**
```
Totally understand - I know how it goes.

If things calm down or this becomes a priority, feel free to reach back out anytime.

In the meantime, here's a quick tip: [Link to free resource about lead response time]
```

---

## 🔧 Advanced Configuration

### Custom Campaign Name
```bash
./automation/instantly-campaign-launcher.py \
  --leads leads.csv \
  --campaign-name "My Custom Campaign"
```

### List Existing Campaigns
```bash
./automation/instantly-campaign-launcher.py \
  --api-key YOUR_KEY \
  --list-campaigns
```

### A/B Testing Subject Lines
In Instantly.ai dashboard:
1. Create campaign variants
2. Test these subject lines:
   - "Quick question about missed calls at {{company_name}}"
   - "{{first_name}}, are you losing 20-30% of your incoming calls?"
   - "Missed call = missed paycheck at {{company_name}}?"
3. Auto-select winner after 50 sends

---

## 🚨 Troubleshooting

### Low Open Rate (<30%)
**Likely causes:**
- Subject line too salesy
- Sender email has low reputation
- Emails going to spam

**Solutions:**
- Warm up sender email first
- Test different subject lines
- Check spam score at mail-tester.com

### Low Reply Rate (<3%)
**Likely causes:**
- Email too long
- Value prop unclear
- Weak call-to-action

**Solutions:**
- Shorten email 1
- Make CTA more specific
- Add urgency/scarcity

### Getting Angry Replies
**Likely causes:**
- Wrong target audience
- Too aggressive tone
- Sending too frequently

**Solutions:**
- Review lead list quality
- Soften messaging
- Reduce send frequency

---

## 📅 Ongoing Management

### Daily:
- Check replies
- Respond to interested leads
- Book demos

### Weekly:
- Review dashboard metrics
- Adjust subject lines if needed
- A/B test improvements

### Monthly:
- Analyze conversion rates
- Refresh lead list
- Update sequences based on learnings

---

## 🔐 Security Notes

- **Never commit API keys** - use environment variables
- **GDPR compliance** - only email B2B contacts
- **CAN-SPAM compliance** - include unsubscribe option
- **Keep lead data secure** - don't share CSVs publicly

---

## 📞 Support

**Instantly.ai Issues:**
- Check their API docs: https://developer.instantly.ai
- Support: support@instantly.ai

**Voxable Questions:**
- Demo line: 267-550-0466
- Pricing/features: [Your contact info]

---

## ✅ Checklist

**Before Launch:**
- [ ] API key configured
- [ ] Lead list validated (emails + names)
- [ ] Dry run successful
- [ ] Email sequences reviewed
- [ ] Sending schedule configured
- [ ] Auto-stop rules set
- [ ] Test batch sent (10-20 leads)

**After Launch:**
- [ ] Monitor daily for first week
- [ ] Respond to all replies within 2 hours
- [ ] Track conversion metrics
- [ ] Adjust based on performance
- [ ] Scale up gradually

**Ongoing:**
- [ ] Check dashboard daily
- [ ] Export replies weekly
- [ ] Update sequences monthly
- [ ] Refresh lead list as needed

---

Good luck! 🚀

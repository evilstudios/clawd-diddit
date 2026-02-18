# Afoodable Campaign - Email Forwarding Setup

**Campaign emails:** jessica@ecostratagem.com, kenneth@ecostratagem.com  
**Goal:** Route all replies to your main inbox automatically

---

## Option 1: Gmail Forwarding (Recommended)

### For jessica@ecostratagem.com:

1. **Login to Gmail** as jessica@ecostratagem.com
2. Click **Settings** (gear icon) → **See all settings**
3. Go to **Forwarding and POP/IMAP** tab
4. Click **Add a forwarding address**
5. Enter your main email (e.g., mitch@evilstudios.com)
6. Click **Next** → **Proceed** → **OK**
7. Check your main inbox for verification email
8. Click verification link in that email
9. Back in jessica's settings, select **Forward a copy of incoming mail to [your email]**
10. Choose: **keep Gmail's copy in the Inbox** (so you have backup)
11. Click **Save Changes**

### For kenneth@ecostratagem.com:

Repeat steps 1-11 above

---

## Option 2: Gmail Filters (If You Want Selective Forwarding)

If you only want to forward **replies to Afoodable campaign** (not all emails):

### For jessica@ecostratagem.com:

1. Login to Gmail as jessica@ecostratagem.com
2. Click **Settings** → **See all settings**
3. Go to **Filters and Blocked Addresses** tab
4. Click **Create a new filter**
5. In **Subject** field, enter keywords from your campaign:
   - "Re: " (catches all replies)
   - Or specific subject lines from your sequence
6. Click **Create filter**
7. Check **Forward it to:** and select your main email
8. Check **Apply the filter to matching conversations** (applies to existing)
9. Click **Create filter**

### For kenneth@ecostratagem.com:

Repeat steps 1-9 above

---

## Option 3: Instantly.ai Webhook (Advanced)

If Instantly.ai has webhook support:

1. Go to Instantly.ai → Campaign Settings
2. Look for **Webhooks** or **Integrations**
3. Set webhook URL to forward replies to your system
4. Parse incoming replies and forward to main inbox

**Note:** Check if Instantly has native reply forwarding in settings first.

---

## Option 4: Email Client Auto-Forward Rules

### Apple Mail:
1. Add jessica@ecostratagem.com and kenneth@ecostratagem.com accounts
2. Create rule: Forward all incoming to main email
3. Keep Mail.app running on a device

### Outlook/Thunderbird:
Similar rule-based forwarding available

---

## Testing Forwarding

After setup:

1. Send test email to jessica@ecostratagem.com
2. Reply to that email from another account
3. Verify reply arrives in your main inbox
4. Repeat for kenneth@ecostratagem.com

---

## Recommended: Set Up Reply-To Header

In Instantly.ai campaign settings:

1. Go to Campaign → Email Settings
2. Look for **Reply-To** field
3. Set: `mitch@evilstudios.com` (your main email)
4. Now when prospects hit "Reply", it goes directly to you

**This is the cleanest solution** - no forwarding needed!

---

## Inbox Organization

Once forwarding is set up, create labels/folders in your main inbox:

### Gmail Labels:
- `Afoodable/Jessica Replies`
- `Afoodable/Kenneth Replies`
- `Afoodable/Hot Leads`
- `Afoodable/Booked Demos`

### Filter Setup:
1. Create filter: From `jessica@ecostratagem.com`
2. Apply label: `Afoodable/Jessica Replies`
3. Star the conversation
4. Repeat for Kenneth

---

## Daily Monitoring Checklist

**Morning (9am EST):**
- [ ] Check jessica@ecostratagem.com inbox
- [ ] Check kenneth@ecostratagem.com inbox
- [ ] Review forwarded emails in main inbox
- [ ] Respond to any replies within 2 hours

**Evening (5pm EST):**
- [ ] Check both inboxes again
- [ ] Respond to any new replies
- [ ] Log replies in tracking spreadsheet

---

## Troubleshooting

**Issue: Forwarding not working**
- Check spam folder in main inbox
- Verify forwarding address is confirmed
- Check Gmail forwarding limit (500 emails/day)

**Issue: Replies going to spam**
- Add jessica@ecostratagem.com and kenneth@ecostratagem.com to contacts
- Mark forwarded emails as "Not Spam"
- Create filter to never send to spam

**Issue: Can't access jessica/kenneth accounts**
- Get credentials from Instantly.ai account
- Or check password manager

---

## Security Note

Since these are campaign accounts:
- Use strong unique passwords
- Enable 2FA if possible
- Don't use for personal communication
- Monitor for unauthorized access

---

## Quick Start (5 Minutes)

**Fastest path:**

1. Login to Instantly.ai
2. Go to campaign settings
3. Set **Reply-To: your-main-email@domain.com**
4. Save

Done! All replies now route to your main inbox automatically.

---

**Recommendation:** Use Reply-To method (5 min) + Gmail forwarding as backup (10 min). Best of both worlds.

# Zendesk Macros Setup Guide

**For:** Evil Apples Support (evilstudios.zendesk.com)  
**Purpose:** Create saved replies for common support scenarios

---

## 📌 What Are Macros?

Macros are **saved replies** in Zendesk that let you respond to common issues with one click. They can:
- Insert pre-written text
- Update ticket status
- Add tags
- Assign tickets
- Trigger notifications

---

## 🛠️ How to Create Macros

1. **Go to:** Admin Center → Objects and Rules → Macros
2. **Click:** "Add macro"
3. **Configure:**
   - **Title:** What agents see (e.g., "Android Chat Bug Response")
   - **Actions:** What happens when you apply the macro
   - **Comment:** The response text (with placeholders)

---

## 🎯 Recommended Macros for Evil Apples

### **MACRO 1: Android Chat Bug (Critical)**

**Title:** `Android Chat Bug - Fix in Progress`

**Actions:**
- Set Status → Pending
- Add Tags → `android_chat_bug`, `critical`
- Set Priority → High

**Comment/Response:**
```
Hi {{ticket.requester.first_name}},

Thanks for reporting this! You're absolutely right — there's a bug affecting Android users where the system navigation bar is blocking the chat input and send button.

**Good news:** Our dev team is working on a fix right now. This is our top priority, and we're aiming to have it resolved in the next 48-72 hours.

**What's happening:**
A recent update inadvertently caused the chat UI to be hidden behind the navigation bar on certain Android devices. We've identified the issue and are testing a fix now.

**We'll notify you as soon as the update is live.** In the meantime, thanks for your patience and for sticking with us! Your feedback as a beta tester is incredibly valuable.

If you have any other feedback or issues, feel free to reach out!

Best,
{{current_user.name}}
Evil Apples Support Team
```

---

### **MACRO 2: "Must Be Logged In" Error**

**Title:** `Login Error - Troubleshooting Steps`

**Actions:**
- Set Status → Pending
- Add Tags → `login_error`, `troubleshooting_sent`

**Comment/Response:**
```
Hi {{ticket.requester.first_name}},

Sorry you're seeing that frustrating error! This usually happens when there's a temporary session issue between the app and our servers.

**Here's how to fix it:**

1. **Force close** the app completely (don't just minimize it)
2. **Clear the app cache:**
   - **iOS:** Settings > General > iPhone Storage > Evil Apples > Offload App (then reinstall)
   - **Android:** Settings > Apps > Evil Apples > Storage > Clear Cache
3. **Restart your device**
4. **Open the app** and log in again using your preferred method (email, SMS, or Game Center)

**If that doesn't work:**
- Try logging out and back in using the **email magic link** method (we'll send you a login link)
- Make sure you're on the latest version of the app (check your app store for updates)

Let me know if you're still seeing the error after trying these steps, and I'll dig deeper!

Best,
{{current_user.name}}
Evil Apples Support Team
```

---

### **MACRO 3: Account Recovery - Info Request**

**Title:** `Account Recovery - Need More Info`

**Actions:**
- Set Status → Pending
- Add Tags → `account_recovery`, `awaiting_info`

**Comment/Response:**
```
Hi {{ticket.requester.first_name}},

I can help you recover your account! First, let me check what we can find.

**To locate your account, I need a bit more info:**

1. **What email address or phone number** did you originally use?
2. **What was your username** in the game?
3. **Do you remember any decks or purchases** you had?
4. **What device/platform** did you play on originally? (iOS or Android)

**Important to know:**
- If your account was **only backed up to Game Center or Google Play** and you switched devices, we may not be able to recover it if it wasn't linked to an email/SMS.
- If you had **in-app purchases**, we can verify them through Apple/Google receipts.

**Once I have this info, I'll do my best to track down your account and get you back in the game!**

In the meantime, here's how to **prevent this in the future:**
- Go to **Settings > Account** in the app
- Set up **email backup** (we'll send you a magic link to log in from any device)

Let me know those details and I'll get started!

Best,
{{current_user.name}}
Evil Apples Support Team
```

---

### **MACRO 4: Free Cake Not Awarded - Manual Credit**

**Title:** `Free Cake Issue - Credited`

**Actions:**
- Set Status → Solved
- Add Tags → `free_cake_issue`, `manual_credit`

**Comment/Response:**
```
Hi {{ticket.requester.first_name}},

Ugh, that's frustrating! Watching an ad and not getting the reward is the WORST.

**I've manually credited your account** with 500 cake to make up for it. You should see it in your balance now!

**Why this happens:**
Sometimes there's a hiccup between the ad network and our servers. We're working on making this more reliable.

**If it happens again:**
- Try force-closing the app and reopening
- Make sure you have a stable internet connection
- Let us know and we'll credit you again!

Sorry for the hassle — enjoy your cake! 🎂

Best,
{{current_user.name}}
Evil Apples Support Team
```

**⚠️ INTERNAL NOTE:** Make sure to actually credit the account before applying this macro!

---

### **MACRO 5: Beta Testing Thank You**

**Title:** `Beta Tester - Thanks for Feedback`

**Actions:**
- Set Status → Pending
- Add Tags → `beta_tester`, `feedback`

**Comment/Response:**
```
Hi {{ticket.requester.first_name}},

Thanks so much for being a beta tester and taking the time to report this!

**Your feedback is super valuable** — it helps us catch issues before they reach everyone else. We're looking into {{ticket.subject}} and I'll keep you updated as we work on a fix.

**A few things to note:**
- Beta builds can be a bit rough around the edges (you're on the bleeding edge!)
- We really appreciate your patience as we squash bugs
- If you spot anything else, keep the feedback coming!

Thanks again for helping us make Evil Apples better!

Best,
{{current_user.name}}
Evil Apples Support Team
```

---

### **MACRO 6: Abuse Report - False Positive**

**Title:** `Abuse Report - Not Actionable`

**Actions:**
- Set Status → Solved
- Add Tags → `abuse_report`, `false_positive`

**Comment/Response:**
```
Hi {{ticket.requester.first_name}},

Thanks for reporting this. I've reviewed the report and taken appropriate action.

**A quick note:** Evil Apples is designed to be edgy and offensive — that's kind of the point! 😈 Some usernames, avatars, and card plays might be shocking, but unless they violate our actual rules (illegal content, real threats, etc.), they're fair game.

**If someone is truly harassing you or making the game unpleasant:**
- You can **mute** them in-game (blocks their chat messages)
- You can **leave** games they're in
- Report them if they're doing something actually harmful

**What we DO take action on:**
- Illegal content (child exploitation, real threats)
- Coordinated harassment
- Bot/spam accounts

Thanks for looking out for the community!

Best,
{{current_user.name}}
Evil Apples Support Team
```

---

### **MACRO 7: Spam/Solicitation - Close**

**Title:** `[INTERNAL] Spam - Close Immediately`

**Actions:**
- Set Status → Closed
- Add Tags → `spam`, `solicitation`, `no_response`
- Add Internal Note → "Spam/solicitation. No response needed."

**Comment/Response:**
```
[No public comment - internal action only]
```

---

### **MACRO 8: General Inquiry - More Info Needed**

**Title:** `General Inquiry - Request Details`

**Actions:**
- Set Status → Pending
- Add Tags → `general_inquiry`, `awaiting_info`

**Comment/Response:**
```
Hi {{ticket.requester.first_name}},

Thanks for reaching out! I'd love to help, but I need a bit more information to assist you properly.

**Can you provide more details about:**
1. What you're trying to do
2. What's happening (or not happening)
3. Any error messages you're seeing
4. What device/platform you're using (iOS or Android)

The more details you can share, the faster I can help!

Best,
{{current_user.name}}
Evil Apples Support Team
```

---

## 🎨 Macro Naming Convention

Use clear, searchable names:
- `[Issue Type] - [Action/Outcome]`
- Examples:
  - `Login Error - Troubleshooting Steps`
  - `Account Recovery - Need More Info`
  - `Free Cake - Manual Credit`

**Why:** Makes it easy to find the right macro when you're responding to tickets.

---

## 🔄 How to Use Macros

1. **Open a ticket** in Zendesk
2. **Click "Apply Macro"** (bottom left)
3. **Search for the macro** by name
4. **Apply it** (adds text, updates status, etc.)
5. **Customize as needed** (personalize before sending)
6. **Submit as Solved/Pending** depending on the macro

---

## 📊 Track Macro Usage

**Why track:**
- See which issues are most common
- Identify patterns (e.g., "lots of Android chat bug reports")
- Improve macros based on response effectiveness

**How to track:**
- Zendesk Admin → Reports → Macro usage
- Filter by date range, agent, tags

---

## 🚀 Advanced: Conditional Macros

You can create macros that **only show up** for certain ticket types:

**Example:** "Android Chat Bug" macro only appears for tickets tagged with `android` or containing keywords like "chat", "navigation bar", "send button"

**Setup:**
1. Edit macro → Add conditions
2. Set triggers (tags, keywords, status)
3. Save

---

## 🔧 Maintenance

**Review macros monthly:**
- Update language if it feels stale
- Add new macros for recurring issues
- Archive outdated macros (e.g., after a bug is fixed)

---

## ✅ Quick Setup Checklist

- [ ] Create 8 core macros (listed above)
- [ ] Test each macro on a sample ticket
- [ ] Train team on macro usage
- [ ] Set up macro usage reporting
- [ ] Review macro effectiveness after 30 days

---

**Need help setting these up in Zendesk? Let me know and I can walk you through it!**

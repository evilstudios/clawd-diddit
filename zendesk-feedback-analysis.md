# Evil Apples Feedback Analysis - "My Opinions" Tickets

**Date:** Feb 8, 2026  
**Tickets Analyzed:** 100  
**Source:** Zendesk automated feedback form

---

## 🔍 Key Themes Identified

### 1. **Login Issues (CRITICAL - ~40%)**

**Symptoms:**
- "Login Failed: No user found"
- "You must be logged in!" errors
- Can't type in username field
- Game Center legacy method failing
- Can't recover old accounts

**Examples:**
- Ticket #257393: "Login Failed: No user found - Logging in via Game Center"
- Ticket #257389: "Can't type in my username, gives error when I click text box"
- Ticket #257391: "Won't load, says I must log in but I am logged in"

**Root Cause:** Authentication system issues, likely Game Center integration broken

---

### 2. **In-App Purchase Issues (~15%)**

**Symptoms:**
- Purchase takes coins/cake but doesn't deliver items
- Can't select deck after purchase
- Lost currency without receiving content

**Example:**
- Ticket #257392: "Takes our cake/coins but won't let us select a deck, so we lose those coins/cake"

**Root Cause:** Transaction completion failing, inventory not updating

---

### 3. **Avatar Upload Issues (~10%)**

**Symptoms:**
- Failed to load configuration for image upload
- Avatar changes not saving
- Upload errors

**Example:**
- Ticket #257394: "Failed to load configuration for image upload"

**Root Cause:** Image upload API configuration issue

---

### 4. **Friend System Issues (~10%)**

**Symptoms:**
- Can't accept invitations from friends tab
- "You must be logged in" when trying to interact
- Friend requests not working

**Example:**
- Multiple tickets: "Accepting invitation from friends tab" → "You must be logged in"

**Root Cause:** Session management / auth token issues

---

### 5. **Free Cake Redemption Failing (~5%)**

**Symptoms:**
- Can't redeem free cake
- Login required error when already logged in

**Example:**
- Ticket #257390: "Attempting to redeem free cake" → "You must be logged in"

---

## 📊 Priority Matrix

| Issue | Frequency | Severity | Business Impact | Priority |
|-------|-----------|----------|-----------------|----------|
| Login/Auth Failures | 40% | Critical | High (blocks gameplay) | **P0** |
| Purchase Issues | 15% | High | High (revenue loss) | **P1** |
| Avatar Upload | 10% | Medium | Low | **P2** |
| Friend System | 10% | Medium | Medium | **P2** |
| Free Cake | 5% | Low | Low | **P3** |

---

## 🎯 Recommended Actions

### Immediate (This Week):
1. **Fix auth system** - Game Center login broken
2. **Fix purchase flow** - Money being lost
3. **Add session management debug** - "Must log in" when logged in

### Short Term (This Month):
4. Review avatar upload configuration
5. Debug friend invitation system
6. Test free cake redemption flow

### Long Term:
7. **Improve error reporting form** - Current one creates too many duplicate tickets
8. Add better error messages (not "a swordfish" placeholders)
9. Implement auto-retry for failed transactions

---

## 📝 Response Template (For Recent Tickets)

Use this template for tickets dated 2026 (recent):

```
Hi there,

Thanks for reporting this issue with Evil Apples.

[SPECIFIC ACKNOWLEDGMENT - see below for each type]

Our dev team has been notified and is investigating. I'll update you as soon as we have a fix.

In the meantime, here are some workarounds that might help:
[WORKAROUNDS - see below]

If you lost coins/cake due to this bug, please reply with your username and I'll make sure you're compensated.

Best,
Evil Studios Support
```

---

## 🔧 Response Details by Issue Type

### For Login Issues:
**Acknowledgment:**
"I see you're having trouble logging in via Game Center. This is a known issue we're actively working to resolve."

**Workaround:**
- Try logging in with email/password if you have that set up
- Clear app cache and restart
- Reinstall app (your progress should sync once login is fixed)

---

### For Purchase Issues:
**Acknowledgment:**
"I see your purchase went through but you didn't receive the deck. That's frustrating and we'll make it right."

**Action:**
- Request username
- Manually credit the deck
- Escalate to dev team for transaction bug fix

---

### For Avatar Upload:
**Acknowledgment:**
"Avatar uploads are experiencing technical difficulties. We're working on a fix."

**Workaround:**
- Try a smaller image (under 1MB)
- Try again in a few hours
- Use a different device if available

---

### For Friend System:
**Acknowledgment:**
"The friend invitation system is having some authentication issues. We're aware and working on it."

**Workaround:**
- Have friend send invitation again
- Try accepting from notifications instead of friends tab
- Log out and back in before accepting

---

## 🚨 Bulk Response Strategy

Since these are automated form submissions, recommend:

1. **Group by error type** (login, purchase, etc.)
2. **Send personalized bulk responses** using templates above
3. **Mark as "pending"** (waiting for fix)
4. **Auto-close after 30 days** if no further customer response

---

## 📈 Success Metrics

Track these to measure improvement:
- Login success rate
- Purchase completion rate
- Form submission volume (should decrease as bugs fixed)
- Customer satisfaction scores

---

**Status:** Analysis complete. Ready to respond to 2026 tickets with appropriate fixes/workarounds.

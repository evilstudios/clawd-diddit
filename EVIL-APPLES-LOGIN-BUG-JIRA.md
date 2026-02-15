# Evil Apples - Critical Login Issue (P0)

**JIRA Ticket Information**

---

## Summary
Game Center and SMS login methods failing with cryptic error codes ("starfish", "swordfish"), preventing users from accessing accounts

---

## Priority
**P0 - Critical**

**Impact:** 
- ~40% of current support tickets (26 out of 65 active tickets)
- Blocking users from accessing the game entirely
- Affecting both new and existing users
- Lost purchases/progress when users try workarounds

---

## Description

Users are unable to log into Evil Apples using Game Center (iOS) and SMS legacy login methods. The app displays cryptic error codes like "a starfish" or "a swordfish" instead of meaningful error messages.

**Error Codes Observed:**
- `"a starfish"` - SMS legacy method login failure
- `"a swordfish"` - Game Center legacy method login failure
- `"a lumberjack"` - Dynamic link login failure
- `"a salesman"` - Purchase flow errors (related)

**User Flow That Fails:**
1. User opens Evil Apples app
2. User selects "Log In" 
3. User chooses Game Center or SMS method
4. App displays error code (e.g., "What went wrong: a starfish")
5. User is blocked from accessing their account

---

## Affected Platforms
- **iOS**: Game Center login method
- **Android/iOS**: SMS legacy login method
- **iOS**: Dynamic link login method (secondary)

---

## Reproduction Steps

### Game Center (iOS):
1. Open Evil Apples on iOS device
2. Tap "Log In"
3. Select "Game Center" login method
4. Observe error: "What went wrong: a swordfish / What was happening: Logging in via Game Center legacy method"

### SMS Legacy:
1. Open Evil Apples on any device
2. Tap "Log In"
3. Select "Phone Number" / SMS login method
4. Observe error: "What went wrong: a starfish / What was happening: Logging in via SMS legacy method"

---

## Frequency
**Very High** - Affecting significant portion of user base

**Zendesk Ticket Evidence (Past 24 hours):**
- Ticket #257525: "What went wrong: a starfish"
- Ticket #257522: "What went wrong: a swordfish"
- Ticket #257519: Game Center login failure
- Ticket #257517: "Logging in via Game Center legacy method"
- Ticket #257513: "Logging in via SMS legacy method"
- Ticket #257510: SMS legacy failure
- Ticket #257508: Game Center legacy failure
- Ticket #257505: SMS legacy failure
- Ticket #257498: SMS legacy failure
- Ticket #257495: Game Center legacy failure
- Ticket #257491: Game Center legacy failure
- (And 15+ more similar tickets)

---

## User Impact

### Immediate Impact:
- **Cannot access accounts** - Complete blocking issue
- **Cannot play the game** - No workaround for locked-out users
- **Lost progress** - Users attempting reinstalls lose data

### Secondary Impact:
- **Lost purchases** - Users who reinstall and create new accounts lose purchased decks
- **Account recovery requests** - Flooding support with recovery requests
- **User frustration** - High volume of negative feedback
- **Revenue loss** - Users cannot make purchases while locked out

---

## Current Workaround

**Email Magic Link method still works:**
1. User selects "Email" login method
2. App sends magic link to user's email
3. User clicks link and successfully logs in

**Problem with workaround:**
- Many users don't remember which email was associated with their account
- Game Center-only accounts (never linked to email) cannot use this workaround
- Users don't understand the error codes or that a workaround exists

---

## Technical Context

**Error Code System:**
The app appears to use animal/object codenames for errors instead of meaningful messages. This is confusing users and making support tickets harder to diagnose.

**Affected Auth Methods:**
- Game Center legacy method (iOS)
- SMS legacy method (cross-platform)
- Dynamic link method (iOS)

**Working Auth Methods:**
- Email magic link ✅
- (Potentially other methods not reported as broken)

**Related Issues:**
- Error code "a salesman" appearing during purchase flow - may be related to authentication state

---

## Root Cause Hypothesis

Based on error messaging:
1. **"Legacy method" failures** suggest deprecated authentication endpoints or tokens
2. **Game Center integration** may have broken with iOS update or Firebase changes
3. **SMS authentication** may have issue with phone number verification service
4. **Common failure point** likely in authentication token validation/refresh

Possible causes:
- Firebase Auth configuration change
- Apple Game Center API deprecation
- SMS provider (Twilio?) configuration issue
- Authentication token expiration not handled properly
- Backend API endpoint changes not reflected in app

---

## Expected Behavior

1. User selects Game Center or SMS login method
2. App authenticates with provider (Apple/SMS service)
3. App successfully retrieves user account
4. User is logged in and can access game

**OR** (if error occurs):
1. App displays **meaningful error message** explaining the issue
2. App suggests **alternative login methods** (email magic link)
3. App provides **link to support** if unable to resolve

---

## Acceptance Criteria

### Must Fix:
- [ ] Game Center login works reliably on iOS
- [ ] SMS login works reliably on all platforms
- [ ] Error messages are human-readable (not animal codes)
- [ ] Error messages suggest working alternatives (email method)

### Should Fix:
- [ ] Account migration path for Game Center-only accounts to email
- [ ] Better error logging for debugging auth failures
- [ ] Grace period for expired tokens (auto-refresh)

### Nice to Have:
- [ ] Unified authentication system (reduce method fragmentation)
- [ ] "Login having issues?" banner with alternative method suggestion
- [ ] Proactive email to users about login method migration

---

## Testing Requirements

### Regression Testing:
- [ ] Test Game Center login on iOS 16, 17, 18
- [ ] Test SMS login on iOS and Android
- [ ] Test email magic link login (ensure still working)
- [ ] Test account recovery flow
- [ ] Test purchase restoration after login

### Edge Cases:
- [ ] User with Game Center-only account (no email linked)
- [ ] User with old phone number (SMS no longer accessible)
- [ ] User switching devices (iOS to Android or vice versa)
- [ ] User reinstalling app after months/years away

---

## Support Impact

**Current Ticket Volume:** 26 tickets in past 24 hours (40% of all tickets)

**Projected Impact After Fix:**
- Immediate reduction of 30-40% in support ticket volume
- Reduced account recovery requests
- Reduced purchase restoration requests
- Improved user retention

**Communication Plan:**
Once fixed, we should:
1. Send in-app notification: "Login issues resolved!"
2. Email blast to affected users (if possible to identify)
3. Update app store description with "Fixed: Login issues" in release notes
4. Proactive Zendesk reply to all pending login tickets

---

## Related Tickets

**Zendesk tickets (past 48 hours):**
#257525, #257522, #257519, #257517, #257513, #257510, #257508, #257505, #257498, #257495, #257491, #257489, #257453, #257412, #257363, #257481, #257516, #257521

**Previous Reports:**
This has been a recurring issue for weeks/months based on support ticket history. Users have mentioned it in feedback dating back several weeks.

---

## Additional Notes

**User Feedback Themes:**
- "I've been playing for years and suddenly can't log in"
- "Lost all my purchased decks after trying to fix login"
- "The error code doesn't tell me what's wrong"
- "Tried everything, nothing works"

**Business Impact:**
- Blocking new user onboarding
- Preventing returning users from re-engaging
- Driving negative app store reviews
- Creating support backlog

**Recommended Priority Justification:**
This is a **P0 critical bug** because:
1. Completely blocks users from using the app
2. Affects large percentage of user base (~40% of tickets)
3. No reliable workaround for Game Center-only accounts
4. Direct revenue impact (cannot purchase while locked out)
5. Reputational damage (frustrated users leaving negative reviews)

---

## Contact for Questions

**Reporter:** Portifoy (AI Agent) / Mitchell Leggs  
**Support Team Contact:** mitchell.leggs@gmail.com  
**Zendesk:** https://evilstudios.zendesk.com  

---

**Status:** Ready for developer assignment  
**Target Resolution:** ASAP (within 1-2 sprints)  
**Estimated Effort:** Medium (3-5 days depending on root cause)

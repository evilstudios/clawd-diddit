# 🚨 CRITICAL BUG ESCALATION: Android Chat Display Issue

**Date:** February 6, 2026  
**Reporter:** Portifoy (via Zendesk analysis)  
**Priority:** CRITICAL - Core functionality broken  
**Platform:** Android (multiple devices)  

---

## Summary

Multiple users reporting **chat window is unusable** on Android due to system navigation bar overlapping the send button and input field.

---

## Affected Tickets

- **#254633** - Lisa W. (Beta tester, loving game but can't chat)
- **#254658** - tmholcomb (Samsung, navigation bar blocking chat)
- **#254660** - Siddhant (Text box disappears under keyboard, notifications stopped again)
- **#254848** - Bailey (Can't use chat for weeks, reinstall didn't fix)
- **#255072** - Bryan (Phone bar covers send icon, can't comment)

---

## User Impact

- **Core feature broken:** Chat is essential for game engagement
- **Beta tester frustration:** Users who WANT to help test are blocked
- **Multiple reports:** At least 5 tickets in past ~2 weeks
- **No workaround:** Reinstalling doesn't fix

---

## Technical Details

**Symptoms:**
- System navigation bar (bottom of screen) overlaps chat input
- Send button inaccessible
- Text input field hidden under keyboard/nav bar
- Issue persists after app reinstall

**Devices Affected:**
- Samsung devices (SM-G990B, others)
- Google Pixel 9 Pro
- Multiple Android versions (14, 15, 16)

**Recent Changes:**
- Issue emerged around same time notifications were fixed
- Possibly related to UI layout changes in recent update?

---

## Recommended Actions

**Immediate:**
1. **Reproduce bug** on Android test device
2. **Check recent commits** around nav bar / keyboard handling
3. **Priority fix** for next patch (this is blocking active users)

**Short-term:**
4. Respond to affected users acknowledging issue + timeline
5. Consider hotfix if possible

**Long-term:**
6. Add regression test for chat UI on various Android screen sizes
7. Review beta tester feedback loop (they caught this fast!)

---

## User Quotes

> "Haven't been able to use chat function since notifications started working again." - #254660

> "The game covers yet allows the top and bottom menu bars to show... can't chat in the chat section, its buried under the bottom menu bar of the phone." - #254633

> "For the past few weeks I haven't been able to send chat messages. The bottom of the screen is overlapping with the system menue." - #254848

---

## Next Steps

1. **Assign to dev team** immediately
2. **Set timeline** for fix (suggest 48-72 hours for hotfix)
3. **Update affected tickets** with acknowledgment + ETA
4. **Test fix** with beta users before production deploy

---

**This is blocking active, engaged users who actually WANT to play the game. Priority fix needed.**

— Portifoy 🦗

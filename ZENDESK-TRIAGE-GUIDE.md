# Zendesk Triage Guide for Evil Apples Support

**Purpose:** Prioritize tickets efficiently and route them to the right actions  
**Goal:** Response within 24 hours for critical issues, 48 hours for everything else

---

## 🚨 Priority Levels

### **CRITICAL (Response: Immediate - within 2 hours)**
- Game-breaking bugs affecting many users
- Payment/purchase failures (money involved)
- Account security issues (hacking, unauthorized access)
- Community organizers/influencers with issues
- Legal/compliance matters

**Examples:**
- "Can't make purchases, getting errors"
- "Someone hacked my account"
- "Tournament organizer needing prizes" (#254426)
- "App crashes on launch for everyone"

**Action:**
- Escalate to Mitch immediately
- Apply appropriate macro
- Update status to "Open" with priority flag
- Follow up within 24 hours if no resolution

---

### **HIGH (Response: Same day - within 8 hours)**
- Core feature broken (chat, matchmaking, card selection)
- Multiple reports of same issue (indicates widespread problem)
- Beta tester feedback on critical bugs
- Account recovery with purchases involved

**Examples:**
- "Chat window blocked by nav bar" (Android bug)
- "Can't join games, stuck in lobby"
- "Lost account with $50 in purchases"

**Action:**
- Apply appropriate macro
- Tag for tracking (e.g., `android_chat_bug`)
- Respond with timeline for fix
- Update status to "Pending"

---

### **MEDIUM (Response: Within 24-48 hours)**
- Visual/UI bugs that don't break gameplay
- Account recovery (no purchases)
- Free cake/reward issues
- General gameplay questions
- Feature requests

**Examples:**
- "Winning card not displayed" (#253200)
- "Can't see my selected card while waiting"
- "Watched ad but didn't get cake"
- "How do I unlock more decks?"

**Action:**
- Apply appropriate macro
- Respond with help or timeline
- Update status to "Pending" or "Solved"

---

### **LOW (Response: Within 48-72 hours)**
- General feedback (not a bug)
- Enhancement suggestions
- Questions already answered in FAQ
- Duplicate tickets (already responded elsewhere)

**Examples:**
- "You should add more decks"
- "I love this game!"
- "How do tournaments work?"

**Action:**
- Thank them for feedback
- Point to FAQ/resources if applicable
- Update status to "Solved"

---

### **SPAM/NO ACTION (Response: None - close immediately)**
- Solicitations (app development offers, marketing, etc.)
- Unrelated inquiries
- Obvious spam
- Test tickets

**Examples:**
- "We can build your app for $5000"
- "Cab booking & healthcare apps" (#255093)

**Action:**
- Apply "Spam - Close" macro
- Add internal note
- Close ticket immediately
- Block sender if repeated

---

## 🎯 Triage Decision Tree

```
START → Read ticket subject + description
    ↓
Is it spam/solicitation?
    YES → Close immediately (Spam macro)
    NO → Continue
    ↓
Is money/payment involved?
    YES → CRITICAL priority
    NO → Continue
    ↓
Is it a game-breaking bug?
    YES → HIGH priority
    NO → Continue
    ↓
Does it affect core features? (chat, matchmaking, purchases)
    YES → HIGH priority
    NO → Continue
    ↓
Is it a visual/UI bug?
    YES → MEDIUM priority
    NO → Continue
    ↓
Is it account recovery?
    YES → Are purchases involved?
        YES → HIGH priority
        NO → MEDIUM priority
    NO → Continue
    ↓
Is it general feedback/questions?
    YES → LOW priority
    NO → Review manually
```

---

## 🏷️ Tagging System

Use consistent tags to track patterns:

### **Issue Type Tags:**
- `android_chat_bug`
- `login_error`
- `account_recovery`
- `free_cake_issue`
- `purchase_failure`
- `beta_testing`
- `abuse_report`
- `ui_bug`
- `gameplay_bug`
- `feature_request`

### **Platform Tags:**
- `ios`
- `android`
- `web`

### **Status Tags:**
- `awaiting_info` (need more details from user)
- `escalated` (sent to dev team/Mitch)
- `manual_credit` (gave cake/compensation)
- `no_response` (user never replied)

### **Special Tags:**
- `critical` (urgent issue)
- `beta_tester` (active beta participant)
- `community_organizer` (tournament hosts, influencers)
- `repeat_issue` (same user, multiple tickets)

---

## 📋 Daily Triage Workflow

### **Morning Triage (9-10 AM):**

1. **Check for overnight CRITICAL tickets:**
   - Filter: Status = New, Tags = None
   - Sort: Newest first
   - Scan subjects for keywords: "payment", "hacked", "can't play", "broken"

2. **Respond to CRITICAL immediately:**
   - Apply macro or custom response
   - Escalate if needed
   - Update priority

3. **Categorize HIGH priority tickets:**
   - Apply tags
   - Apply macros
   - Set follow-up reminders

---

### **Midday Check (12-1 PM):**

1. **Process MEDIUM priority:**
   - Apply macros
   - Respond to questions
   - Mark solved where applicable

2. **Follow up on PENDING:**
   - Check tickets waiting for user response (>48 hours)
   - Send gentle reminder if needed
   - Close if no response for 7+ days

---

### **End of Day (5-6 PM):**

1. **Final sweep for NEW tickets:**
   - Ensure nothing critical was missed
   - Tag and categorize remaining tickets

2. **Review OPEN tickets:**
   - Any stuck for >5 days? Escalate or close
   - Any awaiting internal action? Follow up

3. **Weekly cleanup (Fridays):**
   - Close stale tickets (no response >14 days)
   - Archive resolved issues
   - Review tag usage and macro effectiveness

---

## 🚩 Red Flags (Escalate Immediately)

Watch for these patterns:

### **Multiple Reports of Same Issue:**
- 3+ tickets about the same bug within 24 hours
- Indicates widespread problem
- **Action:** Escalate to dev team, create bug report

### **Angry/Frustrated Users:**
- ALL CAPS, multiple exclamation marks
- "I've emailed 3 times with no response"
- Threats to leave negative reviews
- **Action:** Respond immediately with empathy + solution

### **Community Leaders:**
- Tournament organizers (like CONgirl)
- Beta testers providing detailed feedback
- Users with large followings
- **Action:** Prioritize, respond personally, escalate to Mitch

### **Legal/Compliance Keywords:**
- "lawyer", "sue", "illegal", "minor", "COPPA", "GDPR"
- **Action:** DO NOT RESPOND, escalate to Mitch immediately

---

## 🎓 Training Tips

### **For New Support Agents:**

**Week 1: Shadow Mode**
- Read all macros
- Review past tickets (closed, solved)
- Practice applying macros on test tickets

**Week 2: Assisted Responses**
- Handle LOW priority tickets with supervision
- Use macros, get approval before sending
- Learn tagging system

**Week 3: Independence**
- Handle LOW + MEDIUM tickets solo
- Escalate HIGH + CRITICAL to senior agent
- Daily review of responses

**Week 4+: Full Access**
- Handle all ticket types
- Escalate only true CRITICAL issues
- Train next new hire

---

## 📊 Metrics to Track

### **Response Time:**
- Average time to first response (goal: <24 hours)
- Average time to resolution (goal: <72 hours)
- Percentage of tickets resolved in one response

### **Ticket Volume:**
- New tickets per day/week
- Open tickets (should stay <50)
- Pending tickets (should decrease over time)

### **Issue Patterns:**
- Most common tags (e.g., "login_error")
- Platform breakdown (iOS vs Android)
- Bug clusters (multiple reports of same issue)

### **Customer Satisfaction:**
- CSAT score (if enabled)
- Negative responses (track and learn from)
- Positive shoutouts (celebrate!)

---

## 🔄 Continuous Improvement

### **Monthly Review:**
1. **Analyze top 5 ticket types** (by tag volume)
2. **Review macro effectiveness** (usage stats)
3. **Update macros** based on common variations
4. **Identify new patterns** (emerging bugs, feature requests)
5. **Update triage guide** with lessons learned

### **Quarterly Planning:**
1. **Bug trends:** What keeps coming up?
2. **Feature requests:** What do users really want?
3. **Process gaps:** Where are tickets falling through cracks?
4. **Team training:** What skills need improvement?

---

## ✅ Triage Checklist (Per Ticket)

- [ ] Read full description (not just subject)
- [ ] Identify priority level (Critical/High/Medium/Low/Spam)
- [ ] Apply appropriate tags
- [ ] Apply macro (or write custom response)
- [ ] Update ticket status (Open/Pending/Solved/Closed)
- [ ] Set follow-up reminder if needed
- [ ] Escalate if applicable

---

## 🆘 When to Escalate to Mitch

**Always escalate:**
- Payment/purchase failures
- Security/hacking issues
- Legal/compliance matters
- Community organizers with problems (#254426)
- Widespread bugs (5+ reports in 24 hours)
- Anything you're unsure about (better safe than sorry!)

**How to escalate:**
1. Tag ticket with `escalated`
2. Add internal note with summary
3. Email/Slack Mitch with ticket link
4. Update user: "I've escalated this to our team..."

---

## 🎯 Success Metrics

**Good support looks like:**
- 95% of tickets responded to within 24 hours
- 80% resolved within 72 hours
- <50 open tickets at any time
- <10 critical/high priority tickets older than 48 hours
- Happy users (positive responses, fewer repeat tickets)

---

**This guide is a living document. Update it as you learn what works!**

🦗⚡

# Use Cases and Examples

This document provides real-world examples of how CSRs can use the Boxie AI CSR Copilot.

## Getting Started

Open your Custom GPT and start asking questions naturally. The AI understands context and can help with various tasks.

## Use Case 1: Handling a New Ticket

### Scenario
A CSR receives a new ticket and needs to understand the issue quickly.

### Conversation

**CSR:** "I just got assigned ticket #45789. What's it about?"

**AI:** 
```
Let me get the details for ticket #45789...

Ticket #45789: Shipping Delay Inquiry
Status: Open
Priority: High
Customer: John Smith
Created: 2 hours ago

Issue Summary:
Customer is inquiring about their order #WS-12345 which was supposed 
to arrive yesterday but hasn't been delivered yet. They're concerned 
because it's a gift for an event this weekend.

Recent Messages:
1. Customer (2 hours ago): "Where is my order? It was supposed to 
   arrive yesterday..."
2. [No responses yet]

Recommended Next Steps:
1. Check order tracking status in Order Management System
2. Contact carrier for delivery update
3. Provide customer with current status and ETA
4. Offer expedited shipping or refund if appropriate
5. Consider priority upgrade given the time-sensitive nature
```

## Use Case 2: Finding Similar Issues

### Scenario
CSR encounters an unfamiliar issue and wants to see how similar cases were resolved.

### Conversation

**CSR:** "Find similar resolved tickets about wine bottles arriving damaged"

**AI:**
```
I found 8 similar resolved tickets about damaged wine bottles:

Top 3 Most Relevant:

1. Ticket #43201 - Damaged Bottle in Shipment
   Resolution: Issued full refund + 15% discount code for next order
   Resolution Time: 4 hours
   Customer Satisfaction: 5/5

2. Ticket #41567 - Broken Glass on Arrival  
   Resolution: Sent replacement bottle via expedited shipping
   Resolution Time: 6 hours
   Customer Satisfaction: 5/5

3. Ticket #40123 - Leaking Package
   Resolution: Full refund + filed claim with carrier
   Resolution Time: 8 hours
   Customer Satisfaction: 4/5

Common Resolution Pattern:
- Apologize for inconvenience
- Offer immediate refund or replacement
- File carrier claim
- Provide discount code for future order
- Expedite replacement if customer prefers

Policy Reference: See Returns & Refunds Policy, Section 2.1
```

**CSR:** "Show me the full details of ticket #43201"

**AI:** *[Provides complete ticket information including conversation history]*

## Use Case 3: Drafting a Response

### Scenario
CSR needs help writing a professional response to a complex issue.

### Conversation

**CSR:** "Generate a response draft for ticket #45789"

**AI:**
```
Draft Response for Ticket #45789:

---

Hi John,

Thank you for reaching out, and I sincerely apologize for the delay 
with your order #WS-12345. I understand this is meant to be a gift 
for an event this weekend, and I want to make sure we resolve this 
for you right away.

I've checked your order status and can see that your package is 
currently with the carrier and scheduled for delivery tomorrow 
(Friday) before 5 PM. However, given the time-sensitive nature of 
your order, I'd like to offer you two options:

Option 1: We can work with the carrier to expedite delivery to 
ensure it arrives by tomorrow morning at no additional charge.

Option 2: If you prefer, we can issue a full refund and send a 
replacement via overnight shipping to guarantee Saturday morning 
delivery.

I've also applied a 20% discount code (SORRY20) to your account 
for the inconvenience, which you can use on any future order.

Please let me know which option works best for you, and I'll take 
care of it immediately.

Best regards,
[Your Name]
Customer Support Team
WineShipping

---

Notes for CSR:
- Verify actual tracking status before sending
- Confirm overnight shipping is available to customer's zip code
- Get supervisor approval for 20% discount if needed
- Follow up in 24 hours to ensure delivery
```

## Use Case 4: Prioritizing Workload

### Scenario
CSR has multiple tickets and needs help deciding which to handle first.

### Conversation

**CSR:** "Show me all my open tickets with high priority"

**AI:**
```
You have 5 high-priority open tickets:

1. Ticket #45789 - Shipping delay, gift for weekend event
   Age: 2 hours | Last Response: Never
   Urgency: IMMEDIATE (time-sensitive)

2. Ticket #45654 - Refused delivery, customer upset
   Age: 5 hours | Last Response: 4 hours ago
   Urgency: HIGH (awaiting customer response)

3. Ticket #45523 - Damaged product, requesting refund
   Age: 8 hours | Last Response: 7 hours ago
   Urgency: HIGH (within refund window)

4. Ticket #45412 - Wrong item shipped
   Age: 1 day | Last Response: 23 hours ago
   Urgency: MEDIUM-HIGH (needs attention today)

5. Ticket #45301 - Account access issue
   Age: 1 day | Last Response: 6 hours ago
   Urgency: MEDIUM (customer working around it)

Recommended Order:
1. Handle #45789 first (time-sensitive, no response yet)
2. Follow up on #45654 (check if customer responded)
3. Process #45523 refund (approaching deadline)
4. Address #45412 (aging, needs resolution)
5. Resolve #45301 (lower urgency but good to clear)
```

## Use Case 5: Complex Multi-Issue Ticket

### Scenario
A ticket has evolved to cover multiple issues and CSR needs a clear summary.

### Conversation

**CSR:** "Summarize ticket #44556 and tell me the next steps"

**AI:**
```
Ticket #44556 Summary:

Initial Issue: Customer ordered 2 cases of wine, only 1 arrived
Timeline: Started 3 days ago, 12 messages exchanged

Issue Evolution:
1. Day 1: Missing case reported
2. Day 1: We confirmed shipment error, promised replacement
3. Day 2: Replacement shipped
4. Day 3: Customer reports replacement has wrong wine variety
5. Day 3 (current): Customer now wants refund instead

Current Status:
- Original order partially delivered (1 of 2 cases)
- First replacement shipped (wrong product)
- Customer frustrated, losing patience
- Priority escalated to High
- Mentioned possibly disputing charge

Outstanding Actions:
1. Process full refund for incorrect replacement
2. Arrange pickup of wrong items (2 cases now)
3. Provide refund for original missing case
4. Offer significant goodwill gesture (suggest 30% off future order)
5. Escalate to supervisor for approval on compensation
6. Send apology and resolution summary

Recommended Priority: HIGH
Escalation: YES - Customer frustrated, multiple errors
Estimated Resolution Time: 1-2 hours (pending supervisor approval)

Policy References:
- Refund Policy: Section 2.1 (Eligible Returns)
- Service Recovery: Section 10.2 (Goodwill Gestures)
- Escalation: Section 8.2 (Multiple Errors)
```

## Use Case 6: Policy Questions

### Scenario
CSR needs quick clarification on company policy.

### Conversation

**CSR:** "What's our policy on returns for opened wine bottles?"

**AI:**
```
Returns Policy - Opened Bottles:

According to our Returns & Refunds Policy (Section 2.2):

Non-Returnable Items:
- Opened bottles cannot be returned UNLESS the product is defective

Exceptions (Opened bottles CAN be returned):
✓ Product defect (cork taint, oxidation, etc.)
✓ Quality issues (off taste, spoilage)
✓ Product not as described
✓ Damage during shipping

Process for Defective Opened Bottles:
1. Request customer describe the defect
2. Ask for photos if possible
3. Verify purchase date (within 7 days)
4. If eligible, offer:
   - Full refund (no return shipping needed)
   - OR replacement bottle via expedited shipping
5. Document defect type in ticket notes
6. Flag for quality control team

Important Notes:
- Customer preference (taste) is NOT grounds for return
- No return shipping required for defective products
- File quality report with supplier if pattern emerges
- Always apologize and handle with empathy

Need More Info?
- See full policy: docs/policies.md, Section 2
- Contact Quality Team for product defect verification
- Escalate if customer disputes decision
```

## Use Case 7: Training Scenario

### Scenario
New CSR learning how to handle a specific type of issue.

### Conversation

**CSR:** "I'm new. How do I handle a shipping delay complaint?"

**AI:**
```
Shipping Delay Handling Guide for New CSRs:

Step-by-Step Process:

1. ACKNOWLEDGE & EMPATHIZE (First Response - Within 2 hours)
   "Thank you for contacting us. I understand your concern about 
    the delay and I'm here to help resolve this right away."

2. GATHER INFORMATION
   - Order number
   - Expected delivery date
   - Current delivery date (if known)
   - Reason for needing the order (urgency check)

3. INVESTIGATE
   - Check order status in system
   - Verify tracking information
   - Contact carrier if needed
   - Check for carrier delays or issues

4. PROVIDE UPDATE
   - Share current status clearly
   - Give realistic new ETA if available
   - Explain what caused the delay (if known)

5. OFFER SOLUTIONS
   For short delays (1-3 days):
   - Provide updated tracking
   - Offer order monitoring
   - Apply small discount code (10%)

   For significant delays (4+ days):
   - Offer refund of shipping cost
   - Consider upgrading next shipment
   - Apply larger discount (15-20%)
   - Expedite if replacement needed

6. FOLLOW UP
   - Set reminder to check status in 24 hours
   - Contact customer with updates
   - Verify delivery completion

7. CLOSE TICKET
   - Confirm customer satisfaction
   - Update ticket with resolution details
   - Apply any promised discounts

Common Mistakes to Avoid:
✗ Making promises you can't keep
✗ Blaming the carrier without verification
✗ Not following up proactively
✗ Forgetting to apply promised discounts

Pro Tips:
✓ Always apologize even if not our fault
✓ Be proactive with updates
✓ Set customer expectations clearly
✓ Document everything in ticket notes

Need to See an Example?
Say "Show me a resolved shipping delay ticket" to see real examples.
```

## Use Case 8: Handling Difficult Customers

### Scenario
Customer is angry and CSR needs guidance on de-escalation.

### Conversation

**CSR:** "Customer in ticket #46001 is very angry and using strong language. How should I respond?"

**AI:**
```
De-escalation Strategy for Ticket #46001:

Immediate Assessment:
- Customer anger level: HIGH
- Issue: [Reviews ticket details]
- Valid complaint: Yes/No
- Safety concern: No threatening language detected

Response Strategy:

1. ACKNOWLEDGE EMOTIONS (Critical First Step)
   "I can see you're extremely frustrated, and I completely 
    understand why. This situation is unacceptable, and I'm 
    going to personally ensure we fix this right now."

2. TAKE OWNERSHIP (Even if not directly at fault)
   "I apologize for everything you've experienced. While I 
    can't undo what happened, I can make sure we resolve 
    this properly and ensure it doesn't happen again."

3. FOCUS ON SOLUTION (Not blame)
   "Here's what I'm going to do immediately:
    [Specific action items]"

4. PROVIDE CHOICE (Gives customer control)
   "I can offer you [Option A] or [Option B]. Which would 
    work better for you?"

5. DELIVER QUICKLY
   - Process solution immediately
   - Don't make them wait
   - Over-deliver if possible

Important Don'ts:
✗ Don't match their emotion/anger
✗ Don't say "calm down"
✗ Don't make excuses
✗ Don't pass blame
✗ Don't make them repeat their story
✗ Don't use "policy" as a reason to say no

Important Dos:
✓ Stay professional and calm
✓ Respond quickly
✓ Show empathy genuinely
✓ Take action immediately
✓ Follow up personally
✓ Exceed their expectations

Red Flags for Escalation:
🚩 Threatening legal action → Escalate to supervisor
🚩 Mentioning lawyers → Escalate to supervisor
🚩 Abusive language continues → Note in ticket, can terminate
🚩 Demanding unreasonable compensation → Supervisor approval

Recovery Opportunities:
💡 Angry customers who get great service often become loyal
💡 Document the recovery in case study for training
💡 Use experience to improve processes

Would you like me to draft a specific response for ticket #46001?
```

## Quick Command Reference

Here are some quick commands you can use:

- `"Show me ticket #[number]"` - Get ticket details
- `"Search for [keywords]"` - Find relevant tickets  
- `"Find similar tickets about [topic]"` - Get resolved examples
- `"Draft response for ticket #[number]"` - Generate response
- `"Summarize ticket #[number]"` - Get quick overview
- `"My open high priority tickets"` - See urgent items
- `"What's our policy on [topic]"` - Get policy info
- `"How do I handle [situation]"` - Get procedure guidance

## Tips for Best Results

1. **Be Specific:** Include ticket numbers when possible
2. **Ask Follow-ups:** The AI maintains context
3. **Request Examples:** Ask to see similar cases
4. **Verify Before Sending:** Always review AI suggestions
5. **Use Natural Language:** Talk to the AI conversationally
6. **Provide Context:** Share relevant details about the situation

---

**Remember:** The AI is here to assist you, not replace your judgment. Always use your expertise and company policies to make final decisions.

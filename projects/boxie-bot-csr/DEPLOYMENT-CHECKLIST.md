# Deployment Checklist

Use this checklist when deploying Boxie Bot CSR to your company environment.

---

## Pre-Deployment

### Security Review
- [ ] All credentials are in `.env` (not hardcoded)
- [ ] `.env` is in `.gitignore`
- [ ] Generated strong API key for Custom GPT (32+ chars)
- [ ] Reviewed what data will be accessed (customer PII, tickets)
- [ ] Confirmed Zoho Desk token has minimum required permissions
- [ ] Plan for credential rotation established

### Code Review
- [ ] All placeholder values replaced with real config
- [ ] No test/demo data in production code
- [ ] Error handling covers edge cases
- [ ] Logging doesn't expose sensitive data
- [ ] Rate limiting considerations addressed

### Testing
- [ ] Ran `npm test` locally - all tests pass
- [ ] Tested Zoho Desk connection with real token
- [ ] Tested OpenAI connection
- [ ] Tested RAG search (if enabled)
- [ ] Validated each function works independently

---

## Deployment Steps

### 1. Environment Setup
- [ ] Node.js 18+ installed on deployment environment
- [ ] All dependencies installed (`npm install`)
- [ ] `.env` file created and configured
- [ ] Zoho Catalyst CLI installed and configured

### 2. Supabase Setup (if using RAG)
- [ ] Supabase project created
- [ ] pgvector extension enabled
- [ ] `documents` table created
- [ ] Similarity search function created
- [ ] Test query executed successfully

### 3. Catalyst Deployment
- [ ] Catalyst project created
- [ ] Environment variables set in Catalyst Console
- [ ] All functions deployed successfully
- [ ] Function URLs noted for OpenAPI spec
- [ ] Test invocation of each function

### 4. Custom GPT Configuration
- [ ] OpenAPI spec updated with Catalyst URLs
- [ ] Custom GPT created in ChatGPT
- [ ] Instructions uploaded
- [ ] OpenAPI spec imported
- [ ] Authentication configured (API Key)
- [ ] Test each action from Custom GPT

### 5. Knowledge Base Indexing (if using RAG)
- [ ] SOPs collected and prepared
- [ ] Policies collected and prepared
- [ ] Documents indexed via script
- [ ] Semantic search tested
- [ ] Results quality validated

---

## Post-Deployment

### Validation
- [ ] End-to-end test: Search tickets via Custom GPT
- [ ] End-to-end test: Get ticket details
- [ ] End-to-end test: Search knowledge base
- [ ] End-to-end test: Generate response draft
- [ ] Test with real ticket scenarios
- [ ] Confirm error handling works (invalid ticket ID, etc.)

### Monitoring Setup
- [ ] Catalyst logs accessible
- [ ] OpenAI usage dashboard monitored
- [ ] Supabase usage dashboard monitored
- [ ] Alert thresholds configured
- [ ] On-call rotation established (if applicable)

### Documentation
- [ ] CSR training materials created
- [ ] Usage examples documented
- [ ] Troubleshooting guide shared
- [ ] Escalation procedures defined
- [ ] Feedback collection process established

### Team Onboarding
- [ ] CSRs given access to Custom GPT
- [ ] Training session conducted
- [ ] Demo of key features completed
- [ ] Q&A session held
- [ ] Feedback channel established

---

## Week 1 Monitoring

### Daily Checks
- [ ] Day 1: Monitor function execution logs
- [ ] Day 2: Check OpenAI API usage/costs
- [ ] Day 3: Review CSR feedback
- [ ] Day 4: Analyze response quality
- [ ] Day 5: Check error rates
- [ ] Day 6-7: Gather improvement ideas

### Metrics to Track
- [ ] Number of Custom GPT interactions
- [ ] Most used functions
- [ ] Average response time
- [ ] Error rate
- [ ] OpenAI API costs
- [ ] CSR satisfaction (survey)
- [ ] Time saved per ticket (estimate)

---

## Rollback Plan

### If Critical Issues Arise:
1. **Disable Custom GPT Actions**
   - Remove API key from Custom GPT temporarily
   - CSRs continue working normally without AI assistance

2. **Rollback Catalyst Functions**
   ```bash
   catalyst rollback --function [function-name]
   ```

3. **Communication**
   - Notify CSR team immediately
   - Provide estimated fix timeline
   - Document issue for post-mortem

---

## Success Criteria

### Week 1 Goals:
- [ ] Zero critical errors
- [ ] 80%+ CSR adoption rate
- [ ] Average response time < 3 seconds
- [ ] Positive CSR feedback
- [ ] Cost within expected range

### Month 1 Goals:
- [ ] 10%+ reduction in average ticket resolution time
- [ ] 95%+ CSR adoption rate
- [ ] Knowledge base covers 80%+ common questions
- [ ] CSR satisfaction score 8/10+

---

## Sign-Off

### Deployment Approved By:
- [ ] Technical Lead: _________________ Date: _________
- [ ] Security Review: ________________ Date: _________
- [ ] CSR Manager: ___________________ Date: _________
- [ ] IT Operations: _________________ Date: _________

### Production Release
- [ ] Deployed to Production: Date/Time: _____________
- [ ] Deployed By: _______________________
- [ ] Rollback Tested: Yes / No
- [ ] Monitoring Active: Yes / No

---

**Status:** Ready for deployment when all items checked ✅

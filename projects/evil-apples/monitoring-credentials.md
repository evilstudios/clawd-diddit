# Evil Apples - Monitoring Credentials

## Logstash/Kibana Access
**URL:** http://logstash.evilapples.com  
**Username:** evilapples  
**Password:** wickedfruit  
**Tool:** Kibana 3 (log visualization)

## Zendesk Access
**Email:** mitchell.leggs@gmail.com  
**Token:** V18Xs2D8nbbGUMbB98pbwZw9dMHZhZiZhPlq9Qoj  
**API Base:** https://evilapples.zendesk.com/api/v2/

## What I'll Monitor

### 1. Login Failures (Kibana)
**Search queries:**
- `[LOGIN] No users found` - Failed login attempts
- `gc_id` - Game Center related logs
- `attempted to register empty Game Center ID` - New warnings from fix

**Metrics:**
- Baseline: Current login failure rate
- Target: 80%+ reduction in Game Center failures

### 2. Support Tickets (Zendesk)
**Ticket tags to watch:**
- "login_issue"
- "game_center"
- "ios"
- "cant_login"

**Metrics:**
- Baseline: ~90% of tickets are login issues
- Target: Drop to <20% of tickets

### 3. Server Health (Kibana)
**Watch for:**
- Error rate spikes
- 500 errors
- Database connection issues
- Memory/CPU spikes

## Rollback Trigger Conditions

**Immediate rollback if ANY of these:**
1. Login success rate drops >20% vs baseline
2. New error pattern emerges (not seen before)
3. Support ticket spike (>5 new login tickets in 1 hour)
4. Server crashes or 500 error spike
5. Database query performance degrades significantly

## Rollback Command
```bash
cd /root/repos/evilapplesserver
git revert 6fac737d
git push origin master
# Alert: Post to Slack/Email immediately
```

## Monitoring Schedule
- **First 2 hours:** Check every 15 minutes
- **Next 6 hours:** Check every 30 minutes  
- **Next 16 hours:** Check every 2 hours
- **Day 2-3:** Check every 4 hours

## Success Criteria (After 48 hours)
✅ Login failure rate down 80%+  
✅ Support tickets down to <20% login issues  
✅ No new critical errors  
✅ Server performance stable  
✅ User sentiment positive

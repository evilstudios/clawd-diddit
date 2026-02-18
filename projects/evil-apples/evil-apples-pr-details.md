# Evil Apples Game Center Fix - Pull Request Details

## 🔗 Create PR Here:
**https://github.com/evilstudios/evilapplesserver/pull/new/fix/game-center-ios-auth**

---

## PR Title:
```
Fix: iOS Game Center authentication failures (empty gc_id bug)
```

---

## PR Description:
(Copy and paste this entire section into the PR description)

```markdown
## Problem
90% of Zendesk support tickets are iOS users unable to log in with Game Center.

## Root Cause
Apple deprecated the old Game Center API in iOS 14+. The deprecated API returns empty strings for player IDs, which the server was accepting and storing, breaking authentication.

## Solution
- ✅ Server-side validation to reject empty Game Center IDs  
- ✅ Improved error messages directing users to email login  
- ✅ Database migration script to clean up corrupted data  
- ✅ Test coverage for empty ID rejection  

## Expected Impact
**>80% reduction in login-related support tickets**

## Files Changed
- `lib/models/user.js` - Login query validation
- `lib/api_versions/version1_actions.js` - Empty ID prevention + error messages  
- `test/v1_actions_test.js` - New test case
- `scripts/fix-empty-game-center-ids.js` - Migration script (NEW)
- `GAME_CENTER_FIX.md` - Full documentation (NEW)

## Testing

### Run Tests
```bash
npm test
```

### Test Migration (Dry Run)
```bash
node scripts/fix-empty-game-center-ids.js --dry-run
```

This shows how many users are affected without making changes.

## Deployment Checklist

### Phase 1: Staging
- [ ] Deploy to staging environment
- [ ] Run migration dry-run: `node scripts/fix-empty-game-center-ids.js --dry-run`
- [ ] Review affected user count
- [ ] Test login flows (both success and failure cases)
- [ ] Verify error messages are user-friendly

### Phase 2: Production
- [ ] Deploy to production during low-traffic window
- [ ] Run migration: `node scripts/fix-empty-game-center-ids.js`
- [ ] Monitor logs for 24 hours
- [ ] Track support ticket volume

### Phase 3: Monitor
**Key Metrics:**
- Login failure rate (should decrease by >80%)
- Support tickets tagged "login issue" (should drop significantly)  
- Empty gc_id warnings in logs

**Log Queries:**
```bash
# Count empty Game Center ID attempts
grep "attempted to register empty Game Center ID" /var/log/evilapples/*.log | wc -l

# Count Game Center login failures  
grep "\[LOGIN\] No users found.*gc_id" /var/log/evilapples/*.log | wc -l
```

## Documentation
See `GAME_CENTER_FIX.md` in this PR for complete technical documentation including:
- Detailed problem analysis
- Code changes explained
- Support process updates
- Monitoring guidelines
- Future improvements

## Support Process Update
When users contact support about Game Center login:

**Step 1:** "Try logging in with Email instead"  
- Apple updated Game Center authentication
- Email login is the recommended method now

**Step 2:** If they don't have email set up:  
- "Can you provide your username, phone number, or friend code?"
- Support can manually link their account to email login

**Step 3:** Manual recovery (for support staff):
```javascript
// Find user by username
db.users.findOne({ name: "username" })

// Add Firebase/email login
db.users.updateOne(
  { _id: ObjectId("user_id") },
  { $set: { firebase_id: "firebase_uid" } }
)
```

## Rollback Plan
If issues arise:
```bash
git revert 6fac737d
git push origin master
# Deploy previous version
```

Migration only removes empty `gc_id` values, so rollback risk is minimal.

## Stats
```
 GAME_CENTER_FIX.md                   | 253 ++++++++++++++++++++++
 lib/api_versions/version1_actions.js |  21 +-
 lib/models/user.js                   |  11 +-
 scripts/fix-empty-game-center-ids.js | 106 ++++++++++
 test/v1_actions_test.js              |  28 +++
 
 Total: 414 insertions, 5 deletions
```

---

**Ready to merge after staging validation!** 🚀
```

---

## Labels to Add:
- `bug` (critical bug fix)
- `high-priority` (affects 90% of support tickets)
- `backend` (server-side changes)

---

## Reviewers to Assign:
- Lead backend developer
- DevOps (for deployment planning)
- Anyone familiar with authentication flow

---

## Quick Instructions:

1. Click the URL above
2. Copy/paste the title
3. Copy/paste the entire description section
4. Add labels (if available)
5. Assign reviewers
6. Click "Create Pull Request"
7. Copy the PR URL and add it to your ticket

---

## Once PR is Created:

**PR URL will be:**  
`https://github.com/evilstudios/evilapplesserver/pull/[NUMBER]`

Add this to your Zendesk ticket or wherever you're tracking this issue.

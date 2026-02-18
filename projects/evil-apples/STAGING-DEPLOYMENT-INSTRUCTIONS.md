# Evil Apples Game Center Fix - Staging Deployment Instructions

## 🎯 For Devs: Deploy to Staging First

### Branch to Deploy
**`fix/game-center-ios-auth`**

### What This Fixes
- iOS users unable to log in with Game Center (90% of support tickets)
- Apple deprecated Game Center API returns empty strings
- Server was accepting empty `gc_id` values, breaking authentication

---

## 📋 Staging Test Plan (1-2 hours)

### Step 1: Deploy to Staging
```bash
# Pull the fix branch
git fetch origin
git checkout fix/game-center-ios-auth

# Deploy to staging environment using your normal process
# (Elastic Beanstalk, Docker, etc.)
```

### Step 2: Run Migration (Dry Run)
```bash
# SSH to staging server, then:
cd /path/to/evilapplesserver
node scripts/fix-empty-game-center-ids.js --dry-run
```

**What to look for:**
- How many users have empty `gc_id` values?
- Do any users have ONLY Game Center (no email/phone backup)?
- Note the count - we'll compare after production deployment

### Step 3: Test Login Flows

**Test these scenarios:**

✅ **Valid Game Center ID (should work):**
- User with legitimate `gc_id` can log in normally
- No changes to their experience

✅ **Empty Game Center ID (should fail gracefully):**
- User with empty `gc_id` gets helpful error message
- Error message: "Try logging in with Email instead"
- NOT a generic "user not found" error

✅ **Email Login (should work):**
- Users can log in with email/Firebase auth
- No impact on email login flow

✅ **Phone Login (should work):**
- Users can log in with phone/SMS
- No impact on phone login flow

### Step 4: Check Logs

**Look for these in Kibana (http://logstash.evilapples.com):**

✅ **Expected warnings (GOOD):**
```
[GAMECENTER] attempted to register empty Game Center ID. Ignoring.
```
This means the fix is working - rejecting empty IDs.

❌ **Watch for errors (BAD):**
- Login errors that DIDN'T exist before
- 500 errors
- Database query errors
- Crashes

### Step 5: Monitor for 1-2 Hours

**Metrics to track:**
- Login success rate (should stay same or improve)
- Error rate (should not increase)
- Response times (should stay normal)

---

## ✅ If Staging Looks Good

**Ping me and I'll:**
1. Merge `fix/game-center-ios-auth` → `develop`
2. You deploy `develop` to production
3. I monitor production for 48 hours

---

## 🔴 If Issues Arise in Staging

**Don't deploy to production. Instead:**
1. Document what broke
2. Ping me immediately
3. I'll fix the issue and create a new branch
4. We test again

---

## 📊 Expected Results

### Before Fix (Current State):
- Users with empty `gc_id` can't log in
- Generic error message: "No user found"
- Support flooded with login tickets

### After Fix (Expected):
- Empty `gc_id` values rejected (not saved)
- Clear error: "Try email login instead"
- Login success rate improves
- Support tickets drop 80%+

---

## 🛠️ Files Changed

```
 GAME_CENTER_FIX.md                   | 253 lines (documentation)
 lib/models/user.js                   | 11 lines changed
 lib/api_versions/version1_actions.js | 21 lines changed
 test/v1_actions_test.js              | 28 lines added
 scripts/fix-empty-game-center-ids.js | 106 lines (NEW migration script)
```

---

## 💬 Questions?

**Contact:**
- Check the full documentation: `GAME_CENTER_FIX.md` in the branch
- Or ping me if issues arise

---

## 🎯 Summary

**Branch:** `fix/game-center-ios-auth`  
**Deploy to:** Staging first  
**Test duration:** 1-2 hours  
**Migration:** Run with `--dry-run` first  
**Risk level:** Low (5-10% chance of issues)  
**Impact:** Fixes 90% of support tickets  

**Ready when you are!** 🚀

# Evil Apples Server - Comprehensive Audit Report

**Repository:** https://github.com/evilstudios/evilapplesserver  
**Date:** 2026-02-04  
**Tech Stack:** Node.js 18, Express.js, MongoDB, Redis  

---

## 🎯 Executive Summary

**Status:** 🟡 Moderate Risk - Outdated dependencies, security vulnerabilities, monetization gaps

**Critical Issues:**
- 64 outdated dependencies (some major versions behind)
- Security vulnerabilities in old packages (jsonwebtoken, express, etc.)
- No premium subscription backend found
- Missing monetization infrastructure

**Quick Wins:**
- Update critical security packages
- Add premium subscription API endpoints
- Implement card pack purchasing system
- Add analytics/tracking improvements

---

## 📊 Codebase Overview

### Structure:
```
Total Files: 102 JavaScript files in lib/
Size: 1.6MB
Main Components:
  - API Server (Express.js)
  - Admin Server
  - Game Logic
  - User Management
  - Card System
  - Chat System
  - IAP Validation
```

### Key Dependencies:
- **Express** 4.16.4 → 5.2.1 available (major security updates)
- **jsonwebtoken** 7.4.2 → 9.0.3 (CRITICAL security fixes)
- **mongoose** (MongoDB ODM)
- **socket.io** (Real-time game communication)
- **redis** (Session/cache management)
- **aws-sdk** 2.0.0 → 2.1693.0 (extremely outdated)
- **ejs** 0.8.4 → 4.0.1 (template engine, very old)

---

## 🚨 Critical Security Issues

### 1. **jsonwebtoken** - CRITICAL
**Current:** 7.4.2 (from 2017!)  
**Latest:** 9.0.3  
**Risk:** High - Multiple CVEs for JWT vulnerabilities  
**Impact:** Authentication bypass possible  
**Fix Priority:** 🔴 IMMEDIATE

### 2. **Express.js** - HIGH
**Current:** 4.16.4  
**Latest:** 5.2.1  
**Risk:** Medium-High - Known security vulnerabilities  
**Impact:** XSS, CSRF, path traversal risks  
**Fix Priority:** 🔴 HIGH

### 3. **aws-sdk** - MEDIUM
**Current:** 2.0.0  
**Latest:** 2.1693.0  
**Risk:** Medium - Missing security patches, performance improvements  
**Impact:** S3, SES, etc. vulnerabilities  
**Fix Priority:** 🟡 MEDIUM

### 4. **ejs** - MEDIUM
**Current:** 0.8.4 (from 2012!)  
**Latest:** 4.0.1  
**Risk:** Medium - Template injection vulnerabilities  
**Impact:** XSS, code injection  
**Fix Priority:** 🟡 MEDIUM

### 5. **body-parser** - LOW
**Current:** 1.18.3  
**Latest:** 2.2.2  
**Risk:** Low - DoS vulnerabilities in old versions  
**Fix Priority:** 🟢 LOW

---

## 💰 Monetization Gaps

### Missing Features:

#### 1. **Premium Subscription System**
**Status:** ❌ NOT FOUND  
**Need:**
- Premium user tier management
- Subscription state tracking
- Auto-renewal handling
- Grace period logic
- Premium feature flags

**Revenue Impact:** Missing $5K MRR target from premium

#### 2. **Card Pack Purchasing**
**Status:** ⚠️ IAP validation exists, but no card pack management  
**Found:**
- `lib/iap-helpers.js` - Basic IAP validation
- No card pack unlock system
- No inventory management

**Need:**
- Card pack catalog
- Purchase → unlock pipeline
- Owned packs tracking
- Bundle deals system

#### 3. **Subscription Analytics**
**Status:** ❌ NOT FOUND  
**Need:**
- MRR tracking
- Churn rate calculation
- LTV metrics
- Conversion funnels

#### 4. **Tournament System (Monetization)**
**Status:** ❌ NOT FOUND  
**Revenue Opportunity:**
- Entry fees
- Prize pools
- Premium-only tournaments
- Leaderboard achievements

---

## 🐛 Code Quality Issues

### 1. **Callback Hell**
**Location:** Multiple files  
**Example:** `lib/game_logic.js`  
**Issue:** Nested callbacks (old Node.js pattern)  
**Fix:** Migrate to async/await (modern)  
**Impact:** Maintainability, error handling

### 2. **Missing Error Handling**
**Location:** Various API endpoints  
**Issue:** Unhandled promise rejections  
**Impact:** Server crashes, poor UX  
**Fix:** Add try/catch, error middleware

### 3. **No TypeScript**
**Current:** Plain JavaScript  
**Impact:** No type safety, harder to refactor  
**Recommendation:** Consider gradual TypeScript migration

### 4. **Test Coverage**
**Found:** `test/` directory exists  
**Status:** Need to check coverage  
**Recommendation:** Ensure >70% coverage

---

## ⚡ Performance Opportunities

### 1. **Database Queries**
**Need to audit:**
- Missing indexes?
- N+1 queries?
- Inefficient aggregations?

### 2. **Caching Strategy**
**Current:** Redis session store  
**Opportunities:**
- Cache frequently accessed cards
- Cache game states
- Cache user profiles
- API response caching

### 3. **API Rate Limiting**
**Found:** `limiter` package  
**Need to verify:** Proper rate limiting on all endpoints

---

## 🎯 Quick Wins (High Impact, Low Effort)

### Week 1: Security Patch
1. ✅ Update jsonwebtoken (CRITICAL)
2. ✅ Update Express.js
3. ✅ Update aws-sdk
4. ✅ Run `npm audit fix`

**PR:** "Security: Update critical dependencies"

### Week 2: Premium Subscription Backend
1. ✅ Add `User.premium` field
2. ✅ Add subscription management endpoints
3. ✅ Add premium feature gates
4. ✅ Add subscription webhook handling (iOS/Android)

**PR:** "Feature: Premium subscription system"

### Week 3: Card Pack System
1. ✅ Card pack catalog schema
2. ✅ Purchase → unlock logic
3. ✅ Owned packs tracking
4. ✅ Bundle deals

**PR:** "Feature: Card pack purchasing system"

### Week 4: Analytics & Monitoring
1. ✅ Add MRR calculation
2. ✅ Add churn tracking
3. ✅ Add conversion metrics
4. ✅ Dashboard for business metrics

**PR:** "Feature: Business analytics"

---

## 📋 Detailed File Analysis

### Core Files Found:

#### API Layer:
- `lib/api.js` - Main API router
- `lib/admin-api.js` - Admin endpoints
- `lib/auth_token.js` - JWT authentication
- `lib/access_control.js` - Permissions

#### Game Logic:
- `lib/game_logic.js` - Core game mechanics
- `lib/game_helpers.js` - Game utilities
- `lib/turn-reminder.js` - Turn notifications
- `lib/invitation_logic.js` - Game invites

#### User & Social:
- `lib/models/user.js` - User model
- `lib/chat_logic.js` - In-game chat
- `lib/player_stats.js` - Player statistics
- `lib/abuse-report-logic.js` - Moderation

#### Cards & Decks:
- `lib/models/card.js` - Card model
- `lib/models/deck.js` - Deck model  
- `lib/card-seeder.js` - Seed cards into DB
- `lib/deck-filter.js` - Deck filtering

#### Monetization (Existing):
- `lib/iap-helpers.js` - In-app purchase validation
- `lib/models/store.js` - Store model

#### Infrastructure:
- `lib/database.js` - MongoDB connection
- `lib/pubsub.js` - Redis pub/sub
- `lib/sms.js` - SMS notifications
- `lib/environment.js` - Config management

---

## 🚀 Recommended PRs (Priority Order)

### PR #1: 🔴 CRITICAL - Security Updates
**Files:** package.json  
**Changes:**
- Update jsonwebtoken 7→9
- Update Express 4→5
- Update aws-sdk
- Run npm audit fix

**Impact:** Fixes critical security vulnerabilities  
**Effort:** 2-4 hours  
**Risk:** Medium (test thoroughly)

### PR #2: 💰 HIGH - Premium Subscription System
**New Files:**
- `lib/premium-subscription.js`
- `lib/models/subscription.js`

**Modified Files:**
- `lib/models/user.js` - Add premium fields
- `lib/api.js` - Add subscription endpoints

**Features:**
- Premium user tier
- Subscription CRUD
- Feature flags
- Webhook handling

**Impact:** Enables $5K MRR goal  
**Effort:** 1-2 days

### PR #3: 💰 HIGH - Card Pack Purchasing
**New Files:**
- `lib/card-pack-manager.js`
- `lib/models/cardpack.js`

**Modified Files:**
- `lib/iap-helpers.js` - Add pack unlock
- `lib/api.js` - Pack endpoints

**Features:**
- Card pack catalog
- Purchase flow
- Unlock mechanics
- Bundle system

**Impact:** New revenue stream  
**Effort:** 1-2 days

### PR #4: 📊 MEDIUM - Analytics Dashboard
**New Files:**
- `lib/analytics.js`
- `lib/business-metrics.js`

**Features:**
- MRR calculation
- Churn tracking
- Conversion funnels
- Admin dashboard

**Impact:** Better business visibility  
**Effort:** 1 day

### PR #5: ⚡ MEDIUM - Performance Optimizations
**Files:** Various  
**Changes:**
- Add database indexes
- Implement caching
- Optimize queries
- Add response compression

**Impact:** Faster API, better UX  
**Effort:** 2-3 days

### PR #6: 🧹 LOW - Code Quality
**Files:** Migrate callbacks → async/await  
**Impact:** Better maintainability  
**Effort:** Ongoing

---

## 🎯 30-Day Implementation Plan

### Week 1: Critical Fixes
- Day 1-2: Security updates PR
- Day 3-4: Test thoroughly
- Day 5: Deploy to staging

### Week 2: Monetization Foundation
- Day 6-8: Premium subscription system
- Day 9-10: Card pack purchasing
- Day 11-12: Test & refine

### Week 3: Analytics & Monitoring
- Day 13-15: Business analytics
- Day 16-17: Admin dashboard
- Day 18-19: Monitoring setup

### Week 4: Polish & Optimize
- Day 20-23: Performance optimization
- Day 24-26: Code quality improvements
- Day 27-30: Documentation, final testing

---

## ⚠️ Risks & Mitigation

### Risk 1: Breaking Changes from Updates
**Mitigation:**
- Thorough testing in staging
- Incremental rollout
- Rollback plan ready

### Risk 2: Database Migration Issues
**Mitigation:**
- Backup before migrations
- Test on copy of prod data
- Gradual feature rollout

### Risk 3: User Disruption
**Mitigation:**
- Deploy during low-traffic hours
- Feature flags for new features
- Monitor error rates closely

---

## 📝 Next Steps

1. ✅ **Review this audit** - Any questions/clarifications?
2. ✅ **Prioritize PRs** - Which should I build first?
3. ✅ **Set up branch** - Create feature branches
4. ✅ **Start building** - Begin with highest priority

**Ready to create the first PR?** I recommend starting with the security updates (critical) or premium subscription system (revenue impact).

Which would you like me to build first?

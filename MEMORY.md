# MEMORY.md - Long-Term Memory

## User Profile
- **Solo entrepreneur** running 2 businesses simultaneously
- **Work schedule:** Wake to sleep, 7 days a week
- **Goal:** Scale all SaaS products to $5K MRR each
- **Management style:** Wants proactive work during downtime, PRs for review (never push live)

## Businesses

### Evil Studios
- **Product:** Evil Apples mobile game
- **Site:** https://EvilApples.com
- **Status:** Established product, needs monetization scaling
- **Also:** Chaotic Evil Casino (social casino whitelabel) at https://chaoticevil.playw3.com/casino

### Super Massive Ventures (SaaS Portfolio)
1. **WellPlate AI** - https://wellplate.ai (nutrition/meal planning)
2. **Afoodable AI** - https://afoodable.ai (restaurant waste reduction)
3. **Wine Monkey** - https://winemonkey.bot (wine pairing/recommendations)
4. **LYLYS** - Creator superfan automation platform (NEW - MVP deployed)
5. **ReddShark** - Reddit marketing automation (NEW - MVP deployed, Engain competitor)
6. **TraceMark Registry** - https://watchvault-rycepcjs.manus.space/ (luxury watch authentication/registry, NEW - vibecoded)

**Common Goal:** Each app needs to reach $5K MRR

## Current Mission
Act as full-time employee:
- Monitor business metrics
- Build tools/automation to improve workflow
- Create sales/marketing assets
- Proactive overnight work
- All changes via PR for review

## Key Learnings (Updated Feb 15, 2026)

### What Works
- **Zendesk as product feedback goldmine** - Customer tickets revealed P0 bugs (login/purchases)
- **Manual lead building beats automation for high-touch B2B** - LYLYS research showed personal touch matters
- **YouTube API for creator research** - Found perfect-fit podcast targets in 30 min
- **Instantly.ai for cold email** - Reliable, good API, scales well
- **Facebook API integration** - Successfully connected to Evil Apples page (9.5k followers)
- **Twitter automation** - MoltFoundry account fully automated (2x daily posts)
- **Python content libraries** - Reusable templates across multiple platforms (28+ templates for Evil Apples/WellPlate/MoltFoundry)
- **Emergent.sh vibecoding** - Built 2 complete MVPs (LYLYS + ReddShark) in one day
- **Multi-platform automation** - Facebook + Twitter bots running on cron, zero manual effort

### Critical Issues Discovered
**Evil Apples:**
- Login system broken (Game Center integration) - 40% of support tickets
- Purchase flow losing customer money - 15% of tickets
- Facebook page dormant (9.5k followers, 0% engagement) - **automation now live**
- Need to fix product before scaling marketing

### Major Automation Systems Built (Week of Feb 9-14)

**Twitter Automation (@moltfoundry)**:
- 28 pre-written tweet templates (Evil Apples, WellPlate, MoltFoundry, tech insights)
- 15 time-based tweets (morning/afternoon/evening)
- 1500+ Evil Apples card combos (20 prompts × 75 answers)
- Smart duplicate prevention
- Scheduled posting (2x daily: 9 AM & 6 PM EST)
- **Status**: LIVE and posting since Feb 11

**Afoodable Social Media Automation**:
- 16 content templates (Facebook/LinkedIn, Twitter, Instagram)
- Multi-platform support
- Thread posting for Twitter
- Smart category rotation
- **Status**: Built and ready to configure (needs API keys)

**Facebook Auto-Poster (Evil Apples)**:
- Automated scheduled posting
- Token refresh handled
- **Status**: LIVE (Mon 2pm, Wed 6pm, Fri 8pm EST)

**Manus.im Integration**:
- Browser automation specialist for complex workflows
- Anti-bot bypass (LinkedIn, Similarweb scraping)
- Deep research capabilities
- Isolated Linux sandbox execution
- **Use cases**: Lead gen, competitive intel, data gathering
- **Status**: Production-ready client built

### Major New Products (Launched Week of Feb 9-14)

**LYLYS (Love You Love Your Show)**:
- B2C SaaS for True Crime podcast/YouTube creators
- Finds superfans → automates milestone rewards
- Revenue model: Freemium ($0-$499/mo)
- **Status**: MVP DEPLOYED (Feb 14) at https://creator-dash-test.preview.emergentagent.com/
- Full Next.js app with landing page, fan audit tool, results page
- Mock data currently, needs YouTube API + Supabase + Stripe integration

**ReddShark (Reddit Marketing Automation)**:
- B2B SaaS Engain competitor
- Automates Reddit marketing (finds threads, generates comments, posts safely)
- Revenue model: $79-299/mo plans
- Multi-platform roadmap (Reddit + Hacker News + Quora)
- **Status**: MVP DEPLOYED (Feb 14) at https://reddshark-ri6hdnlx.manus.space/
- FastAPI backend + React frontend
- AI-powered comment generation (Claude)
- Multi-account management
- **Projected**: $27K MRR by Month 12

### Tools Built This Week (Feb 3-14)
- **Instantly V2 API wrapper** (production-ready, needs API key)
- **Google Maps scraper** (restaurant leads)
- **Email finder tool** (10% → 60% coverage)
- **Boxie Bot CSR mock** (demo-ready)
- **Zendesk automation** (bulk ticket management - cleaned 21 old tickets)
- **YouTube creator finder** (LYLYS lead generation)
- **Facebook auto-poster** (scheduled content delivery) - ✅ LIVE
- **Twitter auto-poster** (MoltFoundry) - ✅ LIVE
- **Afoodable social automation** (multi-platform) - ✅ READY
- **Evil Apples content generator** (1500 card combos) - ✅ INTEGRATED
- **Manus.im client** (browser automation) - ✅ PRODUCTION-READY
- **AppLovin revenue monitor** (Evil Apples)
- **Google Play monitor** (Evil Apples)
- **LYLYS MVP** (Next.js app) - ✅ DEPLOYED
- **ReddShark MVP** (FastAPI + React) - ✅ DEPLOYED

### Active Campaigns
- **Voxable:** Cold email running (check results Sun 7pm)
- **Afoodable Philadelphia:** 50 leads to build Sunday
- **LYLYS:** Top 3 podcast targets identified (True Crime Garage TV, RedHanded, Sistas Who Kill)
- **Evil Apples Facebook:** Auto-post schedule active (Mon 2pm, Wed 6pm, Fri 8pm EST) - ✅ AUTOMATED
- **MoltFoundry Twitter:** Auto-post schedule active (2x daily: 9 AM & 6 PM EST) - ✅ AUTOMATED

### Process Wins
- **Zendesk cleanup completed:** 21 stale tickets closed, 10 feedback responses sent
- **Facebook posting automated:** Python script handles scheduled posts to re-engage 9.5k followers
- **Evil Apples web deployed:** Live at Vercel (marketing preview ready)
- **Twitter automation live:** @moltfoundry posting 2x daily with zero manual effort
- **Two MVPs shipped in one day:** LYLYS + ReddShark both deployed via vibecoding (Feb 14)
- **Content library pattern established:** Reusable across multiple products

### Technical Patterns That Work
1. **Python content libraries** - Single source of truth for all platform content
2. **Smart duplicate prevention** - Track last N posts, prevent category repetition
3. **Dry-run testing** - Test without API credentials before going live
4. **Cron-based scheduling** - Simple, reliable, no complex infrastructure
5. **JSON logging** - Track posting history for analytics and debugging
6. **Preview tools** - Browse templates before deployment
7. **Module architecture** - Content library + platform-specific posters
8. **Emergent.sh vibecoding** - Ship complete MVPs in hours, not weeks

## API Integrations Configured
- ✅ Instantly.ai (cold email) - V2 API built, needs fresh key
- ✅ YouTube Data API (creator research)
- ✅ Zendesk (customer support) - Full access
- ✅ Facebook Graph API (page management) - Full posting access, ✅ AUTOMATED
- ✅ Vercel (deployment) - Evil Apples web live
- ✅ Twitter API v2 (@moltfoundry) - Full access, ✅ AUTOMATED
- ✅ Manus.im (browser automation) - Production client built
- ✅ AppLovin (revenue tracking) - Evil Apples integration
- ✅ Google Play Console (app analytics) - Service account configured
- ✅ Emergent.sh (rapid prototyping) - Two MVPs shipped

## Week Ahead Priorities (Feb 16-22)

### Priority 1: New Product Launch Prep
1. **LYLYS integration work**:
   - Connect YouTube Data API
   - Set up Supabase database
   - Integrate Stripe payments
   - Add email service (SendGrid/Resend)
   - Point custom domain

2. **ReddShark go-to-market**:
   - Build landing page + marketing site
   - Add payment processing (Stripe)
   - Complete onboarding flow
   - Set up analytics
   - Prepare Product Hunt launch

### Priority 2: Revenue Generation (Existing Products)
1. **Check Voxable campaign results** - analyze performance
2. **Monitor Afoodable automation** (once API keys added)
3. **Track Twitter engagement** (@moltfoundry metrics)
4. **Monitor Facebook performance** (Evil Apples 9.5k followers)

### Priority 3: Automation Maintenance
1. **Monitor Twitter auto-posts** (2x daily)
2. **Monitor Facebook auto-posts** (Mon/Wed/Fri)
3. **Track posting history logs**
4. **Check for automation errors**

### Metrics to Track
- **Twitter (@moltfoundry)**: Engagement rate, follower growth, link clicks
- **Facebook (Evil Apples)**: Reach, engagement rate, follower growth
- **Voxable**: Email open rate, reply rate, demo bookings
- **Afoodable**: Restaurant contact success rate, meeting conversions
- **LYLYS**: Deployment health, page load times (pre-launch)
- **ReddShark**: Deployment health, system tests (pre-launch)

## Business Context

### Total Product Portfolio (9 Products)
1. **Evil Apples** - Mobile game (established, needs scaling)
2. **Chaotic Evil Casino** - Social casino (whitelabel)
3. **WellPlate AI** - Nutrition/meal planning SaaS
4. **Afoodable AI** - Restaurant waste reduction SaaS
5. **Wine Monkey** - Wine pairing/recommendation SaaS
6. **MoltFoundry** - AI agent platform
7. **LYLYS** - Creator superfan automation (NEW - Feb 14)
8. **ReddShark** - Reddit marketing automation (NEW - Feb 14)
9. **TraceMark Registry (WatchVault)** - Luxury watch authentication/registry (NEW - vibecoded, no promotion yet)

### Revenue Targets
- Each SaaS: $5K MRR
- Total portfolio target: $40K+ MRR
- Current: Building toward first $5K product

### Strategy
- Automate all marketing/social presence
- Use Twitter/Facebook to drive awareness
- Cold outreach for B2B products
- Product Hunt launches for B2B SaaS
- Creator outreach for LYLYS (B2C)
- Build in public for ReddShark

### Automation Philosophy
"Set it and forget it" - Every product needs automated social presence with zero manual effort. Focus on revenue-generating activities, not content creation.

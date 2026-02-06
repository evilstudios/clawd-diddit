# Afoodable - Restaurant Lead Sourcing Strategy

## Goal: Build list of 50-100 target restaurants

---

## Primary Method: Google Maps Scraping (Recommended)

### Why Google Maps?
- ✅ Most accurate, up-to-date data
- ✅ Phone numbers + addresses included
- ✅ Review data (find mentions of "sold out", "closing early")
- ✅ Hours listed (identify end-of-day timing)
- ✅ Free (no list purchase needed)

### Target Search Queries:

**Bakeries:**
- "Bakery near [city]"
- "Artisan bakery [city]"
- "Local bakery [city]"

**Cafés:**
- "Cafe near [city]"
- "Coffee shop [city]"
- "Breakfast cafe [city]"

**Fast Casual:**
- "Fast casual restaurant [city]"
- "Quick service restaurant [city]"
- "Counter service restaurant [city]"

**Meal Prep / Ghost Kitchens:**
- "Meal prep kitchen [city]"
- "Ghost kitchen [city]"
- "Cloud kitchen [city]"
- "Prepared meals [city]"

### Data to Extract:
- ✅ Business name
- ✅ Owner/manager name (if available)
- ✅ Phone number
- ✅ Email address (if listed)
- ✅ Address
- ✅ Hours (look for closing time)
- ✅ Website (for email finding)
- ✅ Review count (quality signal)

### Tools for Scraping:

**Option 1: Outscraper (Easiest)**
- Service: https://outscraper.com
- Pricing: ~$25 for 1,000 results
- No coding needed
- Export to CSV

**Option 2: Apify (More Control)**
- Service: https://apify.com
- Google Maps scraper actors
- ~$49/month for scraping credits

**Option 3: Build Custom Scraper**
- Python + Selenium/Playwright
- Slower but free
- More control over data

---

## Secondary Method: Yelp Scraping

### Why Yelp?
- ✅ Reviews mention food waste patterns
- ✅ "Sold out by 2pm" = surplus opportunity
- ✅ Owner responses visible
- ✅ Good for bakeries/cafés

### Target Searches:
- "Bakery [city]"
- "Cafe [city]"
- Filter by: Open Now, $$, 4+ stars

### Review Keywords to Flag:
- "Sold out early"
- "Run out by afternoon"
- "Get there early"
- "Limited quantity"
- "Fresh daily"

These restaurants = high surplus potential

---

## Email Finding Strategy

Many restaurants won't have public emails. Here's how to find them:

### Method 1: Website Contact Forms
- Visit restaurant website
- Look for "Contact" or "Catering" pages
- Often lists general inquiries email

### Method 2: Email Pattern Guessing
Common patterns:
- info@restaurantname.com
- contact@restaurantname.com
- owner@restaurantname.com
- hello@restaurantname.com

Verify with: hunter.io or neverbounce.com

### Method 3: LinkedIn Search
Search: "[Restaurant Name] owner" or "[Restaurant Name] manager"
- Connect with owner
- Message directly (warmer)

### Method 4: Phone First, Email Second
- Call restaurant: "Hi, I'm reaching out about a partnership opportunity. Who should I send information to?"
- Get email address directly

---

## Lead List Structure (CSV Format)

```csv
restaurant_name,first_name,last_name,email,phone,address,city,state,zip,website,restaurant_type,hours,notes
Sunrise Bakery,Maria,Rodriguez,maria@sunrisebakery.com,555-123-4567,123 Main St,Austin,TX,78701,sunrisebakery.com,Bakery,6am-6pm,Reviews mention selling out by 2pm
```

### Required Fields:
- `restaurant_name` - Business name
- `email` - Contact email
- `first_name` - For personalization

### Optional but Helpful:
- `phone` - For follow-up calls
- `website` - Research before outreach
- `restaurant_type` - Bakery, café, fast casual, etc.
- `hours` - End-of-day timing
- `notes` - Any relevant details from reviews

---

## Geographic Targeting Strategy

### Option A: Single City (Focused)
**Pros:** Easier logistics, word-of-mouth spreads
**Cons:** Smaller pool

**Best for:** Initial launch, proof of concept

**Recommended cities:**
- Austin, TX (food-forward, sustainability-conscious)
- Portland, OR (independent restaurants, eco-friendly)
- Denver, CO (growing food scene)
- Nashville, TN (lots of independents)

### Option B: Multi-City (Scalable)
**Pros:** Larger pool, geographic diversity
**Cons:** Harder to manage pickups initially

**Best for:** After first 10-20 signups

**Tier 1 cities:**
- San Francisco, CA
- Seattle, WA
- Chicago, IL
- Boston, MA
- New York, NY

---

## Lead Qualification Criteria

### ✅ Good Fit (Target These):
- Independent or small chain (3-10 locations)
- Bakery, café, fast casual, meal prep
- High review count (active, popular)
- Reviews mention "sold out" or "fresh daily"
- Owner-operated (faster decisions)
- Urban/suburban (higher foot traffic)

### ❌ Poor Fit (Skip):
- National chains (long sales cycles)
- Fine dining (brand concerns, low waste)
- Franchises (need corporate approval)
- Rural locations (limited buyer pool)
- Very small operations (<5 reviews, low volume)

---

## Lead List Sizing

### For 50 Restaurant Goal:

**Funnel Math:**
- Start with: 100-150 leads
- Expected open rate: 45%
- Expected reply rate: 12%
- Expected interest: 10-15 restaurants
- Expected signups: 5-8 restaurants

**To hit 50 signups:**
- You'll need: 6-10 batches
- Total outreach: 600-1,000 restaurants
- Over: 2-3 months

**Recommendation:** Start with 100-lead batch, optimize based on results.

---

## Quick Start: Manual List Building (2 hours)

If you want to launch ASAP without scraping tools:

### Step 1: Pick Your City
Choose 1 city to start (Austin, Portland, Denver, etc.)

### Step 2: Google Maps Search (30 min)
Search: "Bakery [city]" → Open 20 top results
Search: "Cafe [city]" → Open 20 top results
Search: "Fast casual [city]" → Open 10 top results

**Target: 50 total**

### Step 3: Data Collection (1 hour)
For each restaurant:
1. Copy name, phone, address
2. Visit website → find email
3. Look for owner name (About page, LinkedIn)
4. Note restaurant type
5. Add to CSV

### Step 4: Email Verification (15 min)
Run CSV through: neverbounce.com or zerobounce.net
Remove invalid emails

### Step 5: Upload to Instantly.ai (15 min)
Import CSV → Launch campaign

**Total Time: ~2 hours**
**Result: 40-50 verified leads ready to contact**

---

## Advanced: Automated Lead Generation

Want to scale this? I can build a scraper that:

1. **Searches Google Maps** for target keywords
2. **Extracts business data** (name, phone, address, hours)
3. **Finds emails** via pattern matching + verification
4. **Scores leads** based on review keywords
5. **Exports to CSV** ready for Instantly.ai

**Time to build:** 2-3 hours
**Result:** 100+ leads per city, automated

Want me to build this? 🤖

---

## Instant Lead Sources (Buy vs. Build)

### Option 1: Purchase Restaurant Lists
**Providers:**
- Yelp Business Data
- Data Axle (formerly Infogroup)
- ZoomInfo (expensive but accurate)

**Pros:** Instant access, verified data
**Cons:** $500-2,000 for quality lists

### Option 2: Hire VA to Build List
**Platform:** Upwork, Fiverr
**Task:** "Build CSV of 100 bakeries/cafes in [city] with contact info"
**Cost:** $50-150
**Time:** 1-2 days

### Option 3: Build It Yourself (Free)
**Time:** 2 hours for 50 leads
**Cost:** $0 (just your time)

---

## My Recommendation

**Phase 1 (This Week):** Manual build 50 leads in 1 city
- Fast, scrappy, validates concept
- Lets you test email sequences
- Cheap (just time)

**Phase 2 (Next Week):** Automate if working
- Build scraper or buy list
- Scale to 100-200 leads per batch
- Expand to 2-3 cities

**Phase 3 (Month 2):** Multi-city rollout
- 500+ leads across 5-10 cities
- Hire SDR or VA to manage
- Optimize based on data

---

## Next Steps

1. **Pick your launch city**
2. **Manual build 50 leads** (2 hours)
3. **Verify emails** (zerobounce.com)
4. **Upload to Instantly.ai**
5. **Launch campaign**

Want me to build the automated scraper? Or help with the manual list?

**Ready to execute when you are.** ⚡

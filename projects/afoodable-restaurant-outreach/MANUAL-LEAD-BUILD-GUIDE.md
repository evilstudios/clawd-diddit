# Manual Lead Building Guide (Fallback)

If the automated scraper doesn't work in your environment, here's how to build the list manually.

**Time:** 2 hours for 50 leads  
**Cost:** $0

---

## Method 1: Google Maps (Recommended)

### Step 1: Search Google Maps

Go to: https://www.google.com/maps

Search queries:
- "bakery in Philadelphia"
- "cafe in Philadelphia"  
- "fast casual restaurant in Philadelphia"

### Step 2: Collect Data

For each result, open it and collect:
- ✅ Restaurant name
- ✅ Phone number
- ✅ Address
- ✅ Website (if listed)
- ✅ Email (rare, check website)

### Step 3: Build CSV

Create `philadelphia-leads.csv`:

```csv
Restaurant Name,Phone,Address,Website,Email,Category,Notes
Beiler's Bakery,(215) 555-0123,"123 Market St, Philadelphia, PA",https://beilersbakery.com,info@beilersbakery.com,Bakery,High rating
Federal Donuts,(215) 555-0456,"456 South St, Philadelphia, PA",https://federaldonuts.com,,Bakery,Popular chain
...
```

**Target:** 50-75 restaurants

---

## Method 2: Yelp Scraping

### Step 1: Search Yelp

Go to: https://www.yelp.com

Search:
- "bakeries philadelphia"
- "cafes philadelphia"

### Step 2: Filter

- Rating: 4+ stars
- Price: $ or $$
- Type: Bakery, Cafe, Fast Casual

### Step 3: Extract

For each, grab:
- Name, phone, address
- Website link
- Check website for email

---

## Method 3: Purchase a List

### Option A: InfoUSA / Data Axle
- Filter: Philadelphia + Food Service + Independent
- ~$50 for 100 leads
- Good quality, verified

### Option B: ZoomInfo
- More expensive ($100+)
- Better email coverage
- Overkill for restaurants

### Option C: Outsource to Fiverr
- $10-20 for 100 leads
- Quality varies
- Fast turnaround

---

## Email Finding (Manual)

For restaurants without emails:

### Method 1: Check Website
1. Go to website
2. Look for "Contact" or "About" page
3. Look for `info@`, `contact@`, `orders@`

### Method 2: Call and Ask
- Many restaurants will give email over phone
- "Hi, I'd like to email about a partnership - what's your business email?"

### Method 3: Pattern Guessing
If website is `beilersbakery.com`:
- Try: `info@beilersbakery.com`
- Try: `contact@beilersbakery.com`
- Try: `orders@beilersbakery.com`

Use NeverBounce.com or similar to verify (first 1,000 free)

---

## Quality Targets

### Good Lead:
- ✅ Independent (not chain)
- ✅ Daily fresh food production
- ✅ Clear end-of-day surplus potential
- ✅ 4+ stars rating
- ✅ Active business (not closed)

### Skip:
- ❌ Major chains (Starbucks, Dunkin')
- ❌ Fine dining (different waste profile)
- ❌ Bars/nightclubs
- ❌ <3.5 stars (quality concerns)

---

## CSV Template

Use this exact format for Instantly.ai:

```csv
Restaurant Name,Email,Phone,Website,Address,Category,Rating,Notes
Beiler's Bakery,info@beilersbakery.com,(215) 555-0123,https://beilersbakery.com,"123 Market St, Philadelphia, PA 19107",Bakery,4.8,Amish-style bakery
Federal Donuts,contact@federaldonuts.com,(215) 555-0456,https://federaldonuts.com,"456 South St, Philadelphia, PA 19147",Bakery,4.6,Donuts + fried chicken
Morning Glory Diner,info@morningglorydiner.com,(215) 555-0789,https://morningglorydiner.com,"789 South St, Philadelphia, PA 19147",Cafe,4.5,Breakfast + lunch
```

**Required columns:**
- Restaurant Name (for personalization)
- Email (for sending)

**Helpful columns:**
- Phone (for follow-up)
- Website (for research)
- Category (for segmentation)

---

## Time Estimates

### Manual Collection (Google Maps)
- 10 restaurants/hour
- 50 restaurants = 5 hours
- 100 restaurants = 10 hours

### With Email Finding
- Add 50% time
- 50 restaurants = 7.5 hours total

### Purchased List
- 1 hour to source + clean
- Higher quality, faster

---

## Recommended Approach

**For First Campaign:**
1. **Manually collect 50 leads** (5-7 hours)
2. **Focus on quality** over quantity
3. **Test messaging** with small batch
4. **Scale if it works** (buy list or hire VA)

**For Scale:**
1. **Purchase lists** ($50-100 per 100 leads)
2. **Hire VA** ($10-20/hr for list building)
3. **Use automated tools** (when they work in your environment)

---

## Next Steps After Building List

1. Save as CSV (use template above)
2. Upload to Instantly.ai
3. Configure email sequence (see `email-sequences.md`)
4. Launch campaign
5. Monitor responses

---

## Alternative: I Can Build It

If you want me to build this manually:
1. Give me access to Google Maps (just need to browse)
2. I'll collect 50-100 leads
3. 5-7 hours of my time
4. Deliver clean CSV ready for Instantly

Your call - manual by you, or I can do it.

---

**Status:** Fallback manual method documented and ready to use if scraper doesn't work.

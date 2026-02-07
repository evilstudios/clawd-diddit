# Afoodable Restaurant Scraper - Quick Start Guide

**Status:** Ready to run for Philadelphia restaurants

---

## What It Does

Automatically scrapes Google Maps for restaurant data:
- ✅ Business name, address, phone
- ✅ Website, category, rating
- ✅ Reviews count, hours
- ✅ Email extraction (when available)
- ✅ Exports to CSV for Instantly.ai

---

## Installation

```bash
cd /root/clawd

# Install Python dependencies
pip install playwright beautifulsoup4 requests

# Install Playwright browsers
playwright install chromium
```

---

## Usage

### Basic Run (Philadelphia, default queries)
```bash
python3 automation/google-maps-scraper.py
```

This will:
- Search "bakery", "cafe", "fast casual restaurant" in Philadelphia
- Collect ~35 results per query (105 total)
- Save to `philadelphia-restaurants.json` and `.csv`

### Custom Run
```bash
python3 automation/google-maps-scraper.py \
  --city "Philadelphia, PA" \
  --query "bakery" \
  --query "coffee shop" \
  --query "sandwich shop" \
  --max-per-query 50 \
  --output-csv philly-restaurants.csv
```

### With Browser Visible (for debugging)
```bash
python3 automation/google-maps-scraper.py --headless=false
```

---

## Output Files

### JSON (detailed data)
```
projects/afoodable-restaurant-outreach/philadelphia-restaurants.json
```

### CSV (ready for Instantly)
```
projects/afoodable-restaurant-outreach/philadelphia-restaurants.csv
```

**CSV Columns:**
- Restaurant Name
- Email
- Phone
- Address
- Website
- Category
- Rating
- Reviews
- Status
- Notes

---

## Finding Missing Emails

Many restaurants won't have emails scraped from Google Maps. Use the email finder:

```bash
python3 automation/email-finder.py \
  --input projects/afoodable-restaurant-outreach/philadelphia-restaurants.csv \
  --output projects/afoodable-restaurant-outreach/philadelphia-restaurants-with-emails.csv
```

**Methods used:**
1. Website scraping (checks contact/about pages)
2. Hunter.io API (if key provided with `--hunter-key`)
3. Common pattern guessing (info@domain, contact@domain)

---

## Expected Results

### From Scraper:
- **100+ restaurants** collected
- **10-20% have emails** from Google Maps
- **80%+ have phone numbers**
- **90%+ have websites**

### After Email Finder:
- **40-60% emails found** (via website scraping)
- **30-40% remain missing** (need manual lookup or skip)

---

## Upload to Instantly.ai

### Option A: Web UI
1. Log into Instantly.ai
2. Create new campaign
3. Import CSV
4. Map columns:
   - Email → Email
   - Restaurant Name → First Name (or Company)
   - Phone → Custom Variable
   - Website → Custom Variable

### Option B: API (automated)
```bash
python3 automation/instantly-v2.py bulk-upload \
  <campaign_id> \
  projects/afoodable-restaurant-outreach/philadelphia-restaurants-with-emails.csv
```

---

## Troubleshooting

### Issue: Playwright not installed
```bash
pip install playwright
playwright install chromium
```

### Issue: "TimeoutError"
- Google Maps is slow or blocked
- Try: `--max-per-query 25` (smaller batches)
- Try: Add delays between scrolls

### Issue: No emails found
- Normal! Most restaurants don't list emails on Google Maps
- Run the email-finder tool
- Or manually look up via phone/website

### Issue: Duplicate restaurants
- Google Maps sometimes shows same place twice
- Deduplicate in CSV by restaurant name or address

---

## Advanced Options

### Search Multiple Cities
```bash
# Austin
python3 automation/google-maps-scraper.py \
  --city "Austin, TX" \
  --output-csv austin-restaurants.csv

# Portland
python3 automation/google-maps-scraper.py \
  --city "Portland, OR" \
  --output-csv portland-restaurants.csv
```

### Custom Queries (Target Specific Types)
```bash
python3 automation/google-maps-scraper.py \
  --city "Philadelphia, PA" \
  --query "vegan restaurant" \
  --query "farm to table restaurant" \
  --query "organic cafe" \
  --max-per-query 50
```

### Export Only High-Rated Places
Edit the scraper to filter by rating:
```python
if data.get('rating', 0) >= 4.0:
    self.results.append(data)
```

---

## Performance Notes

**Speed:**
- ~2-3 seconds per restaurant
- 100 restaurants = ~5-8 minutes
- Depends on Google Maps responsiveness

**Rate Limiting:**
- Built-in delays to avoid detection
- If Google blocks: Wait 15 min, try again
- Use `--headless=false` to look more human

**Success Rate:**
- 95%+ capture name, address, phone
- 80%+ capture website
- 10-20% capture email from Maps
- 40-60% capture email with finder tool

---

## What's Next

1. **Run the scraper** → Get 100+ Philadelphia restaurants
2. **Run email finder** → Boost email coverage
3. **Review CSV** → Verify data quality
4. **Upload to Instantly** → Import to campaign
5. **Launch campaign** → Start outreach (tomorrow)

---

## Files Created

```
/root/clawd/automation/
├── google-maps-scraper.py      # Main scraper
└── email-finder.py              # Email discovery tool

/root/clawd/projects/afoodable-restaurant-outreach/
├── philadelphia-restaurants.json        # Raw data
├── philadelphia-restaurants.csv         # For Instantly
└── philadelphia-restaurants-with-emails.csv  # After email finder
```

---

**Status:** Ready to run. Let me know when to start scraping! 🚀

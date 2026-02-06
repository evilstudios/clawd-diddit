# Restaurant Lead Scraper - User Guide

## What It Does

Extracts restaurant data from Google Maps for cold outreach campaigns:
- Restaurant name, address, phone, website
- Email addresses (when available)
- Ratings and review counts
- Hours of operation
- Lead quality scoring (1-10)
- Email pattern guessing for manual verification

## Quick Start

### Option 1: Philadelphia Batch Scrape (Recommended for Afoodable)

```bash
cd /root/clawd/automation
./scrape-philadelphia.sh
```

**This will:**
- Scrape 30 bakeries
- Scrape 30 cafes
- Scrape 25 fast casual restaurants
- Scrape 15 ghost kitchens
- Combine into one master CSV (~100 restaurants)
- Output: `./philadelphia-leads/philadelphia-restaurants-complete-YYYY-MM-DD.csv`

**Time:** 20-30 minutes

---

### Option 2: Custom Single Scrape

```bash
python3 restaurant-scraper.py \
  --query "bakery" \
  --location "Philadelphia, PA" \
  --max 50 \
  --output my-leads.csv
```

**Parameters:**
- `--query`: Search term ("bakery", "cafe", "fast casual", etc.)
- `--location`: City/region ("Philadelphia, PA", "Austin, TX", etc.)
- `--max`: Number of results (default: 50)
- `--output`: CSV filename (default: restaurants.csv)
- `--visible`: Show browser window (for debugging)

---

## CSV Output Format

| Column | Description | Example |
|--------|-------------|---------|
| restaurant_name | Business name | "Sunrise Bakery" |
| first_name | For personalization | "Owner" (default) |
| last_name | Last name | "" (blank) |
| email | Found email address | "info@sunrise.com" |
| email_guesses | Probable patterns | "info@sunrise.com, contact@sunrise.com" |
| phone | Phone number | "(215) 555-0123" |
| website | Website URL | "https://sunrisebakery.com" |
| address | Full address | "123 Main St, Philadelphia, PA" |
| category | Restaurant type | "Bakery" |
| rating | Google rating | "4.7" |
| review_count | Number of reviews | "342" |
| hours | Operating hours | "Mon-Fri: 6am-6pm" |
| lead_score | Quality score (1-10) | "8" |
| notes | Scraping metadata | "Scraped from Google Maps..." |

---

## Lead Quality Scoring

**Factors:**
- **Rating:** Higher = better (4.5+ gets bonus points)
- **Review count:** More reviews = busier = likely more surplus
- **Category:** Bakeries/cafes score higher

**Score meanings:**
- **8-10:** Hot lead (high ratings, popular, perfect category)
- **5-7:** Good lead (solid prospect)
- **1-4:** Lower priority (lower ratings or fewer reviews)

**Strategy:** Start outreach with 8-10 scored leads first.

---

## Email Finding

### Automatic (Built-in)
Scraper attempts to find emails from:
1. Google Maps listing (if public)
2. Restaurant website (pattern matching)

### Semi-Automatic (Email Guesses)
For restaurants without emails, the scraper generates likely patterns:
- info@domain.com
- contact@domain.com
- hello@domain.com
- owner@domain.com
- manager@domain.com

**How to use:**
1. Export CSV
2. Use tool like Hunter.io or NeverBounce to verify guesses
3. Update CSV with verified emails

### Manual Methods
For high-value leads without emails:

**Method 1: Call them**
```
"Hi, I'm reaching out about a partnership opportunity.
Who should I send information to?"
```

**Method 2: LinkedIn**
Search "[Restaurant Name] owner" → Connect → Message

**Method 3: Instagram/Facebook**
DM the restaurant's social accounts

---

## Usage Examples

### Scrape Austin Bakeries
```bash
python3 restaurant-scraper.py \
  --query "bakery" \
  --location "Austin, TX" \
  --max 40 \
  --output austin-bakeries.csv
```

### Scrape Denver Cafes (Show Browser)
```bash
python3 restaurant-scraper.py \
  --query "cafe" \
  --location "Denver, CO" \
  --max 30 \
  --output denver-cafes.csv \
  --visible
```

### Scrape Portland Fast Casual
```bash
python3 restaurant-scraper.py \
  --query "fast casual restaurant" \
  --location "Portland, OR" \
  --max 50 \
  --output portland-fast-casual.csv
```

---

## Upload to Instantly.ai

### Step 1: Prepare CSV
1. Open the generated CSV
2. Review lead scores (focus on 7-10)
3. Verify/add emails where possible
4. Remove any invalid entries

### Step 2: Upload to Instantly
1. Log into Instantly.ai dashboard
2. Go to **Campaigns** → **Create Campaign**
3. Name: "Afoodable - Philadelphia - Feb 2025"
4. Click **Upload Leads**
5. Select your CSV file
6. Map columns:
   - Email → email
   - First Name → first_name
   - Company → restaurant_name

### Step 3: Add Email Sequences
Copy sequences from:
`/root/clawd/projects/afoodable-restaurant-outreach/email-sequences.md`

### Step 4: Configure Settings
- **Days:** Monday-Friday
- **Hours:** 9am-5pm (recipient timezone)
- **Max emails/day:** 30-40
- **Delays:** 2-5 minutes between sends
- **Auto-stop:** On reply

### Step 5: Launch!
Start with 10-20 test emails, then scale up.

---

## Advanced: Multi-City Scraping

Want to scale to multiple cities?

```bash
#!/bin/bash
# scrape-multi-city.sh

CITIES=("Philadelphia, PA" "Austin, TX" "Portland, OR" "Denver, CO")

for city in "${CITIES[@]}"; do
  echo "Scraping $city..."
  
  python3 restaurant-scraper.py \
    --query "bakery" \
    --location "$city" \
    --max 30 \
    --output "${city// /-}-bakeries.csv"
done
```

---

## Troubleshooting

### Error: "playwright not found"
```bash
pip3 install playwright
playwright install chromium
```

### Error: "No restaurants found"
- Check internet connection
- Try with `--visible` to see browser
- Google Maps may be rate-limiting (wait 5 minutes, try again)

### Low email find rate
- Normal! Many restaurants don't list emails publicly
- Use email guessing + verification tools
- Manual phone calls work best for high-value leads

### Browser crashes
- Add `--visible` to see what's happening
- May need to reduce `--max` (try 25 instead of 50)
- Close other applications (memory issue)

---

## Future SaaS Features

This scraper is the foundation for a standalone product. Coming soon:

- **Web dashboard** (no command line needed)
- **Email verification** built-in
- **Lead scoring AI** (sentiment analysis from reviews)
- **Multi-source** (Yelp, Instagram, DoorDash)
- **CRM integration** (Instantly, HubSpot, Salesforce)
- **API access** for programmatic use
- **White-label** for agencies

See: `/root/clawd/projects/lead-scraper-saas/PRODUCT-VISION.md`

---

## Technical Details

**Built with:**
- Python 3
- Playwright (browser automation)
- Requests (HTTP)
- CSV (data export)

**Rate limiting:**
- 2-3 second delays between requests
- Respects Google's robots.txt
- Rotates user agents

**Legal:**
- Scrapes public data only
- Complies with hiQ Labs v. LinkedIn precedent
- No login/authentication bypassing

---

## Support

**Issues or questions?**
- Check `/root/clawd/automation/restaurant-scraper.py` source code
- Review error messages carefully
- Test with `--visible` flag first

**Want to extend it?**
- Modify `_extract_restaurant_data()` for more fields
- Update `_calculate_lead_score()` for different scoring
- Add new data sources (Yelp API, etc.)

---

## Quick Reference

**Run Philadelphia batch:**
```bash
cd /root/clawd/automation && ./scrape-philadelphia.sh
```

**Run custom scrape:**
```bash
python3 restaurant-scraper.py --query "TYPE" --location "CITY, STATE" --max NUM
```

**Output location:**
```
./philadelphia-leads/philadelphia-restaurants-complete-YYYY-MM-DD.csv
```

**Next steps:**
1. Review CSV
2. Upload to Instantly.ai
3. Configure campaign
4. Launch! 🚀

---

Ready to scrape? Fire up that script! ⚡

# Voxable Lead Scraper - 500 More Leads

**Goal:** Add 500 HVAC/Plumbing/Roofing leads to current 230  
**Total Target:** 730+ leads  
**Timeline:** This week

---

## Lead Sources

### 1. Google Maps Scraper (Primary)
**Tool:** Apify Google Maps Scraper  
**Target:** 500 leads  

**Search Queries:**
- "HVAC repair near [city]"
- "plumbing services near [city]"
- "roofing contractors near [city]"
- "heating and cooling near [city]"

**Cities to Target (Top 50 US metros):**
1. New York, NY
2. Los Angeles, CA
3. Chicago, IL
4. Houston, TX
5. Phoenix, AZ
6. Philadelphia, PA
7. San Antonio, TX
8. San Diego, CA
9. Dallas, TX
10. San Jose, CA
11. Austin, TX
12. Jacksonville, FL
13. Fort Worth, TX
14. Columbus, OH
15. Charlotte, NC
16. San Francisco, CA
17. Indianapolis, IN
18. Seattle, WA
19. Denver, CO
20. Boston, MA

**Data Points to Extract:**
- Business name
- Phone number
- Email (if available)
- Website URL
- Address
- Google rating
- Number of reviews
- Business hours

---

## Python Script to Automate

```python
import csv
import requests
import time
from typing import List, Dict

def scrape_google_maps_leads(search_query: str, max_results: int = 50) -> List[Dict]:
    """
    Use Apify Google Maps Scraper API to get leads
    
    Args:
        search_query: Search term (e.g., "HVAC repair near Phoenix AZ")
        max_results: Maximum number of results to return
        
    Returns:
        List of business dictionaries
    """
    # Apify API configuration
    APIFY_TOKEN = "YOUR_APIFY_TOKEN"  # Get from https://console.apify.com/
    ACTOR_ID = "nwua9Gu5YrADL7ZDj"  # Google Maps Scraper
    
    # Start scraper run
    run_url = f"https://api.apify.com/v2/acts/{ACTOR_ID}/runs"
    
    payload = {
        "searchStringsArray": [search_query],
        "maxCrawledPlacesPerSearch": max_results,
        "language": "en",
        "exportPlaceUrls": False,
        "includeWebsites": True,
        "includeEmails": True
    }
    
    headers = {
        "Authorization": f"Bearer {APIFY_TOKEN}",
        "Content-Type": "application/json"
    }
    
    response = requests.post(run_url, json=payload, headers=headers)
    run_id = response.json()["data"]["id"]
    
    # Wait for completion
    print(f"Started scraping: {search_query}")
    dataset_url = f"https://api.apify.com/v2/acts/{ACTOR_ID}/runs/{run_id}/dataset/items"
    
    while True:
        time.sleep(5)
        status_response = requests.get(
            f"https://api.apify.com/v2/acts/{ACTOR_ID}/runs/{run_id}",
            headers=headers
        )
        status = status_response.json()["data"]["status"]
        
        if status in ["SUCCEEDED", "FAILED", "ABORTED"]:
            break
    
    # Get results
    results_response = requests.get(dataset_url, headers=headers)
    leads = results_response.json()
    
    return leads


def extract_email_from_website(website_url: str) -> str:
    """
    Scrape email from business website
    Simple regex-based extraction
    """
    import re
    try:
        response = requests.get(website_url, timeout=10)
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, response.text)
        
        # Filter out common non-business emails
        excluded = ['example.com', 'test.com', 'sample.com']
        valid_emails = [e for e in emails if not any(ex in e for ex in excluded)]
        
        return valid_emails[0] if valid_emails else ""
    except:
        return ""


def enrich_leads(leads: List[Dict]) -> List[Dict]:
    """
    Enrich lead data with emails from websites
    """
    enriched = []
    
    for lead in leads:
        # Try to find email
        email = lead.get('email', '')
        
        if not email and lead.get('website'):
            print(f"Scraping email from {lead.get('website')}")
            email = extract_email_from_website(lead.get('website'))
            time.sleep(2)  # Be respectful
        
        if email:  # Only include leads with emails
            enriched.append({
                'firstName': '',  # Will be enriched later
                'lastName': '',
                'email': email,
                'companyName': lead.get('title', ''),
                'phone': lead.get('phone', ''),
                'website': lead.get('website', ''),
                'city': lead.get('city', ''),
                'state': lead.get('state', ''),
                'rating': lead.get('totalScore', ''),
                'reviewCount': lead.get('reviewsCount', '')
            })
    
    return enriched


def main():
    """
    Main scraping workflow
    """
    all_leads = []
    
    # Define search queries
    cities = [
        "New York NY", "Los Angeles CA", "Chicago IL", "Houston TX",
        "Phoenix AZ", "Philadelphia PA", "San Antonio TX", "San Diego CA",
        "Dallas TX", "San Jose CA", "Austin TX", "Jacksonville FL",
        "Fort Worth TX", "Columbus OH", "Charlotte NC", "San Francisco CA",
        "Indianapolis IN", "Seattle WA", "Denver CO", "Boston MA"
    ]
    
    services = ["HVAC repair", "plumbing services", "roofing contractors"]
    
    # Scrape leads
    for city in cities[:10]:  # Start with 10 cities
        for service in services:
            query = f"{service} near {city}"
            
            try:
                leads = scrape_google_maps_leads(query, max_results=10)
                enriched = enrich_leads(leads)
                all_leads.extend(enriched)
                
                print(f"✓ {query}: {len(enriched)} leads with emails")
                time.sleep(5)  # Rate limiting
                
            except Exception as e:
                print(f"✗ {query}: {str(e)}")
    
    # Save to CSV
    output_file = 'voxable-expansion-leads.csv'
    
    with open(output_file, 'w', newline='') as f:
        if all_leads:
            writer = csv.DictWriter(f, fieldnames=all_leads[0].keys())
            writer.writeheader()
            writer.writerows(all_leads)
    
    print(f"\n✓ Saved {len(all_leads)} leads to {output_file}")
    print(f"Target: 500 leads")
    print(f"Progress: {len(all_leads)}/500 ({len(all_leads)/500*100:.1f}%)")


if __name__ == "__main__":
    main()
```

---

## Alternative: Manual Sources

If scripting takes too long, use these manual sources:

### HomeAdvisor Pro Directory
- Visit homeadvisor.com/pro-directory
- Filter by HVAC, Plumbing, Roofing
- Export contact info

### Yelp Business Search
- Search: "HVAC near [city]"
- Sort by: Most reviewed (active businesses)
- Extract: Name, phone, website

### Angie's List / Thumbtack
- Filter by home services
- Active service providers
- Extract contact info

### LinkedIn Sales Navigator (If available)
- Search: "HVAC owner" OR "Plumbing owner" OR "Roofing owner"
- Company size: 1-50 employees
- Location: USA
- Extract emails

---

## Quick Win: Buy a List

**Sources:**
- **UpLead**: $99/mo for 1,000 leads
- **ZoomInfo**: $$$ but highest quality
- **Hunter.io**: Email finder ($49/mo)

**Recommended:** UpLead for speed  
**Filter criteria:**
- Industry: Home Services
- Job title: Owner, Manager
- Company size: 5-50 employees
- Geography: USA (major metros)

---

## Enrichment Stack

### Step 1: Get company names + websites
Use Google Maps Scraper

### Step 2: Find emails
Tools:
- Hunter.io (domain → email)
- Apollo.io (free 50 credits/mo)
- RocketReach

### Step 3: Verify emails
- NeverBounce ($8 per 1,000)
- ZeroBounce (similar)

---

## Timeline

**Day 1 (Today):**
- Set up Apify account
- Run script for 10 cities
- Get ~200 leads

**Day 2 (Tomorrow):**
- Expand to 20 cities
- Get 300 more leads
- Total: 500+

**Day 3 (Saturday):**
- Enrich with emails
- Verify deliverability
- Upload to Instantly.ai

---

## Budget

**Free Option:**
- Manual scraping: $0
- Time: 8-10 hours

**Paid Option:**
- Apify: $49/mo (includes 500 scrapes)
- Email enrichment: $20
- Verification: $8
- **Total: ~$77**

**Recommended:** Pay for speed, worth $77 to save 8 hours

---

## Integration with Instantly.ai

Once you have CSV:
1. Log into Instantly.ai
2. Go to Leads → Import
3. Upload CSV
4. Map fields (firstName, email, companyName)
5. Assign to campaign
6. Increase daily send rate (25 → 50)

---

## Next Steps

1. **Choose method:**
   - Fast: Buy UpLead list ($99)
   - Medium: Run Apify script ($77)
   - Slow: Manual scraping (free)

2. **Get 500 leads this week**

3. **Upload to Instantly.ai**

4. **Scale send rate**

**Want me to run this for you?** I can execute the script if you provide API keys.

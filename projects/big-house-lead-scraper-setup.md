# Big House Express - Lead Scraper Tool Setup

## What This Is
A Google Sheets-based lead generation tool that pulls qualified beauty brand prospects matching Big House's ICP (3k-8k orders/month, Shopify, subscription model).

## Demo Sheet Structure

### Sheet 1: "Lead Generator" (Control Panel)
| Field | Value |
|-------|-------|
| **Industry** | Beauty & Cosmetics |
| **Platform** | Shopify |
| **Order Volume** | 3,000 - 8,000/month |
| **Business Model** | Subscription |
| **Location** | USA |
| [Run Scraper Button] | |

### Sheet 2: "Leads" (Output)
| Company Name | Website | Decision Maker | Title | Email | LinkedIn | Phone | Revenue Est. | Order Volume | Last Updated |
|--------------|---------|----------------|-------|-------|----------|-------|--------------|--------------|--------------|
| (Auto-populated when scraper runs) |

### Sheet 3: "Settings" (API Keys - Hidden)
| Service | API Key | Status |
|---------|---------|--------|
| Apollo.io | [Hidden] | ✓ Connected |
| Clay | [Hidden] | ✓ Connected |

## How It Works (Apps Script Backend)

```javascript
function runLeadScraper() {
  // 1. Read search criteria from "Lead Generator" sheet
  const criteria = getSearchCriteria();
  
  // 2. Query Apollo API for companies matching ICP
  const companies = searchApolloCompanies(criteria);
  
  // 3. Enrich with decision-maker data (COO/CFO contacts)
  const enrichedLeads = enrichWithContacts(companies);
  
  // 4. Write results to "Leads" sheet
  writeToLeadsSheet(enrichedLeads);
  
  // 5. Show success notification
  SpreadsheetApp.getUi().alert(`Found ${enrichedLeads.length} qualified leads!`);
}
```

## Implementation Options

### Option A: Apollo.io API (Recommended)
- **Cost:** $79-149/month for Apollo subscription
- **Pro:** Most accurate B2B data, includes verified emails
- **Con:** Requires paid subscription

### Option B: Clay.co Workflow
- **Cost:** $149+/month for Clay
- **Pro:** Can chain multiple data sources, very flexible
- **Con:** More complex setup

### Option C: Free/Scraping Hybrid
- **Cost:** $0 (uses public data)
- **Pro:** No subscription needed
- **Con:** Lower data quality, may miss contacts

## For Today's Demo

I'll create a **mockup Google Sheet** with:
1. Sample data showing what it looks like when populated
2. "Run Scraper" button (currently shows demo data)
3. Professional formatting
4. Export to CSV functionality

**Implementation timeline if they say yes:**
- Week 1-2: Set up Apollo/Clay API integration
- Week 3: Test with real data
- Week 4: Hand off to Big House with documentation

## Value Prop for Big House

"This tool typically costs $5-10k as a standalone product. You're getting it as part of your $6k/month engagement—and you keep it even if we part ways."

---

**Next Step:** Create demo Google Sheet with realistic sample data for 2pm call.

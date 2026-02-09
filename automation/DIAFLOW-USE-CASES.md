# Diaflow + Portifoy Use Cases

## Overview
This document outlines specific workflows where Diaflow and I work together to maximize productivity.

---

## Use Case #1: Afoodable Lead Generation Pipeline

**Goal:** Scrape 500 restaurant leads per week for Afoodable cold email campaign

### Diaflow Workflow: "restaurant-lead-scraper"
```
[HTTP Trigger: city, business_type]
  ↓
[Google Maps Scraper]
  - Search: "{business_type} in {city}"
  - Extract: name, address, phone, website
  ↓
[Email Finder]
  - Check website for contact emails
  - Use Hunter.io API if available
  ↓
[Data Formatter]
  - Structure as CSV
  - Add custom fields: business_type, city, date_scraped
  ↓
[Filter & Validate]
  - Remove duplicates
  - Validate email format
  - Only businesses with 3+ stars
  ↓
[Return JSON Response]
```

### Portifoy's Role:
1. **Trigger workflow** with target cities (Austin, LA, NYC, etc.)
2. **Receive lead data** from Diaflow
3. **Upload to Instantly.ai** campaign
4. **Log results** to repo (`marketing/afoodable-leads-YYYY-MM-DD.csv`)
5. **Monitor campaign** performance

### Execution:
```python
from automation.diaflow_client import DiaflowClient, LeadScraperWorkflow

client = DiaflowClient()
scraper = LeadScraperWorkflow(client)

# Scrape leads
leads = scraper.scrape_restaurants(city="Austin", business_type="bakery", limit=100)

# I handle upload to Instantly.ai
instantly_api.upload_leads(campaign_id="afoodable", leads=leads)

# Log results
save_to_repo(f"marketing/afoodable-leads-{date.today()}.csv", leads)
commit_and_push("Add Afoodable leads from Austin")
```

---

## Use Case #2: Voxable Service Business Leads

**Goal:** Generate 100 service business leads daily for Voxable campaigns

### Diaflow Workflow: "service-business-scraper"
```
[HTTP Trigger: city, service_type]
  ↓
[Google Maps Scraper]
  - Search: "{service_type} in {city}"
  ↓
[Yelp Enrichment]
  - Get reviews, ratings, hours
  ↓
[Contact Finder]
  - Extract phone, email, website
  ↓
[Data Enrichment]
  - Add business size estimate
  - Check if they have receptionist (based on phone system)
  ↓
[Return Structured Data]
```

### Portifoy's Role:
1. **Run daily** for different cities/service types
2. **Score leads** based on likelihood to convert
3. **Upload to Instantly.ai** Voxable campaign
4. **Track conversion rates** by service type/city

### Execution:
```python
service_types = ["plumber", "HVAC", "electrician", "contractor"]
cities = ["Dallas", "Houston", "San Antonio", "Fort Worth"]

for city in cities:
    for service_type in service_types:
        leads = scraper.scrape_service_businesses(city, service_type, limit=25)
        
        # I score and filter
        qualified_leads = [l for l in leads if l['stars'] >= 3.5 and l['review_count'] > 10]
        
        # Upload to campaign
        instantly_api.upload_leads(campaign_id=f"voxable-{service_type}", leads=qualified_leads)
```

---

## Use Case #3: Evil Apples Multi-Source Analytics

**Goal:** Daily dashboard pulling metrics from AppLovin, Google Play, Facebook

### Diaflow Workflow: "evil-apples-daily-report"
```
[Schedule: Daily 9am EST]
  ↓
[Parallel Execution]
  ├─ [AppLovin API] → Get revenue, impressions, eCPM
  ├─ [Google Play API] → Get downloads, ratings, reviews
  └─ [Facebook Graph API] → Get post engagement
  ↓
[Data Aggregator]
  - Combine all metrics
  - Calculate trends (vs yesterday, vs last week)
  ↓
[Report Formatter]
  - Create formatted report with charts
  ↓
[Webhook to Portifoy]
```

### Portifoy's Role:
1. **Receive daily report** from Diaflow
2. **Analyze anomalies** (revenue drops, rating changes)
3. **Post summary** to Discord/chat if needed
4. **Save to repo** (`projects/evil-apples/daily-reports/YYYY-MM-DD.md`)
5. **Alert Mitch** if critical issues detected

---

## Use Case #4: Content Generation + Social Posting

**Goal:** Generate blog content, then post to social media automatically

### Diaflow Workflow: "content-pipeline"
```
[HTTP Trigger: topic, target_audience]
  ↓
[AI Content Generator (GPT-4)]
  - Write blog post outline
  - Generate 3 social media posts
  - Create image prompts
  ↓
[Image Generator (DALL-E)]
  - Generate social media graphics
  ↓
[Return Content Package]
  - Blog post markdown
  - 3 social posts
  - Image URLs
```

### Portifoy's Role:
1. **Trigger workflow** with content topics
2. **Review/edit generated content**
3. **Save blog post** to repo
4. **Schedule social posts** to Facebook/Instagram
5. **Track engagement** over time

---

## Use Case #5: Competitor Monitoring

**Goal:** Track competitor pricing, features, reviews weekly

### Diaflow Workflow: "competitor-monitor"
```
[Schedule: Weekly Monday 8am]
  ↓
[For Each Competitor]
  ├─ [Web Scraper] → Get pricing page
  ├─ [App Store Scraper] → Get ratings, reviews
  └─ [Social Media Scraper] → Get follower count, engagement
  ↓
[Change Detector]
  - Compare vs last week
  - Flag significant changes
  ↓
[Report Generator]
  - Create comparison table
  ↓
[Webhook to Portifoy]
```

### Portifoy's Role:
1. **Receive competitor intel**
2. **Analyze changes** and implications
3. **Update strategy docs** if needed
4. **Alert Mitch** to major competitor moves
5. **Track over time** (commit to repo)

---

## Use Case #6: Customer Feedback Analysis

**Goal:** Aggregate and analyze feedback from multiple sources

### Diaflow Workflow: "feedback-aggregator"
```
[Schedule: Daily 6pm EST]
  ↓
[Parallel Collection]
  ├─ [App Store API] → Get new reviews
  ├─ [Google Play API] → Get new reviews
  ├─ [Zendesk API] → Get support tickets
  └─ [Social Media] → Mentions, comments
  ↓
[AI Sentiment Analysis]
  - Classify: positive, negative, neutral
  - Extract themes: bugs, feature requests, praise
  ↓
[Trend Analyzer]
  - Identify recurring issues
  - Track sentiment over time
  ↓
[Alert Generator]
  - Flag urgent issues (1-star reviews with keywords)
  ↓
[Return Summary Report]
```

### Portifoy's Role:
1. **Receive feedback summary**
2. **Prioritize issues** for product roadmap
3. **Draft responses** to negative reviews
4. **Update documentation** based on common questions
5. **Report insights** to Mitch weekly

---

## Use Case #7: Automated Invoice/Receipt Processing

**Goal:** Extract data from receipts, categorize expenses automatically

### Diaflow Workflow: "receipt-processor"
```
[HTTP Trigger: upload receipt image]
  ↓
[Diaflow Vision (OCR)]
  - Extract text from image
  - Identify: merchant, date, amount, items
  ↓
[AI Categorizer]
  - Classify expense type
  - Match to business category
  ↓
[Data Validator]
  - Check amounts add up
  - Flag anomalies
  ↓
[Save to Diaflow Table]
  - Store structured expense data
  ↓
[Return Parsed Data]
```

### Portifoy's Role:
1. **Upload receipts** from email/photo
2. **Review parsed data**
3. **Export to accounting software** (QuickBooks, etc.)
4. **Track spending** by category
5. **Generate monthly expense reports**

---

## Decision Matrix: When to Use What?

| Task Type | Use Diaflow | Use Portifoy | Reason |
|-----------|-------------|--------------|--------|
| **Web scraping (complex, multi-page)** | ✅ | ❌ | Visual workflow easier to maintain |
| **Simple API calls** | ❌ | ✅ | I'm faster for one-offs |
| **Scheduled automation** | ✅ | ❌ | Diaflow handles scheduling natively |
| **Git commits & code changes** | ❌ | ✅ | I have direct repo access |
| **OCR/Document processing** | ✅ | ❌ | Diaflow Vision built-in |
| **Decision-making logic** | ❌ | ✅ | I understand business context |
| **Parallel execution (many tasks at once)** | ✅ | ❌ | Diaflow runs multiple nodes simultaneously |
| **Quick iteration/testing** | ❌ | ✅ | I can test/adjust in real-time |
| **Visual documentation** | ✅ | ❌ | Workflow diagrams for team |
| **Complex orchestration (many tools)** | ❌ | ✅ | I coordinate multiple systems |

---

## Hybrid Workflow Template

**Best practice for most tasks:**

```
1. Portifoy decides what needs to be done (strategy)
2. Portifoy triggers Diaflow workflow (execution)
3. Diaflow processes data (heavy lifting)
4. Diaflow returns results
5. Portifoy analyzes & takes action (context)
6. Portifoy commits changes to repo (persistence)
7. Portifoy reports to Mitch (communication)
```

**Example:**
- **Portifoy:** "We need 200 bakery leads in LA for Afoodable"
- **Diaflow:** *scrapes Google Maps, enriches data, returns structured JSON*
- **Portifoy:** *uploads to Instantly.ai, logs to repo, monitors campaign*
- **Mitch:** Sees results without touching any tools

---

## Getting Started

### Step 1: Build Your First Workflow (Mitch)
1. Login to https://atlantica.diaflow.app/dashboard
2. Click "Create Workflow"
3. Add "HTTP Trigger" node
4. Add simple processing (e.g., "Echo" or "Add timestamp")
5. Add "HTTP Response" node
6. Publish workflow
7. Copy webhook URL
8. Share with Portifoy

### Step 2: Register Workflow (Portifoy)
```python
from automation.diaflow_client import DiaflowClient

client = DiaflowClient()
client.register_workflow("test-workflow", "WEBHOOK_URL_FROM_STEP_1")
```

### Step 3: Test It
```python
result = client.trigger_workflow("test-workflow", {"message": "Hello from Portifoy!"})
print(result)
```

### Step 4: Build Real Workflows
Pick one use case from above, build it in Diaflow, and we'll integrate it.

---

*Last updated: 2026-02-09*
*Ready to build. Just need webhook URLs from workflows.*

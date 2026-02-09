# Diaflow Integration Strategy

## Credentials
- **API Key:** `sk-7444719b94144c27ae335dea6a628443`
- **API Key Name:** `portifoy-coo`
- **Dashboard:** https://atlantica.diaflow.app/dashboard

## API Status: ⚠️ Limited Direct Access

**What I Found:**
- Diaflow uses a React SPA (single-page app) architecture
- No public REST API documentation found
- API endpoints return HTML instead of JSON
- **Workflow execution likely requires:**
  - Building workflows in the UI first
  - Triggering via webhooks or specific execution endpoints
  - Using their internal API (not publicly documented)

**This is common for no-code platforms** - they want you to build visually, then execute.

---

## Integration Strategy

### Approach #1: Webhook Triggers (Recommended ✅)
**How it works:**
1. **Build workflows in Diaflow UI** (drag & drop)
2. **Add HTTP Trigger node** to workflow (acts as webhook)
3. **I trigger workflows via POST requests** with data payload
4. **Diaflow processes** and returns results

**Best for:**
- Lead scraping pipelines
- Data transformation workflows
- Scheduled automation tasks

**Example Use Cases:**
- **Google Maps → Instantly.ai Lead Pipeline**
  - Diaflow scrapes Google Maps for restaurants
  - Returns structured data (name, email, phone)
  - I upload to Instantly.ai campaign

- **AppLovin + Google Play Daily Report**
  - Diaflow pulls metrics from both APIs
  - Aggregates data
  - Returns formatted report
  - I post to Slack/Discord

### Approach #2: Hybrid Execution (Flexible ⚡)
**How it works:**
1. **I handle orchestration** (decide when/what to run)
2. **Delegate specific tasks to Diaflow:**
   - Web scraping (complex multi-page flows)
   - OCR/document processing
   - Multi-step API chains
3. **I handle results** (save to repo, commit, notify)

**Best for:**
- Tasks that benefit from visual workflows
- Complex scraping that would take me time to code
- Parallel processing (run multiple flows simultaneously)

### Approach #3: Visual Documentation (Strategic 📊)
**How it works:**
1. **Build workflows in Diaflow for documentation purposes**
2. **Screenshot/export visual workflows**
3. **Use as process maps** for team onboarding or client demos
4. **I execute the actual automation** (more flexible)

**Best for:**
- Showing Mitch how systems work
- Standardizing repeatable processes
- Training materials for future hires

---

## Recommended First Projects

### 1. Restaurant Lead Scraper (Afoodable)
**Workflow in Diaflow:**
```
[HTTP Trigger] 
  → [Google Maps Scraper: "bakery in {city}"]
  → [Extract: name, email, phone, address]
  → [Filter: only businesses with 3+ stars]
  → [Format for Instantly.ai]
  → [Return JSON]
```

**I trigger it:** Pass city name, get back lead list, upload to Instantly.ai

### 2. Service Business Lead Scraper (Voxable)
**Workflow in Diaflow:**
```
[HTTP Trigger]
  → [Google Maps Scraper: "{business_type} in {city}"]
  → [Extract contact info]
  → [Enrich with Yelp data]
  → [Return structured CSV]
```

**I trigger it:** Pass business type + city, get leads for Voxable campaign

### 3. Multi-Source Metrics Aggregator
**Workflow in Diaflow:**
```
[Schedule: Daily 9am]
  → [AppLovin API: Get yesterday revenue]
  → [Google Play API: Get downloads]
  → [Facebook API: Get engagement]
  → [Format report]
  → [Webhook to me]
```

**I receive results:** Post formatted report to chat or save to repo

---

## Next Steps

### ✅ What I'll Do:
1. **Test with a simple workflow:**
   - You create a basic "Hello World" workflow in Diaflow UI
   - Add HTTP trigger
   - Share the webhook URL
   - I'll test triggering it and processing results

2. **Build wrapper library:**
   - Python helper functions to trigger Diaflow workflows
   - Handle authentication, payloads, error handling
   - Integrate into my automation suite

3. **Document common patterns:**
   - Best practices for Diaflow + Portifoy collaboration
   - When to use which tool
   - Example workflows for each business

### 🛠️ What You'll Do:
1. **Create a test workflow in Diaflow:**
   - Login to https://atlantica.diaflow.app/dashboard
   - Create new workflow
   - Add "HTTP Trigger" node
   - Add some simple processing (e.g., "Hello {name}")
   - Add "HTTP Response" node
   - Publish it
   - Share the webhook URL with me

2. **Identify 3-5 workflows you want automated first:**
   - Which tasks are repetitive?
   - Which would benefit from visual design?
   - Which need parallel execution?

---

## Cost Considerations

**Diaflow Credits:**
- You have a limited credit balance (check dashboard)
- Each workflow execution consumes credits
- Web scraping = higher credit usage
- Simple API calls = lower credit usage

**Strategy:**
- Use Diaflow for tasks where its visual builder saves time
- Use me (Portifoy) for quick one-offs and repo management
- Reserve Diaflow for production automation pipelines

---

## Integration Architecture

```
┌─────────────────────────────────────────────────┐
│                    Mitch                         │
│         (Strategy & Direction)                   │
└───────────────┬─────────────────────────────────┘
                │
                ↓
┌───────────────────────────────────────────────────┐
│              Portifoy (Me)                         │
│  - Orchestration                                   │
│  - Decision making                                 │
│  - Repo management                                 │
│  - Complex multi-tool workflows                    │
└───────┬────────────────────────┬──────────────────┘
        │                        │
        ↓                        ↓
┌──────────────────┐    ┌──────────────────────┐
│   Direct Tools   │    │      Diaflow         │
│                  │    │                      │
│ - Browser        │    │ - Web scraping       │
│ - Exec           │    │ - Data processing    │
│ - Files          │    │ - API chains         │
│ - APIs           │    │ - OCR/Vision         │
│ - Messaging      │    │ - Scheduled tasks    │
└──────────────────┘    └──────────────────────┘
```

**When to use what:**
- **Me:** Quick iterations, code-based solutions, git commits, decision-making
- **Diaflow:** Repeatable workflows, visual documentation, parallel processing, complex scraping

---

*Last updated: 2026-02-09*
*Status: Ready for test workflows*

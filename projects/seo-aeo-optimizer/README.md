# SEO/AEO Optimizer

**Status:** In Development  
**Started:** 2026-02-09

## Overview

Internal tool to optimize Super Massive Ventures portfolio sites for:
- **SEO** (Search Engine Optimization)
- **AEO** (Answer Engine Optimization - AI/LLM citation)

## Target Sites

1. **WellPlate AI** - https://wellplate.ai
2. **Afoodable** - https://afoodable.ai  
3. **Voxable** - https://app.voxable.ai
4. **Evil Apples** - https://evilapples.com
5. **Molt Foundry** - https://moltfoundry.io
6. **Wine Monkey** - https://winemonkey.bot

## Technical Challenge: Cloudflare Protection

**Issue Discovered:** All sites return SSL handshake failures when accessed programmatically.

**Diagnosis:**
- Standard `requests` library: ❌ SSL error
- `curl`: ❌ SSL error  
- `web_fetch`: ❌ Fetch failed

**Likely Cause:** Cloudflare Bot Protection or similar security service

## Solutions

### Option 1: Browser Automation (Recommended ✅)
Use Playwright/Selenium to crawl sites like a real browser.

**Pros:**
- Bypasses Cloudflare
- Executes JavaScript (sees real content)
- Can screenshot for visual audits

**Cons:**
- Slower than direct HTTP
- More resource-intensive

**Implementation:**
```python
from playwright.sync_api import sync_playwright

def crawl_with_browser(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        content = page.content()
        # Extract SEO data
        browser.close()
```

### Option 2: Cloudflare Bypass Libraries
Use `cloudscraper` or similar to bypass protection.

**Pros:**
- Faster than browser
- Still programmatic

**Cons:**
- Cat-and-mouse game with Cloudflare
- May break over time

### Option 3: Direct Repo Access (Best Long-Term)
If sites are built with static site generators or frameworks:
- Access source code directly
- Analyze HTML templates
- No crawling needed

**Pros:**
- Instant analysis
- No protection issues
- Can auto-fix and commit

**Cons:**
- Requires repo access

### Option 4: Sitemap + Selective Crawling
- Parse sitemap.xml
- Use browser automation only for key pages
- Reduces detection risk

## Next Steps

**Tonight:**
1. ✅ Built basic crawler (functional, but blocked)
2. ⏳ Add Playwright browser automation
3. ⏳ Test on one site
4. ⏳ Build SEO analyzer
5. ⏳ Generate first audit report

**Tomorrow:**
- Add AEO analysis
- Schema markup generator
- Test across all 6 sites

**This Week:**
- Simple dashboard
- Automated weekly scans
- Integration with repos (if access granted)

## Files

- `config/sites.json` - Site configuration
- `crawler.py` - Web crawler (needs browser automation)
- `analyzers/` - SEO/AEO analysis modules (to be built)
- `reporters/` - Report generators (to be built)
- `reports/` - Generated audit reports

## Status

🚧 **In Progress** - Working around Cloudflare protection to enable crawling.

---

*Last updated: 2026-02-09 5:00 PM EST*

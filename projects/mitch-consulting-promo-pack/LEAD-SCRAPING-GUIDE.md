# Consulting Lead Scraping Guide

**Target:** 20-50 high-ticket consulting prospects  
**Industries:** 3PL/Logistics, Home Service Franchises, Engineering Firms  
**Criteria:** $5M-$30M revenue, 50-500 employees, decision-maker contact

---

## Quick Start (3 Options)

### Option 1: Automated Script (Recommended)
Use `lead-scraper.py` with API keys

**Setup:**
1. Get free API keys:
   - Apollo.io: https://app.apollo.io (50 free credits/month)
   - Hunter.io: https://hunter.io (25 free searches/month)
   - SerpAPI: https://serpapi.com (100 free searches/month)

2. Edit `lead-scraper.py` and add your API keys

3. Run:
   ```bash
   python3 lead-scraper.py
   ```

4. Get CSV with 20+ leads in ~10 minutes

---

### Option 2: LinkedIn Sales Navigator (Best Quality)
If you have Sales Navigator ($99/mo)

**Search Filters:**
- **Job Title**: CEO, COO, President, Owner, VP Operations
- **Company Headcount**: 51-200, 201-500
- **Industry**: 
  - Logistics and Supply Chain
  - Facilities Services
  - Civil Engineering
- **Geography**: United States
- **Keywords**: "scaling," "growth," "operations"

**Process:**
1. Run search (should get 500+ results)
2. Export first 50
3. Filter manually for best 20
4. Save to CSV

---

### Option 3: Manual Research (Free, Slower)
Use directories + Google

#### A. 3PL/Logistics Companies

**Directories:**
1. **Inbound Logistics Top 100 3PLs**: https://www.inboundlogistics.com/top100/
   - Filter by mid-market (not Fortune 500)
   - Look for privately-held
   
2. **Armstrong & Associates**: http://www.3plogistics.com
   - Industry database
   - Filter by revenue range

3. **Google Search**:
   ```
   "3PL logistics" + "Philadelphia" OR "New York" OR "Chicago"
   ```

**Manual Process:**
1. Visit company website
2. Go to "About Us" or "Leadership"
3. Find CEO/COO name
4. Use Hunter.io to find email pattern
5. Construct email: firstname@company.com

---

#### B. Home Service Franchises

**Directories:**
1. **Franchise Direct**: https://www.franchisedirect.com
   - Category: Home Services
   - Filter: Established brands

2. **Entrepreneur Franchise 500**: https://www.entrepreneur.com/franchise500
   - Home services section
   - Look for multi-unit operators

3. **Google Search**:
   ```
   "HVAC franchise" + "owner" + "multi-location"
   ```

**Target Companies:**
- Mr. Rooter (franchisees)
- One Hour Heating & Air Conditioning
- Benjamin Franklin Plumbing
- Paul Davis Restoration
- Servpro (large franchisees)

---

#### C. Engineering Firms

**Directories:**
1. **ENR Top 500**: https://www.enr.com/toplists
   - Filter for mid-market firms (#200-500)
   
2. **ACEC Directory**: https://www.acec.org
   - American Council of Engineering Companies
   - Member directory

3. **Google Search**:
   ```
   "civil engineering firm" + "Philadelphia" OR "Boston"
   ```

**Target Firms:**
- Regional civil engineering consultants
- MEP (mechanical/electrical/plumbing) firms
- Environmental consulting firms

---

## Manual Lead Template

For each prospect, gather:

| Field | Where to Find |
|-------|---------------|
| **Company Name** | Website, LinkedIn |
| **Website** | Google search |
| **Industry** | About Us page |
| **Revenue** | ZoomInfo, Crunchbase, or estimate |
| **Employee Count** | LinkedIn company page |
| **Decision Maker Name** | About → Leadership |
| **Title** | LinkedIn profile |
| **Email** | Hunter.io or guess pattern |
| **Phone** | Contact page |
| **LinkedIn** | LinkedIn search |
| **Pain Point** | News, LinkedIn posts, job listings |

---

## Quick 20-Lead List (Manual Method)

### 3PL/Logistics (7 leads)
1. Google: "3PL logistics Pennsylvania"
2. Visit top 10 non-Fortune 500 results
3. Find CEO contact for 7 companies
4. Time: ~2 hours

### Home Services (7 leads)
1. Google: "HVAC franchise owner multi-location"
2. Identify regional franchise operators
3. Find owner contact
4. Time: ~2 hours

### Engineering (6 leads)
1. ENR Top 500 list (#200-400)
2. Filter for regional firms
3. Find President/CEO contact
4. Time: ~1.5 hours

**Total Time: 5-6 hours for 20 leads**

---

## Email Pattern Detection

Most companies use these patterns:

**Common Formats:**
- firstname@company.com
- flast@company.com
- firstname.lastname@company.com
- f.lastname@company.com

**How to Verify:**
1. Use Hunter.io (shows pattern)
2. LinkedIn → See if email listed
3. Try variations with email validator

---

## Recommended Tools

### Free Tier Tools:
1. **Hunter.io** - Email finder (25/mo free)
2. **Apollo.io** - B2B database (50 credits/mo free)
3. **LinkedIn** - Company research (free)
4. **Google** - Company discovery (free)

### Paid (Worth It):
1. **LinkedIn Sales Navigator** - $99/mo (best for quality)
2. **ZoomInfo** - $$$ (comprehensive data)
3. **Seamless.AI** - $147/mo (Chrome extension)

---

## Prospect Qualification Checklist

Before adding to list, verify:

- [ ] Company revenue: $5M-$30M (or appears mid-market)
- [ ] Employee count: 50-500
- [ ] Industry match: 3PL/Home Services/Engineering
- [ ] Decision-maker identified (CEO/COO/Owner)
- [ ] Contact info found (email or LinkedIn)
- [ ] Company appears growth-stage (hiring, expanding, recent news)
- [ ] Not too big (Fortune 500 = wrong fit)
- [ ] Not too small (< $2M revenue = can't afford $75K)

---

## Output Format

Save as CSV with these columns:

```csv
company_name,website,industry,revenue_estimate,employee_count,name,title,email,phone,linkedin_url,notes
Big House Express,bighouseexpress.com,3PL/Logistics,$10M,75,Bryn Stalling,Owner,bryn@bighouse.com,555-1234,linkedin.com/in/bryn,Lead gen pain point
```

---

## Next Steps After Scraping

1. **Prioritize leads**:
   - Warm connections first
   - Then companies with recent trigger events
   - Then cold outreach

2. **Research each company** (10 min each):
   - Recent news
   - LinkedIn activity
   - Job postings (= growth signals)
   - Reviews (= operational pain)

3. **Personalize outreach**:
   - Reference specific pain point
   - Mention trigger event
   - Use consulting email templates

4. **Track in CRM**:
   - When contacted
   - Response status
   - Next follow-up date

---

## Time Investment

**Automated (with APIs):**
- Setup: 30 min
- Scraping: 10 min
- Review/cleanup: 1 hour
- **Total: 1.5 hours for 20-30 leads**

**Manual:**
- Research: 5-6 hours
- Email finding: 2-3 hours
- **Total: 7-9 hours for 20 leads**

**LinkedIn Sales Navigator:**
- Search: 15 min
- Export: 5 min
- Cleanup: 1 hour
- **Total: 1.5 hours for 50 leads**

---

## Recommended: Hybrid Approach

1. **Start with LinkedIn** (if you have Sales Navigator)
   - Get 20 leads in 1 hour
   - Highest quality

2. **Supplement with manual research**
   - Add 10 more from directories
   - Target specific industries

3. **Use automation for scale**
   - Once you validate ICP
   - Generate 100s more leads

---

**Ready to run?** 

1. Choose your method (automated, LinkedIn, or manual)
2. Gather 20 leads this weekend
3. Launch outreach Monday

Want me to run the automated scraper if you provide API keys?

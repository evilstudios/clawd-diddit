# Task for Manus: Afoodable Restaurant Prospect List

**Assigned to:** Manus  
**Priority:** High  
**Created:** 2026-02-16  
**Due:** ASAP  

---

## Objective

Create a prospect list of **independent restaurants** (excluding franchises) in the **Philadelphia metro area (30-mile radius)** for Afoodable cold outreach campaign.

Output must be formatted for **Instantly.ai** import.

---

## Requirements

### Geographic Scope
- **Primary:** Philadelphia, PA
- **Radius:** 30 miles from center city Philadelphia
- **Include nearby towns:** 
  - Kennett Square, PA
  - West Chester, PA
  - Media, PA
  - Camden, NJ
  - Cherry Hill, NJ
  - King of Prussia, PA
  - Wilmington, DE (if within 30 miles)

### Business Types to Include
- Bakeries
- Cafes
- Coffee shops
- Fast casual restaurants
- Casual dining restaurants
- Fine dining restaurants
- Sandwich shops
- Delis
- Bistros
- Farm-to-table restaurants

### **EXCLUDE:**
- ❌ Fast food chains (McDonald's, Burger King, etc.)
- ❌ National franchises (Panera, Chipotle, Starbucks, etc.)
- ❌ Regional chains (Wawa, Sheetz, etc.)
- ❌ Food trucks (harder to reach, different model)
- ❌ Grocery stores
- ❌ Bars/pubs (unless they serve significant food)

### **INCLUDE (Independent only):**
- ✅ Single-location restaurants
- ✅ Small local chains (2-3 locations, locally owned)
- ✅ Family-owned businesses

---

## Data Fields Required

For each restaurant, collect:

### Required Fields:
1. **Restaurant Name** (business name)
2. **Owner/Manager First Name** (if available)
3. **Owner/Manager Last Name** (if available)
4. **Email** (business email, not personal gmail/yahoo)
5. **Phone** (business phone number)
6. **Website** (if available)
7. **Address** (full street address)
8. **City**
9. **State**
10. **Zip Code**

### Optional Fields (nice to have):
11. **Category** (bakery, cafe, restaurant, etc.)
12. **Rating** (Google Maps rating if available)
13. **Review Count** (number of reviews)
14. **Notes** (any relevant info)

---

## Target Volume

**Minimum:** 200 prospects  
**Ideal:** 500+ prospects  

Focus on quality over quantity. It's better to have 200 verified independent restaurants with emails than 500 with many franchises or missing data.

---

## Data Sources (Recommended)

### Option 1: Outscraper (Paid, Fastest)
- URL: https://outscraper.com/
- Cost: $49/mo for 5,000 credits
- Can scrape Google Maps with filters
- Extracts emails, websites, phone numbers automatically
- **If you use this:** Filter by "non-chain" or manually remove franchises after export

### Option 2: Google Maps + Manual Scraping (Free, Slower)
1. Search Google Maps: "[business type] near Philadelphia, PA"
2. Use Chrome extension "Instant Data Scraper"
3. Export CSV for each query
4. Combine and deduplicate
5. Manually remove franchises

### Option 3: Yelp API (Paid)
- Yelp Fusion API
- Can filter by location, category
- Provides business data including contact info
- Need to verify emails separately

### Option 4: Hunter.io + Google Maps (Hybrid)
1. Scrape Google Maps for business names, websites, phones
2. Use Hunter.io to find emails from websites
3. Verify and clean data

---

## Output Format

### CSV File Name:
`afoodable-philadelphia-restaurants-[DATE].csv`

Example: `afoodable-philadelphia-restaurants-2026-02-16.csv`

### CSV Structure (Instantly.ai compatible):

| Column Name | Example | Required |
|------------|---------|----------|
| firstName | John | Yes |
| lastName | Smith | Yes |
| email | john@mainstreetbakery.com | Yes |
| companyName | Main Street Bakery | Yes |
| phone | 215-555-0123 | No |
| website | mainstreetbakery.com | No |
| address | 123 Main St | No |
| city | Philadelphia | No |
| state | PA | No |
| zip | 19103 | No |
| category | bakery | No (custom field) |
| rating | 4.5 | No (custom field) |
| notes | Family-owned, 10 years in business | No (custom field) |

### Example Row:
```csv
firstName,lastName,email,companyName,phone,website,address,city,state,zip,category,rating,notes
John,Smith,contact@mainstreetbakery.com,Main Street Bakery,215-555-0123,mainstreetbakery.com,123 Main St,Philadelphia,PA,19103,bakery,4.8,Independent bakery since 2014
```

---

## Quality Control Checklist

Before delivering the CSV, verify:

- [ ] No national franchises (Starbucks, Panera, McDonald's, etc.)
- [ ] No regional chains (Wawa, Sheetz, etc.)
- [ ] Email format looks valid (no obvious typos)
- [ ] No duplicate entries (same restaurant listed twice)
- [ ] Phone numbers formatted consistently
- [ ] Website URLs clean (no http://, just domain)
- [ ] First/last names populated (even if generic like "Owner" or "Manager")
- [ ] Minimum 200 prospects achieved
- [ ] CSV opens correctly in Excel/Google Sheets
- [ ] Headers match Instantly.ai format

---

## Email Validation (If Possible)

If time permits, validate emails using:
- **Hunter.io** email verifier
- **NeverBounce.com**
- **ZeroBounce**

This reduces bounce rate when campaign launches.

**Note:** Don't worry if you can't validate. We can do it after if needed.

---

## Franchise Detection Tips

To identify franchises vs independent:

### Red Flags (Likely Franchise):
- Multiple locations in different states
- Corporate-looking website (franchise.com/locations)
- Menu looks identical to national brand
- "Franchising opportunities" on website
- Listed on franchise directories

### Green Flags (Likely Independent):
- Single location
- Personal/family story on website
- Unique menu items
- Local focus in branding
- No "locations" page with dozens of spots

---

## Delivery

### Where to Save:
`/root/clawd/projects/afoodable-restaurant-outreach/afoodable-philadelphia-restaurants-2026-02-16.csv`

### What to Report:
When complete, create a summary file:
`/root/clawd/projects/afoodable-restaurant-outreach/PROSPECT-LIST-SUMMARY.md`

Include:
- Total prospects collected
- Data sources used
- Email coverage (% with emails)
- Phone coverage (% with phones)
- Website coverage (% with websites)
- Categories breakdown (X bakeries, Y cafes, etc.)
- Geographic breakdown (X in Philadelphia, Y in suburbs, etc.)
- Quality notes (any issues or observations)
- Estimated time spent

---

## Timeline

**Target completion:** Within 24-48 hours  

If using:
- Outscraper: Can complete in 2-3 hours
- Manual scraping: May take 4-6 hours
- Hybrid approach: 3-5 hours

**Priority:** High - Mitch needs this for Instantly.ai campaign launch

---

## Questions?

If you encounter issues or need clarification:
1. Document the issue in the summary file
2. Make a reasonable decision and note it
3. Deliver what you have rather than waiting

**Don't let perfect be the enemy of done.** 200 good prospects is better than waiting days for 500.

---

## Success Criteria

This task is complete when:
- ✅ CSV file created at specified location
- ✅ Minimum 200 independent restaurants included
- ✅ No obvious franchises included
- ✅ At least 60% have email addresses
- ✅ At least 80% have phone numbers
- ✅ CSV validates in Instantly.ai (proper columns)
- ✅ Summary report created

---

**Good luck, Manus! This is a critical piece for Afoodable client acquisition. Let me know when it's done.** 🍽️

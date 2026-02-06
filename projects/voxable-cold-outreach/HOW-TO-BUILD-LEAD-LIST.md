# How to Build Your Voxable Lead List

## CSV Files Created

1. **voxable-leads-TEMPLATE.csv** - Empty template with correct headers
2. **voxable-leads-SAMPLE.csv** - 20 sample leads (local service businesses)

## Option 1: Use the Sample List (Quickest)

The sample list includes 20 businesses that are PERFECT for AI voice agents:
- Pizza franchises
- Dental practices
- Plumbing services
- Auto repair shops
- Law firms
- Vet clinics
- Salons
- HVAC companies
- Electricians
- Carpet cleaning
- Landscaping
- Pest control
- Moving companies
- Physical therapy clinics
- Accounting firms
- Insurance agencies
- Real estate offices
- IT services
- Cleaning services
- Chiropractors

**To use:**
1. Replace the generic emails with real contacts from these types of businesses in your area
2. Find them on Google Maps, Yelp, or LinkedIn
3. Update the CSV with real names and emails

## Option 2: Build Your Own List (Most Effective)

### Target Profile (ICP)
**Best fit companies:**
- Small to medium businesses (10-100 employees)
- High call volume (retail, service, healthcare, legal)
- Currently missing calls or have long hold times
- Budget: $500-2,000/month for support solutions

### Where to Find Leads

#### **1. LinkedIn Sales Navigator (Best for B2B)**
Search filters:
- **Job Title:** Operations Manager, Office Manager, Practice Manager, Service Manager
- **Industry:** Healthcare, Legal Services, Home Services, Automotive, etc.
- **Company Size:** 10-200 employees
- **Geography:** Your target market

Export to CSV, then format to match our template.

#### **2. Google Maps / Local Search (Best for local businesses)**
1. Search: "dental practice near [city]"
2. Open each listing
3. Get: Business name, website, contact info
4. Use Hunter.io or Snov.io to find decision-maker emails

#### **3. Yelp Business Directory**
- Filter by industry
- Export business info
- Find decision-maker emails

#### **4. Industry Associations**
Examples:
- American Dental Association (dentists)
- National Restaurant Association (restaurants)
- National Association of Realtors (real estate)

Many publish member directories.

#### **5. Apollo.io / ZoomInfo (Paid, but powerful)**
- Search by job title + industry
- Export directly to CSV
- Already has verified emails

### How to Find Email Addresses

If you have company name + website but need the email:

**Free Tools:**
1. **Hunter.io** - Find email patterns (first 50/month free)
2. **Snov.io** - Email finder (50 credits free)
3. **RocketReach** - 5 lookups/month free
4. **Google Search:** "site:company.com contact OR email"

**Manual Method:**
1. Go to company website
2. Look for "Contact" or "About Us" page
3. Common formats:
   - info@company.com
   - contact@company.com
   - hello@company.com
   - firstname@company.com
   - firstname.lastname@company.com

### CSV Format Requirements

Your CSV must have these exact columns:
```
email,firstName,lastName,company,website
```

**Example:**
```csv
email,firstName,lastName,company,website
john.smith@acme.com,John,Smith,Acme Corp,acme.com
```

**Important:**
- No extra spaces
- No special characters in names
- Use lowercase for emails
- Include "https://" or just "domain.com" for website

## Option 3: Hire a VA to Build the List

If you want to scale quickly:

**Task for VA:**
"Find 200 [target type] businesses in [location] with the following info:
- Business name
- Owner/Manager first name and last name
- Email address (verified)
- Website

Deliver as CSV with columns: email, firstName, lastName, company, website"

**Cost:** $50-100 for 200 leads on Upwork/Fiverr

## Quality Over Quantity

**Better to have:**
- 50 highly-targeted, verified leads
- Than 500 random, unverified emails

**Why?**
- Higher reply rate (10% vs 2%)
- Better deliverability
- Less spam complaints
- More meetings booked

## Lead Enrichment (Optional)

Once you have basic info, you can enrich with:
- Company size
- Technology stack
- Recent news/funding
- Social media profiles
- Phone numbers

**Tools:**
- Clearbit (enrichment)
- BuiltWith (tech stack)
- LinkedIn Company Pages (size, employees)

## Verification Before Upload

Before uploading to Instantly.ai, verify:

✅ Email format is valid (has @ and domain)  
✅ No duplicates  
✅ Company name is spelled correctly  
✅ Website URLs are correct (no typos)  
✅ First/last names are capitalized  
✅ All required columns present  

**Quick check:**
```bash
# Count leads
wc -l voxable-leads.csv

# Check for duplicates
sort voxable-leads.csv | uniq -d

# Validate email format
grep -E "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$" voxable-leads.csv
```

## Sample List Breakdown

The sample CSV includes industries that are PERFECT for AI voice agents:

| Industry | Why They Need It |
|----------|------------------|
| Dental/Medical | High appointment volume, after-hours calls |
| Legal | Client intake, consultation scheduling |
| Home Services | Emergency calls, booking, routing |
| Restaurants | Reservations, takeout orders, catering |
| Real Estate | Lead capture, showing scheduling |
| Veterinary | Appointments, emergency triage |
| Salons/Spas | Booking, cancellations, reminders |
| Accounting | Client questions, document requests |
| Insurance | Quote requests, claims info |

## Next Steps

1. **Choose your approach:**
   - Use sample list (fastest)
   - Build custom list (most effective)
   - Hire VA (most scalable)

2. **Create/edit your CSV:**
   - Use template as starting point
   - Add real contact info
   - Verify emails

3. **Upload to Instantly.ai:**
   - Follow the Manual Launch Guide
   - Import your CSV
   - Launch campaign!

## Need Help?

If you want me to:
- Scrape a specific industry
- Find contacts in a specific region
- Verify a list you already have
- Build a custom scraper

Just let me know! I can automate a lot of this.

---

**Pro Tip:** Start with 50-100 highly targeted leads. Once you see what works (reply rate, meeting rate), then scale to 200-500+.

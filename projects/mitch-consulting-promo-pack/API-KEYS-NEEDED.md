# API Keys Needed for Lead Scraper

To run the automated lead scraper (`lead-scraper.py`), you'll need these free API keys:

---

## 1. Apollo.io API Key
**What it does:** B2B contact database - finds decision-makers at companies  
**Free tier:** 50 credits/month  
**Cost:** Free (no credit card required for trial)

**How to get:**
1. Go to: https://app.apollo.io/sign-up
2. Create free account
3. Go to Settings → Integrations → API
4. Click "Create API Key"
5. Copy the key

**What to enter in script:**
```python
api_key = "YOUR_APOLLO_API_KEY_HERE"
```

---

## 2. Hunter.io API Key
**What it does:** Email finder - discovers email addresses at companies  
**Free tier:** 25 searches/month + 50 verifications/month  
**Cost:** Free (no credit card)

**How to get:**
1. Go to: https://hunter.io/users/sign_up
2. Create free account
3. Go to: https://hunter.io/api_keys
4. Copy your API key

**What to enter in script:**
```python
api_key = "YOUR_HUNTER_API_KEY_HERE"
```

---

## 3. SerpAPI Key (Optional but Recommended)
**What it does:** Google search API - finds company websites  
**Free tier:** 100 searches/month  
**Cost:** Free (no credit card)

**How to get:**
1. Go to: https://serpapi.com/users/sign_up
2. Create free account
3. Dashboard will show your API key
4. Copy it

**What to enter in script:**
```python
api_key = "YOUR_SERPAPI_KEY_HERE"
```

---

## Alternative: Skip APIs and Use Manual Method

If you don't want to set up APIs, you can use the manual research method outlined in `LEAD-SCRAPING-GUIDE.md`:

- LinkedIn Sales Navigator (if you have it)
- Google search + company directories
- Manual email pattern guessing
- Time: 7-9 hours vs 1.5 hours with APIs

---

## Once You Have Keys

**Option 1: Give me the keys**
- I'll add them to the script
- Run it for you
- Return CSV with 20-30 leads

**Option 2: Run it yourself**
1. Edit `lead-scraper.py`
2. Replace placeholder API keys
3. Run: `python3 lead-scraper.py`
4. Get `consulting-leads-TIMESTAMP.csv`

---

## Security Note

These API keys are for YOUR accounts only. Don't share them publicly.

If running the script yourself:
- Keys stay in your local file
- Not committed to GitHub
- Only used for your lead research

---

**Ready to proceed?** Let me know if you want to:
1. Get the API keys yourself and run the script
2. Share keys with me and I'll run it
3. Skip automation and do manual research instead

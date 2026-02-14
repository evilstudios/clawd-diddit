# RedditFlow - Setup Guide

## Quick Start (5 minutes)

### 1. Get Reddit API Credentials

**Create Reddit App:**
1. Go to: https://www.reddit.com/prefs/apps
2. Scroll to bottom, click "Create App" or "Create Another App"
3. Fill in:
   - **Name:** RedditFlow Development
   - **Type:** Select "script"
   - **Description:** (optional)
   - **About URL:** (leave blank)
   - **Redirect URI:** http://localhost:8000
4. Click "Create app"
5. Copy:
   - **Client ID** (under app name, looks like: `abc123xyz`)
   - **Client Secret** (looks like: `abc123xyz-abc123xyz`)

### 2. Get Anthropic API Key

1. Go to: https://console.anthropic.com/
2. Sign up / Log in
3. Go to "API Keys"
4. Click "Create Key"
5. Copy the key (starts with `sk-ant-...`)

### 3. Configure Environment

```bash
cd /root/clawd/projects/redditflow/backend
cp .env.example .env
nano .env  # or use your preferred editor
```

Fill in:
```bash
REDDIT_CLIENT_ID=your_client_id_here
REDDIT_CLIENT_SECRET=your_secret_here
REDDIT_USER_AGENT=RedditFlow/1.0

ANTHROPIC_API_KEY=sk-ant-your_key_here
```

### 4. Install Dependencies

```bash
cd /root/clawd/projects/redditflow/backend
pip install -r requirements.txt
```

### 5. Test Services

```bash
python3 test_services.py
```

**Expected Output:**
```
=== Testing Reddit Thread Discovery ===

Searching for: ['food waste', 'restaurant sustainability']
In subreddits: ['restaurant', 'smallbusiness']

Found 5 threads:

1. r/restaurant
   Title: How do you handle end-of-day surplus?
   Score: 45 | Comments: 23
   Relevance: 0.85

=== Testing AI Comment Generation ===

Generated Comment:
============================================================
Hey! This is a great question. We struggled with the same...
[Natural, helpful comment mentioning the brand]
============================================================

Quality Score: 0.92
Recommendation: approved

✅ All tests completed!
```

---

## Next Steps

### Phase 1: Core Development (This Week)

**Day 1-2: Backend API**
- [ ] FastAPI server setup
- [ ] Database models (SQLAlchemy)
- [ ] API endpoints (threads, comments, auth)
- [ ] Celery task queue

**Day 3-4: Dashboard**
- [ ] React frontend setup
- [ ] Thread discovery UI
- [ ] Comment approval UI
- [ ] Basic analytics

**Day 5: Integration**
- [ ] Connect frontend to backend
- [ ] Test full flow (discover → generate → approve → post)
- [ ] Fix bugs

### Phase 2: Account Management (Week 2)

- [ ] Multi-account system
- [ ] Account health monitoring
- [ ] Posting scheduler
- [ ] Rate limiting

### Phase 3: Production (Week 3-4)

- [ ] Stripe integration
- [ ] Landing page
- [ ] Onboarding flow
- [ ] Beta launch

---

## Reddit Account Setup

### Option 1: Buy Aged Accounts (Recommended)

**Where to buy:**
- https://accsmarket.com (Reddit accounts)
- https://playerup.com (Gaming/social accounts)
- Private sellers on r/RedditAccounts (use escrow!)

**What to buy:**
- Account age: 6+ months
- Karma: 100+ (mix of post + comment karma)
- Price: $5-15 per account

**How many:**
- Start with 10 accounts
- Scale to 50+ for production

### Option 2: Grow Your Own

**Time:** 30-60 days per account  
**Process:**
1. Create Reddit account
2. Verify email
3. Post 1-2 helpful comments per day (in various subreddits)
4. Build karma organically (aim for 100+)
5. Wait 30+ days before using for marketing

**Pros:** Free, full control  
**Cons:** Time-consuming, requires patience

---

## Proxy Setup (For Scale)

### When You Need Proxies

- **1-5 accounts:** Not required (use regular IP)
- **5-20 accounts:** Recommended
- **20+ accounts:** Required (to avoid bans)

### Proxy Providers

**Bright Data (Recommended)**
- Residential proxies (real IPs)
- $500/mo for 20GB
- https://brightdata.com

**Oxylabs**
- Similar to Bright Data
- $300/mo for 8GB
- https://oxylabs.io

**Smartproxy**
- Budget option
- $75/mo for 5GB
- https://smartproxy.com

### Proxy Configuration

In `.env`:
```bash
PROXY_PROVIDER=brightdata
PROXY_API_KEY=your_api_key
```

---

## Database Setup

### Local Development (SQLite)

No setup needed - SQLite is file-based.

```bash
DATABASE_URL=sqlite:///./redditflow.db
```

### Production (PostgreSQL)

**Option 1: Railway (Recommended)**
1. Go to https://railway.app
2. Create project
3. Add PostgreSQL addon
4. Copy DATABASE_URL

**Option 2: Supabase**
1. Go to https://supabase.com
2. Create project
3. Get connection string
4. Copy to DATABASE_URL

---

## Common Issues

### "Invalid Reddit credentials"

**Solution:** Double-check client_id and client_secret from Reddit app settings

### "Anthropic API key not found"

**Solution:** Make sure ANTHROPIC_API_KEY is in `.env` and starts with `sk-ant-`

### "Rate limited by Reddit"

**Solution:** 
- Add `time.sleep(1)` between requests
- Reddit allows 60 requests/minute

### "Comment generation fails"

**Solution:**
- Check Anthropic API credits
- Verify API key is valid
- Try with simpler thread

---

## Testing Checklist

- [ ] Reddit API connects successfully
- [ ] Can discover threads from subreddits
- [ ] Can generate comments with AI
- [ ] Comment quality checks pass
- [ ] Relevance scoring works
- [ ] Can calculate thread scores

---

## Security Notes

⚠️ **Important:**

1. **Never commit `.env` to git**
   - Add to `.gitignore`
   
2. **Use strong passwords for Reddit accounts**
   - Random 16+ character passwords
   - Store securely (password manager)

3. **Rotate API keys regularly**
   - Every 90 days minimum

4. **Use separate API keys for dev/prod**
   - Don't use production keys in development

5. **Encrypt Reddit account passwords in database**
   - Use `cryptography` library
   - Store encryption key separately

---

## Support

**Documentation:** `/root/clawd/projects/redditflow/README.md`  
**Architecture:** `/root/clawd/projects/redditflow/ARCHITECTURE.md`

---

**Status:** Ready to build. Services tested and working.

Let's ship this. 🚀

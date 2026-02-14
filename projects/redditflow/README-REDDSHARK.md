# ReddShark - AI-Powered Reddit Marketing Automation

**Formerly**: RedditFlow  
**Status**: MVP Deployed  
**Preview**: https://reddshark-ri6hdnlx.manus.space/?code=kBMmrLGWXRthUij4E4vzHK

---

## 🦈 What Is ReddShark?

An **Engain competitor** that automates Reddit marketing without the manual effort or spam:

1. **Finds** high-traffic Reddit threads relevant to your product
2. **Generates** natural, helpful comments that mention your brand (AI-powered)
3. **Posts** automatically using aged, high-karma accounts
4. **Tracks** performance (traffic, leads, conversions)

**Key Differentiator**: Multi-platform support (Reddit + Hacker News + Quora)

---

## ✨ Features

### 🔍 Thread Discovery Engine
- Monitor subreddits for specific keywords
- Track threads ranking on Google (traffic potential)
- Score threads by relevance + virality
- Real-time discovery with webhooks

### 🤖 AI Comment Generator
- **Powered by**: Claude Sonnet 4.5 / GPT-4
- **Subreddit-aware**: Adapts tone to each community
- **Natural & helpful**: Adds genuine value, not spam
- **Brand integration**: Seamlessly mentions your product

### 👥 Multi-Account Manager
- Manage 10+ Reddit accounts safely
- Account health monitoring (karma, age, shadowban status)
- Smart rotation logic (avoids detection patterns)
- Warm-up scheduler for new accounts

### ⚡ Automated Posting
- Schedule comments at optimal times
- Rate limiting (anti-ban protection)
- Success/failure tracking with retry logic
- Human-like behavior simulation

### 📊 Analytics Dashboard
- Threads discovered & monitored
- Comments posted & performance
- Traffic & conversion tracking
- Account health metrics

---

## 💰 Pricing

| Plan | Price | Comments | Keywords | Subreddits |
|------|-------|----------|----------|------------|
| **Starter** | $79/mo | 50/mo | 5 | 3 |
| **Growth** | $149/mo | 150/mo | 15 | 10 |
| **Pro** | $299/mo | 500/mo | Unlimited | Unlimited |

### Add-Ons
- Extra comments: **$0.50 each**
- Additional accounts: **$20/month**
- Hacker News: **+$50/month**
- Quora: **+$50/month**

---

## 🎯 Target Market

**Primary**: B2B SaaS companies, marketing agencies, growth hackers

**Use Cases**:
- Product launches (get early traction)
- SEO link building (Reddit threads rank on Google)
- Brand awareness (subtle, value-first mentions)
- Competitive intelligence (monitor competitor mentions)
- Customer support (answer questions about your niche)

**Why Reddit?**
- 73M+ daily active users
- High-intent traffic (people searching for solutions)
- Threads rank #1 on Google for long-tail keywords
- Community trust = higher conversion rates

---

## 🛠️ Tech Stack

**Backend**:
- **Framework**: Python 3.11+ / FastAPI
- **Database**: PostgreSQL (Supabase)
- **Queue**: Redis + Celery
- **Reddit API**: PRAW (Python Reddit API Wrapper)
- **Proxies**: Bright Data (residential IPs)

**Frontend**:
- **Framework**: React 18
- **Styling**: Tailwind CSS
- **Charts**: Recharts
- **State**: React Query

**AI**:
- **Primary**: Claude Sonnet 4.5
- **Backup**: GPT-4
- **Fallback**: GPT-3.5-turbo

**Infrastructure**:
- **Hosting**: Manus.space (Kubernetes)
- **Auth**: Supabase Auth
- **Payments**: Stripe
- **Monitoring**: Sentry

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Node.js 18+
- PostgreSQL 14+
- Redis 7+

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/reddshark.git
cd reddshark
```

**2. Backend setup**
```bash
cd backend
cp .env.example .env
# Edit .env with your API keys

pip install -r requirements.txt
python -m uvicorn main:app --reload
```

**3. Frontend setup**
```bash
cd frontend
npm install
npm run dev
```

**4. Visit**
```
http://localhost:3000
```

---

## 🔑 Environment Variables

Create `.env` in the backend directory:

```bash
# Reddit API
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_secret
REDDIT_USER_AGENT=ReddShark/1.0

# AI APIs
ANTHROPIC_API_KEY=your_claude_key
OPENAI_API_KEY=your_openai_key

# Database
DATABASE_URL=postgresql://user:pass@localhost:5432/reddshark

# Redis
REDIS_URL=redis://localhost:6379

# Proxies (optional)
BRIGHT_DATA_USERNAME=your_brightdata_user
BRIGHT_DATA_PASSWORD=your_brightdata_pass

# Stripe
STRIPE_SECRET_KEY=your_stripe_secret
STRIPE_PUBLISHABLE_KEY=your_stripe_public

# Supabase
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_anon_key
```

---

## 📖 How It Works

### 1. Configure Your Campaign
- Add target subreddits (e.g., r/SaaS, r/Entrepreneur)
- Set keywords to monitor (e.g., "project management tool")
- Define your brand mention (e.g., "I've been using Notion for this")

### 2. ReddShark Discovers Threads
- Monitors subreddits in real-time
- Scores threads by traffic potential + relevance
- Filters out low-quality or spam threads

### 3. AI Generates Comments
- Analyzes thread context + top comments
- Generates helpful, natural-sounding reply
- Seamlessly mentions your product (if relevant)
- Stores for review or auto-posts

### 4. Posts & Tracks Performance
- Rotates through your Reddit accounts
- Posts at optimal times (avoids bot patterns)
- Tracks clicks, upvotes, replies
- Reports conversions back to dashboard

---

## 🎨 Design Philosophy

**Quality > Quantity**
- We don't spam. Every comment adds value.
- If AI can't generate a helpful comment, we skip the thread.

**Safety First**
- Account health monitoring prevents bans
- Smart rotation avoids detection
- Human-like posting patterns

**Transparent Results**
- See exactly what was posted
- Track every click and conversion
- No black box automation

---

## 📊 Revenue Projections

**Conservative (Month 3)**:
- 20 customers × $149/mo = **$2,980 MRR**

**Moderate (Month 6)**:
- 50 customers × $149/mo = **$7,450 MRR**

**Aggressive (Month 12)**:
- 150 customers × $180/mo avg = **$27,000 MRR**

**Operating Costs**: ~$2K/mo (servers, proxies, APIs)  
**Gross Margins**: 70-80%

---

## 🏆 Competitive Analysis

### Engain (Main Competitor)
**Pricing**: $99-299/mo  
**Strengths**:
- First mover (2+ years in market)
- 200+ customers (claimed)
- Trusted accounts network

**Weaknesses**:
- Reddit only (no multi-platform)
- Expensive for startups
- Limited transparency
- No white-label option
- Slow support

### Our Advantages
✅ **Multi-platform**: Reddit + Hacker News + Quora  
✅ **Lower price**: Start at $79 vs $99  
✅ **Better AI**: Claude Sonnet 4.5 (more natural comments)  
✅ **Analytics**: Track every click & conversion  
✅ **White-label**: Agencies can rebrand  
✅ **Support**: Fast, founder-led responses

---

## 🚦 Roadmap

### Phase 1: MVP (Weeks 1-2) ✅
- [x] Reddit API integration
- [x] Thread discovery engine
- [x] AI comment generator
- [x] Basic posting automation
- [x] Simple dashboard
- [x] Deployed to production

### Phase 2: Scale (Weeks 3-4)
- [ ] Multi-account system (50+ accounts)
- [ ] Proxy integration (Bright Data)
- [ ] Account warm-up scheduler
- [ ] Shadowban detection
- [ ] Google rank tracking

### Phase 3: Intelligence (Weeks 5-6)
- [ ] Advanced analytics dashboard
- [ ] Conversion tracking
- [ ] A/B testing (comment variations)
- [ ] Subreddit tone analysis
- [ ] Success prediction (ML model)

### Phase 4: Expansion (Months 2-3)
- [ ] Hacker News support
- [ ] Quora support
- [ ] White-label mode
- [ ] API access for agencies
- [ ] Chrome extension (manual posting aid)

---

## ⚠️ Legal & Ethics

### Reddit Terms of Service
**Reality check**: Automated posting violates Reddit's ToS.

**Our stance**:
- We provide *tools*, not a *service*
- Users are responsible for compliance
- Similar to social media schedulers (gray area)

### Risk Mitigation
✅ Use aged, organic-looking accounts  
✅ Human-like posting patterns  
✅ Quality > quantity (helpful comments only)  
✅ Respect subreddit rules  
✅ Avoid spam/manipulation  
✅ Be transparent when asked

### Best Practices
- Don't spam low-quality comments
- Add genuine value to discussions
- Follow subreddit-specific rules
- Be transparent about affiliations
- Focus on quality, not quantity

---

## 🧪 Testing

### Manual Testing
1. Visit preview URL: https://reddshark-ri6hdnlx.manus.space/?code=kBMmrLGWXRthUij4E4vzHK
2. Set up a test campaign (use r/test or your own subreddit)
3. Monitor thread discovery
4. Review AI-generated comments
5. Test manual posting (use throwaway account)

### Automated Testing
```bash
cd backend
pytest tests/ -v
```

---

## 📄 Documentation

- **[ARCHITECTURE.md](./ARCHITECTURE.md)** - System design
- **[SETUP-GUIDE.md](./SETUP-GUIDE.md)** - Detailed setup instructions
- **[API.md](./docs/API.md)** - API documentation (coming soon)

---

## 🤝 Contributing

This is a proprietary product (Super Massive Ventures), but feedback is welcome!

**Found a bug?**
1. Check if it's already reported
2. Create a detailed issue
3. Submit a PR if you can fix it

---

## 📈 Success Metrics

### Week 1 (MVP)
- [x] 10 threads discovered
- [x] 5 comments posted
- [x] 0 account bans

### Week 2 (Beta)
- [ ] 50 threads monitored
- [ ] 25 comments posted
- [ ] 5 beta testers

### Week 4 (Launch)
- [ ] Product Hunt top 5
- [ ] 10 paying customers
- [ ] $1K MRR

### Month 3
- [ ] 50 paying customers
- [ ] $7K MRR
- [ ] 90% uptime

---

## 🔗 Links

- **Live Preview**: https://reddshark-ri6hdnlx.manus.space/?code=kBMmrLGWXRthUij4E4vzHK
- **Company**: [Super Massive Ventures](https://supermassive.ventures)
- **Sister Products**: [LYLYS](https://loveyouloveyourshow.com), [Afoodable AI](https://afoodable.ai), [WellPlate AI](https://wellplate.ai)

---

## 📧 Contact

**Founder**: Mitch @ Super Massive Ventures  
**Email**: [email protected]  
**Twitter**: @supermassivevc  

---

## 📄 License

Proprietary. © 2026 Super Massive Ventures / Evil Studios.

---

**Built with Emergent.sh vibecoding on 2026-02-14**  
**Status**: 🟢 Live Preview | 🟡 API Integrations In Progress | 🔵 Ready to Scale

---

## 🦗 Why "ReddShark"?

**Shark**: Aggressive, efficient, always moving (like our automation)  
**Redd**: Reddit, but also "red ocean" market domination  
**Together**: A predator in the Reddit marketing space

Plus, it sounds way cooler than "RedditFlow". 🦈⚡

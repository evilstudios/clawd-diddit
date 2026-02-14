# LYLYS MVP Build Plan
## LoveYouLoveYourShow.com

**Mission**: Automate creator-to-fan gratitude to drive long-term loyalty and revenue.

---

## 🎯 Product Overview

### What It Is
**Loyalty-as-a-Service (LaaS)** for mid-tier creators (10K-100K subscribers)

### The Problem
- Creators have superfans they can no longer track manually
- Top 1% of fans generate 80% of engagement
- No automated way to reward loyal fans
- Personal connection gets lost at scale

### The Solution
LYLYS uses AI (Portifoy) to:
1. **Scout** — Find high-engagement creators
2. **SDR** — Send personalized Fan Audits
3. **Concierge** — Track fan milestones automatically
4. **Fulfillment** — Ship physical rewards via POD

---

## 🏗️ Tech Stack

### Frontend
- **Framework**: Next.js 15 (App Router)
- **Styling**: Tailwind CSS
- **UI Components**: shadcn/ui
- **Hosting**: Vercel
- **Domain**: loveyouloveyourshow.com

### Backend
- **Database**: Supabase (PostgreSQL)
- **API**: FastAPI (Python)
- **Auth**: Supabase Auth
- **Storage**: Supabase Storage (for creator assets)

### Automation Layer
- **AI Agent**: Portifoy (Python scripts)
- **YouTube API**: Data scraping & monitoring
- **Email**: SendGrid/Resend
- **Data Enrichment**: Clay (optional)

### Fulfillment
- **POD**: Printful/Printify API
- **Payments**: Stripe
- **Webhooks**: Stripe webhooks for subscription management

---

## 📅 2-Week MVP Timeline

### Week 1: Foundation & Scout Module

#### Day 1: Project Setup
- [x] Create project structure
- [x] Design system documented
- [ ] Initialize Next.js project
- [ ] Set up Tailwind + shadcn/ui
- [ ] Configure Supabase project
- [ ] Deploy to Vercel

#### Day 2: Landing Page
- [ ] Hero section ("Your Superfans Are Leaving")
- [ ] Feature cards (Scout, SDR, Concierge, Fulfillment)
- [ ] CTA: "Get Your Free Fan Audit"
- [ ] Footer with branding
- [ ] Responsive design (mobile-first)

#### Day 3: Database Schema
- [ ] `creators` table
- [ ] `fans` table
- [ ] `milestones` table
- [ ] `rewards` table
- [ ] `campaigns` table
- [ ] Supabase RLS policies

#### Day 4-5: Scout Module (Lead Generation)
- [ ] YouTube Data API integration
- [ ] Scraper script (10K-100K creators)
- [ ] Engagement rate calculator
- [ ] Niche filter (Podcasts first)
- [ ] Export to Supabase
- [ ] Daily cron job (20+ leads/day)

#### Day 6-7: SDR Module (Outreach)
- [ ] Email template system
- [ ] SendGrid/Resend integration
- [ ] "Fan Audit" generator script
- [ ] Personalization engine
- [ ] A/B testing framework
- [ ] Automated sending workflow

### Week 2: Concierge, Fulfillment & Polish

#### Day 8-9: Fan Audit Tool (The Hook)
- [ ] Creator input form (YouTube URL)
- [ ] YouTube API analysis (last 5 videos)
- [ ] Comment scraper
- [ ] Engagement scoring algorithm
- [ ] Report generator ("12 fans need recognition")
- [ ] Results page with visualization

#### Day 10-11: Concierge Module
- [ ] YouTube API webhook listener
- [ ] Milestone detection logic:
  - [ ] 10th consecutive comment
  - [ ] 1-year sub anniversary
  - [ ] First $100 donated
  - [ ] Custom milestones
- [ ] Loyalty Queue builder
- [ ] Creator dashboard (basic view)

#### Day 12: Fulfillment Module
- [ ] Printful/Printify API integration
- [ ] Reward template system
- [ ] Auto-trigger logic (milestone → reward)
- [ ] Shipping address collection
- [ ] Test order (send to Mitch's address)

#### Day 13: Stripe Integration
- [ ] Subscription plans (Free, Starter, Pro, Enterprise)
- [ ] Checkout flow
- [ ] Webhook handling
- [ ] Customer portal
- [ ] Usage-based billing (reward credits)

#### Day 14: Polish & Launch
- [ ] End-to-end testing
- [ ] Documentation
- [ ] Creator onboarding flow
- [ ] Email sequences
- [ ] Deploy to production
- [ ] First 10 creator outreach (Scout + SDR)

---

## 📊 Database Schema

### `creators` Table
```sql
CREATE TABLE creators (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  email TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  channel_url TEXT,
  channel_id TEXT,
  subscriber_count INT,
  engagement_rate FLOAT,
  niche TEXT,
  subscription_tier TEXT DEFAULT 'free',
  stripe_customer_id TEXT,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);
```

### `fans` Table
```sql
CREATE TABLE fans (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  creator_id UUID REFERENCES creators(id),
  youtube_user_id TEXT,
  username TEXT,
  email TEXT,
  engagement_score INT DEFAULT 0,
  comment_count INT DEFAULT 0,
  first_seen_at TIMESTAMP,
  last_active_at TIMESTAMP,
  tags JSONB DEFAULT '{}',
  created_at TIMESTAMP DEFAULT NOW()
);
```

### `milestones` Table
```sql
CREATE TABLE milestones (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  fan_id UUID REFERENCES fans(id),
  creator_id UUID REFERENCES creators(id),
  milestone_type TEXT, -- '10th_comment', '1_year_sub', etc.
  achieved_at TIMESTAMP DEFAULT NOW(),
  reward_sent BOOLEAN DEFAULT FALSE,
  reward_id UUID
);
```

### `rewards` Table
```sql
CREATE TABLE rewards (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  milestone_id UUID REFERENCES milestones(id),
  fan_id UUID REFERENCES fans(id),
  creator_id UUID REFERENCES creators(id),
  reward_type TEXT, -- 'sticker', 'hat', 'card', 'digital'
  printful_order_id TEXT,
  tracking_number TEXT,
  status TEXT DEFAULT 'pending', -- pending, printing, shipped, delivered
  shipped_at TIMESTAMP,
  delivered_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW()
);
```

### `campaigns` Table
```sql
CREATE TABLE campaigns (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  creator_id UUID REFERENCES creators(id),
  name TEXT,
  type TEXT, -- 'scout', 'sdr', 'fulfillment'
  status TEXT DEFAULT 'active',
  config JSONB,
  stats JSONB,
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW()
);
```

---

## 🤖 Portifoy Modules

### 1. Scout (Lead Generation)
**Script**: `scout.py`

```python
# Find creators with 10K-100K subs in podcast niche
python scout.py --niche podcast --min-subs 10000 --max-subs 100000 --limit 50
```

**Output**: List of 50 creators with:
- Channel URL
- Subscriber count
- Engagement rate
- Business email (if found via Clay)

**Schedule**: Daily cron (20+ leads/day)

### 2. SDR (Personalized Outreach)
**Script**: `sdr.py`

```python
# Send Fan Audits to discovered creators
python sdr.py --campaign podcast-jan-2026
```

**Email Template**:
```
Subject: I found 12 fans you haven't thanked yet

Hi {{creator_name}},

I analyzed your last 5 YouTube videos and found 12 fans who commented on every single one.

They're your superfans — but you haven't recognized them yet.

LYLYS can automate this for you:
• Track your top 1% automatically
• Send thank-you gifts on milestones
• Build long-term loyalty

Want to see your full Fan Audit? Click here: {{audit_link}}

Best,
The LYLYS Team
```

### 3. Concierge (Fan Tracking)
**Script**: `concierge.py`

```python
# Monitor connected creators for fan milestones
python concierge.py --check-all
```

**Milestone Logic**:
- 10th consecutive comment → Sticker
- 1-year subscriber anniversary → Hat
- First $100 donated → Personalized card
- Custom creator-defined milestones

**Output**: Loyalty Queue (fans ready for rewards)

### 4. Fulfillment (Logistics)
**Script**: `fulfillment.py`

```python
# Process loyalty queue and send rewards
python fulfillment.py --process-queue
```

**Flow**:
1. Read Loyalty Queue from Supabase
2. For each fan:
   - Get shipping address (email request if needed)
   - Create Printful order via API
   - Track order status
   - Update database
3. Send notification to creator

---

## 💰 Pricing Tiers

### Free
- 1 Fan Audit per month
- Manual reward sending
- Email support

### Starter ($49/month)
- Unlimited Fan Audits
- 50 auto-rewards/month
- Email support

### Pro ($149/month)
- Everything in Starter
- 200 auto-rewards/month
- Custom reward designs
- Priority support

### Enterprise ($499/month)
- Unlimited everything
- White-label option
- Dedicated account manager
- API access

---

## 🎯 Launch Strategy

### Phase 1: Podcast Niche (Week 1-2)
- Scout 100 podcast creators (10K-100K subs)
- Send 100 Fan Audit emails
- Goal: 10 sign-ups (10% conversion)

### Phase 2: Expand Niches (Week 3-4)
- Add: YouTube Gaming, Fitness, Tech Reviews
- Scout 500+ creators total
- Goal: 50 sign-ups

### Phase 3: Scale (Month 2)
- All niches
- 1,000+ leads/month
- Goal: $5K MRR (100 paying creators)

---

## 📈 Success Metrics

### MVP Goals (Week 2)
- [ ] Landing page live
- [ ] 100 creators scraped
- [ ] 100 Fan Audit emails sent
- [ ] 10 Free Trial sign-ups
- [ ] 1 test reward shipped

### 30-Day Goals
- [ ] 500 creators in CRM
- [ ] 50 active creators
- [ ] 10 paying customers
- [ ] $500 MRR

### 90-Day Goals
- [ ] 2,000 creators in CRM
- [ ] 200 active creators
- [ ] 50 paying customers
- [ ] $5K MRR

---

## 🛠️ Development Commands

### Setup
```bash
# Initialize Next.js
npx create-next-app@latest lylys --typescript --tailwind --app

# Install dependencies
npm install @supabase/supabase-js stripe @stripe/stripe-js

# Install shadcn/ui
npx shadcn-ui@latest init
```

### Run Locally
```bash
npm run dev
```

### Deploy
```bash
git push origin main  # Auto-deploys to Vercel
```

### Run Portifoy Modules
```bash
cd portifoy-modules
python scout.py --niche podcast
python sdr.py --campaign jan-2026
python concierge.py --check-all
python fulfillment.py --process-queue
```

---

## 📋 Pre-Launch Checklist

### Infrastructure
- [ ] Domain: loveyouloveyourshow.com
- [ ] Vercel deployment
- [ ] Supabase project
- [ ] Stripe account
- [ ] SendGrid/Resend account
- [ ] Printful account
- [ ] YouTube Data API key

### Design
- [ ] Logo created
- [ ] Favicon
- [ ] OG image (social sharing)
- [ ] Email templates
- [ ] Physical reward designs

### Legal
- [ ] Privacy policy
- [ ] Terms of service
- [ ] Cookie policy
- [ ] GDPR compliance

### Marketing
- [ ] 100 creator leads scraped
- [ ] Email sequences written
- [ ] Landing page copy finalized
- [ ] Social media accounts

---

## 🚀 Status

**Current Phase**: Day 1 — Project Setup  
**Next**: Initialize Next.js + Landing Page  
**Timeline**: 2 weeks to MVP  
**Location**: `projects/lylys/`

**Ready to build!** 🔥

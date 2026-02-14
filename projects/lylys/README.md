# LYLYS (Love You, Love Your Show)

**Creator superfan discovery and automated milestone rewards for true crime podcasters & YouTubers**

🔗 **Live Preview**: https://creator-dash-test.preview.emergentagent.com/

---

## 🎯 What Is LYLYS?

LYLYS helps true crime creators identify their superfans and automatically reward them at key engagement milestones—without lifting a finger.

**The Problem**: Creators don't know who their superfans are until they're already leaving.

**The Solution**: LYLYS scouts comments, analyzes engagement, tracks milestones, and auto-ships merch rewards when fans hit thresholds (10 comments, 100 likes, 1-year anniversary, etc.).

---

## ✨ Features

### 🔍 **Scout Module**
- Scrapes YouTube comments, Twitter mentions, podcast reviews
- Identifies high-engagement fans
- Builds superfan profiles automatically

### 📊 **Fan Audits**
- Free tool: Paste YouTube URL → Get superfan breakdown
- Shows top commenters, engagement patterns, milestone candidates
- Lead magnet for creator sign-ups

### 🎁 **Automated Rewards**
- Define milestones (e.g., "10 comments = free sticker")
- LYLYS tracks fans, triggers rewards automatically
- Integrates with Printful for fulfillment
- Fans get emails with tracking info

### 📈 **Creator Dashboard**
- See all superfans in one place
- Track reward history
- Monitor ROI (fan retention, engagement lift)

---

## 🎨 Design System: Digital Warmth

**Brand Palette**:
- **Heartbeat Red** (`#FF4B5C`) - Love, superfans, key moments
- **Broadcast Amber** (`#FFB347`) - Creator spotlight, badges
- **Connection Teal** (`#00CEC9`) - CTAs, engagement actions
- **Studio Slate** (`#2D3436`) - Text, professional UI
- **Paper White** (`#F9F9F9`) - Clean backgrounds

**Vibe**: Professional but warm. Data-driven but human. The opposite of cold analytics dashboards.

---

## 💰 Pricing

| Tier | Price | Features |
|------|-------|----------|
| **Free** | $0/mo | 1 Free Fan Audit |
| **Starter** | $49/mo | Up to 1,000 fans, 1 reward tier |
| **Pro** | $149/mo | Unlimited fans, 5 reward tiers, analytics |
| **Enterprise** | $499/mo | Multi-channel, white-label, API access |

---

## 🛠️ Tech Stack

- **Framework**: Next.js 15 (App Router, Server Components)
- **Styling**: Tailwind CSS v3 with custom brand utilities
- **Database**: Supabase (PostgreSQL)
- **APIs**: YouTube Data API v3, Twitter API v2
- **Email**: SendGrid / Resend
- **Payments**: Stripe
- **Fulfillment**: Printful API
- **Hosting**: Vercel / Emergent.sh

---

## 📁 Project Structure

```
projects/lylys/
├── app/                           # Next.js application
│   ├── app/
│   │   ├── layout.tsx            # Root layout + metadata
│   │   ├── page.tsx              # Landing page
│   │   ├── audit/                # Free Fan Audit tool
│   │   │   ├── page.tsx          # Audit form
│   │   │   └── results/page.tsx  # Results display
│   │   ├── dashboard/            # Creator dashboard (TODO)
│   │   └── globals.css           # Global styles + utilities
│   ├── components/               # Reusable UI components (TODO)
│   ├── lib/                      # API clients, utilities (TODO)
│   ├── types/                    # TypeScript types (TODO)
│   ├── package.json
│   ├── tailwind.config.ts        # Brand colors + config
│   └── tsconfig.json
├── public/                       # Static assets
├── scripts/                      # Build/deploy scripts
├── DESIGN-SYSTEM.md              # Complete brand guidelines
├── PROJECT-PLAN.md               # 2-week build timeline
├── STATUS.md                     # Current build status
├── INVESTOR-PITCH.md             # Pitch deck content
├── LYLYS-PRODUCT-BRIEF.md        # Product vision
└── README.md                     # This file
```

---

## 🚀 Getting Started

### Prerequisites
- Node.js 18+ (v22 recommended)
- npm or yarn
- API keys (see below)

### Local Development

```bash
cd projects/lylys/app
npm install
npm run dev
```

Open http://localhost:3000 to see the app.

### Environment Variables

Create `.env.local` in `app/`:

```bash
# YouTube Data API
YOUTUBE_API_KEY=your_youtube_api_key

# Database (Supabase)
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key

# Email (SendGrid or Resend)
SENDGRID_API_KEY=your_sendgrid_key
# OR
RESEND_API_KEY=your_resend_key

# Payments (Stripe)
STRIPE_SECRET_KEY=your_stripe_secret
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=your_stripe_publishable

# Fulfillment (Printful)
PRINTFUL_API_KEY=your_printful_key
```

---

## 📦 Current Status

**Phase**: MVP Deployed (2026-02-14)  
**Preview**: https://creator-dash-test.preview.emergentagent.com/

### ✅ Complete
- [x] Landing page (hero, features, pricing, testimonials)
- [x] Fan Audit tool (form + results page)
- [x] Design system applied (Digital Warmth palette)
- [x] Responsive mobile-first design
- [x] Production deployment

### ⏳ In Progress / TODO
- [ ] YouTube API integration (currently shows mock data)
- [ ] Supabase database setup
- [ ] Email service integration
- [ ] Stripe payment flow
- [ ] Printful reward fulfillment
- [ ] Creator dashboard
- [ ] Authentication (NextAuth.js)

---

## 🎯 Target Market

**Primary**: True crime podcast/YouTube creators with 10K-500K subscribers

**Why True Crime?**
- Highly engaged fanbase (superfans leave tons of comments)
- Niche community (fans identify with the genre)
- Creators monetize well (merch, Patreon, ads)
- Underserved by existing tools (built for bigger creators)

**Expansion**: Can adapt to other niches (gaming, beauty, finance, etc.)

---

## 🧪 Testing the Preview

### Test the Landing Page
Visit: https://creator-dash-test.preview.emergentagent.com/

### Test the Fan Audit Tool
1. Click "Get Your Free Fan Audit"
2. Enter any YouTube video URL (mock data will display)
3. Review the superfan analysis on results page

**Note**: Currently shows hardcoded demo data. Real YouTube API integration coming soon.

---

## 📈 Success Metrics

### Launch Goals (Week 1)
- [ ] 100 landing page visits
- [ ] 10 Free Fan Audits completed
- [ ] 1 paying customer

### Growth Goals (Month 1)
- [ ] 1,000 page views
- [ ] 50 sign-ups (free tier)
- [ ] 5 paying customers ($49+ tier)
- [ ] $500 MRR

### Scale Goals (Month 3)
- [ ] 10,000 page views
- [ ] 500 sign-ups
- [ ] 50 paying customers
- [ ] $5,000 MRR

---

## 🤝 Contributing

This is a solo founder project (Mitch @ Super Massive Ventures), but feedback is welcome!

If you spot bugs or have suggestions:
1. Open an issue in the repo
2. Submit a PR with fixes
3. Reach out directly

---

## 📄 License

Proprietary. © 2026 Super Massive Ventures / Evil Studios.

---

## 🔗 Links

- **Live Preview**: https://creator-dash-test.preview.emergentagent.com/
- **Future Domain**: loveyouloveyourshow.com
- **Company**: [Super Massive Ventures](https://supermassive.ventures)
- **Sister Products**: [Afoodable AI](https://afoodable.ai), [WellPlate AI](https://wellplate.ai)

---

**Built with Emergent.sh vibecoding on 2026-02-14**  
**Status**: 🟢 Live Preview | 🟡 API Integrations Pending | 🔵 Ready to Scale

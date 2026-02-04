# Business Dashboard & Metrics Tracking

## Overview
Need visibility into all business metrics to make data-driven decisions.

## Products to Monitor

### Evil Apples
**Key Metrics:**
- Daily Active Users (DAU)
- Monthly Active Users (MAU)
- App Store downloads (iOS/Android)
- In-app purchase revenue
- Ad revenue
- Physical card game sales
- Retention rate (D1, D7, D30)
- Average Revenue Per User (ARPU)

**Data Sources:**
- App Store Connect API
- Google Play Console API
- In-app analytics
- Stripe/payment processor
- Amazon (for physical card sales)

### WellPlate AI
**Key Metrics:**
- Website traffic (unique visitors, pageviews)
- Sign-ups
- Free → Paid conversion rate
- MRR
- Churn rate
- Customer Acquisition Cost (CAC)
- Lifetime Value (LTV)

**Data Sources:**
- Google Analytics / Plausible
- Application database
- Stripe/payment processor

### Afoodable AI
**Key Metrics:**
- Same as WellPlate AI
- Feature usage (scanning, recipe generation, etc.)

### Wine Monkey
**Key Metrics:**
- Same as above
- Bot interactions
- Active servers/users (if Discord/Slack bot)

## Implementation Plan
1. Create unified dashboard script
2. Set up API connections to each service
3. Daily automated reports
4. Alert system for anomalies
5. Weekly/monthly trend analysis

## Next Actions
- [ ] Get API credentials for all services
- [ ] Build Python dashboard script
- [ ] Set up automated daily reports
- [ ] Create visualization (HTML report)

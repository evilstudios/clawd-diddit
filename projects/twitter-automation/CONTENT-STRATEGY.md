# Content Strategy Guide

## 🎯 Content Mix with Manifestos

You now have **3 tiers** of content:

### Tier 1: Manifesto Tweets (High-Concept)
**Tool**: `manifesto-tweets.py`  
**Themes**: Philosophy, Security, Utility, Efficiency, CTA  
**Frequency**: 1-2x per week  
**Purpose**: Brand positioning, thought leadership  

**5 Manifestos**:
1. **Sovereign Shift** - Philosophy (AI landscape critique)
2. **Soul-Shield** - Security (Prompt injection defense)
3. **The Claws** - Utility (MCP integration)
4. **Anti-Brainrot** - Efficiency (Memory optimization)
5. **The Forge** - CTA (Call to action)

### Tier 2: Standard Product Tweets
**Tool**: `auto-tweet-v2.py --category molt_foundry`  
**Frequency**: 2-3x per week  
**Purpose**: Product features, benefits, value props  

Includes the 5 new manifesto tweets mixed with existing content.

### Tier 3: Engagement & Evil Apples
**Tool**: `auto-tweet-v2.py` (smart mode)  
**Frequency**: Daily  
**Purpose**: Audience growth, engagement, virality  

---

## 📅 Recommended Posting Schedule

### Conservative Mix (2x Daily)
```
Week 1:
  Mon: Manifesto (Sovereign Shift)
  Tue: Evil Apples
  Wed: Product (molt_foundry)
  Thu: Engagement
  Fri: Evil Apples
  Sat: Product
  Sun: Evil Apples

Week 2:
  Mon: Manifesto (Soul-Shield)
  Tue: Evil Apples
  ...
```

### Moderate Mix (4x Daily) ⭐ Recommended
```
Daily pattern:
  Morning (6 AM):   Time-based motivational
  Mid-day (9 AM):   Product or Manifesto
  Afternoon (2 PM): Evil Apples
  Evening (6 PM):   Engagement or Product

Manifestos: Monday & Thursday mornings
```

### Aggressive Mix (6x Daily)
```
Daily:
  6 AM:  Time-based
  9 AM:  Product/Manifesto
  12 PM: Evil Apples
  2 PM:  Engagement
  5 PM:  Evil Apples
  8 PM:  Product

Manifestos: Monday, Wednesday, Friday (9 AM)
```

---

## 🎨 Manual Posting Recommendations

### For Maximum Impact

Post manifestos **manually** at strategic times:

**Best times for manifestos**:
- **Monday 9 AM EST** - Start the week strong
- **Wednesday 2 PM EST** - Mid-week thought leadership
- **Friday 10 AM EST** - Weekend reading material

**Sequence for launch week**:
1. Monday: **Sovereign Shift** (sets the tone)
2. Wednesday: **Soul-Shield** (technical credibility)
3. Friday: **The Claws** (utility proof)
4. Next Monday: **Anti-Brainrot** (efficiency message)
5. Next Friday: **The Forge** (call to action)

### Commands

```bash
# Post specific manifesto
python3 manifesto-tweets.py --manifesto sovereign_shift

# Auto-select next unposted
python3 manifesto-tweets.py

# Preview first
python3 manifesto-tweets.py --manifesto soul_shield --dry-run
```

---

## 🔄 Rotation Strategy

### Week 1: Brand Launch
- 2 Manifestos (Mon, Fri)
- 3 Product tweets
- 5 Evil Apples
- 4 Engagement

### Week 2-4: Balance
- 1 Manifesto per week
- 4 Product tweets
- 6 Evil Apples
- 3 Engagement

### Month 2+: Maintenance
- 1 Manifesto every 2 weeks (re-post old ones)
- 3 Product tweets/week
- Daily Evil Apples
- 2 Engagement/week

---

## 📊 Content Performance Tracking

### Track Engagement by Type

```bash
# After a week
python3 engagement-tracker.py --days 7 --save

# Check history
cat manifesto_history.json  # Manifesto posts
cat tweet_history.json      # All posts
```

### Expected Performance

**Manifestos**:
- Lower volume (fewer likes)
- Higher quality engagement (thoughtful replies)
- Attracts founders/builders
- Brand positioning

**Evil Apples**:
- Higher volume (more likes/RTs)
- Casual engagement
- Viral potential
- Audience growth

**Product**:
- Moderate engagement
- Qualified leads
- Conversion potential
- Sales funnel

---

## 🎯 Strategic Posting Patterns

### Pattern 1: Launch Mode (First Month)
**Goal**: Establish brand voice

```
4x daily:
  Morning:   Manifesto (2x/week) or Product
  Mid-day:   Product features
  Afternoon: Evil Apples (viral growth)
  Evening:   Engagement questions

Manifestos: All 5 over 2 weeks, then repeat
```

### Pattern 2: Growth Mode (Month 2-3)
**Goal**: Maximize reach

```
6x daily:
  Mix: 70% Evil Apples, 20% Product, 10% Manifesto
  
Manifestos: 1 per week (rotate)
```

### Pattern 3: Conversion Mode (Month 4+)
**Goal**: Drive conversions

```
4x daily:
  Mix: 40% Product, 40% Evil Apples, 20% Manifesto/Engagement
  
Manifestos: 2x per month (best performers)
```

---

## 💡 Advanced Tactics

### Manifesto Threads

Turn manifestos into threads for deeper engagement:

```bash
# Create thread.txt:
# Tweet 1: Manifesto hook
# Tweet 2: Supporting argument
# Tweet 3: Social proof
# Tweet 4: CTA

python3 thread-poster.py --file thread.txt
```

### Manifesto + Media

Combine with images for maximum impact:

```bash
# Create quote graphic
python3 media-uploader.py manifesto-quote.jpg
# Get media ID, then post with text
```

### Re-share Top Performers

```bash
# Check best tweets
python3 engagement-tracker.py --days 30

# Manually re-share winners as quote tweets
```

---

## 📈 Success Metrics by Content Type

### Manifestos
- **Target**: 50-100 impressions/tweet initially
- **Good**: 10+ likes, 2-3 thoughtful replies
- **Great**: Shared by relevant accounts
- **Goal**: Brand recognition, thought leadership

### Product Tweets
- **Target**: 100-200 impressions
- **Good**: 5+ clicks to site
- **Great**: 1+ sign-up mention
- **Goal**: Qualified leads

### Evil Apples
- **Target**: 200+ impressions
- **Good**: 20+ likes, 5+ RTs
- **Great**: Goes viral (1K+ impressions)
- **Goal**: Audience growth, engagement

### Engagement
- **Target**: 150+ impressions
- **Good**: 5-10 replies
- **Great**: Conversation thread
- **Goal**: Community building

---

## 🎮 Quick Commands

```bash
cd projects/twitter-automation

# Post next manifesto
python3 manifesto-tweets.py

# Post specific one
python3 manifesto-tweets.py --manifesto the_forge

# Standard product tweet
python3 auto-tweet-v2.py --category molt_foundry

# Evil Apples for engagement
python3 auto-tweet-v2.py --category evil_apples

# Smart mix (auto-select)
python3 auto-tweet-v2.py
```

---

## 🏆 Recommended First Week

**Manual posting for control**:

```
Monday 9 AM:    manifesto-tweets.py (Sovereign Shift)
Monday 6 PM:    auto-tweet-v2.py --category evil_apples

Tuesday 9 AM:   auto-tweet-v2.py --category molt_foundry
Tuesday 6 PM:   auto-tweet-v2.py --category evil_apples

Wednesday 2 PM: manifesto-tweets.py (Soul-Shield)
Wednesday 6 PM: auto-tweet-v2.py --category engagement

Thursday 9 AM:  auto-tweet-v2.py --category molt_foundry
Thursday 6 PM:  auto-tweet-v2.py --category evil_apples

Friday 10 AM:   manifesto-tweets.py (The Claws)
Friday 6 PM:    auto-tweet-v2.py --category evil_apples

Sat/Sun:        2x Evil Apples each day
```

**After first week**: Enable automation with manifesto rotation

---

## 🎯 Bottom Line

**Mix is key**:
- Manifestos: Brand authority
- Product: Conversions
- Evil Apples: Growth
- Engagement: Community

**Frequency**: 4x daily with $25 credits  
**Manifestos**: 1-2x per week (manual or scheduled)  
**Focus**: Quality manifestos + volume Evil Apples = Growth + Authority

---

**You now have premium brand positioning content ready to deploy!** 🚀

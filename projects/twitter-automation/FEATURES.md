# Twitter Automation - All Features

Complete feature set for powerful Twitter automation.

## 🎯 Core Features

### 1. Media Upload Support
**File**: `media-uploader.py`

Upload images and videos to Twitter:
```bash
# Upload single image
python3 media-uploader.py image.jpg --alt-text "Description"

# Upload multiple images (up to 4)
python3 media-uploader.py img1.jpg img2.jpg img3.jpg

# Get media ID for use in tweets
python3 media-uploader.py logo.png --json
```

**Use with tweets**:
```bash
# Upload media, get ID, then post
MEDIA_ID=$(python3 media-uploader.py image.jpg --json | jq -r .media_id)
python3 twitter-poster.py post --text "Check this out!" --media-id $MEDIA_ID
```

### 2. Thread Posting
**File**: `thread-poster.py`

Post multi-tweet threads automatically:
```bash
# From command line
python3 thread-poster.py --tweets \
  "Tweet 1: Starting a thread..." \
  "Tweet 2: More details here..." \
  "Tweet 3: And wrapping up!"

# From file (one tweet per line)
python3 thread-poster.py --file my-thread.txt

# From JSON
python3 thread-poster.py --file thread.json

# Dry run first
python3 thread-poster.py --file my-thread.txt --dry-run
```

**Thread file formats**:

Plain text (one per line):
```
This is tweet 1
This is tweet 2
This is tweet 3
```

Markdown (separated by ---):
```
First tweet in the thread

---

Second tweet with more content

---

Final tweet
```

JSON:
```json
[
  "First tweet",
  "Second tweet", 
  {
    "text": "Third tweet with media",
    "media_ids": ["123456789"]
  }
]
```

### 3. Engagement Tracking
**File**: `engagement-tracker.py`

Track and analyze tweet performance:
```bash
# Analyze last 7 days
python3 engagement-tracker.py

# Analyze last 30 days
python3 engagement-tracker.py --days 30

# Save metrics for historical tracking
python3 engagement-tracker.py --save

# JSON output for automation
python3 engagement-tracker.py --json
```

**Metrics tracked**:
- Total likes, retweets, replies, quotes
- Average engagement per tweet
- Engagement rate (%)
- Best performing tweet
- Impressions and reach

**Historical data**: Saved to `engagement_metrics.json`

### 4. Evil Apples Content Generator
**File**: `evil-apples-generator.py`

Generate random card combos from Evil Apples:
```bash
# Generate one combo
python3 evil-apples-generator.py

# Generate multiple combos
python3 evil-apples-generator.py --count 5

# Twitter-ready format (no markdown)
python3 evil-apples-generator.py --twitter-format

# No call-to-action
python3 evil-apples-generator.py --no-cta

# JSON output
python3 evil-apples-generator.py --json
```

**Output example**:
```
What's the newest TikTok trend that's sending Gen Z to the ER?

A) a virtual reality hand job
B) Cocaine Train

🤔 Which is funnier? Vote below!

😈 Play Evil Apples: evilapples.com
```

### 5. Enhanced Auto-Tweeting
**File**: `auto-tweet-v2.py`

Smart auto-posting with multiple strategies:

**Smart Mode** (default - AI-like selection):
```bash
python3 auto-tweet-v2.py
```

Selection algorithm:
- 30% Evil Apples combos (generated fresh each time)
- 40% Time-based tweets (morning/afternoon/evening)
- 30% Standard category tweets (products/engagement)

**Specific Categories**:
```bash
# Always Evil Apples
python3 auto-tweet-v2.py --category evil_apples

# Time-based only
python3 auto-tweet-v2.py --category time_based

# Specific product
python3 auto-tweet-v2.py --category molt_foundry
python3 auto-tweet-v2.py --category wellplate_ai
python3 auto-tweet-v2.py --category engagement
```

**Time-Based Tweets**:
- **Morning** (6 AM - 12 PM): Motivational, coffee, building
- **Afternoon** (12 PM - 6 PM): Progress updates, product mentions
- **Evening** (6 PM - 6 AM): Reflection, relaxation, results

### 6. Template Preview
**File**: `preview-tweets.py`

Browse all available tweet templates:
```bash
# Count templates
python3 preview-tweets.py --count

# Show all templates
python3 preview-tweets.py

# Show specific category
python3 preview-tweets.py --category evil_apples

# Get random examples
python3 preview-tweets.py --random 10
```

## 🔧 Integration Examples

### Morning Automation
```bash
# 9 AM: Post motivational + Evil Apples combo
python3 auto-tweet-v2.py --category time_based
sleep 3600  # Wait 1 hour
python3 auto-tweet-v2.py --category evil_apples
```

### Content with Images
```bash
# Create Evil Apples card combo as image, then post
python3 evil-apples-generator.py --twitter-format > tweet.txt
# (Use external tool to create image)
MEDIA_ID=$(python3 media-uploader.py combo-card.jpg --json | jq -r .media_id)
python3 twitter-poster.py post --text "$(cat tweet.txt)" --media-id $MEDIA_ID
```

### Thread Launch
```bash
# Create announcement thread
cat > thread.txt << 'EOF'
🚀 Launching something new!

We're excited to announce...

Here's how it works:

1. Step one
2. Step two
3. Profit!

Try it now: evilapples.com 😈🍎
EOF

python3 thread-poster.py --file thread.txt --dry-run
# Review, then post for real
python3 thread-poster.py --file thread.txt
```

### Weekly Analytics
```bash
# Get engagement report
python3 engagement-tracker.py --days 7 --save > weekly-report.txt

# Tweet best-performing content
BEST=$(python3 engagement-tracker.py --json | jq -r '.best_performing.text')
python3 twitter-poster.py post --text "This week's top tweet: $BEST"
```

## 📊 A/B Testing (Manual)

Test different tweet styles:

```bash
# Version A: Direct
python3 twitter-poster.py post --text "Evil Apples: The savage party game. Download now!"

# Version B: Question
python3 twitter-poster.py post --text "Ever wanted to find out how dark your friends' humor is? Try Evil Apples 😈"

# Track performance after 24h
python3 engagement-tracker.py --days 1
```

## 🤖 Advanced Automation

### Smart Scheduling
```bash
#!/bin/bash
# smart-poster.sh - Posts based on time of day

HOUR=$(date +%H)

if [ $HOUR -ge 6 ] && [ $HOUR -lt 12 ]; then
    # Morning: motivational
    python3 auto-tweet-v2.py --category time_based
elif [ $HOUR -ge 12 ] && [ $HOUR -lt 18 ]; then
    # Afternoon: product or Evil Apples
    python3 auto-tweet-v2.py --category smart
else
    # Evening: engagement
    python3 auto-tweet-v2.py --category engagement
fi
```

### Performance-Based Posting
```bash
#!/bin/bash
# post-winner.sh - Re-share top performing content

# Get best tweet from last week
BEST_ID=$(python3 engagement-tracker.py --days 7 --json | jq -r '.best_performing.id')

# Quote tweet it
python3 twitter-poster.py post \
  --text "Still one of our favorites 🔥" \
  --quote $BEST_ID
```

## 📈 Analytics Dashboard (Manual)

Track these metrics weekly:

```bash
# Week 1
python3 engagement-tracker.py --days 7 --save

# Week 2
python3 engagement-tracker.py --days 7 --save

# Compare in engagement_metrics.json
```

Look for:
- Which time slots perform best
- Which categories get most engagement
- Which Evil Apples combos go viral
- Engagement rate trends

## 🎯 Strategy Recommendations

### Daily Mix
- 2x Evil Apples combos (high engagement)
- 1x Product mention (WellPlate/MoltFoundry)
- 1x Engagement question
- 1x Time-appropriate motivational

### Growth Phase
Focus on viral content:
- 70% Evil Apples (shareable, funny)
- 20% Engagement (build community)
- 10% Product (soft sell)

### Conversion Phase
Focus on products:
- 40% Product features/benefits
- 30% Evil Apples (keep engagement)
- 30% Social proof/testimonials

## 🚀 Quick Wins

1. **Evil Apples Power Hour**: Post 3-4 combos in succession
   ```bash
   for i in {1..4}; do
     python3 auto-tweet-v2.py --category evil_apples
     sleep 600  # 10 min between
   done
   ```

2. **Thread Storm**: Launch product with 5-tweet thread
   ```bash
   python3 thread-poster.py --file product-launch.txt
   ```

3. **Engagement Bomb**: Ask question + post Evil Apples combo
   ```bash
   python3 auto-tweet-v2.py --category engagement
   sleep 300
   python3 auto-tweet-v2.py --category evil_apples
   ```

## 🔮 Future Enhancements

Easy to add:
- [ ] Auto-reply to mentions
- [ ] Schedule tweets for specific times
- [ ] Poll creation
- [ ] Hashtag optimization
- [ ] Competitor monitoring
- [ ] Trending topic integration
- [ ] Image generation from Evil Apples combos
- [ ] Video clip posting
- [ ] Twitter Spaces automation

---

**All features ready to use. Just need permission fix to start posting!**

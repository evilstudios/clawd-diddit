#!/bin/bash
#
# Scrape Philadelphia Restaurants for Afoodable Campaign
# Targets: Bakeries, Cafes, Fast Casual, Ghost Kitchens
#

set -e

echo "🍎 Afoodable Philadelphia Restaurant Scraper"
echo "=============================================="
echo ""

LOCATION="Philadelphia, PA"
OUTPUT_DIR="./philadelphia-leads"
DATE=$(date +%Y-%m-%d)

# Create output directory
mkdir -p "$OUTPUT_DIR"

echo "📍 Location: $LOCATION"
echo "📂 Output: $OUTPUT_DIR"
echo ""

# Scrape different restaurant types
echo "🥐 Scraping bakeries..."
python3 restaurant-scraper.py \
  --query "bakery" \
  --location "$LOCATION" \
  --max 30 \
  --output "$OUTPUT_DIR/bakeries-$DATE.csv"

echo ""
echo "☕ Scraping cafes..."
python3 restaurant-scraper.py \
  --query "cafe" \
  --location "$LOCATION" \
  --max 30 \
  --output "$OUTPUT_DIR/cafes-$DATE.csv"

echo ""
echo "🍔 Scraping fast casual restaurants..."
python3 restaurant-scraper.py \
  --query "fast casual restaurant" \
  --location "$LOCATION" \
  --max 25 \
  --output "$OUTPUT_DIR/fast-casual-$DATE.csv"

echo ""
echo "👻 Scraping ghost kitchens & meal prep..."
python3 restaurant-scraper.py \
  --query "ghost kitchen" \
  --location "$LOCATION" \
  --max 15 \
  --output "$OUTPUT_DIR/ghost-kitchens-$DATE.csv"

# Combine all CSVs
echo ""
echo "📊 Combining all results..."
OUTPUT_FILE="$OUTPUT_DIR/philadelphia-restaurants-complete-$DATE.csv"

# Combine CSVs (skip header for subsequent files)
head -1 "$OUTPUT_DIR/bakeries-$DATE.csv" > "$OUTPUT_FILE"
tail -n +2 "$OUTPUT_DIR/bakeries-$DATE.csv" >> "$OUTPUT_FILE"
tail -n +2 "$OUTPUT_DIR/cafes-$DATE.csv" >> "$OUTPUT_FILE"
tail -n +2 "$OUTPUT_DIR/fast-casual-$DATE.csv" >> "$OUTPUT_FILE"
tail -n +2 "$OUTPUT_DIR/ghost-kitchens-$DATE.csv" >> "$OUTPUT_FILE"

# Count results
TOTAL=$(tail -n +2 "$OUTPUT_FILE" | wc -l)

echo ""
echo "✅ Scraping complete!"
echo ""
echo "📊 Results:"
echo "   Total restaurants: $TOTAL"
echo "   Output file: $OUTPUT_FILE"
echo ""
echo "Next steps:"
echo "1. Review the CSV file"
echo "2. Upload to Instantly.ai dashboard"
echo "3. Set up campaign with email sequences"
echo "4. Launch! 🚀"
echo ""

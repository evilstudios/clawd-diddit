#!/bin/bash
# Enhanced Twitter Auto-Posting Schedule Setup
# With multiple frequency options

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🤖 Twitter Auto-Posting Schedule Setup"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "💰 With $25 in credits, you can post much more frequently!"
echo ""
echo "Select posting frequency:"
echo ""
echo "  1) Conservative (2x daily)  - 9 AM, 6 PM EST"
echo "     Cost: ~$0.03/month | $25 lasts 69 years"
echo ""
echo "  2) Moderate (4x daily) ⭐ RECOMMENDED"
echo "     Times: 6 AM, 9 AM, 2 PM, 6 PM EST"
echo "     Cost: ~$0.06/month | $25 lasts 34 years"
echo ""
echo "  3) Active (6x daily)"
echo "     Times: 6 AM, 9 AM, 12 PM, 2 PM, 5 PM, 8 PM EST"
echo "     Cost: ~$0.09/month | $25 lasts 22 years"
echo ""
echo "  4) Aggressive (8x daily)"
echo "     Every 3 hours from 6 AM to 11 PM EST"
echo "     Cost: ~$0.12/month | $25 lasts 17 years"
echo ""
echo "  5) Custom - Enter your own schedule"
echo ""

read -p "Choose option (1-5): " -n 1 -r
echo ""

case $REPLY in
  1)
    SCHEDULE="Conservative (2x daily)"
    CRONS=(
      "0 14 * * * cd $SCRIPT_DIR && python3 auto-tweet-v2.py >> $SCRIPT_DIR/auto-tweet.log 2>&1"
      "0 23 * * * cd $SCRIPT_DIR && python3 auto-tweet-v2.py >> $SCRIPT_DIR/auto-tweet.log 2>&1"
    )
    ;;
  2)
    SCHEDULE="Moderate (4x daily) ⭐"
    CRONS=(
      "0 11 * * * cd $SCRIPT_DIR && python3 auto-tweet-v2.py >> $SCRIPT_DIR/auto-tweet.log 2>&1"
      "0 14 * * * cd $SCRIPT_DIR && python3 auto-tweet-v2.py >> $SCRIPT_DIR/auto-tweet.log 2>&1"
      "0 19 * * * cd $SCRIPT_DIR && python3 auto-tweet-v2.py >> $SCRIPT_DIR/auto-tweet.log 2>&1"
      "0 23 * * * cd $SCRIPT_DIR && python3 auto-tweet-v2.py >> $SCRIPT_DIR/auto-tweet.log 2>&1"
    )
    ;;
  3)
    SCHEDULE="Active (6x daily)"
    CRONS=(
      "0 11 * * * cd $SCRIPT_DIR && python3 auto-tweet-v2.py >> $SCRIPT_DIR/auto-tweet.log 2>&1"
      "0 14 * * * cd $SCRIPT_DIR && python3 auto-tweet-v2.py >> $SCRIPT_DIR/auto-tweet.log 2>&1"
      "0 17 * * * cd $SCRIPT_DIR && python3 auto-tweet-v2.py >> $SCRIPT_DIR/auto-tweet.log 2>&1"
      "0 19 * * * cd $SCRIPT_DIR && python3 auto-tweet-v2.py >> $SCRIPT_DIR/auto-tweet.log 2>&1"
      "0 22 * * * cd $SCRIPT_DIR && python3 auto-tweet-v2.py >> $SCRIPT_DIR/auto-tweet.log 2>&1"
      "0 1 * * * cd $SCRIPT_DIR && python3 auto-tweet-v2.py >> $SCRIPT_DIR/auto-tweet.log 2>&1"
    )
    ;;
  4)
    SCHEDULE="Aggressive (8x daily)"
    CRONS=(
      "0 11,14,17,19,21,23,1,3 * * * cd $SCRIPT_DIR && python3 auto-tweet-v2.py >> $SCRIPT_DIR/auto-tweet.log 2>&1"
    )
    ;;
  5)
    echo ""
    echo "Custom schedule - Edit manually with: crontab -e"
    echo "Example format:"
    echo "  0 14 * * * cd $SCRIPT_DIR && python3 auto-tweet-v2.py >> $SCRIPT_DIR/auto-tweet.log 2>&1"
    exit 0
    ;;
  *)
    echo "Invalid option. Exiting."
    exit 1
    ;;
esac

echo ""
echo "📅 Installing: $SCHEDULE"
echo ""

# Remove existing auto-tweet cron jobs
crontab -l 2>/dev/null | grep -v "auto-tweet" | crontab -

# Add new jobs
(
  crontab -l 2>/dev/null
  for cron in "${CRONS[@]}"; do
    echo "$cron"
  done
) | crontab -

echo "✅ Cron jobs installed!"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📊 Schedule Summary:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

case $REPLY in
  1)
    echo "  🌅 9:00 AM EST (14:00 UTC)"
    echo "  🌆 6:00 PM EST (23:00 UTC)"
    ;;
  2)
    echo "  🌅 6:00 AM EST (11:00 UTC)"
    echo "  ☕ 9:00 AM EST (14:00 UTC)"
    echo "  🌤️  2:00 PM EST (19:00 UTC)"
    echo "  🌆 6:00 PM EST (23:00 UTC)"
    ;;
  3)
    echo "  🌅 6:00 AM EST (11:00 UTC)"
    echo "  ☕ 9:00 AM EST (14:00 UTC)"
    echo "  🌤️  12:00 PM EST (17:00 UTC)"
    echo "  ⏰ 2:00 PM EST (19:00 UTC)"
    echo "  🌇 5:00 PM EST (22:00 UTC)"
    echo "  🌙 8:00 PM EST (01:00 UTC)"
    ;;
  4)
    echo "  Every 3 hours: 6 AM, 9 AM, 12 PM, 2 PM, 4 PM, 6 PM, 8 PM, 10 PM EST"
    ;;
esac

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "💡 Management:"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  View jobs:    crontab -l"
echo "  Edit jobs:    crontab -e"
echo "  View logs:    tail -f $SCRIPT_DIR/auto-tweet.log"
echo "  Test post:    cd $SCRIPT_DIR && python3 auto-tweet-v2.py"
echo "  Check credits: cd $SCRIPT_DIR && python3 credit-monitor.py"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎉 Automation Active! Tweets will post automatically."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

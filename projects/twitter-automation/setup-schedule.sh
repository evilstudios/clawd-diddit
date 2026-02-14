#!/bin/bash
# Setup automated Twitter posting schedule

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "🤖 Setting up Twitter Auto-Posting Schedule"
echo ""
echo "This will add cron jobs to post tweets automatically:"
echo "  - 2x daily: Morning (9 AM) and Evening (6 PM) EST"
echo "  - Rotates through all content categories"
echo ""

# Convert to user's timezone (assuming EST for now)
# Morning: 9 AM EST = 14:00 UTC
# Evening: 6 PM EST = 23:00 UTC

read -p "Install automated posting schedule? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Cancelled."
    exit 0
fi

# Create cron entries
CRON_MORNING="0 14 * * * cd $SCRIPT_DIR && python3 auto-tweet.py >> $SCRIPT_DIR/auto-tweet.log 2>&1"
CRON_EVENING="0 23 * * * cd $SCRIPT_DIR && python3 auto-tweet.py >> $SCRIPT_DIR/auto-tweet.log 2>&1"

# Add to crontab
(crontab -l 2>/dev/null | grep -v "auto-tweet.py"; echo "$CRON_MORNING"; echo "$CRON_EVENING") | crontab -

echo ""
echo "✅ Cron jobs installed!"
echo ""
echo "Schedule:"
echo "  🌅 Morning: 9:00 AM EST (14:00 UTC)"
echo "  🌆 Evening: 6:00 PM EST (23:00 UTC)"
echo ""
echo "View logs: tail -f $SCRIPT_DIR/auto-tweet.log"
echo "List cron jobs: crontab -l"
echo "Remove schedule: crontab -e (then delete the auto-tweet.py lines)"
echo ""

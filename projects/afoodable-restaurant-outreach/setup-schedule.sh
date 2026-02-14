#!/bin/bash
# Afoodable Social Media Automation - Cron Setup
# Sets up automated posting to Facebook and Twitter

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_DIR="$SCRIPT_DIR"

echo "🚀 Afoodable Social Media Automation - Cron Setup"
echo ""
echo "This will schedule:"
echo "  • Facebook posts: 10 AM & 6 PM EST (daily)"
echo "  • Twitter posts: 11 AM & 5 PM EST (daily)"
echo ""

# Check if scripts exist
if [ ! -f "$SCRIPT_DIR/facebook-auto-poster.py" ]; then
    echo "❌ Error: facebook-auto-poster.py not found"
    exit 1
fi

if [ ! -f "$SCRIPT_DIR/twitter-auto-poster.py" ]; then
    echo "❌ Error: twitter-auto-poster.py not found"
    exit 1
fi

# Make scripts executable
chmod +x "$SCRIPT_DIR/facebook-auto-poster.py"
chmod +x "$SCRIPT_DIR/twitter-auto-poster.py"

# Check for Python 3
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: python3 not found. Please install Python 3."
    exit 1
fi

echo "📝 Current crontab:"
crontab -l 2>/dev/null || echo "(empty)"
echo ""

read -p "⚠️  This will ADD new cron jobs. Continue? (y/n) " -n 1 -r
echo ""

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Cancelled"
    exit 0
fi

# Create temporary crontab file
TEMP_CRON=$(mktemp)

# Get existing crontab (if any)
crontab -l 2>/dev/null > "$TEMP_CRON" || true

# Add Afoodable automation jobs
cat >> "$TEMP_CRON" << EOF

# Afoodable Social Media Automation (added $(date +%Y-%m-%d))
# Facebook: 10 AM & 6 PM EST
0 15 * * * cd $SCRIPT_DIR && /usr/bin/python3 facebook-auto-poster.py >> $LOG_DIR/facebook-auto.log 2>&1
0 23 * * * cd $SCRIPT_DIR && /usr/bin/python3 facebook-auto-poster.py >> $LOG_DIR/facebook-auto.log 2>&1

# Twitter: 11 AM & 5 PM EST
0 16 * * * cd $SCRIPT_DIR && /usr/bin/python3 twitter-auto-poster.py >> $LOG_DIR/twitter-auto.log 2>&1
0 22 * * * cd $SCRIPT_DIR && /usr/bin/python3 twitter-auto-poster.py >> $LOG_DIR/twitter-auto.log 2>&1
EOF

# Install new crontab
crontab "$TEMP_CRON"
rm "$TEMP_CRON"

echo ""
echo "✅ Cron jobs installed successfully!"
echo ""
echo "📅 Schedule (UTC times shown, adjust for EST):"
echo "   • Facebook: 15:00 UTC (10 AM EST), 23:00 UTC (6 PM EST)"
echo "   • Twitter: 16:00 UTC (11 AM EST), 22:00 UTC (5 PM EST)"
echo ""
echo "📋 View cron jobs:"
echo "   crontab -l"
echo ""
echo "📝 View logs:"
echo "   tail -f $LOG_DIR/facebook-auto.log"
echo "   tail -f $LOG_DIR/twitter-auto.log"
echo ""
echo "🛑 Remove cron jobs:"
echo "   crontab -e  (then manually delete the Afoodable lines)"
echo ""
echo "⚙️  Don't forget to set up your API credentials!"
echo "   export FACEBOOK_PAGE_ID=\"...\""
echo "   export FACEBOOK_PAGE_ACCESS_TOKEN=\"...\""
echo "   export TWITTER_API_KEY=\"...\""
echo "   (see AUTOMATION-README.md for details)"
echo ""
echo "🧪 Test first with dry-run:"
echo "   DRY_RUN=true python3 facebook-auto-poster.py"
echo "   DRY_RUN=true python3 twitter-auto-poster.py"
echo ""
echo "✅ All set! Automation will run automatically."

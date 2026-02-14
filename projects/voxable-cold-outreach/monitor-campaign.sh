#!/bin/bash
# Voxable Campaign Monitor
# Checks campaign status via Instantly.ai API

export INSTANTLY_API_KEY="ZmY1YTRkZTktYmRiNC00N2ZiLWFmMzktN2JhNzg5YmNlYWI4OnZxcWhDU0d4YUdURg=="
CAMPAIGN_ID="cf9d41e0-20b1-49c7-8b1c-7843888dae4f"
LOG_FILE="campaign-monitor.log"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🎯 VOXABLE CAMPAIGN MONITOR"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Time: $(date '+%Y-%m-%d %H:%M:%S %Z')"
echo ""

# Check campaign status
echo "📊 Campaign Status:"
STATUS=$(curl -s -X GET "https://api.instantly.ai/api/v2/campaigns" \
  -H "Authorization: Bearer $INSTANTLY_API_KEY" \
  -H "Content-Type: application/json" | jq -r '.items[] | select(.id=="'$CAMPAIGN_ID'") | .status')

if [ "$STATUS" = "1" ]; then
    echo "   ✅ ACTIVE"
elif [ "$STATUS" = "0" ]; then
    echo "   ⏸️  PAUSED"
else
    echo "   ❓ UNKNOWN (Status: $STATUS)"
fi

echo ""
echo "📧 Configuration:"
curl -s -X GET "https://api.instantly.ai/api/v2/campaigns" \
  -H "Authorization: Bearer $INSTANTLY_API_KEY" \
  -H "Content-Type: application/json" | jq -r '.items[] | select(.id=="'$CAMPAIGN_ID'") | 
    "   Daily Limit: \(.daily_limit) emails/day\n   Stop on Reply: \(.stop_on_reply)\n   Open Tracking: \(.open_tracking)\n   Link Tracking: \(.link_tracking)\n   Sender: \(.email_list[0])"'

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "⏰ Next check in 30 minutes"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Log to file
{
  echo "$(date '+%Y-%m-%d %H:%M:%S') - Status: $STATUS"
} >> "$LOG_FILE"

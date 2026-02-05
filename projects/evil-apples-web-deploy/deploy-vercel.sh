#!/bin/bash
#
# Deploy Evil Apples Web Client to Vercel
#

set -e

echo "🍎 Evil Apples Web - Deploying to Vercel"
echo "=========================================="

cd /root/repos/evilapplesserver/web-client

# Build
echo ""
echo "📦 Building production bundle..."
npm run build

# Check if Vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo ""
    echo "⚠️  Vercel CLI not found. Installing..."
    npm install -g vercel
fi

# Deploy
echo ""
echo "🚀 Deploying to Vercel..."
echo ""
echo "You'll be prompted to:"
echo "  1. Log in (if first time)"
echo "  2. Link to project (or create new)"
echo "  3. Confirm settings"
echo ""
echo "Press Enter to continue..."
read

vercel --prod

echo ""
echo "✅ Deployment complete!"
echo ""
echo "Next steps:"
echo "  1. Visit your deployment URL"
echo "  2. Set up custom domain: play.evilapples.com"
echo "  3. Configure environment variables:"
echo "     VITE_API_URL=https://api.evilapples.com"
echo "     VITE_SOCKET_URL=wss://api.evilapples.com"
echo ""
echo "🎉 Evil Apples is LIVE on the web!"

# Deploy Evil Apples Web - RIGHT NOW 🚀

## Fastest Path to Live Website

Since the web client is already built, let's deploy it **immediately** and connect to backend later.

## Option 1: Static Deploy (5 minutes) ⚡

### Deploy to Vercel (Recommended - Free & Fast)

```bash
cd /root/repos/evilapplesserver/web-client

# Build production version
npm run build

# Install Vercel CLI
npm i -g vercel

# Deploy! (follow prompts)
vercel --prod

# Result: https://evil-apples-web.vercel.app (or custom domain)
```

**What you'll get:**
- Live website in 2 minutes
- Auto SSL/HTTPS
- Global CDN
- Custom domain support (play.evilapples.com)

### Alternative: Netlify

```bash
cd /root/repos/evilapplesserver/web-client
npm run build

# Install Netlify CLI
npm i -g netlify-cli

# Deploy
netlify deploy --prod --dir=dist
```

## Option 2: GitHub Pages (Free, No CLI needed)

```bash
cd /root/repos/evilapplesserver/web-client

# Build
npm run build

# Push to GitHub
git init
git add .
git commit -m "Evil Apples Web Client"
git branch -M main
git remote add origin https://github.com/evilstudios/evil-apples-web.git
git push -u origin main

# Enable GitHub Pages in repo settings → Pages
# Point to main branch, /dist folder
```

Live at: `https://evilstudios.github.io/evil-apples-web/`

## What's the Catch?

**The frontend is built and ready.** However:

1. **Backend connection needed** for:
   - Guest login
   - Matchmaking
   - Real-time gameplay
   - Game state sync

2. **Right now it will:**
   - Load perfectly
   - Show UI/components
   - But can't connect to game server yet

## Two-Phase Launch Strategy

### Phase 1: Deploy Frontend NOW (Today ✅)
- Deploy static site (Vercel/Netlify)
- Show "Coming Soon" or "Beta Mode" banner
- Collect emails for launch notification
- Test UI/UX with real users
- Generate buzz

### Phase 2: Connect Backend (Tomorrow/This Week)
- Set up backend WebSocket handlers
- Configure CORS for web domain
- Add guest authentication
- Enable full gameplay

## Quick "Landing Page" Mode

If backend isn't ready, convert to landing page temporarily:

```jsx
// src/App.jsx - Add this at top
const BETA_MODE = true;

if (BETA_MODE) {
  return (
    <div className="landing-page">
      <h1>🍎 Evil Apples - Web Version Coming Soon!</h1>
      <p>Play the hilarious card game in your browser</p>
      <input placeholder="Enter email for early access" />
      <button>Notify Me</button>
      <img src="screenshot.png" alt="Preview" />
    </div>
  );
}
```

## Recommendation for TODAY

**Deploy the frontend now to Vercel:**

```bash
cd /root/repos/evilapplesserver/web-client

# Build
npm run build

# Deploy
npx vercel --prod

# Takes 2 minutes
```

**Result:**
✅ Live website
✅ Working URL to share
✅ Test UI on real devices
✅ Show progress to stakeholders
✅ SEO/discovery starts

**Then tonight/tomorrow:**
- Wire up backend
- Enable full gameplay
- Switch from "beta" to "live"

## Environment Variables for Vercel

When deploying, set these in Vercel dashboard:

```bash
VITE_API_URL=https://api.evilapples.com
VITE_SOCKET_URL=wss://api.evilapples.com
```

(We'll configure these once backend is ready)

## DNS Setup (After Deploy)

Once deployed, point your domain:

```
Type: CNAME
Name: play
Value: cname.vercel-dns.com
```

Result: `play.evilapples.com` → Your web app

---

## Action Items RIGHT NOW:

1. `cd /root/repos/evilapplesserver/web-client`
2. `npm run build`
3. `npx vercel --prod`
4. Share the URL! 🎉

**Time: 5 minutes**
**Result: Live website**

Ready? Let's ship it! 🚀

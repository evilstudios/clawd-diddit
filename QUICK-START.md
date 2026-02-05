# 🚀 Quick Start - Your Next Actions

## Voxable Cold Outreach (Ready to Launch)

**What you need:**
1. Instantly.ai API key - [Get it here](https://app.instantly.ai/app/settings/api)
2. Your 230-lead CSV file

**Launch commands:**
```bash
# Set API key
export INSTANTLY_API_KEY="your_key_here"

# Test (dry run)
./automation/instantly-campaign-launcher.py \
  --leads your-leads.csv \
  --dry-run

# Launch for real
./automation/instantly-campaign-launcher.py \
  --leads your-leads.csv

# Monitor performance
./automation/voxable-lead-tracker.py \
  --campaign "Voxable - Local Service - Feb 2025" \
  --dashboard
```

**Time:** 10 minutes
**Expected:** 8-15 interested leads → 4-8 demos → 1-3 customers

---

## Evil Apples Web (Deploy in 5 Minutes)

**Deploy NOW:**
```bash
cd /root/repos/evilapplesserver/web-client
npx vercel --prod
```

Follow prompts → Get live URL → Done! ✅

**Or use the script:**
```bash
/root/clawd/projects/evil-apples-web-deploy/deploy-vercel.sh
```

**Result:** Live website at `https://[your-url].vercel.app`

**Custom domain:** Point `play.evilapples.com` → Vercel (in Vercel dashboard)

---

## Backend Integration (Later/Tomorrow)

If you want full gameplay working:

```bash
# Start MongoDB
sudo mongod --dbpath /data/db --fork --logpath /var/log/mongodb.log

# Start Evil Apples server
cd /root/repos/evilapplesserver
npm start
```

Then configure CORS + guest auth (see `SETUP.md`)

---

## Files to Review

**Everything is in:** `/root/clawd/`

**Key docs:**
- `TODAY-DELIVERABLES.md` - What was built
- `automation/README-VOXABLE-OUTREACH.md` - Voxable guide
- `projects/evil-apples-web-deploy/STATUS.md` - Evil Apples status

**Quick access:**
```bash
cd /root/clawd
cat TODAY-DELIVERABLES.md
```

---

## Your Call

**Voxable:** Get API key → Launch
**Evil Apples:** Deploy now (5 min) OR wire backend first (3 hours)

Ready when you are! 🚀

# 🚀 Friday Launch Day - Feb 7, 2025

## Launch Targets

### 1. Voxable Cold Outreach Campaign
### 2. Evil Apples Web Version

---

## Pre-Launch Checklist (Wed-Thu)

### Voxable Prep:
- [ ] Get fresh Instantly.ai API key
- [ ] Prepare 230-lead CSV file
- [ ] Test API key with dry-run
- [ ] Review email sequences
- [ ] Set up monitoring dashboard

### Evil Apples Prep:
- [ ] Choose deployment path (fast or full)
- [ ] If full: Configure backend (MongoDB, CORS, guest auth)
- [ ] Test build locally
- [ ] Prepare Vercel account
- [ ] Set up custom domain DNS (if using play.evilapples.com)

---

## Friday Launch Timeline

### Morning (Voxable - 30 min)
**9:00 AM** - Launch Voxable Campaign
```bash
export INSTANTLY_API_KEY="your_fresh_key"
cd /root/clawd
./automation/instantly-campaign-launcher.py --leads voxable-leads.csv
```

**Expected:**
- Campaign live in Instantly.ai
- First emails sending within hours
- Dashboard monitoring active

---

### Afternoon (Evil Apples - 1-4 hours)

**Option A: Fast Deploy (5 min)**
```bash
cd /root/repos/evilapplesserver/web-client
npx vercel --prod
```
Result: Live URL immediately

**Option B: Full Deploy (3-4 hours)**
1. Start MongoDB + backend
2. Configure CORS
3. Test gameplay
4. Deploy frontend
Result: Fully functional game

---

## Post-Launch Actions

### Voxable (Friday Evening):
- [ ] Check dashboard for first opens/replies
- [ ] Verify emails are sending
- [ ] Monitor deliverability
- [ ] Prepare response templates

### Evil Apples:
- [ ] Test website on multiple devices
- [ ] Share URL with team/testers
- [ ] Monitor for issues
- [ ] Set up analytics (optional)

---

## Weekend Monitoring

### Saturday/Sunday:
- Check Voxable replies (respond within 2 hours)
- Monitor Evil Apples traffic
- Note any bugs or issues
- Prepare for Monday optimization

---

## What's Already Ready

✅ Voxable automation tools built
✅ Evil Apples production build complete
✅ Documentation comprehensive
✅ Scripts tested and working
✅ Deployment guides written

**All systems GO for Friday! 🚀**

---

## Between Now and Friday

I'll:
- Keep systems updated
- Monitor for any issues
- Be ready to help with prep
- Answer any questions

You:
- Review the tools/docs
- Get Instantly.ai API key
- Prepare lead CSV
- Decide Evil Apples deploy path
- Enjoy the anticipation! 😎

---

**Target:** Both live by Friday 5 PM
**Confidence:** 100% ready ✅

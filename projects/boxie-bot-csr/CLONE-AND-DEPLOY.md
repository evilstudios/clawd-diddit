# Clone and Deploy to Your Company

This repository is ready to be cloned to your company's environment with all placeholder credentials.

---

## What's Included

✅ **Complete source code** - All functions and clients implemented  
✅ **Placeholder credentials** - All sensitive values in `.env.example`  
✅ **Documentation** - Setup guides, checklists, and instructions  
✅ **Testing** - Local test script to validate configuration  
✅ **Custom GPT config** - OpenAPI spec + instructions ready to use  
✅ **Deployment-ready** - Structured for Zoho Catalyst deployment

---

## Quick Clone & Deploy

### 1. Clone to Your Company Repo

```bash
# Clone this repo
git clone <this-repo-url> boxie-bot-csr

# Push to your company's git
cd boxie-bot-csr
git remote remove origin
git remote add origin <your-company-repo-url>
git push -u origin main
```

### 2. Configure Credentials

```bash
# Copy environment template
cp src/.env.example src/.env

# Edit with your actual credentials
nano src/.env
```

**Required:**
- `ZOHO_DESK_ORG_ID` - From your Zoho Desk URL
- `ZOHO_DESK_API_TOKEN` - Generate in Zoho Desk Settings → API
- `OPENAI_API_KEY` - From OpenAI platform
- `API_KEY` - Generate a secure random string (32+ chars)

**Optional (for RAG):**
- `SUPABASE_URL`
- `SUPABASE_SERVICE_KEY`

### 3. Test Locally

```bash
npm install
npm test
```

Should show:
```
✅ Config loaded
✅ Zoho Desk connection working
✅ OpenAI connection working
✅ RAG enabled (if configured)
```

### 4. Deploy to Catalyst

```bash
# Install Catalyst CLI
npm install -g zoho-catalyst-cli

# Login
catalyst login

# Initialize project
catalyst init

# Deploy functions
catalyst deploy
```

### 5. Configure Custom GPT

1. Update `custom-gpt/openapi-spec.yaml` with your Catalyst function URLs
2. Go to ChatGPT → Create Custom GPT
3. Upload instructions from `custom-gpt/instructions.md`
4. Import `custom-gpt/openapi-spec.yaml`
5. Configure authentication:
   - Type: API Key
   - Header: `X-API-Key`
   - Value: Your `API_KEY` from `.env`

### 6. Index Knowledge Base (if using RAG)

```bash
# Set up Supabase (see README-SETUP.md for SQL script)
# Then index your documents:
node scripts/index-document.js --file "./docs/refund-policy.pdf"
```

---

## File Structure

**Configuration:**
- `src/.env.example` - Template for credentials
- `src/config.js` - Configuration loader

**Core Logic:**
- `src/zoho-desk-client.js` - Zoho Desk API integration
- `src/rag-client.js` - Vector search (RAG)

**Catalyst Functions:**
- `catalyst-functions/searchTickets.js`
- `catalyst-functions/getTicketDetails.js`
- `catalyst-functions/ragSearch.js`
- `catalyst-functions/generateResponse.js`

**Custom GPT:**
- `custom-gpt/openapi-spec.yaml` - Update URLs before importing
- `custom-gpt/instructions.md` - Copy to Custom GPT

**Documentation:**
- `README-SETUP.md` - Complete setup guide
- `DEPLOYMENT-CHECKLIST.md` - Track deployment progress
- `ZOHO-CATALYST-RESEARCH.md` - Architecture notes

---

## Security Notes

✅ **No secrets in code** - All credentials via `.env`  
✅ **`.gitignore` configured** - `.env` won't be committed  
✅ **API key authentication** - Custom GPT requires key  
✅ **Input validation** - All functions validate inputs  
✅ **Error handling** - Doesn't expose sensitive data

**Before deploying:**
1. Review `.env` file - ensure it's not in git
2. Generate strong API key (use `openssl rand -hex 32`)
3. Limit Zoho Desk token permissions to minimum required
4. Set up monitoring and alerts
5. Complete security review with your team

---

## Support & Documentation

**Setup Help:**
- Follow [README-SETUP.md](./README-SETUP.md) step-by-step

**Deployment:**
- Use [DEPLOYMENT-CHECKLIST.md](./DEPLOYMENT-CHECKLIST.md)

**Troubleshooting:**
- Check function logs in Catalyst Console
- Run `npm test` to validate config
- See README-SETUP.md troubleshooting section

**Platform Docs:**
- Zoho Catalyst: https://catalyst.zoho.com/help
- Supabase: https://supabase.com/docs
- OpenAI: https://platform.openai.com/docs

---

## Estimated Deployment Time

- **Configuration:** 30 minutes
- **Local testing:** 15 minutes
- **Catalyst deployment:** 30 minutes
- **Supabase setup:** 30 minutes (if using RAG)
- **Custom GPT config:** 15 minutes
- **Knowledge base indexing:** 1-2 hours (depends on volume)

**Total:** 3-4 hours for full deployment

---

## Cost Estimate

**Development/Testing:**
- Free tier sufficient for all services

**Production (Monthly):**
- Catalyst: $0-50
- Supabase: $0-25
- OpenAI: $20-100

**Total:** $20-175/month (typical: $30-50)

---

## Next Steps

1. Clone to your company repo ✅
2. Follow [README-SETUP.md](./README-SETUP.md)
3. Use [DEPLOYMENT-CHECKLIST.md](./DEPLOYMENT-CHECKLIST.md)
4. Train CSR team on Custom GPT usage
5. Monitor usage and costs for first week
6. Gather feedback and iterate

---

**Status:** Ready to clone and deploy with your company's credentials ✅

**Questions?** Review documentation or reach out to your development team.

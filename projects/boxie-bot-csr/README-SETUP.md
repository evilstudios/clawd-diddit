# Boxie Bot CSR - Setup Guide

Complete setup instructions for deploying to your company environment.

---

## Prerequisites

- Node.js 18+ installed
- Zoho Desk account with API access
- Zoho Catalyst account
- OpenAI API key
- Supabase account (for RAG, optional but recommended)

---

## Step 1: Clone and Install

```bash
# Clone this repo to your company environment
git clone <your-company-repo-url>
cd boxie-bot-csr

# Install dependencies
npm install
```

---

## Step 2: Configure Environment Variables

```bash
# Copy example env file
cp src/.env.example src/.env

# Edit .env with your actual credentials
nano src/.env
```

### Required Configuration:

#### Zoho Desk
1. Log into https://desk.zoho.com
2. Go to: **Settings → API → Generate Token**
3. Copy your Org ID from the URL: `desk.zoho.com/support/<ORG_ID>/`
4. Add to `.env`:
```bash
ZOHO_DESK_ORG_ID=your_actual_org_id
ZOHO_DESK_API_TOKEN=your_actual_api_token
```

#### OpenAI
1. Go to https://platform.openai.com/api-keys
2. Create new API key
3. Add to `.env`:
```bash
OPENAI_API_KEY=sk-your-actual-openai-key
```

#### Security API Key (for Custom GPT)
Generate a secure random string:
```bash
# On Mac/Linux
openssl rand -hex 32

# Or use any password generator
```
Add to `.env`:
```bash
API_KEY=your_generated_secure_key
```

---

## Step 3: Set Up Supabase (RAG - Optional)

### 3a. Create Supabase Project
1. Go to https://supabase.com
2. Create new project
3. Copy URL and keys from Settings → API

### 3b. Enable pgvector Extension
Run in Supabase SQL Editor:
```sql
-- Enable vector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Create documents table
CREATE TABLE documents (
  id BIGSERIAL PRIMARY KEY,
  document_id TEXT NOT NULL,
  chunk_index INTEGER NOT NULL,
  title TEXT NOT NULL,
  content TEXT NOT NULL,
  embedding vector(1536),
  metadata JSONB DEFAULT '{}'::jsonb,
  created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create index for vector similarity search
CREATE INDEX ON documents USING ivfflat (embedding vector_cosine_ops)
WITH (lists = 100);

-- Create similarity search function
CREATE OR REPLACE FUNCTION match_documents(
  query_embedding vector(1536),
  match_threshold float DEFAULT 0.7,
  match_count int DEFAULT 5
)
RETURNS TABLE (
  id bigint,
  document_id text,
  title text,
  content text,
  metadata jsonb,
  similarity float
)
LANGUAGE plpgsql
AS $$
BEGIN
  RETURN QUERY
  SELECT
    documents.id,
    documents.document_id,
    documents.title,
    documents.content,
    documents.metadata,
    1 - (documents.embedding <=> query_embedding) as similarity
  FROM documents
  WHERE 1 - (documents.embedding <=> query_embedding) > match_threshold
  ORDER BY documents.embedding <=> query_embedding
  LIMIT match_count;
END;
$$;
```

### 3c. Add Supabase to .env
```bash
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_ANON_KEY=your-anon-key
SUPABASE_SERVICE_KEY=your-service-role-key
```

---

## Step 4: Test Locally

```bash
# Test configuration
npm test

# Should output:
# ✅ Config loaded
# ✅ Zoho Desk connection working
# ✅ OpenAI connection working
# ✅ RAG enabled (if configured)
```

---

## Step 5: Deploy to Zoho Catalyst

### 5a. Install Catalyst CLI
```bash
npm install -g zoho-catalyst-cli
```

### 5b. Login to Catalyst
```bash
catalyst login
```

### 5c. Create Catalyst Project
```bash
# Create new project
catalyst init

# Project name: boxie-csr
# Select: Node.js 18
```

### 5d. Deploy Functions
```bash
# Deploy all functions
catalyst deploy

# Or deploy individually:
catalyst deploy:function searchTickets
catalyst deploy:function getTicketDetails
catalyst deploy:function ragSearch
catalyst deploy:function generateResponse
```

### 5e. Set Environment Variables in Catalyst
```bash
# Go to Catalyst Console → Settings → Environment Variables
# Add all variables from your .env file
```

---

## Step 6: Configure Custom GPT

### 6a. Create OpenAPI Spec
Your deployed Catalyst functions will be available at:
```
https://your-project.catalyst.zoho.com/baas/v1/functions/searchTickets/execute
https://your-project.catalyst.zoho.com/baas/v1/functions/getTicketDetails/execute
https://your-project.catalyst.zoho.com/baas/v1/functions/ragSearch/execute
https://your-project.catalyst.zoho.com/baas/v1/functions/generateResponse/execute
```

### 6b. Import to ChatGPT
1. Go to ChatGPT → Create Custom GPT
2. Upload `custom-gpt/openapi-spec.yaml` (update URLs with your Catalyst endpoints)
3. Copy instructions from `custom-gpt/instructions.md`
4. Configure authentication:
   - Type: API Key
   - Header: `X-API-Key`
   - Value: Your `API_KEY` from `.env`

---

## Step 7: Index Knowledge Base (RAG)

### Upload Documents
Use the provided script to index your SOPs and policies:

```bash
# Index a single document
node scripts/index-document.js \
  --file "./docs/refund-policy.pdf" \
  --title "Refund Policy" \
  --id "refund-policy-v1"

# Index a directory
node scripts/index-directory.js \
  --dir "./docs/policies" \
  --prefix "policy"
```

---

## Step 8: Test End-to-End

### Test in Custom GPT:
```
"Search for open tickets with high priority"
"Show me details for ticket #12345"
"What's our refund policy?"
"Generate a response for ticket #12345"
```

---

## Troubleshooting

### Issue: "ZOHO_DESK_API_TOKEN invalid"
- Regenerate token in Zoho Desk
- Ensure token has proper permissions
- Check orgId matches your Desk URL

### Issue: "RAG not configured"
- Verify Supabase credentials in `.env`
- Check pgvector extension is enabled
- Run the SQL setup script again

### Issue: "Custom GPT can't reach functions"
- Verify Catalyst function URLs are correct
- Check API key in Custom GPT matches `.env`
- Ensure functions are deployed (not just saved)

### Issue: "OpenAI API rate limit"
- Check your OpenAI usage dashboard
- Consider upgrading to higher tier
- Implement caching for embeddings

---

## Security Checklist

- [ ] `.env` file is NOT committed to git
- [ ] API keys are stored in Catalyst environment variables (not hardcoded)
- [ ] Custom GPT API key is strong (32+ characters)
- [ ] Zoho Desk token has minimum required permissions
- [ ] Supabase RLS policies are configured (optional, for multi-tenant)
- [ ] Functions validate all inputs
- [ ] Sensitive data is not logged

---

## Monitoring

### View Logs
```bash
# Catalyst CLI
catalyst logs --function searchTickets --tail

# Or in Catalyst Console
# Go to: Functions → [Function Name] → Logs
```

### Monitor Usage
- OpenAI: https://platform.openai.com/usage
- Supabase: Project Dashboard → Database → Usage
- Catalyst: Console → Analytics

---

## Cost Estimates

**Development (Free Tier):**
- Catalyst: Free tier (generous limits)
- Supabase: Free tier (500MB, 50,000 requests)
- OpenAI: Pay-per-use (~$5-10/month for testing)

**Production (Per Month):**
- Catalyst: $0-50 (likely stays in free tier)
- Supabase: $0-25 (free tier → paid if needed)
- OpenAI: $20-100 (depends on CSR usage)

**Total:** $20-175/month (typical: $30-50)

---

## Support

For issues specific to this implementation, contact your development team.

For Zoho Catalyst support: https://catalyst.zoho.com/help
For Supabase support: https://supabase.com/docs

---

## Next Steps

1. Test with sample tickets
2. Train CSR team on Custom GPT usage
3. Monitor usage and costs for first week
4. Gather feedback and iterate
5. Scale to full team

**Status:** Ready for company deployment ✅

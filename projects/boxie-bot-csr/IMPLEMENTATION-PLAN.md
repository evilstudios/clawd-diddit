# Boxie Bot CSR - Implementation Plan

**For Mitch:** Complete roadmap from spec → production

---

## Current Status

**What Exists:**
- ✅ Complete architecture documentation (86KB)
- ✅ Project summary and use cases
- ✅ Custom GPT setup guide
- ✅ Full technical specifications

**What's Missing:**
- ❌ Actual code implementation
- ❌ TypeScript source files
- ❌ Zoho Desk API client
- ❌ MCP server implementation
- ❌ RAG/vector DB integration
- ❌ OpenAPI spec file
- ❌ Custom GPT instructions
- ❌ Deployment configuration

**Status:** Documentation complete, code not started yet

---

## What Boxie Bot CSR Does

**Purpose:** AI-powered assistant for Customer Service Reps using Zoho Desk

**Core Functionality:**
1. **Ticket Management** - Search, view, update Zoho Desk tickets
2. **AI Response Generation** - Draft replies using past resolutions + RAG context
3. **Smart Summaries** - Quick ticket overview + recommended next steps
4. **Knowledge Base** - RAG-powered search across SOPs, policies, guidelines
5. **Similar Ticket Search** - Find how similar issues were resolved previously

**Integration Points:**
- **Zoho Desk** - Ticket system integration
- **OpenAI Embeddings** - Vector search for knowledge base
- **Custom GPT** - ChatGPT Actions interface
- **Vector DB** (Weaviate/Pinecone/Milvus) - Semantic search backend

---

## Implementation Phases

### Phase 1: Core MCP Server (Week 1)
**Goal:** Basic Zoho Desk integration without RAG

**Tasks:**
1. Initialize TypeScript project (tsconfig, package.json)
2. Build Zoho Desk API client
   - Authentication
   - Ticket CRUD operations
   - Thread/message retrieval
   - Search functionality
3. Implement MCP server with 6 core tools:
   - `searchTickets`
   - `getTicketDetails`
   - `getTicketThread`
   - `getSimilarResolvedTickets`
   - `generateResponseDraft` (basic, no RAG yet)
   - `summarizeAndNextSteps`
4. Create `.env.example` and configuration
5. Build and test locally

**Deliverables:**
- Working MCP server
- Zoho Desk integration tested
- Basic tool functionality verified

**Time Estimate:** 8-12 hours

---

### Phase 2: Custom GPT Integration (Week 1-2)
**Goal:** Connect Custom GPT to MCP server

**Tasks:**
1. Generate OpenAPI spec from MCP tools
2. Create Custom GPT instructions
3. Upload SOPs and policies as knowledge files
4. Configure ChatGPT Actions
5. Deploy MCP server to accessible endpoint
6. Test end-to-end with Custom GPT

**Deliverables:**
- Custom GPT configured and working
- OpenAPI spec file
- Deployment on production server
- Test cases validated

**Time Estimate:** 6-8 hours

---

### Phase 3: RAG Integration (Week 2-3)
**Goal:** Add vector database for dynamic knowledge retrieval

**Tasks:**
1. Set up vector database (recommend: Pinecone for simplicity)
2. Create embedding pipeline for SOPs/policies
3. Build `/rag/search` tool
4. Integrate RAG into `generateResponseDraft`
5. Optimize prompt injection with retrieved context
6. Test semantic search accuracy

**Deliverables:**
- Vector DB operational
- RAG search working
- Enhanced response generation
- Knowledge base indexed

**Time Estimate:** 12-16 hours

---

### Phase 4: Production Hardening (Week 3-4)
**Goal:** Security, monitoring, scalability

**Tasks:**
1. Add authentication layer (API keys)
2. Implement rate limiting
3. Set up logging and monitoring
4. Create error tracking (Sentry/similar)
5. Write deployment docs (Docker/Lambda)
6. Load testing
7. Create admin dashboard (optional)

**Deliverables:**
- Production-ready deployment
- Monitoring dashboards
- Security audit passed
- Documentation complete

**Time Estimate:** 10-12 hours

---

## Tech Stack Decisions

### Required
- **Runtime:** Node.js 18+
- **Language:** TypeScript 5.7+
- **Framework:** MCP SDK 1.0+
- **API Client:** Zoho Desk REST API v1
- **Embeddings:** OpenAI Embeddings API

### Vector DB Options (Pick One)
| Option | Pros | Cons | Cost |
|--------|------|------|------|
| **Pinecone** | Easiest setup, managed | Paid only | $70/mo starter |
| **Weaviate Cloud** | Great features, free tier | More complex | Free → $25/mo |
| **Supabase + pgvector** | Free PostgreSQL, simple | DIY setup | Free tier OK |

**Recommendation:** Start with **Supabase + pgvector** (free tier, easy to upgrade)

### Deployment Options (Pick One)
| Option | Pros | Cons | Cost |
|--------|------|------|------|
| **Fly.io** | Easy, free tier, persistent | Learning curve | Free → $5/mo |
| **Railway** | Dead simple, auto-deploy | Paid after trial | $5/mo |
| **AWS Lambda** | Serverless, scalable | Cold starts | Pay-per-use |
| **Digital Ocean** | Simple VM, full control | Manual setup | $6/mo |

**Recommendation:** **Railway** for fastest deployment, **Fly.io** for long-term

---

## Resource Requirements

### Zoho Desk
- API credentials (Org ID + API Token)
- Desk account with API access enabled
- Test tickets for development

### OpenAI
- API key for embeddings
- Estimated cost: $1-5/month for embeddings
- GPT-4 access for Custom GPT (ChatGPT Plus subscription)

### Vector Database
- Free tier sufficient for <100k vectors
- SOPs/policies likely <1k documents = <10k vectors

### Server
- 512MB RAM minimum
- 1GB recommended
- Free tier options available

---

## Quick Start Options

### Option A: Fast Track (Portifoy Builds It)
**Timeline:** 3-4 days (working hours)
**Your Time:** ~2 hours (provide credentials, test)

**Day 1-2:** Core MCP server + Zoho integration  
**Day 3:** Custom GPT setup + deployment  
**Day 4:** RAG integration + polish

**What I Need:**
1. Zoho Desk API credentials
2. OpenAI API key
3. Sample SOPs/policies to index
4. 30 min for testing/feedback

---

### Option B: Guided Build (You Build, I Guide)
**Timeline:** 1-2 weeks (your pace)
**Your Time:** 10-15 hours total

**I'll provide:**
- Step-by-step instructions
- Code templates and examples
- Troubleshooting support
- Review and feedback

---

### Option C: Hybrid (We Split It)
**Timeline:** 5-7 days
**Your Time:** 5-6 hours

**You handle:**
- Zoho API credentials setup
- Deployment configuration
- Testing and feedback

**I handle:**
- Core code implementation
- MCP server and tools
- RAG integration
- Documentation

---

## Next Steps (Pick One)

### If You Want Me to Build It:
1. Provide Zoho Desk credentials (`.env` format):
   ```
   ZOHO_DESK_ORG_ID=your_org_id
   ZOHO_DESK_API_TOKEN=your_token
   ```
2. Share OpenAI API key (or I'll use project key)
3. Provide 2-3 sample SOPs/policies to index
4. I'll have Phase 1 (core server) done in 24 hours

### If You Want to Build It Yourself:
1. I'll create starter templates + detailed guide
2. You work through implementation
3. I review and troubleshoot as needed

### If You're Not Sure Yet:
- I can build a **minimal proof-of-concept** (4 hours)
- Just basic Zoho integration + 2-3 tools
- You can test before committing to full build

---

## Cost Breakdown

**Development:** $0 (Portifoy does it)  
**APIs:**
- OpenAI Embeddings: $1-5/month
- Zoho Desk: Existing account (no extra cost)

**Infrastructure:**
- Vector DB: $0 (Supabase free tier)
- Server: $0-5/month (Railway/Fly.io free tier)

**Total Monthly:** $1-10/month

---

## Questions to Answer

Before starting, clarify:

1. **Who's the customer?**
   - Internal tool for your CSRs?
   - Product to sell to other companies?
   - Both?

2. **Zoho Desk setup?**
   - Do you have Zoho Desk account already?
   - What's your Desk org structure?
   - How many CSRs will use it?

3. **Timeline priority?**
   - Need it ASAP for customer demo?
   - Can build iteratively over weeks?
   - Just exploring feasibility?

4. **Build approach?**
   - Want me to build everything?
   - Prefer to learn and build yourself?
   - Hybrid approach?

---

**Status:** Ready to start. Just need direction from Mitch.

**Recommendation:** I build Phase 1 (core server) first as proof-of-concept. Takes 8 hours, costs $0, proves viability. Then decide on Phase 2-4.

---

**Next Action:** Mitch answers questions above → I start building

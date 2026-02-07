# Zoho Catalyst MCP + RAG Research & Implementation

**Date:** Feb 7, 2026  
**Purpose:** Research Zoho Catalyst's capabilities for MCP server hosting and RAG implementation

---

## Research Questions

### 1. MCP Server on Catalyst
- ✅ **Catalyst Functions** - Serverless functions (Node.js, Python, Java)
- ❓ Can Catalyst Functions expose MCP protocol endpoints?
- ❓ Does Catalyst have native MCP support or need custom implementation?
- ❓ How to deploy long-running MCP server vs serverless functions?

### 2. RAG on Catalyst
- ✅ **Catalyst DataStore** - Relational database (PostgreSQL-based)
- ❓ Does Catalyst have native vector database support?
- ❓ Can we use pgvector extension in Catalyst DataStore?
- ❓ Alternative: External vector DB (Pinecone/Weaviate) via Functions?

### 3. Zoho Desk Integration
- ✅ **Catalyst Functions** can call Zoho Desk API
- ✅ OAuth/API tokens handled within Zoho ecosystem
- ✅ Simplified auth since both are Zoho products

---

## Catalyst Architecture Options

### Option A: Catalyst Functions as MCP Tools (Recommended)

**Architecture:**
```
Custom GPT (OpenAI)
    ↓ (REST API calls via ChatGPT Actions)
Catalyst HTTP Functions
    ├─ searchTickets()
    ├─ getTicketDetails()
    ├─ generateResponse()
    └─ ragSearch()
        ↓
    Zoho Desk API
        ↓
    [External Vector DB: Pinecone/Supabase]
```

**Pros:**
- Serverless = zero infrastructure management
- Auto-scaling
- Simple HTTP endpoints (no complex MCP protocol)
- Easy to test and debug

**Cons:**
- Not true MCP protocol (but Custom GPT doesn't need it)
- Each function is stateless (need external state if needed)

**Implementation:**
1. Create Catalyst Functions for each tool
2. Expose as HTTP endpoints
3. Generate OpenAPI spec for Custom GPT Actions
4. Use external vector DB for RAG (Pinecone free tier)

---

### Option B: Catalyst AppSail + MCP Server

**Architecture:**
```
Custom GPT (OpenAI)
    ↓ (MCP protocol)
Catalyst AppSail (Node.js app)
    ├─ Full MCP Server
    ├─ WebSocket support
    └─ Persistent connections
        ↓
    Zoho Desk API
        ↓
    External Vector DB
```

**Pros:**
- True MCP protocol implementation
- Persistent server (can maintain state)
- More control over architecture

**Cons:**
- More complex setup
- Need to manage app lifecycle
- Overkill for this use case (Custom GPT uses REST, not MCP)

**Implementation:**
1. Deploy Node.js MCP server to Catalyst AppSail
2. Configure networking and persistence
3. Set up WebSocket support
4. More complex than needed for Custom GPT

---

## Recommended Approach: Hybrid

**What we'll build:**

### Phase 1: Catalyst Functions (Core Tools)
```javascript
// Catalyst Function: searchTickets
module.exports = async (catalystApp) => {
  const { status, priority, assignee } = catalystApp.request.query;
  
  // Call Zoho Desk API
  const tickets = await zohoDeskClient.searchTickets({
    status,
    priority,
    assignee
  });
  
  return tickets;
};
```

**Tools to implement as Catalyst Functions:**
1. `searchTickets` - Search Zoho Desk tickets
2. `getTicketDetails` - Get single ticket with full thread
3. `getSimilarTickets` - Find similar resolved tickets
4. `ragSearch` - Semantic search knowledge base
5. `generateResponse` - AI-powered draft generation

---

### Phase 2: RAG Implementation

**Vector Database Options:**

| Option | Pros | Cons | Cost |
|--------|------|------|------|
| **Supabase + pgvector** | Free tier, PostgreSQL, easy | DIY setup | Free |
| **Pinecone** | Purpose-built, managed | Paid only | $70/mo |
| **Catalyst DataStore + Custom** | All Zoho, no external deps | Need to build vector search | Free |

**Recommendation:** Start with **Supabase pgvector** (free tier)
- Catalyst Functions call Supabase API
- 500MB free storage = ~100k vectors
- Upgrade path available

**RAG Architecture:**
```
User Query → Catalyst Function
    ↓
Generate Embedding (OpenAI API)
    ↓
Query Supabase (pgvector semantic search)
    ↓
Retrieve top 5 relevant docs
    ↓
Inject into GPT prompt
    ↓
Return enhanced response
```

---

### Phase 3: Custom GPT Integration

**OpenAPI Spec Structure:**
```yaml
openapi: 3.1.0
info:
  title: Boxie CSR Assistant
  version: 1.0.0
servers:
  - url: https://your-catalyst-project.catalyst.zoho.com

paths:
  /searchTickets:
    post:
      operationId: searchTickets
      summary: Search Zoho Desk tickets
      # ... parameters

  /ragSearch:
    post:
      operationId: ragSearch
      summary: Search knowledge base
      # ... parameters
```

---

## Implementation Steps

### Step 1: Set Up Catalyst Project (1 hour)
1. Log into Catalyst console
2. Create new project: "boxie-csr"
3. Enable required services:
   - ✅ Functions (HTTP)
   - ✅ DataStore (for caching, optional)
   - ✅ Authentication (for Zoho Desk OAuth)

### Step 2: Create Zoho Desk Integration (2 hours)
1. Set up Zoho Desk API credentials
2. Create reusable Desk client module
3. Test basic ticket operations
4. Deploy as Catalyst Function

### Step 3: Build Core Tools (4 hours)
Create Catalyst Functions for:
- `searchTickets`
- `getTicketDetails`
- `getTicketThread`
- `getSimilarTickets`

Test each endpoint independently.

### Step 4: Set Up RAG Infrastructure (3 hours)
1. Create Supabase account (free)
2. Enable pgvector extension
3. Create embeddings table
4. Upload SOPs/policies
5. Generate embeddings via OpenAI
6. Test semantic search

### Step 5: Build RAG Function (2 hours)
1. Create `ragSearch` Catalyst Function
2. Connect to Supabase
3. Implement query → embedding → search flow
4. Return relevant context

### Step 6: Build Response Generator (2 hours)
1. Create `generateResponse` Function
2. Combine ticket data + RAG context
3. Call OpenAI API for draft generation
4. Return formatted response

### Step 7: Generate OpenAPI Spec (1 hour)
1. Document all functions
2. Create OpenAPI 3.1 spec
3. Test with Postman/Insomnia

### Step 8: Configure Custom GPT (1 hour)
1. Create Custom GPT in ChatGPT
2. Upload instructions
3. Import OpenAPI spec
4. Configure authentication (API key)
5. Test all tools

### Step 9: Upload Knowledge Base (2 hours)
1. Prepare SOPs and policies
2. Chunk documents (512 tokens each)
3. Generate embeddings
4. Insert into Supabase
5. Test RAG accuracy

### Step 10: Production Deployment (2 hours)
1. Set environment variables
2. Deploy all functions to production
3. Configure API keys
4. Set up monitoring
5. Create usage docs for CSRs

**Total Time:** 20 hours

---

## Cost Breakdown

### Development
- Catalyst: **$0** (generous free tier)
- Supabase: **$0** (free tier, 500MB)
- OpenAI API: **~$5/month** (embeddings + GPT calls)

### Production (per month)
- Catalyst Functions: **$0-10** (likely free tier covers it)
- Supabase: **$0-25** (free tier → paid if needed)
- OpenAI Embeddings: **$1-3** (one-time for knowledge base)
- OpenAI GPT calls: **$10-50** (depends on CSR usage)

**Total Monthly:** $11-88/month (likely $15-25 in practice)

---

## Questions for Mitch

### 1. Zoho Catalyst Access
- Do you already have Catalyst project set up?
- Can you create one and share project ID?
- Need admin access to deploy functions

### 2. Zoho Desk Credentials
- Org ID
- API token (or OAuth setup)
- Test account access for development

### 3. Knowledge Base Content
- What SOPs/policies exist?
- Format (PDFs, docs, text files)?
- Can you share 2-3 samples?

### 4. OpenAI API Key
- Use existing project key?
- Or create new one for this project?

### 5. Timeline Priority
- Need this ASAP for demo/customer?
- Or can build iteratively over 2-3 weeks?

---

## Next Actions

**Option 1: I Build Everything (Fastest)**
1. Mitch provides credentials (see above)
2. I build all Catalyst Functions
3. Set up RAG infrastructure
4. Create Custom GPT
5. Test and deploy
6. **Timeline:** 3-4 days (working hours)

**Option 2: We Split the Work**
1. Mitch sets up Catalyst project + credentials
2. I build the functions and RAG
3. Mitch tests with real Desk data
4. I configure Custom GPT
5. **Timeline:** 5-7 days

**Option 3: Proof of Concept First**
1. Build minimal version (1-2 tools + basic RAG)
2. Test feasibility
3. Decide on full build
4. **Timeline:** 8 hours → validate approach

---

## Technical Notes

### Catalyst Functions Limitations
- **Timeout:** 60 seconds per execution
- **Memory:** 512MB default, 2GB max
- **Concurrency:** Auto-scales
- **Cold starts:** ~200-500ms (acceptable)

### RAG Performance Targets
- Query latency: <2 seconds
- Embedding generation: ~100ms
- Vector search: ~50-200ms
- Context retrieval: <500ms

### Custom GPT Considerations
- Max 10 Actions (we need 5-6)
- Each action timeout: 45 seconds
- Response size: <100KB
- Authentication: API key or OAuth

---

**Status:** Research complete. Ready to start implementation pending Mitch's answers.

**Recommendation:** Option 1 (I build everything) is fastest. Need credentials to start.

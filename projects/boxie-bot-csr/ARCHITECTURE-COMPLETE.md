# Boxie AI CSR - Complete Architecture Documentation (RAG-Enhanced)

**Version:** 2.0.0 (RAG Integration)  
**Date:** February 4, 2026  
**Status:** RAG Implementation In Progress

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [System Architecture](#system-architecture)
3. [Component Architecture](#component-architecture)
4. [RAG Architecture](#rag-architecture)
   - [Zoho Catalyst Integration](#5-zoho-catalyst-integration-for-rag-new-section)
5. [Data Flow](#data-flow)
6. [API Endpoints](#api-endpoints)
7. [Security Architecture](#security-architecture)
8. [Scalability & Performance](#scalability--performance)
9. [Error Handling](#error-handling)
10. [Monitoring & Observability](#monitoring--observability)
11. [Deployment Architecture](#deployment-architecture)
12. [Future Enhancements](#future-enhancements)

---

## Executive Summary

Boxie AI CSR is an intelligent customer service representative assistant that integrates with Zoho Desk through a Model Context Protocol (MCP) Gateway. The system now includes RAG (Retrieval-Augmented Generation) for dynamic knowledge base retrieval, enabling CSRs to leverage AI-powered insights with real-time policy and SOP context while maintaining direct control and oversight.

### Key Capabilities
- **AI-Powered Assistance**: Generate response drafts and ticket summaries with RAG-injected context
- **Zoho Desk Integration**: Real-time access to tickets and customer data
- **RAG-Enhanced Knowledge Retrieval**: Dynamic context retrieval from vector database for policies, SOPs, and guidelines
- **Multi-Tool Support**: 8+ specialized tools (now including /rag/search) for different CSR workflows
- **Custom GPT Integration**: Seamless ChatGPT Actions integration with RAG support
- **Vector Database**: Semantic search across knowledge base documents
- **Enterprise Security**: Type-safe TypeScript with comprehensive error handling and PII protection

---

## System Architecture

### High-Level Architecture Diagram (RAG-Enhanced)

```
┌─────────────────────────────────────────────────────────────────┐
│                         Custom GPT (ChatGPT)                     │
│                      for CSR Copilot Assistance                  │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  Lightweight Instructions (Focused)                    │    │
│  │  • CSR behavior guidelines                             │    │
│  │  • Role & communication standards                      │    │
│  │  • RAG Integration Instructions                        │    │
│  └────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  Dynamic Context (Retrieved Via RAG)                   │    │
│  │  • Policies & SOPs (from vector DB)                    │    │
│  │  • Company Guidelines                                  │    │
│  │  • Real-time, policy-current information              │    │
│  └────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐    │
│  │  Actions (OpenAPI Specification)                       │    │
│  │  • Tool Integration Endpoints                          │    │
│  │  • NEW: /rag/search endpoint for knowledge base       │    │
│  │  • Request/Response Schemas                            │    │
│  └────────────────────────────────────────────────────────┘    │
│                                                                  │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                    HTTPS/REST API Calls
                           │
    (Tools: searchTickets, getTicket, /rag/search, etc.)
                           │
         ┌─────────────────┴──────────────────┐
         │                                    │
         ▼                                    ▼
    ┌─────────────────┐        ┌────────────────────────┐
    │  MCP Gateway    │        │  RAG Integration       │
    │  (Standard)     │        │  (Vector DB Queries)   │
    └────────┬────────┘        └────────┬───────────────┘
             │                         │
             │                Embedding Query
             │                         │
             │                         ▼
             │              ┌──────────────────────┐
             │              │  OpenAI Embeddings   │
             │              │  API (Inference)     │
             │              └──────────┬───────────┘
             │                         │
             │                    Vector
             │                         │
             │                    ┌────▼──────────────┐
             │                    │ Vector Database   │
             │                    │ (Weaviate/        │
             │                    │  Pinecone/Milvus) │
             │                    │ • Knowledge base  │
             │                    │ • Embeddings      │
             │                    │ • Metadata        │
             │                    └─────┬─────────────┘
             │                          │
             │ ┌────────────────────────┘
             │ │
             ▼ ▼
    ┌──────────────────────────────────────┐
    │  MCP Gateway Server Unified           │
    │  (Node.js 18+ / TypeScript)           │
    │                                       │
    │  ┌──────────────────────────────┐    │
    │  │ Express & Middleware          │    │
    │  │ • Auth, Rate Limit, Logging  │    │
    │  └──────────────────────────────┘    │
    │                                       │
    │  ┌──────────────────────────────┐    │
    │  │ MCP Router & Handlers         │    │
    │  │ • Ticket handlers             │    │
    │  │ • NEW: /rag/search handler   │    │
    │  │ • Query cache (LRU)           │    │
    │  └──────────────────────────────┘    │
    │                                       │
    │  ┌──────────────────────────────┐    │
    │  │ Service Clients               │    │
    │  │ • Zoho Desk Client            │    │
    │  │ • Zoho KB Client              │    │
    │  │ • NEW: Vector DB Client       │    │
    │  │ • Internal Docs Client        │    │
    │  └──────────────────────────────┘    │
    │                                       │
    │  ┌──────────────────────────────┐    │
    │  │ RAG Pipeline Components       │    │
    │  │ • Query embedding             │    │
    │  │ • Similarity search           │    │
    │  │ • Result ranking & filtering  │    │
    │  │ • Context injection           │    │
    │  └──────────────────────────────┘    │
    │                                       │
    └──────────┬───────────────────────────┘
               │
    REST API / OAuth2
               │
    ┌──────────┴──────────┐
    │                     │
    ▼                     ▼
Zoho Desk API         Zoho Desk Database
(Real-time data)      (Records & History)
```

---

## RAG Architecture

### RAG Components Overview

The RAG (Retrieval-Augmented Generation) system enhances the MCP Gateway with semantic search capabilities for dynamic knowledge base retrieval. Instead of static document uploads to Custom GPT, the system dynamically fetches relevant documents based on CSR queries.

### RAG Pipeline

```
Phase 1: DOCUMENT INGESTION (One-time, with updates)
┌──────────────────────────────────────────────────┐
│  Knowledge Base Documents                        │
│  • docs/sop.md (Standard Operating Procedures)  │
│  • docs/policies.md (Customer Service Policies) │
│  • docs/use-cases.md (Business Use Cases)       │
│  • Custom knowledge articles                     │
└──────────┬───────────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────────────────┐
│  Document Chunking & Preprocessing               │
│  • Split by headers (H1, H2, H3)                 │
│  • ~500-1000 tokens per chunk                    │
│  • 100-token overlap between chunks              │
│  • Metadata extraction (source, section, date)   │
└──────────┬───────────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────────────────┐
│  Embedding Generation                            │
│  • OpenAI text-embedding-3-small (1536 dims)    │
│  • Batch processing for efficiency               │
│  • Cached embeddings                             │
└──────────┬───────────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────────────────┐
│  Vector Database Population                      │
│  • Store vectors + metadata                      │
│  • Create similarity indices                     │
│  • Document version tracking                     │
└──────────────────────────────────────────────────┘

Phase 2: RUNTIME RETRIEVAL (Every query)
┌──────────────────────────────────────────────────┐
│  User Query (from Custom GPT)                    │
│  "What's our refund policy for opened products?"│
└──────────┬───────────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────────────────┐
│  Query Embedding                                 │
│  • Convert query to vector                       │
│  • Same model as document embeddings             │
│  • Cached for frequent queries                   │
└──────────┬───────────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────────────────┐
│  Similarity Search (Vector DB)                   │
│  • Cosine similarity calculation                 │
│  • Top-K retrieval (default: 5)                  │
│  • Metadata filtering (by source, date)          │
│  • Relevance scoring                             │
└──────────┬───────────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────────────────┐
│  Result Ranking & Filtering                      │
│  • Sort by relevance score                       │
│  • Filter by threshold (>0.6 default)            │
│  • Deduplication                                 │
│  • Metadata enrichment                           │
└──────────┬───────────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────────────────┐
│  Context Injection                               │
│  • Format retrieved documents                    │
│  • Include source & section info                 │
│  • Prepare for Custom GPT consumption            │
│  • Preserve formatting & links                   │
└──────────┬───────────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────────────────┐
│  Response to Custom GPT                          │
│  {                                               │
│    "query": "refund policy...",                  │
│    "results": [                                  │
│      {                                           │
│        "chunk": "Unopened products: full...",   │
│        "source": "policies.md",                  │
│        "section": "Returns > Refunds",          │
│        "score": 0.94,                           │
│        "date": "2026-02-01"                      │
│      },                                          │
│      ...                                         │
│    ]                                             │
│  }                                               │
└──────────────────────────────────────────────────┘
```

### Vector Database Schema

```
Collection: "knowledge_base"
├─ id (UUID)
├─ content (Text - chunk content)
├─ embedding (Vector - 1536 dimensions)
├─ source (Enum: sop | policies | use_cases | custom)
├─ section (String - breadcrumb: "H1 > H2 > H3")
├─ created_date (DateTime - ISO 8601)
├─ last_updated (DateTime - ISO 8601)
├─ version (Integer - document version)
├─ chunk_index (Integer - position in document)
├─ relevance_tags (Array[String] - keywords)
└─ metadata (Object - custom fields)
```

### RAG Service Client

```typescript
// New service: src/services/ragClient.ts

Interface: RAGSearchRequest
├─ query: string (search query)
├─ limit?: number (default: 5, max: 10)
├─ source_filter?: string[] (filter by sources)
├─ date_range?: { start: Date, end: Date }
└─ relevance_threshold?: number (default: 0.6)

Interface: RAGSearchResult
├─ id: string (chunk ID)
├─ chunk: string (document excerpt)
├─ source: string (sop | policies | etc.)
├─ section: string (breadcrumb path)
├─ relevance_score: number (0-1)
├─ created_date: string (ISO 8601)
├─ last_updated: string (ISO 8601)
└─ metadata: object

Interface: RAGSearchResponse
├─ query: string
├─ results: RAGSearchResult[]
├─ execution_time_ms: number
├─ query_embedding_model: string
└─ cache_hit: boolean
```

### Caching Strategy for RAG

```
LRU Cache Configuration:
├─ Max size: 1000 entries
├─ TTL: 3600 seconds (1 hour)
├─ Cache key: hash(query + filters)
├─ Hit ratio target: 60-70%

Cache Invalidation:
├─ Time-based: 1 hour expiration
├─ Event-based: When documents update
├─ Manual: Admin API endpoint
└─ Partial: Invalidate related queries on update
```

### Document Ingestion Pipeline

```
Automated Ingestion:
├─ Scheduled Job (runs every 6 hours)
├─ Monitors doc files for changes
├─ Detects new/updated documents
├─ Chunks and embeds new content
├─ Updates vector database
└─ Logs ingestion events

Manual Ingestion:
├─ Admin endpoint: POST /admin/rag/ingest
├─ Force re-index documents
├─ Useful after batch updates
└─ Returns status and stats
```

### 1. Custom GPT Layer

**Purpose:** Provides natural language interface for CSRs

**Components:**
- **Static Instructions** (`custom-gpt/instructions.md`)
  - Behavior guidelines and personality
  - Role definition and responsibilities
  - Communication standards
  - Error handling instructions

- **Knowledge Base Documents**
  - Standard Operating Procedures (docs/sop.md)
  - Customer Service Policies (docs/policies.md)
  - Company Guidelines and Standards
  - Provides context for AI responses

- **Actions (OpenAPI)**
  - Tool definitions matching MCP handlers
  - Request/response schemas
  - Authentication configuration
  - Error response schemas

**Data Flow:**
- User inputs query/instruction
- GPT processes with context from knowledge base
- GPT selects appropriate tool(s)
- GPT formats request per OpenAPI spec
- GPT sends HTTPS request to MCP Gateway

### 2. MCP Gateway Layer (Enhanced with RAG)

**Purpose:** Bridge application logic between Custom GPT and Zoho Desk, with RAG-powered knowledge retrieval

**Technology Stack:**
- Node.js 18+ runtime
- TypeScript for type safety
- Express.js for HTTP server
- MCP SDK for message handling
- Axios for HTTP requests
- Pino for structured logging
- **NEW**: Vector DB Client (Weaviate/Pinecone SDK)
- **NEW**: Embedding Client (OpenAI SDK)
- **NEW**: Query Cache (Node-cache or Redis)

**Sub-Components:**

#### a. Server & Middleware Stack

```typescript
Request Flow:
1. Request enters Express → Helmet (security headers)
2. → Body Parser (JSON parsing)
3. → Pino Logger (request logging)
4. → Request ID Middleware (tracking)
5. → Authentication Middleware (API key validation)
6. → Rate Limiter Middleware (request throttling)
7. → Route Handler (endpoint processing)
8. → Error Handler (standardized error responses)
9. → Response sent to client
```

**Middleware Components:**

| Middleware | Purpose | Config |
|-----------|---------|--------|
| Helmet | Security headers | Automatic |
| Body Parser | JSON parsing | 100kb limit |
| Pino Logger | Request logging | Structured JSON |
| Request ID | Request tracking | UUID generation |
| Authentication | API key validation | Query/Header mode |
| Rate Limiter | Request throttling | Configurable limits |
| Error Handler | Error standardization | HTTP status mapping |

#### b. MCP Router & Message Handler (RAG-Aware)

```typescript
Message Handler Flow:
1. Receive POST /mcp/message request
2. Validate against messageRequestSchema
3. Extract operationId and arguments
4. Route to appropriate handler function:
   - Standard handlers: searchTickets, getTicket, etc.
   - NEW RAG handler: /rag/search for knowledge queries
5. Handler executes business logic
6. For RAG queries:
   a) Check cache for similar queries
   b) Embed user query
   c) Search vector database
   d) Format and return results
7. Return standardized MessageResponse
8. Client receives JSON response with RAG context
```

**Handler Functions:**
- `searchTicketsHandler` - Search with filters
- `getTicketHandler` - Retrieve single ticket details
- `getTicketThreadsHandler` - Get conversation history
- `getSimilarResolvedTicketsHandler` - Find similar resolved cases
- `generateResponseDraftHandler` - AI response generation
- `summarizeAndNextStepsHandler` - Ticket summary
- `getContactHandler` - Customer information
- **NEW**: `ragSearchHandler` - Vector database semantic search

#### c. Service Clients (Including RAG)

**Zoho Desk Client** (`src/services/zohoDeskClient.ts`)
```
Responsibilities:
├── Authentication
│   ├── Token management
│   └── Credential validation
├── Ticket Operations
│   ├── Search with filters
│   ├── Get ticket details
│   ├── Get threads/messages
│   ├── Update ticket status
│   └── Add comments
├── Contact Operations
│   ├── Search contacts
│   ├── Get contact details
│   └── Retrieve customer info
└── Error Handling
    ├── Retry logic for transient failures
    ├── Rate limit handling
    └── Auth failure recovery
```

**Vector Database Client** (`src/services/ragClient.ts`) **[NEW]**
```
Responsibilities:
├── Connection Management
│   ├── Connection pooling
│   ├── Reconnection logic
│   └── Health checks
├── Query Operations
│   ├── Semantic search
│   ├── Vector similarity
│   ├── Metadata filtering
│   └── Result ranking
├── Ingestion Pipeline
│   ├── Document chunking
│   ├── Embedding generation
│   ├── Batch insertion
│   └── Version management
└── Performance
    ├── Query caching (LRU)
    ├── Batch operations
    └── Connection pooling
```

**Embedding Client** (`src/services/embeddingClient.ts`) **[NEW]**
```
Responsibilities:
├── Embedding Generation
│   ├── Single query embeddings
│   ├── Batch embeddings
│   ├── Caching
│   └── Error handling
├── Model Management
│   ├── OpenAI API integration
│   ├── Token counting
│   └── Cost tracking
└── Quality Assurance
    ├── Embedding validation
    ├── Dimension verification
    └── Format checking
```

**Zoho Knowledge Base Client** (`src/services/zohoKBClient.ts`)
```
Responsibilities:
├── Article Search
│   ├── Full-text search
│   ├── Category filtering
│   └── Relevance ranking
├── Article Details
│   ├── Content retrieval
│   ├── Metadata parsing
│   └── Link extraction
└── Performance
    ├── Search caching
    └── Result pagination
```

**Internal Docs Client** (`src/services/internalDocs.ts`)
```
Responsibilities:
├── Document Search
│   ├── In-memory search
│   ├── SOP lookup
│   └── Policy reference
└── Data Management
    ├── Document indexing
    ├── Metadata tracking
    └── Version management
```

#### d. RAG Pipeline Components **[NEW]**

**Document Processor** (`src/services/rag/documentProcessor.ts`)
```
Responsibilities:
├── Document Parsing
│   ├── Markdown parsing
│   ├── Header extraction
│   └── Metadata parsing
├── Chunking
│   ├── Smart splitting by headers
│   ├── Size normalization
│   └── Overlap management
└── Versioning
    ├── Document version tracking
    ├── Change detection
    └── Update queuing
```

**Query Processor** (`src/services/rag/queryProcessor.ts`)
```
Responsibilities:
├── Query Enhancement
│   ├── Tokenization
│   ├── Stop word removal
│   └── Spelling correction
├── Embedding Generation
│   ├── Query vector creation
│   ├── Caching
│   └── Batch processing
└── Optimization
    ├── Query expansion
    ├── Intent detection
    └── Filter suggestion
```

**Result Ranker** (`src/services/rag/resultRanker.ts`)
```
Responsibilities:
├── Relevance Scoring
│   ├── Cosine similarity
│   ├── Metadata scoring
│   └── Recency weighting
├── Filtering
│   ├── Threshold filtering
│   ├── Deduplication
│   └── Source filtering
└── Presentation
    ├── Result formatting
    ├── Snippet extraction
    └── Metadata enrichment
```

**Cache Manager** (`src/services/rag/cacheManager.ts`)
```
Responsibilities:
├── Query Cache
│   ├── LRU eviction
│   ├── TTL management
│   └── Cache statistics
├── Invalidation
│   ├── Time-based expiration
│   ├── Event-based invalidation
│   └── Partial updates
└── Monitoring
    ├── Hit ratio tracking
    ├── Performance metrics
    └── Cost analysis
```

#### e. Utilities

- **HTTP Client** (`src/utils/http.ts`)
  - Axios instance with retry logic
  - Exponential backoff for failures
  - Circuit breaker pattern ready
  - Timeout configuration

- **Response Normalization** (`src/utils/normalize.ts`)
  - Consistent field naming
  - Data type conversion
  - Field extraction/mapping
  - Empty value handling

- **Data Sanitization** (`src/utils/sanitize.ts`)
  - PII masking for logs
  - Email obfuscation
  - Phone number masking
  - Sensitive field removal

- **RAG Utilities** (`src/utils/rag.ts`) **[NEW]**
  - Chunk formatting
  - Context injection
  - Metadata formatting
  - Score calculation

### 3. Zoho Desk Integration Layer

**Purpose:** Direct integration with Zoho Desk API

**Authentication:**
- OAuth 2.0 with refresh token
- API token management
- Session handling

**API Endpoints Used:**
```
GET  /tickets                    - List tickets
GET  /tickets/{id}              - Get ticket details
GET  /tickets/{id}/threads      - Get conversation
POST /tickets/{id}/threads      - Add comment
GET  /contacts                  - Search contacts
GET  /contacts/{id}             - Get contact details
GET  /search                    - Full-text search
GET  /departments               - Get departments
```

### 4. Vector Database Layer **[NEW]**

**Purpose:** Store and retrieve embeddings for semantic search

**Technology Options:**
- **Weaviate**: Open-source, deployed on Zoho Catalyst
- **Pinecone**: Managed service (cloud-based)
- **Milvus**: Open-source, high performance

**Connection Architecture:**
```
MCP Gateway
    ↓
Vector DB Client (SDK)
    ├─ Connection pooling
    ├─ Retry logic
    └─ Circuit breaker
    ↓
Vector Database Server
    ├─ Weaviate REST API (port 8080)
    ├─ Authentication (API key)
    └─ HTTPS encryption
```

**Data Storage:**
```
Database Structure:
├─ knowledge_base collection
│  ├─ Documents (vectors + metadata)
│  ├─ Indices (for fast retrieval)
│  └─ Configuration
└─ Document metadata
   ├─ Source information
   ├─ Version tracking
   └─ Update timestamps
```

### 5. Zoho Catalyst Integration for RAG **[NEW SECTION]**

**Purpose:** Leverage Zoho Catalyst ecosystem for serverless RAG infrastructure, keeping all data within the Zoho ecosystem

**Why Zoho Catalyst for RAG?**
- 🔗 **Native Integration**: Direct access to Zoho Desk knowledge base and data
- 🚀 **Serverless**: Pay-per-execution, automatic scaling, no infrastructure management
- 💰 **Cost-Effective**: Only pay for actual function invocations and vector store queries
- 🔐 **Security**: Inherits Zoho's enterprise security and compliance
- ⚡ **Performance**: Low-latency access to Zoho data within the same ecosystem
- 📊 **Unified Monitoring**: Single dashboard for logs, metrics, and performance

#### a. Catalyst Vector Store **[NEW]**

**Component:** `src/services/catalystVectorClient.ts`

**Purpose:** Interface to Zoho Catalyst's vector database for semantic search

```typescript
// Configuration
interface CatalystVectorConfig {
  projectId: string;          // Zoho Catalyst project ID
  tableId: string;            // Vector database table ID
  apiKey: string;             // Catalyst API key
  region: string;             // us | eu | in
  functionUrl: string;        // Catalyst function endpoint
  batchSize: number;          // Batch insertion size (default: 100)
  maxConnections: number;     // Connection pool size (default: 10)
}

// Catalyst Vector Table Schema
interface VectorRecord {
  id: string;                 // UUID: chunk-{source}-{docId}-{chunkIndex}
  content: string;            // Document chunk text
  embedding: number[];        // 1536-dimensional vector (OpenAI)
  source: string;             // sop | policies | use_cases | zoho_kb | custom
  section: string;            // Breadcrumb path (H1 > H2 > H3)
  created_date: string;       // ISO 8601 timestamp
  last_updated: string;       // ISO 8601 timestamp
  version: number;            // Document version for tracking updates
  chunk_index: number;        // Position in document (for context)
  relevance_tags: string[];   // Keywords for faceted search
  metadata: {
    documentId?: string;      // Source document identifier
    articleUrl?: string;      // URL for Zoho KB articles
    author?: string;          // Document author
    department?: string;      // Relevant department
    customFields?: Record<string, any>;
  }
}

// Client Methods
class CatalystVectorClient {
  // Connection and health
  async connect(): Promise<void>;
  async healthCheck(): Promise<boolean>;
  async disconnect(): Promise<void>;

  // Upsert operations
  async upsertEmbedding(record: VectorRecord): Promise<string>;
  async batchUpsert(records: VectorRecord[]): Promise<string[]>;
  
  // Query operations
  async semanticSearch(
    query: string,
    embedding: number[],
    options: {
      limit?: number;           // Default: 5, Max: 10
      threshold?: number;       // Min similarity (0-1), Default: 0.6
      sources?: string[];       // Filter by sources
      dateRange?: { start: Date; end: Date };
    }
  ): Promise<SearchResult[]>;

  // Document management
  async deleteBySource(source: string): Promise<number>;
  async deleteById(id: string): Promise<boolean>;
  async getDocumentVersions(documentId: string): Promise<DocumentVersion[]>;
  async updateDocumentVersion(documentId: string, newVersion: number): Promise<void>;

  // Analytics
  async getStorageStats(): Promise<StorageStats>;
  async getQueryStats(timeRange: string): Promise<QueryStats>;
}
```

#### b. Catalyst Serverless Functions **[NEW]**

**Components:** Catalyst Functions deployed in your Zoho project

**Function 1: Document Ingestion** (Scheduled every 6 hours)

```typescript
// Catalyst Function: /ingestDocuments
// Trigger: Scheduled (6-hour interval)
// Timeout: 300 seconds
// Memory: 512 MB

export async function ingestDocuments(context) {
  const logger = context.logger;
  const stats = { processed: 0, inserted: 0, failed: 0 };

  try {
    // 1. Define documents to ingest
    const docSources = [
      { path: 'docs/policies.md', source: 'policies', type: 'markdown' },
      { path: 'docs/sop.md', source: 'sop', type: 'markdown' },
      { path: 'docs/use-cases.md', source: 'use_cases', type: 'markdown' },
    ];

    // 2. Fetch Zoho KB articles
    const kbArticles = await getZohoKBArticles();
    docSources.push(...kbArticles.map(article => ({
      path: article.id,
      source: 'zoho_kb',
      type: 'zoho_kb',
      metadata: {
        articleUrl: article.webUrl,
        title: article.title,
        updatedTime: article.modifiedTime
      }
    })));

    // 3. Process each document
    for (const docSource of docSources) {
      try {
        // Load document content
        const content = await loadDocument(docSource);
        
        // Chunk the document
        const chunks = chunkDocument(content, {
          chunkSize: 500,
          overlap: 100,
          headingStrategy: 'smart'
        });

        stats.processed += chunks.length;

        // 4. Generate embeddings and insert into Catalyst
        for (const chunk of chunks) {
          try {
            const embedding = await openaiClient.embed(chunk.content);
            
            const record = {
              id: `chunk-${docSource.source}-${chunk.docId}-${chunk.index}`,
              content: chunk.content,
              embedding: embedding,
              source: docSource.source,
              section: chunk.breadcrumb,
              created_date: new Date().toISOString(),
              last_updated: new Date().toISOString(),
              version: 1,
              chunk_index: chunk.index,
              relevance_tags: extractKeywords(chunk.content),
              metadata: {
                documentId: docSource.path,
                ...docSource.metadata
              }
            };

            // Upsert into Catalyst vector store
            await catalystVector.upsertEmbedding(record);
            stats.inserted++;
          } catch (chunkError) {
            logger.error('Chunk processing failed', { error: chunkError, docId: docSource.path });
            stats.failed++;
          }
        }
      } catch (docError) {
        logger.error('Document processing failed', { error: docError, path: docSource.path });
      }
    }

    logger.info('Ingestion complete', stats);
    return {
      success: true,
      message: `Ingested ${stats.inserted} chunks from ${stats.processed} chunks`,
      stats
    };
  } catch (error) {
    logger.error('Ingestion function failed', { error });
    throw error;
  }
}

// Helper: Load document from file or API
async function loadDocument(docSource) {
  if (docSource.type === 'markdown') {
    // Load from repository file system
    return await readFile(docSource.path);
  } else if (docSource.type === 'zoho_kb') {
    // Fetch from Zoho Desk Knowledge Base API
    return await zohoDeskClient.getKBArticle(docSource.path);
  }
}

// Helper: Smart document chunking
function chunkDocument(content, options) {
  const chunks = [];
  const lines = content.split('\n');
  let currentChunk = '';
  let breadcrumb = '';

  for (const line of lines) {
    // Track headers for breadcrumb
    if (line.startsWith('#')) {
      breadcrumb = extractHeadingPath(line, breadcrumb);
    }

    currentChunk += line + '\n';

    // Split when chunk reaches size threshold
    if (currentChunk.length >= options.chunkSize) {
      chunks.push({
        content: currentChunk.trim(),
        breadcrumb,
        index: chunks.length
      });
      // Keep overlap
      currentChunk = currentChunk.slice(-options.overlap);
    }
  }

  // Add remaining content
  if (currentChunk.trim()) {
    chunks.push({
      content: currentChunk.trim(),
      breadcrumb,
      index: chunks.length
    });
  }

  return chunks;
}
```

**Function 2: Semantic Search Query Handler**

```typescript
// Catalyst Function: /queryRAG
// Trigger: HTTP POST
// Timeout: 30 seconds
// Memory: 256 MB

export async function queryRAG(context, request) {
  const { query, limit = 5, filters = {}, includeMetadata = true } = request.body;
  const startTime = Date.now();

  try {
    // 1. Validate request
    if (!query || query.trim().length === 0) {
      return createResponse(400, {
        error: 'Query is required',
        code: 'INVALID_QUERY'
      });
    }

    // 2. Check cache (optional, using Catalyst caching)
    const cacheKey = `rag-query:${hash(JSON.stringify({ query, filters }))}`;
    const cached = await getFromCache(cacheKey);
    if (cached) {
      return createResponse(200, {
        ...cached,
        fromCache: true
      });
    }

    // 3. Generate embedding for query
    const queryEmbedding = await openaiClient.embed(query);

    // 4. Search vector database with filters
    const searchOptions = {
      limit: Math.min(limit, 10),
      threshold: filters.relevanceThreshold || 0.6,
      sources: filters.sourceFilter || undefined,
      dateRange: filters.dateRange || undefined
    };

    const rawResults = await catalystVector.semanticSearch(
      query,
      queryEmbedding,
      searchOptions
    );

    // 5. Format and enrich results
    const results = rawResults.map(result => ({
      id: result.id,
      chunk: result.content,
      source: result.source,
      section: result.section,
      relevance_score: result.similarity_score,
      created_date: result.created_date,
      last_updated: result.last_updated,
      metadata: includeMetadata ? result.metadata : undefined
    }));

    // 6. Cache results
    const response = {
      success: true,
      query,
      results,
      total: results.length,
      executionTime: Date.now() - startTime,
      embeddingModel: 'text-embedding-3-small'
    };

    await setInCache(cacheKey, response, 3600); // Cache for 1 hour

    return createResponse(200, response);
  } catch (error) {
    context.logger.error('RAG query failed', { error, query });
    return createResponse(500, {
      error: 'RAG search failed',
      code: 'SEARCH_ERROR',
      requestId: context.requestId
    });
  }
}

// Helper: Create HTTP response
function createResponse(statusCode, body) {
  return {
    statusCode,
    headers: {
      'Content-Type': 'application/json',
      'X-Response-Time': Date.now()
    },
    body: JSON.stringify(body)
  };
}

// Helper: Caching (using Catalyst Tables or Redis)
async function getFromCache(key) {
  // Implement using Catalyst's caching layer or external Redis
  // Return null if not found
}

async function setInCache(key, value, ttl) {
  // Implement using Catalyst's caching layer or external Redis
}
```

**Function 3: Document Update Handler** (Triggered by webhooks)

```typescript
// Catalyst Function: /onDocumentUpdate
// Trigger: Webhook (when docs are updated in repository)
// Timeout: 120 seconds
// Memory: 512 MB

export async function onDocumentUpdate(context, request) {
  const { documentId, path, action } = request.body;

  try {
    if (action === 'deleted') {
      // Delete all chunks for this document
      const count = await catalystVector.deleteBySource(path);
      context.logger.info(`Deleted ${count} chunks for ${path}`);
    } else if (action === 'updated' || action === 'created') {
      // Re-ingest the document
      const content = await loadDocument({ path, source: getSourceFromPath(path) });
      const chunks = chunkDocument(content, { chunkSize: 500, overlap: 100 });

      let inserted = 0;
      for (const chunk of chunks) {
        const embedding = await openaiClient.embed(chunk.content);
        await catalystVector.upsertEmbedding({
          id: `chunk-${getSourceFromPath(path)}-${documentId}-${chunk.index}`,
          content: chunk.content,
          embedding,
          source: getSourceFromPath(path),
          section: chunk.breadcrumb,
          created_date: new Date().toISOString(),
          last_updated: new Date().toISOString(),
          version: 2,
          chunk_index: chunk.index,
          relevance_tags: extractKeywords(chunk.content),
          metadata: { documentId, path }
        });
        inserted++;
      }

      // Invalidate related queries in cache
      await invalidateRelatedQueries(path);

      return {
        success: true,
        message: `Updated ${inserted} chunks for ${path}`
      };
    }
  } catch (error) {
    context.logger.error('Document update failed', { error, documentId });
    throw error;
  }
}
```

#### c. MCP Gateway RAG Handler Update **[UPDATED]**

**File:** `src/mcp/handlers/ragSearch.ts`

```typescript
import axios from 'axios';
import { logger } from '@/middleware/logging';
import { AppError } from '@/utils/errors';
import { LRUCache } from 'lru-cache';

// In-memory cache for query results (optional, complements Catalyst cache)
const queryCache = new LRUCache<string, RAGSearchResponse>({
  max: 1000,
  ttl: 1000 * 3600  // 1 hour
});

export interface RAGSearchArgs {
  query: string;
  limit?: number;
  source_filter?: string[];
  relevance_threshold?: number;
  include_metadata?: boolean;
}

export interface RAGSearchResponse {
  query: string;
  results: Array<{
    id: string;
    chunk: string;
    source: string;
    section: string;
    relevance_score: number;
    created_date: string;
    last_updated: string;
    metadata?: Record<string, any>;
  }>;
  total: number;
  executionTimeMs: number;
  cacheHit: boolean;
}

export async function ragSearchHandler(args: RAGSearchArgs): Promise<RAGSearchResponse> {
  const { query, limit = 5, source_filter, relevance_threshold, include_metadata = true } = args;

  // 1. Input validation
  if (!query || query.trim().length === 0) {
    throw new AppError('Query cannot be empty', 'INVALID_QUERY');
  }

  if (query.length > 500) {
    throw new AppError('Query exceeds maximum length of 500 characters', 'QUERY_TOO_LONG');
  }

  // 2. Check local cache
  const cacheKey = JSON.stringify({ query: query.toLowerCase(), source_filter, relevance_threshold });
  const cachedResult = queryCache.get(cacheKey);

  if (cachedResult) {
    logger.debug('RAG query cache hit', { query: query.substring(0, 50) });
    return { ...cachedResult, cacheHit: true };
  }

  const startTime = Date.now();

  try {
    // 3. Call Catalyst serverless function
    const response = await axios.post(
      `${process.env.CATALYST_FUNCTION_URL}/queryRAG`,
      {
        query: query.trim(),
        limit: Math.min(limit || 5, 10),  // Enforce max limit
        filters: {
          sourceFilter: source_filter,
          relevanceThreshold: relevance_threshold || 0.6
        },
        includeMetadata: include_metadata
      },
      {
        headers: {
          'Authorization': `Bearer ${process.env.CATALYST_API_KEY}`,
          'Content-Type': 'application/json'
        },
        timeout: 30000  // 30 second timeout
      }
    );

    // 4. Format response
    const result: RAGSearchResponse = {
      query,
      results: response.data.results || [],
      total: response.data.results?.length || 0,
      executionTimeMs: Date.now() - startTime,
      cacheHit: false
    };

    // 5. Cache result locally
    queryCache.set(cacheKey, result);

    // 6. Log metrics
    logger.info('RAG search executed', {
      query: query.substring(0, 50),
      resultsCount: result.total,
      executionTime: result.executionTimeMs
    });

    return result;
  } catch (error) {
    logger.error('RAG search failed', {
      error: error instanceof Error ? error.message : String(error),
      query: query.substring(0, 50)
    });

    if (axios.isAxiosError(error)) {
      if (error.response?.status === 400) {
        throw new AppError('Invalid RAG query', 'RAG_INVALID_QUERY');
      }
      if (error.response?.status === 429) {
        throw new AppError('RAG service rate limited, please retry', 'RAG_RATE_LIMITED');
      }
      if (error.code === 'ECONNABORTED') {
        throw new AppError('RAG service timeout', 'RAG_TIMEOUT');
      }
    }

    throw new AppError('RAG search unavailable', 'RAG_SERVICE_ERROR');
  }
}
```

#### d. Configuration for Catalyst Integration **[NEW]**

**File:** `mcp-config.json` or `.env`

```json
{
  "catalyst": {
    "projectId": "your_catalyst_project_id",
    "tableId": "your_vector_table_id",
    "apiKey": "your_catalyst_api_key",
    "region": "us",
    "functionUrl": "https://catalyst.zoho.com/api/v2/functions/execute",
    "functionNames": {
      "ingestDocuments": "ingestDocuments",
      "queryRAG": "queryRAG",
      "onDocumentUpdate": "onDocumentUpdate"
    },
    "batchSize": 100,
    "maxConnections": 10,
    "timeout": 30000
  },
  "rag": {
    "chunkSize": 500,
    "chunkOverlap": 100,
    "embeddingModel": "text-embedding-3-small",
    "localCacheSize": 1000,
    "localCacheTTL": 3600,
    "catalystCacheTTL": 3600,
    "similarityThreshold": 0.6,
    "maxResults": 10,
    "embeddingBatchSize": 100,
    "ingestionSchedule": "0 */6 * * *"
  },
  "openai": {
    "apiKey": "your_openai_api_key",
    "embeddingModel": "text-embedding-3-small"
  },
  "zohoDesk": {
    "orgId": "your_org_id",
    "apiKey": "your_zoho_desk_api_key"
  }
}
```

#### e. Deployment to Catalyst **[NEW]**

```bash
# 1. Create Catalyst project (via Zoho console)
# https://catalyst.zoho.com

# 2. Create vector table for embeddings
# Table name: knowledge_base
# Columns: id, content, embedding, source, section, created_date, last_updated, version, chunk_index, relevance_tags, metadata (JSON)

# 3. Deploy serverless functions
# Method 1: Upload via Zoho Console
#   - Create new function
#   - Copy ingestDocuments code
#   - Set trigger: Scheduled (every 6 hours)
#   - Save & deploy

# Method 2: CLI (if available)
catalyst deploy --function ingestDocuments
catalyst deploy --function queryRAG
catalyst deploy --function onDocumentUpdate

# 3. Configure webhooks
# POST https://catalyst.zoho.com/api/v2/webhooks
# - Trigger: Document update in repository
# - Target: /onDocumentUpdate function
# - Events: create, update, delete

# 4. Set up monitoring
# - CloudWatch / Catalyst Logs: Monitor function execution
# - Metrics: Invocation count, duration, errors
# - Alerts: Function failures, latency > 5s
```

#### f. Benefits of Catalyst Integration

| Aspect | Benefit |
|--------|---------|
| **Infrastructure** | Serverless = no servers to manage |
| **Cost** | Pay per execution (usually <$1 per 1M queries) |
| **Scaling** | Automatic, handles traffic spikes |
| **Data Security** | Stays within Zoho ecosystem |
| **Integration** | Native access to Zoho Desk KB |
| **Maintenance** | Zoho handles updates, patches |
| **Performance** | Low-latency, optimized for Zoho APIs |
| **Monitoring** | Built-in logging and metrics |

---

## Data Flow

### Flow 1: RAG Search - Retrieve Policy Information **[NEW]**

```
CSR Input (Natural Language)
    ↓
    │ "What's our refund policy for opened products?"
    │
▼────────────────────────────────────────────────────────────────
│ Custom GPT (ChatGPT)                                           │
│ • Analyzes intent as knowledge question                        │
│ • Selects "/rag/search" tool                                   │
│ • Extracts query: "refund policy opened products"              │
│ • Sets limit: 5 results                                        │
└────────────────────────────────────────────────────────────────
    ↓
    │ HTTPS POST /mcp/message
    │ {
    │   "operationId": "/rag/search",
    │   "arguments": {
    │     "query": "refund policy opened products",
    │     "limit": 5,
    │     "source_filter": ["policies"]
    │   }
    │ }
    │
▼────────────────────────────────────────────────────────────────
│ MCP Gateway - RAG Handler                                      │
│ 1. Validate request schema                                     │
│ 2. Check rate limit                                            │
│ 3. Check query cache (LRU)                                    │
│ 4. If cache miss:                                              │
│    a) Embed query: "refund policy..." → [0.23, -0.15, ...]  │
│    b) Call vector DB: Search for top-5 similar documents      │
│    c) Get similarity scores (0.94, 0.87, 0.82, ...)          │
│    d) Filter results (score > 0.6 threshold)                  │
│    e) Format results with metadata                            │
│    f) Store in cache (TTL: 1 hour)                            │
│ 5. Return formatted results                                    │
└────────────────────────────────────────────────────────────────
    ↓
    │ Embedding Generation
    │ Query: "refund policy..." → Embed (1536 dims)
    │ Cost: ~0.0001 per query
    │
    ▼
    │ Vector Similarity Search
    │ Vector DB finds chunks similar to query vector:
    │ • Chunk 1: "Unopened products: full refund"
    │   Score: 0.94 (from policies.md)
    │ • Chunk 2: "Opened products: 50% restocking fee"
    │   Score: 0.92 (from policies.md)
    │ • Chunk 3: "Damaged: full refund + investigation"
    │   Score: 0.87 (from policies.md)
    │
    ▼
    │ Result Formatting
    │ {
    │   "query": "refund policy opened products",
    │   "results": [
    │     {
    │       "id": "chunk-123",
    │       "chunk": "Unopened products: full refund. Opened products: 50% restocking fee applied.",
    │       "source": "policies.md",
    │       "section": "Returns and Refunds > Product Condition",
    │       "relevance_score": 0.94,
    │       "created_date": "2025-12-01T00:00:00Z",
    │       "last_updated": "2026-02-01T00:00:00Z"
    │     },
    │     ...
    │   ],
    │   "execution_time_ms": 145,
    │   "cache_hit": false
    │ }
    │
▼────────────────────────────────────────────────────────────────
│ Custom GPT                                                     │
│ 1. Receive RAG results with policy excerpts                   │
│ 2. Inject context into response generation                     │
│ 3. Formulate answer based on retrieved policies                │
│ 4. Display to CSR with source attribution                      │
│                                                                 │
│ "Based on our policies:                                        │
│  • Unopened products: Full refund                              │
│  • Opened products: 50% restocking fee                         │
│  • Damaged products: Full refund + investigation               │
│                                                                 │
│  Source: policies.md (Updated Feb 1, 2026)                     │
│  [Show Full Policy] [Find Similar Cases]"                      │
└────────────────────────────────────────────────────────────────
    ↓
CSR Gets Policy-Compliant Response
    With citation and source information
```

### Flow 2: Search Tickets

```
CSR Input (Natural Language)
    ↓
    │ "Show me all open tickets with priority High"
    │
▼────────────────────────────────────────────────────────────────
│ Custom GPT (ChatGPT)                                           │
│ • Understands the intent                                       │
│ • Selects "searchTickets" tool                                 │
│ • Extracts parameters:                                         │
│   - status: "Open"                                             │
│   - priority: "High"                                           │
│   - limit: 10                                                  │
└────────────────────────────────────────────────────────────────
    ↓
    │ HTTPS POST /mcp/message
    │ {
    │   "operationId": "searchTickets",
    │   "arguments": {
    │     "status": "Open",
    │     "priority": "High",
    │     "limit": 10
    │   }
    │ }
    │
▼────────────────────────────────────────────────────────────────
│ MCP Gateway                                                    │
│ 1. Validate request schema (Zod)                              │
│ 2. Extract API key from header/query                          │
│ 3. Check rate limits                                          │
│ 4. Route to searchTicketsHandler                              │
│ 5. Handler calls zohoDeskClient.searchTickets()               │
└────────────────────────────────────────────────────────────────
    ↓
    │ REST API Call (OAuth 2.0)
    │ GET https://desk.zoho.com/api/v1/tickets
    │ ?status=Open&priority=High&limit=10
    │ Authorization: Zoho-orgId ZOHO_DESK_ORG_ID
    │ Authorization: Bearer ZOHO_DESK_API_TOKEN
    │
▼────────────────────────────────────────────────────────────────
│ Zoho Desk API                                                  │
│ 1. Validate authentication                                     │
│ 2. Parse query parameters                                      │
│ 3. Query database for matching tickets                        │
│ 4. Build response with ticket details                         │
│ 5. Return JSON array of tickets                               │
└────────────────────────────────────────────────────────────────
    ↓
    │ JSON Response with tickets
    │ [
    │   {
    │     "id": "12345",
    │     "subject": "Order #7890 delayed",
    │     "status": "Open",
    │     "priority": "High",
    │     "customerId": "5678",
    │     "createdTime": "2024-02-01T10:00:00Z"
    │   },
    │   ...
    │ ]
    │
▼────────────────────────────────────────────────────────────────
│ MCP Gateway (Response Handler)                                 │
│ 1. Normalize response data                                     │
│ 2. Format for Custom GPT consumption                           │
│ 3. Log request/response for audit                             │
│ 4. Return standardized response:                               │
│   {                                                            │
│     "success": true,                                           │
│     "operationId": "searchTickets",                            │
│     "data": { "tickets": [...], "count": 5 },                 │
│     "requestId": "uuid-1234"                                  │
│   }                                                            │
└────────────────────────────────────────────────────────────────
    ↓
    │ HTTPS Response
    │
▼────────────────────────────────────────────────────────────────
│ Custom GPT                                                     │
│ 1. Receive structured response                                 │
│ 2. Format results for CSR                                      │
│ 3. Generate summary table                                      │
│ 4. Provide action suggestions                                  │
│ 5. Display to CSR with clickable options                       │
└────────────────────────────────────────────────────────────────
    ↓
CSR Sees Results
    "Found 5 high-priority open tickets. Would you like to:
     1. View details of ticket #12345?
     2. Generate a response for ticket #12346?
     3. Find similar resolved tickets?"
```

### Flow 2: Get Ticket Details

```
CSR Input
    ↓ "Show me full details for ticket #12345"
    ↓
Custom GPT → Selects getTicketDetails tool → Extracts ticketId
    ↓
MCP Gateway
    ├─ Validates schema
    ├─ Checks rate limit
    ├─ Calls zohoDeskClient.getTicket("12345")
    │
    ├─ Makes API call to Zoho Desk:
    │  GET /tickets/12345
    │
    ├─ Receives full ticket object:
    │  {
    │    "id": "12345",
    │    "subject": "...",
    │    "status": "...",
    │    "description": "...",
    │    "attachments": [...],
    │    "customFields": {...},
    │    "timeline": [...]
    │  }
    │
    ├─ Normalizes response
    └─ Returns to Custom GPT
    ↓
Custom GPT Displays
    "Ticket #12345
     Subject: Order #7890 delayed
     Status: Open
     Created: 2024-02-01
     Customer: John Smith (ID: 5678)
     [View Full Conversation] [Generate Response] [Similar Tickets]"
```

### Flow 3: Generate Response Draft (RAG-Enhanced) **[NEW]**

```
CSR Input
    ↓ "Generate a response to ticket #12345"
    ↓
Custom GPT
    ├─ Calls getTicketDetails to get full context
    ├─ Calls getTicketThreads to get conversation
    ├─ Calls getSimilarResolvedTickets for examples
    └─ Prepares context bundle
    ↓
Custom GPT → Calls generateResponseDraft with context + ticket summary
    ↓
MCP Gateway - RAG-Enhanced Handler
    ├─ Receives tool call with:
    │  {
    │    "ticketId": "12345",
    │    "context": {
    │      "ticket": {...},
    │      "threads": [...],
    │      "similarResolved": [...]
    │    }
    │  }
    │
    ├─ STEP 1: Extract relevant information from ticket
    │  ├─ Read ticket subject: "Order #7890 delayed"
    │  ├─ Read issue type: "Shipping delay"
    │  └─ Analyze customer sentiment: Frustrated
    │
    ├─ STEP 2: Query RAG for relevant policies & SOPs
    │  ├─ Call /rag/search with query:
    │  │  "shipping delays refund policy escalation"
    │  │
    │  ├─ RAG returns top-5 relevant documents:
    │  │  • Document 1: "Shipping delay SOP" (score: 0.96)
    │  │  • Document 2: "Refund policy conditions" (score: 0.89)
    │  │  • Document 3: "Customer escalation procedures" (score: 0.85)
    │  │  • Document 4: "Compensation guidelines" (score: 0.82)
    │  │  • Document 5: "Communication standards" (score: 0.78)
    │  │
    │  └─ Cache hit: No (new search)
    │
    ├─ STEP 3: Assemble comprehensive context
    │  ├─ Ticket context (details, threads, customer info)
    │  ├─ RAG-retrieved policies (formatted with source attribution)
    │  ├─ Similar resolved tickets (for tone/approach reference)
    │  ├─ Company communication standards
    │  └─ Escalation guidelines (if applicable)
    │
    ├─ STEP 4: Call AI service with injected RAG context
    │  ├─ System prompt: "You are a professional CSR..."
    │  ├─ RAG Context Injection:
    │  │  [POLICIES & PROCEDURES]
    │  │  • Shipping delays >5 days qualify for $XX compensation
    │  │  • Customer options: Refund, reship, partial credit
    │  │  • Escalation triggers: Repeat delays, customer anger
    │  │  Source: sop.md (Updated Feb 1, 2026)
    │  │
    │  ├─ Ticket Context:
    │  │  • Customer: John Smith
    │  │  • Issue: Order #7890 delayed 7 days
    │  │  • Sentiment: Frustrated (2nd contact)
    │  │  • Options offered: None yet
    │  │
    │  ├─ Similar Cases:
    │  │  • Case #12100: Similar delay → Solution: $50 credit + reship
    │  │  • Case #12050: Same customer → Solution: Full refund + apology
    │  │
    │  └─ Generate: Professional, policy-compliant response
    │
    ├─ STEP 5: Response generation
    │  ├─ AI uses RAG-injected policies to craft response
    │  ├─ Ensures compliance with company guidelines
    │  ├─ Tone matches communication standards
    │  ├─ Offers appropriate compensation per policy
    │  └─ Returns draft with policy citations
    │
    └─ STEP 6: Return response draft
       {
         "success": true,
         "draft": "Dear John,\n\nThank you for your patience...",
         "policyReferences": [
           {
             "policy": "Shipping delay compensation",
             "source": "sop.md",
             "section": "Shipping > Delays > Compensation"
           }
         ],
         "suggestedActions": [
           "Offer $50 credit (policy allows)",
           "Arrange expedited reshipping",
           "Follow up within 24 hours"
         ],
         "complianceScore": 0.98
       }
    ↓
Custom GPT
    ├─ Displays draft to CSR
    ├─ Highlights policy-referenced sections
    ├─ Shows compliance score (0.98 = policy-aligned)
    ├─ Displays source documents for reference
    ├─ Provides edit suggestions (policy-aware)
    └─ Offers options:
       [Use As-Is] [Edit Draft] [View Policy] [View Similar Case] [Regenerate]
    ↓
CSR Sees Response
    "Dear John,
    
     Thank you for your patience regarding order #7890. We sincerely apologize 
     for the delay. Per our shipping policy, we can offer you a $50 account 
     credit and expedited reshipping at no charge.
     
     [Policy: Shipping delay compensation - Updated Feb 1, 2026]
     [Similar Case: #12100 resolved with same solution]
     
     Would you prefer credit, reship, or refund?"
```

**Key Benefits of RAG-Enhanced Response Draft:**

✅ **Policy Compliance**: Every response guaranteed to follow current company policies  
✅ **Real-time Context**: Policies updated automatically via vector DB (no manual sync)  
✅ **Consistent Approach**: Similar cases retrieved to ensure uniform treatment  
✅ **Reduced Risk**: Policy violation warnings shown before sending  
✅ **Audit Trail**: RAG sources documented for compliance audit  
✅ **Continuous Learning**: New policies immediately available without code changes  
✅ **Token Efficiency**: Custom GPT prompts stay lean (context fetched dynamically)

---

## API Endpoints

### Base URL
```
Development: http://localhost:3000
Production:  https://api.yourdomain.com
```

### Health Check Endpoint

**Endpoint:** `GET /health`

**Authentication:** Not required

**Response:**
```json
{
  "status": "ok",
  "timestamp": "2024-02-01T14:30:00Z",
  "version": "1.0.0",
  "uptime": 3600
}
```

### MCP Message Endpoint

**Endpoint:** `POST /mcp/message`

**Authentication:** Required (API Key via query or header)

**Request Format:**
```json
{
  "operationId": "searchTickets|getTicket|getTicketThreads|...",
  "arguments": {
    // Tool-specific arguments
  }
}
```

**Response Format:**
```json
{
  "success": true,
  "operationId": "string",
  "data": {},
  "requestId": "string"
}
```

**Error Response:**
```json
{
  "success": false,
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable error message",
    "details": {}
  },
  "requestId": "string"
}
```

### Tool: searchTickets

**Request:**
```json
{
  "operationId": "searchTickets",
  "arguments": {
    "searchStr": "order delayed",
    "status": "Open",
    "priority": "High",
    "assigneeId": "123",
    "departmentId": "456",
    "limit": 10,
    "offset": 0
  }
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "tickets": [
      {
        "id": "12345",
        "subject": "Order #7890 delayed",
        "status": "Open",
        "priority": "High",
        "customerId": "5678",
        "assigneeId": "123",
        "createdTime": "2024-02-01T10:00:00Z",
        "updatedTime": "2024-02-02T09:00:00Z"
      }
    ],
    "totalCount": 1
  }
}
```

### Tool: getTicket

**Request:**
```json
{
  "operationId": "getTicket",
  "arguments": {
    "ticketId": "12345"
  }
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "ticket": {
      "id": "12345",
      "subject": "Order #7890 delayed",
      "description": "Customer reports shipment delayed...",
      "status": "Open",
      "priority": "High",
      "customerId": "5678",
      "customerEmail": "john@example.com",
      "customerName": "John Smith",
      "assigneeId": "123",
      "assigneeName": "Jane Doe",
      "departmentId": "456",
      "createdTime": "2024-02-01T10:00:00Z",
      "updatedTime": "2024-02-02T09:00:00Z",
      "customFields": {},
      "attachments": []
    }
  }
}
```

### Tool: ragSearch **[NEW]**

**Endpoint:** `POST /mcp/message` with `operationId: "/rag/search"`

**Request:**
```json
{
  "operationId": "/rag/search",
  "arguments": {
    "query": "refund policy for opened products",
    "limit": 5,
    "source_filter": ["policies"],
    "date_range": {
      "start": "2025-01-01",
      "end": "2026-12-31"
    },
    "relevance_threshold": 0.6
  }
}
```

**Response:**
```json
{
  "success": true,
  "operationId": "/rag/search",
  "data": {
    "query": "refund policy for opened products",
    "results": [
      {
        "id": "chunk-uuid-1",
        "chunk": "Unopened products qualify for full refunds within 30 days. Opened products are subject to a 50% restocking fee. Damaged products receive full refund plus investigation...",
        "source": "policies.md",
        "section": "Returns and Refunds > Product Condition",
        "relevance_score": 0.94,
        "created_date": "2025-12-01T00:00:00Z",
        "last_updated": "2026-02-01T00:00:00Z",
        "chunk_index": 2,
        "version": 3
      },
      {
        "id": "chunk-uuid-2",
        "chunk": "For opened wine bottles, we apply a 50% restocking fee as product value is significantly diminished. Customers must provide proof of purchase...",
        "source": "policies.md",
        "section": "Returns and Refunds > Wine Products",
        "relevance_score": 0.89,
        "created_date": "2025-12-15T00:00:00Z",
        "last_updated": "2026-02-01T00:00:00Z",
        "chunk_index": 5,
        "version": 2
      }
    ],
    "total_results": 2,
    "execution_time_ms": 145,
    "query_embedding_model": "text-embedding-3-small",
    "cache_hit": false
  },
  "requestId": "uuid-1234"
}
```

**Error Response:**
```json
{
  "success": false,
  "error": {
    "code": "RAG_SEARCH_ERROR",
    "message": "No relevant documents found matching query",
    "details": {
      "query": "refund policy...",
      "results_found": 0,
      "min_score_found": 0.45
    }
  },
  "requestId": "uuid-1234"
}
```

---

## Security Architecture

### Authentication & Authorization

```
API Key Generation
    ↓
Validation on Each Request
    ├─ Query parameter: ?key=YOUR_API_KEY
    ├─ Header: X-API-Key: YOUR_API_KEY
    ├─ Bearer token: Authorization: Bearer YOUR_API_KEY
    └─ Zoho OAuth: Internal OAuth2 flow
    ↓
Rate Limiting
    ├─ Per IP address
    ├─ Per API key
    ├─ Global limits
    └─ Sliding window algorithm
    ↓
Request Validation
    ├─ Schema validation (Zod)
    ├─ Argument type checking
    ├─ Size limits enforcement
    └─ Injection prevention
```

### Data Protection

**In Transit:**
- TLS 1.2+ for all HTTPS connections
- Certificate pinning for production
- Secure header set via Helmet

**At Rest:**
- Environment variables for secrets
- No hardcoded credentials
- Secure storage in vault/secret manager

**In Logs:**
- PII masking via sanitize utility
- Sensitive fields excluded
- Audit trail for compliance
- Structured logging for security events

### Zohohis Desk Credentials

```
.env file (LOCAL ONLY)
├── ZOHO_DESK_ORG_ID
├── ZOHO_DESK_API_TOKEN
└── ZOHO_DESK_BASE_URL

Production Environment
├── Kubernetes Secrets
├── AWS Secrets Manager
├── Azure Key Vault
└── HashiCorp Vault
```

### Input Validation

```typescript
// Example: searchTickets arguments validated by Zod schema
arguments: {
  searchStr?: string,           // Max 500 chars
  status?: enum(...),           // Only valid statuses
  priority?: enum(...),         // Only valid priorities
  assigneeId?: string,          // UUID format
  limit?: number,               // 1-100 range
  offset?: number               // 0-10000 range
}
```

---

## Scalability & Performance

### Performance Characteristics

| Component | Metric | Target | Method |
|-----------|--------|--------|--------|
| API Response | Latency | < 2s | HTTP timeout |
| Zoho API | Timeout | 30s | With retry |
| Request Rate | Limit | 100/min per key | Sliding window |
| Batch Size | Limit | 100 items | Pagination |
| Memory | Per instance | < 500MB | Node.js config |
| CPU | Per instance | < 80% | Monitoring |

### Horizontal Scaling

```
                         ┌──────────────┐
                         │ Load Balancer│
                         │  (AWS ALB)   │
                         └──────┬───────┘
                                │
                  Distribute traffic evenly
                                │
        ┌─────────────┬─────────────┬──────────────┐
        │             │             │              │
    ┌───▼──────┐  ┌──▼──────┐  ┌──▼──────┐   ┌─▼──────┐
    │ Instance │  │Instance │  │Instance │   │Instance│
    │    1     │  │   2     │  │   3     │   │  N     │
    │ Port 3K  │  │ Port 3K │  │Port 3K  │   │Port 3K │
    └───┬──────┘  └──┬──────┘  └──┬──────┘   └─┬──────┘
        │           │            │             │
        └───────────┼────────────┼─────────────┘
                    │
        Shared cache layer (Redis)
                    │
        Zoho Desk API (single tenant)
```

### Caching Strategy

```
Request Flow:
1. Check Redis cache (30s TTL for searches)
2. If cache hit → Return immediately
3. If cache miss → Call Zoho API
4. Store result in Redis
5. Return to client

Cache Keys:
- searchTickets::{status}::{priority}::{offset}
- getTicket::{ticketId}
- getTicketThreads::{ticketId}
- similarTickets::{ticketId}
```

### Database Connection Pooling

```
HTTP Client Configuration:
├─ Connection pool size: 10-50
├─ Keep-alive enabled
├─ Connection timeout: 5s
├─ Socket timeout: 30s
└─ Idle timeout: 60s
```

---

## Error Handling

### Error Classification

```
┌─────────────────────────────────────────────────────────────┐
│                   Error Received                             │
└────────────────────┬────────────────────────────────────────┘
                     │
        ┌────────────┴────────────┬──────────────┬─────────────┐
        │                         │              │             │
        ▼                         ▼              ▼             ▼
    ┌─────────┐           ┌─────────────┐  ┌────────┐   ┌──────────┐
    │ Client  │           │ Server      │  │Zoho    │   │ Network  │
    │ Error   │           │ Error       │  │ Error  │   │ Error    │
    │ 4xx     │           │ 5xx         │  │(4xx/5x)│   │(timeout) │
    └────┬────┘           └──────┬──────┘  └───┬────┘   └────┬─────┘
         │                       │             │             │
         ├─ Validation error     ├─ Bug        ├─ Auth error ├─ Retry
         ├─ Auth error          ├─ OOM        ├─ Rate limit ├─ Fallback
         ├─ Invalid args        ├─ Crash      ├─ Not found  ├─ Alert
         └─ Bad request         └─ Exception  └─ Api change └─ Log
```

### Error Response Format

```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid argument: ticketId must be a string",
    "details": {
      "field": "ticketId",
      "received": 12345,
      "expected": "string"
    }
  },
  "requestId": "550e8400-e29b-41d4-a716-446655440000",
  "timestamp": "2024-02-02T14:30:00Z"
}
```

### Retry Logic

```
Initial Request
    ↓
Error Received
    ├─ Retryable? (timeout, 429, 5xx)
    │  ├─ Yes → Calculate backoff
    │  │    ├─ Attempt 1: 100ms delay
    │  │    ├─ Attempt 2: 200ms delay
    │  │    ├─ Attempt 3: 400ms delay
    │  │    └─ Attempt 4: 800ms delay
    │  │    (Max 3 retries, 1.5s total)
    │  │
    │  └─ No → Return error
    │
    └─ All retries exhausted → Return error
```

---

## Monitoring & Observability

### Metrics Collection

```
┌──────────────────────────────────────────────────┐
│          Pino Logger (Structured JSON)            │
│  All events logged with context:                 │
│  • timestamp                                      │
│  • level (info, warn, error)                     │
│  • requestId                                      │
│  • operationId                                    │
│  • duration                                       │
│  • status                                         │
│  • error (if applicable)                         │
└──────────────────────────────────────────────────┘
                      │
        ┌─────────────┴──────────────┐
        │                            │
        ▼                            ▼
  ┌──────────────┐            ┌──────────────┐
  │ CloudWatch   │            │ Datadog      │
  │ (AWS)        │            │ (SaaS)       │
  │              │            │              │
  │ - Logs       │            │ - APM        │
  │ - Metrics    │            │ - Metrics    │
  │ - Dashboards │            │ - Dashboards │
  │ - Alerts     │            │ - Alerts     │
  └──────────────┘            └──────────────┘
```

### Key Metrics to Monitor

1. **Request Metrics**
   - Requests per minute
   - Average response time
   - 95th percentile latency
   - 99th percentile latency
   - Error rate (%)

2. **Tool Usage Metrics**
   - Calls per tool
   - Success rate per tool
   - Average duration per tool
   - Failure reasons

3. **RAG-Specific Metrics** **[NEW]**
   - RAG search queries per hour
   - Average RAG query latency (target: <500ms p95)
   - Cache hit ratio (target: 60-70%)
   - Vector DB connectivity health
   - Embedding generation cost (per 1M tokens)
   - Query relevance score distribution
   - Document update frequency
   - Ingestion latency (target: <1 hour)

4. **System Metrics**
   - CPU usage
   - Memory usage
   - Disk I/O
   - Network I/O
   - Instance count
   - Vector DB storage usage

5. **Business Metrics**
   - Ticket resolution time
   - CSR efficiency
   - Customer satisfaction
   - Tool adoption rate
   - RAG accuracy (manual assessment)
   - Policy compliance (audit)

### Logging Strategy

```typescript
// Request entry
logger.info({
  requestId: "uuid",
  operationId: "searchTickets",
  args: { status: "Open" }
}, "Processing MCP request");

// API call
logger.info({
  requestId: "uuid",
  duration: 250,
  endpoint: "GET /tickets",
  statusCode: 200
}, "Zoho API call completed");

// Response
logger.info({
  requestId: "uuid",
  operationId: "searchTickets",
  resultCount: 5,
  duration: 280
}, "MCP request successful");

// Error
logger.error({
  requestId: "uuid",
  operationId: "searchTickets",
  error: "Authentication failed",
  statusCode: 401
}, "MCP request failed");
```

---

## Deployment Architecture

### Development Deployment

```
Developer Laptop
├── Git repository
├── Node.js 18+
├── npm/yarn
├── .env file (local credentials)
├── npm install
├── npm run build
└── npm run dev
    ├── TypeScript compilation
    ├── Hot reload on file changes
    ├── Server on http://localhost:3000
    └── Mock mode enabled (if configured)
```

### Production Deployment Options

#### Option 1: Docker Container (AWS ECS/Fargate)

```
Source Code
    ↓
Docker Build
    ├── FROM node:18-alpine
    ├── COPY package*.json
    ├── RUN npm ci --production
    ├── COPY dist/
    ├── EXPOSE 3000
    └── CMD ["node", "dist/index.js"]
    ↓
ECR Registry
    ↓
ECS Service
├── Task definition
├── Load balancer
├── Auto-scaling
├── CloudWatch logs
└── CloudWatch metrics
```

#### Option 2: Serverless (AWS Lambda)

```
Source Code
    ↓
Webpack/Build
    ↓
Lambda Handler
    ├── Parse HTTP event
    ├── Create Express app
    ├── Route request
    └── Return response
    ↓
API Gateway
    ├── HTTP routes
    ├── CORS
    ├── Rate limiting
    └── Authentication
    ↓
Lambda Layers
    ├── Dependencies
    └── Node modules
```

#### Option 3: Kubernetes (EKS/AKS/GKE)

```
Helm Chart
    ↓
├── Deployment
│   ├── Replicas: 3+
│   ├── CPU limit: 500m
│   ├── Memory limit: 512Mi
│   ├── Health check
│   └── Rolling update
├── Service
│   ├── ClusterIP/LoadBalancer
│   └── Port 3000
├── ConfigMap
│   └── Configuration
└── Secret
    └── Credentials
    ↓
Horizontal Pod Autoscaler
    ├── Min replicas: 3
    ├── Max replicas: 10
    ├── CPU threshold: 70%
    └── Memory threshold: 80%
```

### Environment Configuration

```
Development (.env)
├── NODE_ENV=development
├── LOG_LEVEL=debug
├── MOCK_MODE=true
├── RATE_LIMIT_MAX_REQUESTS=1000
└── PORT=3000

Staging (.env.staging)
├── NODE_ENV=staging
├── LOG_LEVEL=info
├── MOCK_MODE=false
├── RATE_LIMIT_MAX_REQUESTS=500
└── PORT=3000

Production (.env.production)
├── NODE_ENV=production
├── LOG_LEVEL=warn
├── MOCK_MODE=false
├── RATE_LIMIT_MAX_REQUESTS=100
├── PORT=3000
└── SSL_CERT_PATH=/etc/ssl/certs/cert.pem
```

---

## Future Enhancements

### Phase 2 (3-6 months)

- **Advanced AI Integration**
  - GPT-4 integration for better responses
  - Claude integration for alternative AI
  - Fine-tuning on company data

- **Enhanced RAG Capabilities** **[NEW]**
  - Hybrid search (semantic + keyword BM25)
  - Metadata-aware filtering
  - Document ranking by recency
  - Custom fine-tuned embeddings
  - Multi-language support
  - Query expansion and suggestion

- **Additional Integrations**
  - CRM system integration
  - Order management system
  - Inventory tracking
  - Shipping carrier APIs

- **Enhanced Analytics**
  - CSR productivity dashboard
  - Ticket resolution trends
  - Customer satisfaction metrics
  - AI performance metrics
  - RAG relevance dashboard

### Phase 3 (6-12 months)

- **Voice Interface**
  - Voice input for CSRs
  - Voice response synthesis
  - Speech-to-text transcription
  - Voice quality assurance

- **RAG Optimization** **[NEW]**
  - Automated document quality scoring
  - Answer generation from RAG context
  - Interactive context refinement
  - A/B testing for embeddings
  - Cost optimization analysis

- **Real-time Collaboration**
  - Multi-CSR ticket collaboration
  - Live chat integration
  - Video call support
  - Screen sharing

- **Predictive Features**
  - Automated ticket classification
  - Issue prediction
  - Optimal CSR assignment
  - Customer churn prediction

### Phase 4 (12+ months)

- **Platform Expansion**
  - Multi-tenant support
  - White-label solution
  - API marketplace
  - Partner integrations

- **Advanced RAG** **[NEW]**
  - GraphRAG for relationship extraction
  - Query rewriting for better retrieval
  - Fact verification from sources
  - Cross-document question answering
  - Real-time document updates

- **Advanced ML**
  - Custom model training
  - Anomaly detection
  - Recommendation engine
  - Sentiment analysis

---

## Document Information

**Document Version:** 2.0.0 (RAG-Enhanced)  
**Last Updated:** February 4, 2026  
**Author:** Development Team  
**Maintainer:** Architecture Team  
**Status:** RAG Implementation In Progress  

**Related Documents:**
- QUICKSTART.md - Quick setup guide
- README.md - Main project documentation
- docs/deployment.md - Deployment instructions
- docs/sop.md - Standard Operating Procedures
- docs/policies.md - Customer service policies
- RAG-IMPLEMENTATION-GUIDE.md - Detailed RAG design
- ZOHO_ZIA_IMPLEMENTATION_PROMPT.md - Zoho Zia implementation guide

---

**End of Architecture Documentation**

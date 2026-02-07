# Boxie Bot CSR

AI-powered Customer Service Representative assistant for Zoho Desk with RAG (Retrieval-Augmented Generation) capabilities.

## Overview

Boxie Bot CSR is a production-ready Custom GPT that helps customer service representatives work more efficiently by:

- **Searching tickets** with natural language queries
- **Retrieving complete ticket context** including conversation history
- **Searching knowledge base** semantically using RAG
- **Generating response drafts** powered by GPT-4 with company policy context

## Features

✅ **Zoho Desk Integration** - Direct API access to tickets and customer data  
✅ **RAG-Powered Knowledge Base** - Semantic search across SOPs and policies  
✅ **AI Response Generation** - Context-aware draft responses  
✅ **Custom GPT Interface** - Natural language interaction via ChatGPT  
✅ **Serverless Architecture** - Deployed on Zoho Catalyst (zero infrastructure management)  
✅ **Production Ready** - Complete with error handling, logging, and security

## Quick Start

### For Your Company Deployment:

1. **Clone this repository** to your company's git environment
2. **Follow [README-SETUP.md](./README-SETUP.md)** for complete setup instructions
3. **Use [DEPLOYMENT-CHECKLIST.md](./DEPLOYMENT-CHECKLIST.md)** to track deployment progress

### Configuration Required:

- Zoho Desk API credentials
- OpenAI API key
- Supabase account (for RAG, optional)
- Zoho Catalyst project

All credentials are managed via `.env` file (see `.env.example`)

## Project Structure

```
boxie-bot-csr/
├── src/
│   ├── config.js                    # Configuration management
│   ├── zoho-desk-client.js         # Zoho Desk API client
│   ├── rag-client.js               # RAG/vector search client
│   └── .env.example                # Environment variables template
├── catalyst-functions/
│   ├── searchTickets.js            # Search tickets function
│   ├── getTicketDetails.js         # Get ticket details function
│   ├── ragSearch.js                # Knowledge base search function
│   └── generateResponse.js         # AI response generation function
├── custom-gpt/
│   ├── openapi-spec.yaml           # OpenAPI specification for Custom GPT
│   └── instructions.md             # Custom GPT behavior instructions
├── test/
│   └── test-local.js               # Local testing script
├── README-SETUP.md                 # Complete setup guide
├── DEPLOYMENT-CHECKLIST.md         # Deployment checklist
└── package.json                    # Dependencies

```

## Documentation

- **[README-SETUP.md](./README-SETUP.md)** - Step-by-step setup instructions
- **[DEPLOYMENT-CHECKLIST.md](./DEPLOYMENT-CHECKLIST.md)** - Pre-deployment checklist
- **[IMPLEMENTATION-PLAN.md](./IMPLEMENTATION-PLAN.md)** - Original implementation plan
- **[ZOHO-CATALYST-RESEARCH.md](./ZOHO-CATALYST-RESEARCH.md)** - Architecture research notes

## Architecture

```
Custom GPT (ChatGPT)
    ↓
Zoho Catalyst Functions
    ├─ searchTickets
    ├─ getTicketDetails  
    ├─ ragSearch
    └─ generateResponse
        ↓
    ┌───────────────┐
    │  Zoho Desk    │ ← Tickets & Customer Data
    │  Supabase     │ ← Vector DB (RAG)
    │  OpenAI API   │ ← Embeddings & GPT-4
    └───────────────┘
```

## Technology Stack

- **Runtime:** Node.js 18+
- **Platform:** Zoho Catalyst (serverless)
- **Ticketing:** Zoho Desk API v1
- **Vector DB:** Supabase + pgvector
- **AI:** OpenAI GPT-4 + Embeddings
- **Interface:** Custom GPT (ChatGPT Actions)

## Cost Estimates

**Monthly Production Cost:**
- Zoho Catalyst: $0-50 (free tier covers most usage)
- Supabase: $0-25 (free tier → paid if needed)
- OpenAI API: $20-100 (depends on CSR usage)

**Total:** $20-175/month (typical: $30-50)

## Security

- ✅ All credentials managed via environment variables
- ✅ API key authentication for Custom GPT
- ✅ No hardcoded secrets
- ✅ Input validation on all functions
- ✅ Error handling without exposing sensitive data
- ✅ `.env` excluded from git via `.gitignore`

## Testing

```bash
# Install dependencies
npm install

# Copy and configure environment
cp src/.env.example src/.env
# Edit .env with your credentials

# Run local tests
npm test
```

## Deployment

See [README-SETUP.md](./README-SETUP.md) for complete deployment instructions.

Quick summary:
1. Configure `.env`
2. Deploy to Zoho Catalyst: `catalyst deploy`
3. Set up Supabase (for RAG)
4. Configure Custom GPT with OpenAPI spec
5. Index knowledge base documents

## Support

For issues specific to this implementation:
- Review troubleshooting section in [README-SETUP.md](./README-SETUP.md)
- Check Catalyst function logs
- Verify environment variables are set correctly

For platform support:
- Zoho Catalyst: https://catalyst.zoho.com/help
- Supabase: https://supabase.com/docs
- OpenAI: https://platform.openai.com/docs

## License

ISC

---

**Status:** Production-ready mock implementation with placeholder credentials. Clone to your company repo and configure for deployment.

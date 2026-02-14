# RedditFlow - System Architecture

## Overview

High-level architecture for Reddit marketing automation platform.

---

## System Components

```
┌─────────────────────────────────────────────────────────────┐
│                        Frontend (React)                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  Dashboard   │  │   Threads    │  │  Analytics   │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
                              │
                              │ REST API
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                     API Server (FastAPI)                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Auth       │  │   Threads    │  │  Comments    │      │
│  │  Endpoints   │  │  Endpoints   │  │  Endpoints   │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
                              │
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
┌──────────────┐    ┌──────────────┐     ┌──────────────┐
│   Reddit     │    │   AI Agent   │     │  Scheduler   │
│   Service    │    │   (Claude)   │     │   (Celery)   │
└──────────────┘    └──────────────┘     └──────────────┘
        │                     │                     │
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │   PostgreSQL     │
                    │   + Redis        │
                    └──────────────────┘
```

---

## Data Flow

### 1. Thread Discovery
```
User defines keywords
    ↓
Scheduler runs discovery task (every 1 hour)
    ↓
Reddit Service searches subreddits
    ↓
Threads stored in database
    ↓
Ranked by relevance + traffic potential
    ↓
User sees results in dashboard
```

### 2. Comment Generation & Posting
```
User selects thread (or auto-mode enabled)
    ↓
AI Agent analyzes thread context
    ↓
Generates natural comment mentioning brand
    ↓
User approves (or auto-approved in Pro mode)
    ↓
Scheduler assigns to available account
    ↓
Reddit Service posts comment (via PRAW)
    ↓
Success/failure logged
    ↓
Analytics updated
```

### 3. Account Management
```
Accounts stored with metadata (karma, age, last_active)
    ↓
Health check runs daily
    ↓
Warm-up tasks scheduled (1-2 organic comments/day)
    ↓
Account rotation per post (avoid patterns)
    ↓
Shadowban detection (check post visibility)
    ↓
Alerts if account compromised
```

---

## Database Schema

### Users Table
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    plan VARCHAR(50), -- 'starter', 'growth', 'pro'
    credits INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW()
);
```

### Reddit Accounts Table
```sql
CREATE TABLE reddit_accounts (
    id UUID PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    password_encrypted TEXT NOT NULL,
    karma INT DEFAULT 0,
    account_age_days INT,
    last_post_at TIMESTAMP,
    status VARCHAR(50), -- 'active', 'warming_up', 'banned', 'shadowbanned'
    proxy_id UUID REFERENCES proxies(id),
    created_at TIMESTAMP DEFAULT NOW()
);
```

### Threads Table
```sql
CREATE TABLE threads (
    id UUID PRIMARY KEY,
    reddit_id VARCHAR(50) UNIQUE NOT NULL,
    subreddit VARCHAR(100) NOT NULL,
    title TEXT NOT NULL,
    url TEXT NOT NULL,
    author VARCHAR(100),
    score INT DEFAULT 0,
    num_comments INT DEFAULT 0,
    created_utc TIMESTAMP,
    relevance_score FLOAT, -- AI-scored relevance to user's product
    google_rank INT, -- Position in Google search results (if applicable)
    discovered_at TIMESTAMP DEFAULT NOW()
);
```

### Keywords Table
```sql
CREATE TABLE keywords (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    keyword TEXT NOT NULL,
    subreddits TEXT[], -- Array of subreddits to monitor
    active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW()
);
```

### Comments Table
```sql
CREATE TABLE comments (
    id UUID PRIMARY KEY,
    thread_id UUID REFERENCES threads(id),
    reddit_account_id UUID REFERENCES reddit_accounts(id),
    user_id UUID REFERENCES users(id),
    comment_text TEXT NOT NULL,
    reddit_comment_id VARCHAR(50), -- ID after posting
    status VARCHAR(50), -- 'pending', 'approved', 'posted', 'failed'
    posted_at TIMESTAMP,
    clicks INT DEFAULT 0, -- Track link clicks (if possible)
    upvotes INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW()
);
```

### Proxies Table
```sql
CREATE TABLE proxies (
    id UUID PRIMARY KEY,
    ip_address VARCHAR(50),
    port INT,
    protocol VARCHAR(10), -- 'http', 'socks5'
    username VARCHAR(100),
    password_encrypted TEXT,
    country VARCHAR(2),
    status VARCHAR(50), -- 'active', 'banned', 'rotating'
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## Core Services

### 1. Reddit Service (`services/reddit.py`)

**Responsibilities:**
- Reddit API integration (PRAW)
- Thread discovery
- Comment posting
- Account management
- Karma tracking

**Key Functions:**
```python
class RedditService:
    def discover_threads(keywords, subreddits, limit=50)
    def post_comment(thread_id, comment_text, account)
    def get_account_karma(username)
    def check_shadowban(account)
    def warm_up_account(account)  # Post 1-2 organic comments
```

---

### 2. AI Service (`services/ai.py`)

**Responsibilities:**
- Comment generation
- Thread relevance scoring
- Subreddit tone analysis

**Key Functions:**
```python
class AIService:
    def generate_comment(thread, brand_context, subreddit_rules)
    def score_thread_relevance(thread, keywords)
    def analyze_subreddit_tone(subreddit)  # Formal vs casual
```

---

### 3. Scheduler Service (`services/scheduler.py`)

**Responsibilities:**
- Celery task management
- Posting schedule optimization
- Account rotation

**Tasks:**
```python
@celery.task
def discover_threads_task()  # Runs every hour

@celery.task
def post_comment_task(comment_id)  # Posts at optimal time

@celery.task
def warm_up_accounts_task()  # Daily organic activity

@celery.task
def health_check_task()  # Check account status daily
```

---

### 4. Analytics Service (`services/analytics.py`)

**Responsibilities:**
- Track comment performance
- Measure traffic/conversions
- Generate reports

**Key Functions:**
```python
class AnalyticsService:
    def track_comment_performance(comment_id)
    def get_user_dashboard_stats(user_id)
    def generate_weekly_report(user_id)
```

---

## Security & Anti-Ban Measures

### Account Safety
1. **IP Rotation:** Each account uses unique residential proxy
2. **Rate Limiting:** Max 5-10 comments/day per account
3. **Warm-up Period:** New accounts post 1-2 organic comments/day for 30 days
4. **Human-like Timing:** Random delays between actions (2-10 minutes)
5. **Karma Threshold:** Only use accounts with 100+ karma

### Comment Quality
1. **AI Review:** Detect overly promotional language
2. **Subreddit Rules:** Check against subreddit posting guidelines
3. **User Approval:** Manual review for Starter/Growth plans
4. **Spam Filter:** Limit brand mentions (1 per 3 comments)

### Shadowban Detection
1. **Daily Check:** Verify comment visibility
2. **Karma Monitoring:** Sudden drops = likely banned
3. **Manual Verification:** Random spot-checks
4. **Auto-rotation:** Switch accounts if shadowbanned

---

## Scaling Strategy

### Phase 1 (0-50 users)
- Single server (Railway)
- 50 Reddit accounts
- 10 proxies
- Manual monitoring

### Phase 2 (50-200 users)
- Horizontal scaling (multiple workers)
- 200+ accounts
- 50+ proxies
- Automated monitoring

### Phase 3 (200+ users)
- Multi-region deployment
- 1,000+ accounts
- Residential proxy pool
- ML-based ban prediction

---

## API Endpoints

### Authentication
```
POST   /api/auth/register
POST   /api/auth/login
POST   /api/auth/logout
GET    /api/auth/me
```

### Threads
```
GET    /api/threads              # List discovered threads
GET    /api/threads/:id          # Thread details
POST   /api/threads/discover     # Manual discovery
```

### Comments
```
GET    /api/comments             # User's comments
POST   /api/comments             # Create comment (generates AI draft)
POST   /api/comments/:id/approve # Approve + schedule posting
DELETE /api/comments/:id         # Cancel comment
```

### Keywords
```
GET    /api/keywords             # User's tracked keywords
POST   /api/keywords             # Add keyword
PUT    /api/keywords/:id         # Update
DELETE /api/keywords/:id         # Remove
```

### Accounts (Admin)
```
GET    /api/accounts             # List Reddit accounts
POST   /api/accounts             # Add account
PUT    /api/accounts/:id         # Update status
GET    /api/accounts/:id/health  # Health check
```

### Analytics
```
GET    /api/analytics/dashboard  # Overview stats
GET    /api/analytics/comments   # Comment performance
GET    /api/analytics/threads    # Top threads
```

---

## Tech Decisions

### Why FastAPI?
- Fast performance (async)
- Auto-generated API docs (OpenAPI)
- Type safety (Pydantic)
- Easy to deploy

### Why PostgreSQL?
- Relational data (users, accounts, threads)
- JSONB support (flexible metadata)
- Strong consistency

### Why Redis?
- Celery task queue
- Rate limiting
- Caching

### Why PRAW?
- Official Reddit API wrapper
- Well-documented
- Rate limiting built-in

### Why Claude?
- Better at natural language (vs GPT-4)
- Longer context (200K tokens)
- Less "AI-sounding"

---

## Development Environment

### Prerequisites
```bash
Python 3.11+
Node.js 18+
PostgreSQL 15+
Redis 7+
```

### Setup
```bash
# Backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
alembic upgrade head  # Run migrations

# Frontend
cd frontend
npm install
npm run dev

# Workers
celery -A app.tasks worker --loglevel=info
```

---

## Deployment

### Backend (Railway)
- Auto-deploy from GitHub
- Environment variables in Railway dashboard
- PostgreSQL + Redis add-ons

### Frontend (Vercel)
- Auto-deploy from GitHub
- Environment variables in Vercel dashboard

### Workers (Railway)
- Separate worker service
- Same codebase, different start command

---

## Next Steps

1. ✅ Architecture designed
2. ⏳ Database schema implemented
3. ⏳ Reddit service built
4. ⏳ AI service integrated
5. ⏳ API endpoints created
6. ⏳ Frontend dashboard built

---

**Status:** Architecture complete. Moving to implementation.

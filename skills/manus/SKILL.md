# Manus.im Integration Skill

Integration with Manus AI for specialized task execution (browser automation, LinkedIn scraping, deep research).

## Overview

Manus AI is an autonomous agent that operates in a sandboxed Linux environment with:
- Browser operator (bypasses bot detection on LinkedIn, Similarweb, etc.)
- Code execution (Python, JavaScript)
- Wide Research capabilities
- File system persistence
- Internet access

## When to Use Manus

**Delegate to Manus for:**
- LinkedIn scraping (native skills, bypasses detection)
- Similarweb data extraction
- Complex browser automation that requires anti-bot bypass
- Multi-step research tasks that need deep investigation
- Tasks requiring isolated sandbox execution

**Keep with Portifoy (me) for:**
- Local context and memory
- Proactive monitoring and heartbeat checks
- Direct integration with Mitch's messaging and repos
- Quick scripting and automation
- Task routing and result delivery

## Architecture

```
Mitch → Portifoy (Manager/Router)
           ↓
       Decision: Local or Delegate?
           ↓
       Manus (Specialist Executor)
           ↓
       Results → Portifoy analyzes → Delivers to Mitch
```

## API Usage

See `manus_client.py` for the Python wrapper.

**Base URL:** `https://api.manus.ai/v1`

**Authentication:** Custom header `API_KEY: sk-...`

**Key Endpoints:**
- `POST /v1/tasks` - Create task
- `GET /v1/tasks` - List tasks with filtering
- `GET /v1/tasks/{task_id}` - Get specific task

**Agent Profiles:**
- `manus-1.6` - Default balanced mode
- `manus-1.6-lite` - Faster, lighter tasks
- `manus-1.6-max` - Most powerful, slower

**Task Modes:**
- `chat` - Conversational
- `adaptive` - Auto-adjusts based on task
- `agent` - Full autonomous mode

## Integration Points

1. **Lead Generation** - "Find 50 3PL partners in PA with cold storage"
2. **Competitive Intelligence** - "Monitor Evil Apples competitors for feature updates"
3. **Deep Research** - "Research potential acquisition targets in gaming space"
4. **Browser Automation** - "Fill out this form on 20 different websites"

## Cost Tracking

Track credit usage via `credit_usage` field in task responses. Monitor spend and optimize task delegation.

## Security

- API key stored in environment variable `MANUS_API_KEY`
- Never expose key in logs or public repos
- Results may contain sensitive data - handle appropriately

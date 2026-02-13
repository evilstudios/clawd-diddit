# Manus.im Integration

**Status:** ✅ Operational  
**Setup Date:** 2026-02-13  
**API Key:** Configured (see Gateway config)

## Overview

Manus AI is an autonomous agent platform that provides specialized capabilities for:
- Browser automation (LinkedIn, Similarweb, etc.) with anti-bot bypass
- Deep research and data gathering
- Code execution in isolated Linux sandbox
- Multi-step task workflows

## Architecture

```
Portifoy (Manager) → Manus (Executor) → Results → Portifoy (Delivery)
```

**When to use Manus:**
- LinkedIn scraping (native connector, bypasses detection)
- Similarweb data extraction
- Complex browser automation requiring anti-bot measures
- Deep research requiring multiple sources
- Tasks needing isolated sandbox execution

**When to use Portifoy directly:**
- Local file operations
- Quick scripts and automation
- Proactive monitoring
- Direct integration with Mitch's systems
- Tasks requiring personal context/memory

## Setup

### 1. API Key Configuration

The Manus API key should be stored in the Gateway environment:

```bash
# Add to Gateway config or environment
export MANUS_API_KEY="sk-..."
```

**Current key location:** Gateway environment (already configured)

### 2. Python Client

The `manus_client.py` provides a clean wrapper around the Manus API:

```python
from skills.manus.manus_client import ManusClient

client = ManusClient()  # Auto-loads from MANUS_API_KEY env var

# Quick task with result
result = client.quick_task(
    prompt="Research top 3PL companies in Pennsylvania",
    agent_profile="manus-1.6",
    max_wait=180
)
print(result)

# Async task (check later)
task = client.create_task(
    prompt="Scrape LinkedIn for logistics companies",
    wait_for_completion=False
)
print(f"Check: {task['task_url']}")
```

### 3. Agent Profiles

- **manus-1.6** - Default, balanced performance
- **manus-1.6-lite** - Faster, lighter tasks (cheaper)
- **manus-1.6-max** - Most powerful, comprehensive research (slower/pricier)

### 4. Task Modes

- **adaptive** - Auto-adjusts based on task (default)
- **agent** - Full autonomous mode
- **chat** - Conversational interaction

## Usage Examples

See `examples.py` for detailed usage patterns:

```bash
cd /root/clawd/skills/manus
python3 examples.py
```

**Key examples:**
1. Quick research tasks
2. LinkedIn lead generation (requires connector)
3. Competitive app store analysis
4. Data processing and script generation
5. Batch async task creation

## Integration Points

### 1. Lead Generation (Evil Studios / BigHouse)
```python
task = client.create_task(
    prompt="""Find 50 potential 3PL partners in Pennsylvania with cold storage capabilities.
    
    For each company provide:
    - Company name & website
    - Contact information
    - Storage capacity (if available)
    - Key decision maker
    
    Export as CSV.""",
    agent_profile="manus-1.6",
    connectors=["linkedin", "similarweb"]
)
```

### 2. Competitive Intelligence (Evil Apples)
```python
# Scheduled daily via cron or heartbeat
task = client.create_task(
    prompt="""Check top 5 casual mobile games competitors:
    1. Review sentiment analysis (last 7 days)
    2. New feature announcements
    3. Push notification complaints
    4. Monetization changes
    
    Summarize findings in bullet points.""",
    agent_profile="manus-1.6"
)
```

### 3. User Research (MoltFoundry.io / LYLY)
```python
task = client.create_task(
    prompt=f"""Research this new user: {company_name}
    
    Gather:
    - Company background
    - Social media presence
    - Content type
    - Audience size
    - Business model
    
    Create a 1-page profile PDF.""",
    agent_profile="manus-1.6"
)
```

## Cost Management

Monitor credit usage via the `credit_usage` field in task responses:

```python
task = client.get_task(task_id)
credits = task.get('credit_usage', 0)
print(f"Cost: {credits} credits")
```

**Optimization tips:**
- Use `manus-1.6-lite` for simple tasks (saves credits)
- Batch related tasks together
- Set reasonable timeouts to avoid runaway costs
- Track usage in daily logs

## Security

- ✅ API key stored in environment (not in code)
- ✅ Never commit API keys to git
- ✅ Results may contain sensitive data—handle appropriately
- ✅ Review outputs before forwarding to Mitch

## Troubleshooting

**Task timeout:**
- Increase `max_wait` parameter
- Use `wait_for_completion=False` and check URL manually
- Consider using `manus-1.6-max` for complex tasks

**Connection errors:**
- Verify API key is set: `echo $MANUS_API_KEY`
- Check Manus service status: https://manus.im
- Review API docs: https://open.manus.ai/docs

**Task failed:**
```python
task = client.get_task(task_id)
if task.get('status') == 'failed':
    print(f"Error: {task.get('error')}")
```

## Resources

- **API Docs:** https://open.manus.ai/docs
- **Web App:** https://manus.im/app
- **Support:** https://help.manus.im
- **Python Client:** `/root/clawd/skills/manus/manus_client.py`

## Next Steps

1. **Test real workflows** - Run `examples.py` to validate setup
2. **Configure connectors** - Set up LinkedIn, Similarweb in Manus web app
3. **Build orchestration** - Create higher-level wrappers in Portifoy's main codebase
4. **Monitor usage** - Track credits and optimize task delegation

---

**Last Updated:** 2026-02-13  
**Maintained By:** Portifoy ⚡

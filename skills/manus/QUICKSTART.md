# Manus Integration - Quick Start

**Status:** ✅ Ready to use  
**Setup:** Complete  
**API Key:** Configured in `.env.manus`

## 30-Second Usage

```python
# Source the API key
source /root/clawd/.env.manus

# Or in Python
from skills.manus.manus_client import ManusClient

client = ManusClient()

# Quick task with result
result = client.quick_task(
    prompt="Find 10 logistics companies in Pennsylvania",
    max_wait=180
)
print(result)
```

## Common Commands

### 1. Lead Generation
```python
task = client.create_task(
    prompt="Find 50 potential 3PL partners in PA with cold storage. Export as CSV.",
    agent_profile="manus-1.6",
    wait_for_completion=False
)
# Check: task['task_url']
```

### 2. Competitive Research
```python
result = client.quick_task(
    prompt="Analyze competitor game reviews from last 7 days. Focus on push notification complaints.",
    agent_profile="manus-1.6",
    max_wait=120
)
```

### 3. Batch Processing
```python
tasks = []
for company in companies:
    task = client.create_task(
        prompt=f"Research {company} and create 1-page profile",
        wait_for_completion=False
    )
    tasks.append(task)
```

## Agent Profiles

- **manus-1.6-lite** - Fast, cheap (simple tasks)
- **manus-1.6** - Balanced (default)
- **manus-1.6-max** - Powerful, thorough (complex research)

## When to Use Manus

✅ **Use Manus for:**
- LinkedIn scraping
- Browser automation (anti-bot bypass needed)
- Deep multi-source research
- Tasks requiring sandbox isolation

❌ **Use Portifoy for:**
- Local file operations
- Quick scripts
- Personal context/memory
- Direct system integration

## Files

- `manus_client.py` - Python wrapper
- `examples.py` - Usage examples
- `README.md` - Full documentation
- `SKILL.md` - Skill overview
- `.env.manus` - API key (secure)

## Resources

- **Docs:** https://open.manus.ai/docs
- **Web App:** https://manus.im/app
- **This Skill:** `/root/clawd/skills/manus/`

---

**Need help?** Read `README.md` or run `python3 examples.py`

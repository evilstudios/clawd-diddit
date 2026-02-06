# Instantly.ai API Key Troubleshooting

## Issue
The provided API key is returning `ERR_AUTH_FAILED` (401 error).

## API Key Provided
```
ZmY1YTRkZTktYmRiNC00N2ZiLWFmMzktN2JhNzg5YmNlYWI4Ok55ZWNTUWlOdUdYYQ==
```

Decoded to:
```
ff5a4de9-bdb4-47fb-af39-7ba789bceab8:NyecSQiNuGXa
```

## Tested Formats
❌ Base64 version - 401 error
❌ Decoded UUID only - 401 error
❌ Decoded full string - 401 error
❌ As Bearer token - 401 error
❌ With separate secret - 401 error

## Possible Issues

1. **Wrong API Key Type**
   - Instantly.ai might have changed their API key format
   - This might be an OAuth token, not an API key

2. **API Key Not Activated**
   - The key might need to be activated in Instantly dashboard
   - Check if there's a status toggle

3. **Wrong Account/Workspace**
   - API keys are workspace-specific
   - Make sure you're using the right workspace key

4. **API Key Expired**
   - Some keys have expiration dates
   - Check the creation date

## How to Get the Correct API Key

1. Log into Instantly.ai: https://app.instantly.ai
2. Go to **Settings** → **API & Integrations**
3. Look for **API Key** section
4. If there's a "Generate New Key" button, click it
5. Copy the FULL key (should be a long string)
6. It should look like: `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`

## Alternative: Check API Documentation

Visit: https://developer.instantly.ai/

Look for:
- Latest API authentication method
- Example requests
- API key format requirements

## What to Do Next

**Option 1: Get New API Key**
1. Regenerate API key in Instantly dashboard
2. Copy the new key
3. Paste it here

**Option 2: Use Instantly Dashboard**
- Upload leads manually via web interface
- Set up campaign through dashboard
- Use our scripts for monitoring only

**Option 3: Contact Instantly Support**
- support@instantly.ai
- Ask about API key authentication format

## Meanwhile: Alternative Approach

You can still launch the campaign manually:

1. **Export your leads CSV**
2. **Go to Instantly dashboard**
3. **Create campaign** → Upload CSV
4. **Copy email sequences** from `/root/clawd/projects/voxable-cold-outreach/final-sequences.md`
5. **Set up schedule** (Mon-Fri, 9am-5pm, 30-40 emails/day)
6. **Launch!**

Then use our tracker script once you have valid API access.

---

## Test Script

Once you have a new key, test it:

```bash
python3 -c "
import requests
api_key = 'YOUR_NEW_KEY_HERE'
response = requests.get('https://api.instantly.ai/api/v1/campaign/list', params={'api_key': api_key})
print(f'Status: {response.status_code}')
print(response.json() if response.status_code == 200 else response.text)
"
```

If you see `Status: 200`, you're good to go!

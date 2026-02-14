# Twitter Automation Tool

Automated Twitter posting tool using Twitter API v2.

## Setup

Install dependencies:
```bash
pip3 install requests-oauthlib
```

## Usage

### Check Authentication
```bash
python3 twitter-poster.py me
```

### Post a Tweet
```bash
python3 twitter-poster.py post --text "Your tweet text here"
```

### Get Recent Tweets
```bash
python3 twitter-poster.py recent --max-results 10
```

### Delete a Tweet
```bash
python3 twitter-poster.py delete --tweet-id TWEET_ID
```

### Get JSON Output
Add `--json` flag to any command for raw JSON response:
```bash
python3 twitter-poster.py me --json
```

## Features

- ✅ Post tweets
- ✅ Delete tweets
- ✅ Get user info
- ✅ Fetch recent tweets with metrics
- ✅ OAuth 1.0a authentication
- ✅ Twitter API v2 endpoints

## Credentials

Credentials are embedded in the script:
- Consumer Key: `qnuZrAAsXcAvcpmTY3yMQQXGe`
- Access Token: `2021426499317018624-PyI1GqkBQPNlOD2rSITqGBS71SUAa3`

## Examples

### Post a simple tweet
```bash
python3 twitter-poster.py post --text "Building automation tools with Clawdbot! 🤖"
```

### Check who you're authenticated as
```bash
python3 twitter-poster.py me
```

### View your 5 most recent tweets
```bash
python3 twitter-poster.py recent --max-results 5
```

## Future Enhancements

- [ ] Media upload support
- [ ] Scheduled posting
- [ ] Thread support
- [ ] Reply functionality
- [ ] Search and monitoring
- [ ] Rate limit handling
- [ ] Retry logic with exponential backoff

## Integration Ideas

- Schedule tweets via cron jobs
- Auto-post Evil Apples content
- Monitor mentions and auto-respond
- Track engagement metrics
- Cross-post from other platforms

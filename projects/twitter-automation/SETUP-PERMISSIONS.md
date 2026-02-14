# Twitter App Permissions Setup

The Twitter bot needs **Read and Write** permissions to post tweets.

## 🔧 Fix Permissions

1. Go to [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard)

2. Click on your app (the one with Consumer Key: `qnuZrAAsXcAvcpmTY3yMQQXGe`)

3. Go to **"User authentication settings"** or **"App permissions"**

4. Change from **"Read-only"** to **"Read and Write"**

5. **IMPORTANT**: After changing permissions, you must **regenerate your Access Token & Secret**:
   - Go to "Keys and tokens"
   - Click "Regenerate" under "Access Token and Secret"
   - Save the new tokens

6. Update the credentials in `auto-tweet.py`:
   - Replace `ACCESS_TOKEN`
   - Replace `ACCESS_TOKEN_SECRET`

## 📋 Current Status

Your app currently has:
- ❌ **Read-only permissions** (can't post)
- ✅ Consumer Key/Secret are valid

## ✅ After Fixing

You'll be able to:
- Post tweets
- Delete tweets
- Reply to tweets
- All other write operations

## 🧪 Test After Setup

```bash
# Test authentication
python3 twitter-poster.py me

# Try posting (will work after permission fix)
python3 auto-tweet.py --category tech_insights
```

## 🔍 Verify Permissions

You can check current permissions with:
```bash
python3 twitter-poster.py me --json
```

Look for the permissions scope in the response.

## 📝 Notes

- Changing permissions doesn't affect Consumer Key/Secret
- Only Access Token/Secret need regeneration
- This is a one-time setup
- Once fixed, automation will work immediately

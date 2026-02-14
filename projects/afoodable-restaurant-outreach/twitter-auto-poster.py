#!/usr/bin/env python3
"""
Afoodable Twitter Auto-Poster
Posts to Twitter/X automatically with smart content rotation
Supports both single tweets and threads
"""

import json
import random
import os
import sys
from datetime import datetime
from pathlib import Path

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from afoodable_content_library import CONTENT_LIBRARY, format_content, LANDING_PAGE_URL

# Configuration
HISTORY_FILE = "twitter-post-history.json"
MAX_HISTORY = 100
DRY_RUN = os.getenv("DRY_RUN", "false").lower() == "true"

# Twitter API credentials (set via environment variables)
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY", "")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET", "")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN", "")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET", "")

def load_history():
    """Load posting history to prevent duplicates"""
    if not Path(HISTORY_FILE).exists():
        return []
    
    try:
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    except:
        return []

def save_history(history):
    """Save posting history"""
    # Keep only recent entries
    recent = history[-MAX_HISTORY:] if len(history) > MAX_HISTORY else history
    
    with open(HISTORY_FILE, 'w') as f:
        json.dump(recent, f, indent=2)

def get_recent_categories(history, limit=10):
    """Get recently used categories"""
    return [entry['category'] for entry in history[-limit:]]

def select_content():
    """Select next tweet using smart rotation"""
    history = load_history()
    recent_cats = get_recent_categories(history)
    
    # Get all Twitter content
    all_content = CONTENT_LIBRARY.get('twitter', [])
    
    if not all_content:
        raise Exception("No content available in library")
    
    # Filter out recently used categories
    available = [c for c in all_content if c['category'] not in recent_cats]
    
    # If all have been used recently, reset and use all
    if not available:
        available = all_content
    
    # Select random from available
    selected = random.choice(available)
    
    return selected

def post_to_twitter(content, category, is_thread=False):
    """Post content to Twitter"""
    if DRY_RUN:
        print("🧪 DRY RUN MODE - Would post:")
        print(f"   Category: {category}")
        print(f"   Type: {'Thread' if is_thread else 'Single Tweet'}")
        if is_thread:
            for i, tweet in enumerate(content, 1):
                print(f"\n   Tweet {i}/{len(content)}:")
                print(f"   {tweet[:100]}...")
        else:
            print(f"   Content:\n   {content[:200]}...")
        return [{"id": f"dryrun_{int(datetime.now().timestamp())}_{i}"} for i in range(len(content) if is_thread else 1)]
    
    if not all([TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET]):
        raise Exception("Twitter credentials not configured. Set TWITTER_API_KEY, TWITTER_API_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET")
    
    # TODO: Implement actual Twitter API v2 posting
    # This is a placeholder - needs tweepy or requests library
    """
    import tweepy
    
    client = tweepy.Client(
        consumer_key=TWITTER_API_KEY,
        consumer_secret=TWITTER_API_SECRET,
        access_token=TWITTER_ACCESS_TOKEN,
        access_token_secret=TWITTER_ACCESS_SECRET
    )
    
    if is_thread:
        results = []
        reply_to = None
        for tweet in content:
            response = client.create_tweet(
                text=tweet,
                in_reply_to_tweet_id=reply_to
            )
            results.append(response.data)
            reply_to = response.data['id']
        return results
    else:
        response = client.create_tweet(text=content)
        return [response.data]
    """
    
    raise Exception("Twitter API integration not yet implemented. Run with DRY_RUN=true to test content selection.")

def main():
    """Main posting function"""
    print("🐦 Afoodable Twitter Auto-Poster")
    print(f"   Mode: {'DRY RUN' if DRY_RUN else 'LIVE POSTING'}")
    print(f"   Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    try:
        # Select content
        selected = select_content()
        category = selected['category']
        
        # Check if it's a thread
        is_thread = 'tweets' in selected
        
        if is_thread:
            # Format thread tweets
            formatted = format_content(selected, LANDING_PAGE_URL)
            print(f"📝 Selected Category: {category} (THREAD)")
            print(f"📊 Tweets in thread: {len(formatted)}\n")
            print("=" * 60)
            for i, tweet in enumerate(formatted, 1):
                print(f"\nTweet {i}/{len(formatted)}:")
                print(tweet)
                print("-" * 60)
        else:
            # Format single tweet
            formatted = format_content(selected, LANDING_PAGE_URL)
            print(f"📝 Selected Category: {category} (SINGLE TWEET)")
            print()
            print("=" * 60)
            print(formatted)
            print("=" * 60)
        
        # Post to Twitter
        results = post_to_twitter(
            formatted if is_thread else [formatted],
            category,
            is_thread=is_thread
        )
        
        # Save to history
        history = load_history()
        history.append({
            "timestamp": datetime.now().isoformat(),
            "category": category,
            "type": "thread" if is_thread else "single",
            "tweet_ids": [r.get('id', 'unknown') for r in results],
            "content_preview": formatted[0][:100] if is_thread else formatted[:100]
        })
        save_history(history)
        
        print(f"\n✅ Posted successfully!")
        if is_thread:
            print(f"   Thread ID: {results[0].get('id', 'unknown')}")
            print(f"   Total tweets: {len(results)}")
        else:
            print(f"   Tweet ID: {results[0].get('id', 'unknown')}")
        print(f"   Category: {category}")
        
        return 0
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return 1

if __name__ == "__main__":
    exit(main())

#!/usr/bin/env python3
"""
Twitter Thread Poster
Post multi-tweet threads with automatic reply chaining
"""

import os
import sys
import json
import time
from requests_oauthlib import OAuth1Session

# Twitter API credentials
CONSUMER_KEY = "qnuZrAAsXcAvcpmTY3yMQQXGe"
CONSUMER_SECRET = "C4pzqaqfGu8Vz8FwVdWpIKyoKxcdWFAbvLMU9971KffwXcP4t1"
ACCESS_TOKEN = "2021426499317018624-4qUWIkj9GUybgL3nAhYYs0Im4Hjijq"
ACCESS_TOKEN_SECRET = "smrhgjhdfMKft3yB78aZPLBp6SIXNEUpvpxMVgpswbE2f"


class ThreadPoster:
    def __init__(self):
        self.oauth = OAuth1Session(
            CONSUMER_KEY,
            client_secret=CONSUMER_SECRET,
            resource_owner_key=ACCESS_TOKEN,
            resource_owner_secret=ACCESS_TOKEN_SECRET,
        )
        self.base_url = "https://api.twitter.com/2"

    def post_tweet(self, text, reply_to=None, media_ids=None):
        """Post a single tweet, optionally as a reply"""
        endpoint = f"{self.base_url}/tweets"
        
        payload = {"text": text}
        
        if reply_to:
            payload["reply"] = {"in_reply_to_tweet_id": reply_to}
        
        if media_ids:
            payload["media"] = {"media_ids": media_ids}
        
        response = self.oauth.post(endpoint, json=payload)
        
        if response.status_code == 201:
            tweet = response.json()
            return {
                "success": True,
                "tweet_id": tweet["data"]["id"],
                "text": tweet["data"]["text"]
            }
        else:
            return {
                "success": False,
                "error": response.text,
                "status_code": response.status_code
            }

    def post_thread(self, tweets, delay=2):
        """
        Post a thread of tweets
        tweets: list of strings or dicts with 'text' and optional 'media_ids'
        delay: seconds to wait between tweets (avoid rate limits)
        """
        results = []
        previous_tweet_id = None
        
        for i, tweet in enumerate(tweets, 1):
            # Handle both string and dict formats
            if isinstance(tweet, str):
                text = tweet
                media_ids = None
            else:
                text = tweet.get("text", tweet.get("content", ""))
                media_ids = tweet.get("media_ids")
            
            print(f"Posting tweet {i}/{len(tweets)}...")
            
            result = self.post_tweet(
                text=text,
                reply_to=previous_tweet_id,
                media_ids=media_ids
            )
            
            results.append(result)
            
            if result["success"]:
                previous_tweet_id = result["tweet_id"]
                print(f"  ✓ Posted: {result['tweet_id']}")
                
                # Wait between tweets (except after last one)
                if i < len(tweets):
                    time.sleep(delay)
            else:
                print(f"  ✗ Failed: {result['error']}", file=sys.stderr)
                break
        
        return {
            "success": all(r["success"] for r in results),
            "thread_id": results[0]["tweet_id"] if results and results[0]["success"] else None,
            "tweets": results
        }


def parse_thread_file(file_path):
    """
    Parse thread from a file
    Supports:
    - Plain text (one tweet per line, empty lines ignored)
    - JSON (array of strings or objects)
    - Markdown (tweets separated by ---)
    """
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Try JSON first
    if file_path.endswith('.json'):
        return json.loads(content)
    
    # Check for markdown separators
    if '---' in content:
        tweets = [t.strip() for t in content.split('---') if t.strip()]
        return tweets
    
    # Plain text - one tweet per line or paragraph
    tweets = []
    current = []
    
    for line in content.split('\n'):
        line = line.strip()
        if not line:
            if current:
                tweets.append(' '.join(current))
                current = []
        else:
            current.append(line)
    
    if current:
        tweets.append(' '.join(current))
    
    return tweets


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Post Twitter threads")
    parser.add_argument("--file", help="Read thread from file")
    parser.add_argument("--tweets", nargs="+", help="Tweet texts (space-separated)")
    parser.add_argument("--delay", type=int, default=2,
                        help="Delay between tweets in seconds")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show thread without posting")
    parser.add_argument("--json", action="store_true",
                        help="Output JSON response")
    
    args = parser.parse_args()
    
    # Get tweets
    if args.file:
        tweets = parse_thread_file(args.file)
    elif args.tweets:
        tweets = args.tweets
    else:
        print("Error: Provide --file or --tweets", file=sys.stderr)
        sys.exit(1)
    
    if not tweets:
        print("Error: No tweets found", file=sys.stderr)
        sys.exit(1)
    
    # Dry run - just show the thread
    if args.dry_run:
        print(f"[DRY RUN] Thread with {len(tweets)} tweets:\n")
        for i, tweet in enumerate(tweets, 1):
            text = tweet if isinstance(tweet, str) else tweet.get("text", "")
            print(f"{i}. {text}")
            print()
        sys.exit(0)
    
    # Post the thread
    poster = ThreadPoster()
    result = poster.post_thread(tweets, delay=args.delay)
    
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print()
        if result["success"]:
            print(f"✅ Thread posted successfully!")
            print(f"   Thread ID: {result['thread_id']}")
            print(f"   Tweets: {len(result['tweets'])}")
            print(f"   URL: https://twitter.com/moltfoundry/status/{result['thread_id']}")
        else:
            print(f"❌ Thread posting failed")
            print(f"   Posted: {sum(1 for t in result['tweets'] if t['success'])}/{len(result['tweets'])}")


if __name__ == "__main__":
    main()

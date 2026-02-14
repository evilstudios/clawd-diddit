#!/usr/bin/env python3
"""
Twitter Automation Tool
Handles posting tweets, scheduling, and Twitter API v2 operations
"""

import os
import sys
import json
import argparse
from datetime import datetime
from requests_oauthlib import OAuth1Session

# Twitter API credentials
CONSUMER_KEY = "qnuZrAAsXcAvcpmTY3yMQQXGe"
CONSUMER_SECRET = "C4pzqaqfGu8Vz8FwVdWpIKyoKxcdWFAbvLMU9971KffwXcP4t1"
ACCESS_TOKEN = "2021426499317018624-4qUWIkj9GUybgL3nAhYYs0Im4Hjijq"
ACCESS_TOKEN_SECRET = "smrhgjhdfMKft3yB78aZPLBp6SIXNEUpvpxMVgpswbE2f"


class TwitterPoster:
    def __init__(self):
        self.oauth = OAuth1Session(
            CONSUMER_KEY,
            client_secret=CONSUMER_SECRET,
            resource_owner_key=ACCESS_TOKEN,
            resource_owner_secret=ACCESS_TOKEN_SECRET,
        )
        self.base_url = "https://api.twitter.com/2"

    def post_tweet(self, text, media_ids=None, reply_to=None):
        """Post a tweet with optional media and reply context"""
        endpoint = f"{self.base_url}/tweets"
        
        payload = {"text": text}
        
        if media_ids:
            payload["media"] = {"media_ids": media_ids}
        
        if reply_to:
            payload["reply"] = {"in_reply_to_tweet_id": reply_to}
        
        response = self.oauth.post(endpoint, json=payload)
        
        if response.status_code == 201:
            tweet = response.json()
            return {
                "success": True,
                "tweet_id": tweet["data"]["id"],
                "tweet": tweet["data"]
            }
        else:
            return {
                "success": False,
                "error": response.text,
                "status_code": response.status_code
            }

    def get_me(self):
        """Get authenticated user info"""
        endpoint = f"{self.base_url}/users/me"
        params = {"user.fields": "id,name,username,description,profile_image_url"}
        
        response = self.oauth.get(endpoint, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.text, "status_code": response.status_code}

    def delete_tweet(self, tweet_id):
        """Delete a tweet by ID"""
        endpoint = f"{self.base_url}/tweets/{tweet_id}"
        response = self.oauth.delete(endpoint)
        
        if response.status_code == 200:
            return {"success": True, "deleted": True}
        else:
            return {
                "success": False,
                "error": response.text,
                "status_code": response.status_code
            }

    def get_recent_tweets(self, user_id=None, max_results=10):
        """Get recent tweets from user timeline"""
        if not user_id:
            # Get own user ID first
            me = self.get_me()
            if "data" in me:
                user_id = me["data"]["id"]
            else:
                return {"error": "Could not get user ID"}
        
        endpoint = f"{self.base_url}/users/{user_id}/tweets"
        params = {
            "max_results": max_results,
            "tweet.fields": "created_at,public_metrics,text"
        }
        
        response = self.oauth.get(endpoint, params=params)
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.text, "status_code": response.status_code}


def main():
    parser = argparse.ArgumentParser(description="Twitter Automation Tool")
    parser.add_argument("action", choices=["post", "delete", "me", "recent"], 
                        help="Action to perform")
    parser.add_argument("--text", help="Tweet text (for post action)")
    parser.add_argument("--tweet-id", help="Tweet ID (for delete action)")
    parser.add_argument("--max-results", type=int, default=10, 
                        help="Max results for recent tweets")
    parser.add_argument("--json", action="store_true", 
                        help="Output raw JSON response")
    
    args = parser.parse_args()
    
    twitter = TwitterPoster()
    
    if args.action == "post":
        if not args.text:
            print("Error: --text is required for posting", file=sys.stderr)
            sys.exit(1)
        
        result = twitter.post_tweet(args.text)
        
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            if result["success"]:
                print(f"✓ Tweet posted successfully!")
                print(f"  Tweet ID: {result['tweet_id']}")
                print(f"  Text: {result['tweet']['text']}")
            else:
                print(f"✗ Failed to post tweet", file=sys.stderr)
                print(f"  Error: {result['error']}", file=sys.stderr)
                sys.exit(1)
    
    elif args.action == "delete":
        if not args.tweet_id:
            print("Error: --tweet-id is required for deleting", file=sys.stderr)
            sys.exit(1)
        
        result = twitter.delete_tweet(args.tweet_id)
        
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            if result["success"]:
                print(f"✓ Tweet {args.tweet_id} deleted successfully!")
            else:
                print(f"✗ Failed to delete tweet", file=sys.stderr)
                print(f"  Error: {result['error']}", file=sys.stderr)
                sys.exit(1)
    
    elif args.action == "me":
        result = twitter.get_me()
        
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            if "data" in result:
                data = result["data"]
                print(f"✓ Authenticated as:")
                print(f"  Name: {data['name']}")
                print(f"  Username: @{data['username']}")
                print(f"  ID: {data['id']}")
                if "description" in data:
                    print(f"  Bio: {data['description']}")
            else:
                print(f"✗ Failed to get user info", file=sys.stderr)
                print(json.dumps(result, indent=2), file=sys.stderr)
                sys.exit(1)
    
    elif args.action == "recent":
        result = twitter.get_recent_tweets(max_results=args.max_results)
        
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            if "data" in result:
                print(f"✓ Recent tweets:")
                for tweet in result["data"]:
                    print(f"\n  [{tweet['id']}] {tweet['created_at']}")
                    print(f"  {tweet['text'][:100]}...")
                    metrics = tweet.get("public_metrics", {})
                    print(f"  ❤️ {metrics.get('like_count', 0)} | "
                          f"🔄 {metrics.get('retweet_count', 0)} | "
                          f"💬 {metrics.get('reply_count', 0)}")
            else:
                print(f"✗ Failed to get recent tweets", file=sys.stderr)
                print(json.dumps(result, indent=2), file=sys.stderr)
                sys.exit(1)


if __name__ == "__main__":
    main()

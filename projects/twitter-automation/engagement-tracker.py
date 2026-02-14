#!/usr/bin/env python3
"""
Twitter Engagement Tracker
Track likes, retweets, replies, and engagement rates over time
"""

import os
import sys
import json
from datetime import datetime, timedelta
from requests_oauthlib import OAuth1Session

# Twitter API credentials
CONSUMER_KEY = "qnuZrAAsXcAvcpmTY3yMQQXGe"
CONSUMER_SECRET = "C4pzqaqfGu8Vz8FwVdWpIKyoKxcdWFAbvLMU9971KffwXcP4t1"
ACCESS_TOKEN = "2021426499317018624-4qUWIkj9GUybgL3nAhYYs0Im4Hjijq"
ACCESS_TOKEN_SECRET = "smrhgjhdfMKft3yB78aZPLBp6SIXNEUpvpxMVgpswbE2f"


class EngagementTracker:
    def __init__(self):
        self.oauth = OAuth1Session(
            CONSUMER_KEY,
            client_secret=CONSUMER_SECRET,
            resource_owner_key=ACCESS_TOKEN,
            resource_owner_secret=ACCESS_TOKEN_SECRET,
        )
        self.base_url = "https://api.twitter.com/2"
        self.metrics_file = "engagement_metrics.json"

    def get_user_id(self):
        """Get authenticated user ID"""
        endpoint = f"{self.base_url}/users/me"
        response = self.oauth.get(endpoint)
        
        if response.status_code == 200:
            return response.json()["data"]["id"]
        return None

    def get_recent_tweets(self, user_id, max_results=100, days_back=7):
        """Get recent tweets with full metrics"""
        endpoint = f"{self.base_url}/users/{user_id}/tweets"
        
        start_time = (datetime.now() - timedelta(days=days_back)).isoformat() + "Z"
        
        params = {
            "max_results": min(max_results, 100),
            "start_time": start_time,
            "tweet.fields": "created_at,public_metrics,text",
            "expansions": "attachments.media_keys",
            "media.fields": "type,url"
        }
        
        response = self.oauth.get(endpoint, params=params)
        
        if response.status_code == 200:
            return response.json()
        return None

    def calculate_engagement_rate(self, metrics):
        """Calculate engagement rate from public metrics"""
        impressions = metrics.get("impression_count", 0)
        if impressions == 0:
            return 0.0
        
        engagements = (
            metrics.get("like_count", 0) +
            metrics.get("retweet_count", 0) +
            metrics.get("reply_count", 0) +
            metrics.get("quote_count", 0)
        )
        
        return (engagements / impressions) * 100

    def analyze_tweets(self, tweets_data):
        """Analyze tweet performance"""
        if not tweets_data or "data" not in tweets_data:
            return None
        
        tweets = tweets_data["data"]
        
        total_likes = 0
        total_retweets = 0
        total_replies = 0
        total_quotes = 0
        total_impressions = 0
        
        best_performing = None
        best_engagement_rate = 0
        
        for tweet in tweets:
            metrics = tweet.get("public_metrics", {})
            
            likes = metrics.get("like_count", 0)
            retweets = metrics.get("retweet_count", 0)
            replies = metrics.get("reply_count", 0)
            quotes = metrics.get("quote_count", 0)
            impressions = metrics.get("impression_count", 0)
            
            total_likes += likes
            total_retweets += retweets
            total_replies += replies
            total_quotes += quotes
            total_impressions += impressions
            
            engagement_rate = self.calculate_engagement_rate(metrics)
            
            if engagement_rate > best_engagement_rate:
                best_engagement_rate = engagement_rate
                best_performing = {
                    "id": tweet["id"],
                    "text": tweet["text"][:100],
                    "engagement_rate": engagement_rate,
                    "metrics": metrics
                }
        
        avg_engagement_rate = 0
        if total_impressions > 0:
            total_engagements = total_likes + total_retweets + total_replies + total_quotes
            avg_engagement_rate = (total_engagements / total_impressions) * 100
        
        return {
            "total_tweets": len(tweets),
            "total_likes": total_likes,
            "total_retweets": total_retweets,
            "total_replies": total_replies,
            "total_quotes": total_quotes,
            "total_impressions": total_impressions,
            "avg_likes": total_likes / len(tweets) if tweets else 0,
            "avg_retweets": total_retweets / len(tweets) if tweets else 0,
            "avg_engagement_rate": avg_engagement_rate,
            "best_performing": best_performing
        }

    def save_metrics(self, analysis):
        """Save metrics to file for historical tracking"""
        history = []
        
        if os.path.exists(self.metrics_file):
            with open(self.metrics_file, 'r') as f:
                history = json.load(f)
        
        history.append({
            "timestamp": datetime.now().isoformat(),
            "analysis": analysis
        })
        
        # Keep last 30 days
        if len(history) > 30:
            history = history[-30:]
        
        with open(self.metrics_file, 'w') as f:
            json.dump(history, f, indent=2)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Track Twitter engagement")
    parser.add_argument("--days", type=int, default=7,
                        help="Days to look back (default: 7)")
    parser.add_argument("--max-results", type=int, default=100,
                        help="Max tweets to analyze (default: 100)")
    parser.add_argument("--save", action="store_true",
                        help="Save metrics to history file")
    parser.add_argument("--json", action="store_true",
                        help="Output JSON")
    
    args = parser.parse_args()
    
    tracker = EngagementTracker()
    
    print("Fetching tweets...")
    user_id = tracker.get_user_id()
    
    if not user_id:
        print("Error: Could not get user ID", file=sys.stderr)
        sys.exit(1)
    
    tweets_data = tracker.get_recent_tweets(
        user_id,
        max_results=args.max_results,
        days_back=args.days
    )
    
    if not tweets_data:
        print("Error: Could not fetch tweets", file=sys.stderr)
        sys.exit(1)
    
    print("Analyzing engagement...")
    analysis = tracker.analyze_tweets(tweets_data)
    
    if args.save:
        tracker.save_metrics(analysis)
        print("Metrics saved to", tracker.metrics_file)
    
    if args.json:
        print(json.dumps(analysis, indent=2))
    else:
        print("\n" + "="*60)
        print(f"📊 ENGAGEMENT REPORT (Last {args.days} days)")
        print("="*60)
        
        print(f"\n📈 Overview:")
        print(f"   Total tweets: {analysis['total_tweets']}")
        print(f"   Total impressions: {analysis['total_impressions']:,}")
        print(f"   Avg engagement rate: {analysis['avg_engagement_rate']:.2f}%")
        
        print(f"\n💚 Likes:")
        print(f"   Total: {analysis['total_likes']:,}")
        print(f"   Average: {analysis['avg_likes']:.1f} per tweet")
        
        print(f"\n🔄 Retweets:")
        print(f"   Total: {analysis['total_retweets']:,}")
        print(f"   Average: {analysis['avg_retweets']:.1f} per tweet")
        
        print(f"\n💬 Replies:")
        print(f"   Total: {analysis['total_replies']:,}")
        
        if analysis['best_performing']:
            bp = analysis['best_performing']
            print(f"\n🏆 Best Performing Tweet:")
            print(f"   Engagement rate: {bp['engagement_rate']:.2f}%")
            print(f"   Tweet: {bp['text']}...")
            print(f"   Likes: {bp['metrics'].get('like_count', 0)}")
            print(f"   Retweets: {bp['metrics'].get('retweet_count', 0)}")
            print(f"   URL: https://twitter.com/moltfoundry/status/{bp['id']}")
        
        print("\n" + "="*60 + "\n")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Auto-Tweet Bot
Automatically posts engaging tweets about your products/projects
"""

import os
import sys
import json
import random
from datetime import datetime
from requests_oauthlib import OAuth1Session

# Twitter API credentials
CONSUMER_KEY = "qnuZrAAsXcAvcpmTY3yMQQXGe"
CONSUMER_SECRET = "C4pzqaqfGu8Vz8FwVdWpIKyoKxcdWFAbvLMU9971KffwXcP4t1"
ACCESS_TOKEN = "2021426499317018624-4qUWIkj9GUybgL3nAhYYs0Im4Hjijq"
ACCESS_TOKEN_SECRET = "smrhgjhdfMKft3yB78aZPLBp6SIXNEUpvpxMVgpswbE2f"


# Tweet templates for different content types
TWEET_TEMPLATES = {
    "evil_apples": [
        "Playing Evil Apples? Drop your most savage card combo below! 😈🍎",
        "That moment when you draw the PERFECT answer card in Evil Apples... 🔥",
        "Evil Apples: Where friendships are tested and savage humor wins. Download now! 🍎😈",
        "New to Evil Apples? Fair warning: you're about to discover who your friends really are. 💀",
        "Just played Evil Apples and I can't believe someone actually submitted that... 😂🍎",
        "Evil Apples is trending! Join thousands of players creating hilariously offensive card combos. 🎮",
        "Pro tip: The most offensive card usually wins in Evil Apples. You've been warned. 🍎",
    ],
    
    "wellplate_ai": [
        "WellPlate AI: Making nutrition tracking actually useful. No more calorie counting nightmares. 🍽️🤖",
        "Tired of generic meal plans? WellPlate AI personalizes everything based on YOUR goals. Try it free!",
        "WellPlate AI just analyzed my weekly meals and... wow. Time to make some changes! 📊",
        "The future of nutrition is AI-powered and it's here. Check out WellPlate AI! 🚀",
        "WellPlate AI makes meal planning so easy, you'll actually stick to your goals. Finally. 💪",
    ],
    
    "molt_foundry": [
        "Most OpenClaw instances are empty shells. MoltFoundry provides the SOUL for your agent. 🤖✨",
        "Building AI agents? MoltFoundry turns your Claw instance into something actually intelligent. 🧠",
        "The difference between a basic bot and a brilliant agent? MoltFoundry. Simple as that. ⚡",
        "Self-hosted AI agents that actually work. That's the MoltFoundry promise. 🔧",
        "Your agent isn't dumb. It's just missing its soul. MoltFoundry fixes that. 🦗",
    ],
    
    "tech_insights": [
        "Hot take: The best automation is the one you actually use. Build simple, iterate fast. 🚀",
        "Building in public is scary. Shipping broken things is scarier. Not shipping at all? Scariest. 📦",
        "Your side project doesn't need to be perfect. It needs to exist. Ship it. 🎯",
        "The best time to start your SaaS was 5 years ago. The second best time is right now. 💻",
        "Stop planning. Start building. Feedback from real users > 100 perfect mockups. 🔨",
        "Automation tip: If you do it 3x, automate it. Your future self will thank you. ⚙️",
    ],
    
    "engagement": [
        "What's the most useful automation you've built recently? Drop it below! 🤖👇",
        "Building: Evil Apples, WellPlate AI, Afoodable, Wine Monkey, and more. What are you working on? 🚀",
        "Indie dev life: Coffee, code, ship, repeat. What's your routine? ☕💻",
        "Quick poll: What's harder - finding users or building the product? 🤔",
        "Shoutout to everyone grinding on their projects this week. We're all gonna make it. 💪",
    ],
}


class AutoTweeter:
    def __init__(self):
        self.oauth = OAuth1Session(
            CONSUMER_KEY,
            client_secret=CONSUMER_SECRET,
            resource_owner_key=ACCESS_TOKEN,
            resource_owner_secret=ACCESS_TOKEN_SECRET,
        )
        self.base_url = "https://api.twitter.com/2"
        self.history_file = "tweet_history.json"
        self.history = self.load_history()

    def load_history(self):
        """Load tweet history to avoid duplicates"""
        if os.path.exists(self.history_file):
            with open(self.history_file, 'r') as f:
                return json.load(f)
        return {"tweets": []}

    def save_history(self, tweet_text, tweet_id):
        """Save posted tweet to history"""
        self.history["tweets"].append({
            "text": tweet_text,
            "tweet_id": tweet_id,
            "posted_at": datetime.now().isoformat()
        })
        # Keep only last 100 tweets
        if len(self.history["tweets"]) > 100:
            self.history["tweets"] = self.history["tweets"][-100:]
        
        with open(self.history_file, 'w') as f:
            json.dump(self.history, f, indent=2)

    def get_random_tweet(self, category=None):
        """Get a random tweet that hasn't been posted recently"""
        if category and category in TWEET_TEMPLATES:
            templates = TWEET_TEMPLATES[category]
        else:
            # Pick random category
            templates = []
            for category_templates in TWEET_TEMPLATES.values():
                templates.extend(category_templates)
        
        # Filter out recently posted tweets (last 50)
        recent_tweets = {t["text"] for t in self.history["tweets"][-50:]}
        available_tweets = [t for t in templates if t not in recent_tweets]
        
        if not available_tweets:
            # If all tweets were recent, just use any
            available_tweets = templates
        
        return random.choice(available_tweets)

    def post_tweet(self, text):
        """Post a tweet"""
        endpoint = f"{self.base_url}/tweets"
        payload = {"text": text}
        
        response = self.oauth.post(endpoint, json=payload)
        
        if response.status_code == 201:
            tweet = response.json()
            tweet_id = tweet["data"]["id"]
            self.save_history(text, tweet_id)
            return {
                "success": True,
                "tweet_id": tweet_id,
                "text": text
            }
        else:
            return {
                "success": False,
                "error": response.text,
                "status_code": response.status_code
            }


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Auto-Tweet Bot")
    parser.add_argument("--category", 
                        choices=list(TWEET_TEMPLATES.keys()) + ["random"],
                        default="random",
                        help="Tweet category")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show tweet without posting")
    parser.add_argument("--list-categories", action="store_true",
                        help="List available categories")
    
    args = parser.parse_args()
    
    if args.list_categories:
        print("Available categories:")
        for category, templates in TWEET_TEMPLATES.items():
            print(f"\n{category}:")
            print(f"  {len(templates)} templates")
        sys.exit(0)
    
    tweeter = AutoTweeter()
    
    category = args.category if args.category != "random" else None
    tweet_text = tweeter.get_random_tweet(category)
    
    if args.dry_run:
        print(f"[DRY RUN] Would post:")
        print(f"\n  {tweet_text}\n")
        sys.exit(0)
    
    print(f"Posting tweet: {tweet_text[:60]}...")
    result = tweeter.post_tweet(tweet_text)
    
    if result["success"]:
        print(f"\n✅ Tweet posted successfully!")
        print(f"   ID: {result['tweet_id']}")
        print(f"   Text: {result['text']}")
        print(f"   URL: https://twitter.com/moltfoundry/status/{result['tweet_id']}")
    else:
        print(f"\n❌ Failed to post tweet")
        print(f"   Error: {result['error']}")
        sys.exit(1)


if __name__ == "__main__":
    main()

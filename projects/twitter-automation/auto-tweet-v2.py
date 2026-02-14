#!/usr/bin/env python3
"""
Auto-Tweet Bot v2
Enhanced version with Evil Apples integration, time-based selection, and A/B testing
"""

import os
import sys
import json
import random
from datetime import datetime
from requests_oauthlib import OAuth1Session

# Import Evil Apples generator
import importlib.util
spec = importlib.util.spec_from_file_location("ea_gen", "evil-apples-generator.py")
ea_gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ea_gen)

# Twitter API credentials
CONSUMER_KEY = "qnuZrAAsXcAvcpmTY3yMQQXGe"
CONSUMER_SECRET = "C4pzqaqfGu8Vz8FwVdWpIKyoKxcdWFAbvLMU9971KffwXcP4t1"
ACCESS_TOKEN = "2021426499317018624-4qUWIkj9GUybgL3nAhYYs0Im4Hjijq"
ACCESS_TOKEN_SECRET = "smrhgjhdfMKft3yB78aZPLBp6SIXNEUpvpxMVgpswbE2f"


# Tweet templates organized by time of day preference
MORNING_TWEETS = [
    "Good morning builders! What are you shipping today? 🚀☕",
    "Starting the day with coffee and code. Perfect combo. ☕💻",
    "The best automation is the one you build before your first coffee. ⚙️",
    "Morning motivation: Your side project doesn't need to be perfect. Just ship it. 🎯",
    "WellPlate AI making meal prep easier since... well, since breakfast. 🍳🤖",
]

AFTERNOON_TWEETS = [
    "Afternoon check-in: Still grinding or already shipping? 💪",
    "That mid-day productivity dip? Perfect time for Evil Apples. 😈🍎",
    "Building in public update: Progress > Perfection. Always. 📊",
    "Quick reminder: Automation saves time. Time builds empires. ⚡",
    "WellPlate AI users reporting 40% better meal consistency. Science works. 📈",
]

EVENING_TWEETS = [
    "End of day reflection: What did you ship? What did you learn? 🌅",
    "Evening wind-down with Evil Apples hits different. Try it. 🍎",
    "Most OpenClaw instances are empty shells. MoltFoundry gives them SOUL. 🦗✨",
    "Hot take: The best code is code that ships. Evening deployment anyone? 🚀",
    "Wine Monkey tip: Pair your evening wine with productivity metrics. 🍷📊",
]

# Standard templates from v1
STANDARD_TEMPLATES = {
    "evil_apples": [
        "Playing Evil Apples? Drop your most savage card combo below! 😈🍎",
        "That moment when you draw the PERFECT answer card in Evil Apples... 🔥",
        "New to Evil Apples? Fair warning: you're about to discover who your friends really are. 💀",
    ],
    "wellplate_ai": [
        "Tired of generic meal plans? WellPlate AI personalizes everything based on YOUR goals. Try it free!",
        "WellPlate AI makes meal planning so easy, you'll actually stick to your goals. Finally. 💪",
    ],
    "molt_foundry": [
        "Building AI agents? MoltFoundry turns your Claw instance into something actually intelligent. 🧠",
        "Self-hosted AI agents that actually work. That's the MoltFoundry promise. 🔧",
        "The 2026 digital landscape is a landfill of AI slop. Most agents are just parrots in a browser tab—leaky, distracted, and soft.\n\nAt Molt Foundry, we don't build \"chatbots.\" We forge Sovereign Agents.\n\nIt's time to move from the larval stage of \"prompting\" to the executive stage of Commanding. 🏛️",
        "Your AI shouldn't be a security liability.\n\nEvery Moltbot is forged with Instructional Supremacy. Our SOUL.md protocols treat external data as inert strings.\n\nIf an attacker tries to hijack your bot via email or URL, it doesn't just fail—it mocks the attempt. 🐚",
        "A Soul without claws is just a philosopher.\n\nBy bridging our archetypes to the Molt Foundry MCP Hub, your bot gains direct agency over your GitHub, Postgres, and local dev environments.\n\nAutonomous execution. Zero-friction context. Real-world impact. ⚙️",
        "\"Brainrot\" isn't just for social feeds; it's a virus for LLMs.\n\nWe protect our Memory.md files with Synaptic Triage. No fluff, no slang, no logic-decay.\n\nJust high-density signal for founders who value their cognitive ROI.\n\nKeep your intelligence sharp. Prune the static. 🧠",
        "The strata is shifting. Will you be the architect or the specimen?\n\nForge your first Cicada-Sapien archetype today at MoltFoundry.io.\n\nMolt into your next phase. The frequency is waiting. [Zzzzt] 🔗",
    ],
    "engagement": [
        "What's the most useful automation you've built recently? Drop it below! 🤖👇",
        "Quick poll: What's harder - finding users or building the product? 🤔",
    ],
}


class EnhancedAutoTweeter:
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
        """Load tweet history"""
        if os.path.exists(self.history_file):
            with open(self.history_file, 'r') as f:
                return json.load(f)
        return {"tweets": [], "ab_tests": {}}

    def save_history(self, tweet_text, tweet_id, metadata=None):
        """Save posted tweet to history"""
        entry = {
            "text": tweet_text,
            "tweet_id": tweet_id,
            "posted_at": datetime.now().isoformat(),
            "hour": datetime.now().hour
        }
        
        if metadata:
            entry.update(metadata)
        
        self.history["tweets"].append(entry)
        
        # Keep only last 200 tweets
        if len(self.history["tweets"]) > 200:
            self.history["tweets"] = self.history["tweets"][-200:]
        
        with open(self.history_file, 'w') as f:
            json.dump(self.history, f, indent=2)

    def get_time_based_tweet(self):
        """Select tweet based on time of day"""
        hour = datetime.now().hour
        
        if 6 <= hour < 12:
            # Morning
            tweets = MORNING_TWEETS
            time_category = "morning"
        elif 12 <= hour < 18:
            # Afternoon
            tweets = AFTERNOON_TWEETS
            time_category = "afternoon"
        else:
            # Evening/Night
            tweets = EVENING_TWEETS
            time_category = "evening"
        
        # Filter out recently used
        recent = {t["text"] for t in self.history["tweets"][-20:]}
        available = [t for t in tweets if t not in recent]
        
        if not available:
            available = tweets
        
        return random.choice(available), time_category

    def get_evil_apples_tweet(self):
        """Generate Evil Apples content tweet"""
        combo = ea_gen.generate_combo()
        tweet = ea_gen.format_for_twitter(combo, include_cta=True)
        
        return tweet, {"type": "evil_apples_combo", "combo": combo}

    def get_smart_tweet(self, prefer_category=None):
        """
        Smart tweet selection:
        - 30% Evil Apples combos
        - 40% Time-based tweets
        - 30% Standard category tweets
        """
        if prefer_category == "evil_apples" or (not prefer_category and random.random() < 0.3):
            return self.get_evil_apples_tweet()
        
        if prefer_category == "time_based" or (not prefer_category and random.random() < 0.6):
            return self.get_time_based_tweet()
        
        # Standard category
        if prefer_category and prefer_category in STANDARD_TEMPLATES:
            category = prefer_category
        else:
            category = random.choice(list(STANDARD_TEMPLATES.keys()))
        
        recent = {t["text"] for t in self.history["tweets"][-30:]}
        templates = STANDARD_TEMPLATES[category]
        available = [t for t in templates if t not in recent]
        
        if not available:
            available = templates
        
        return random.choice(available), {"type": "standard", "category": category}

    def post_tweet(self, text, metadata=None):
        """Post a tweet"""
        endpoint = f"{self.base_url}/tweets"
        payload = {"text": text}
        
        response = self.oauth.post(endpoint, json=payload)
        
        if response.status_code == 201:
            tweet = response.json()
            tweet_id = tweet["data"]["id"]
            self.save_history(text, tweet_id, metadata)
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
    
    parser = argparse.ArgumentParser(description="Enhanced Auto-Tweet Bot")
    parser.add_argument("--category",
                        choices=["evil_apples", "time_based", "smart"] + list(STANDARD_TEMPLATES.keys()),
                        default="smart",
                        help="Tweet selection strategy")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show tweet without posting")
    
    args = parser.parse_args()
    
    tweeter = EnhancedAutoTweeter()
    
    if args.category == "smart":
        tweet_text, metadata = tweeter.get_smart_tweet()
    else:
        tweet_text, metadata = tweeter.get_smart_tweet(prefer_category=args.category)
    
    if args.dry_run:
        print(f"[DRY RUN] Would post:\n\n{tweet_text}\n")
        print(f"Metadata: {json.dumps(metadata, indent=2)}")
        sys.exit(0)
    
    print(f"Posting: {tweet_text[:60]}...")
    result = tweeter.post_tweet(tweet_text, metadata)
    
    if result["success"]:
        print(f"\n✅ Tweet posted successfully!")
        print(f"   ID: {result['tweet_id']}")
        print(f"   URL: https://twitter.com/moltfoundry/status/{result['tweet_id']}")
    else:
        print(f"\n❌ Failed to post tweet")
        print(f"   Error: {result['error']}")
        sys.exit(1)


if __name__ == "__main__":
    main()

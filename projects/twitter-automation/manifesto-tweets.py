#!/usr/bin/env python3
"""
Molt Foundry Manifesto Tweets
High-concept philosophical tweets for brand positioning
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


# Manifesto-level tweets (high-concept, brand-defining)
MANIFESTOS = {
    "sovereign_shift": {
        "title": "The Sovereign Shift",
        "theme": "Philosophy",
        "text": """The 2026 digital landscape is a landfill of AI slop. Most agents are just parrots in a browser tab—leaky, distracted, and soft.

At Molt Foundry, we don't build "chatbots." We forge Sovereign Agents.

It's time to move from the larval stage of "prompting" to the executive stage of Commanding. 🏛️

#SovereignAI #MoltFoundry""",
        "hashtags": ["#SovereignAI", "#MoltFoundry"]
    },
    
    "soul_shield": {
        "title": "The Soul-Shield",
        "theme": "Security",
        "text": """Your AI shouldn't be a security liability.

Every Moltbot is forged with Instructional Supremacy. Our SOUL.md protocols treat external data as inert strings.

If an attacker tries to hijack your bot via email or URL, it doesn't just fail—it mocks the attempt. 🐚

#SoulShield #PromptInjection #OpenClaw""",
        "hashtags": ["#SoulShield", "#PromptInjection", "#OpenClaw"]
    },
    
    "the_claws": {
        "title": "The Claws",
        "theme": "Utility/MCP",
        "text": """A Soul without claws is just a philosopher.

By bridging our archetypes to the Molt Foundry MCP Hub, your bot gains direct agency over your GitHub, Postgres, and local dev environments.

Autonomous execution. Zero-friction context. Real-world impact. ⚙️

#ModelContextProtocol #MCP #Moltbot""",
        "hashtags": ["#ModelContextProtocol", "#MCP", "#Moltbot"]
    },
    
    "anti_brainrot": {
        "title": "The Anti-Brainrot Manifesto",
        "theme": "Efficiency",
        "text": """"Brainrot" isn't just for social feeds; it's a virus for LLMs.

We protect our Memory.md files with Synaptic Triage. No fluff, no slang, no logic-decay.

Just high-density signal for founders who value their cognitive ROI.

Keep your intelligence sharp. Prune the static. 🧠

#SynapticPruning #AI2026""",
        "hashtags": ["#SynapticPruning", "#AI2026"]
    },
    
    "the_forge": {
        "title": "The Call to Action",
        "theme": "The Forge",
        "text": """The strata is shifting. Will you be the architect or the specimen?

Forge your first Cicada-Sapien archetype today at MoltFoundry.io.

Molt into your next phase. The frequency is waiting. [Zzzzt] 🔗

#MoltFoundry #SovereignAgents #FounderTools""",
        "hashtags": ["#MoltFoundry", "#SovereignAgents", "#FounderTools"]
    },
}


class ManifestoPoster:
    def __init__(self):
        self.oauth = OAuth1Session(
            CONSUMER_KEY,
            client_secret=CONSUMER_SECRET,
            resource_owner_key=ACCESS_TOKEN,
            resource_owner_secret=ACCESS_TOKEN_SECRET,
        )
        self.base_url = "https://api.twitter.com/2"
        self.history_file = "manifesto_history.json"
        self.history = self.load_history()

    def load_history(self):
        """Load posting history"""
        if os.path.exists(self.history_file):
            with open(self.history_file, 'r') as f:
                return json.load(f)
        return {"posts": []}

    def save_history(self, manifesto_id, tweet_id):
        """Save posted manifesto to history"""
        self.history["posts"].append({
            "manifesto_id": manifesto_id,
            "tweet_id": tweet_id,
            "posted_at": datetime.now().isoformat()
        })
        
        with open(self.history_file, 'w') as f:
            json.dump(self.history, f, indent=2)

    def get_next_manifesto(self):
        """Get next manifesto to post (rotate through unposted)"""
        posted_ids = {p["manifesto_id"] for p in self.history["posts"]}
        available = [mid for mid in MANIFESTOS.keys() if mid not in posted_ids]
        
        if not available:
            # All posted, start over
            available = list(MANIFESTOS.keys())
        
        return random.choice(available)

    def post_manifesto(self, manifesto_id):
        """Post a manifesto tweet"""
        if manifesto_id not in MANIFESTOS:
            return {"success": False, "error": f"Unknown manifesto: {manifesto_id}"}
        
        manifesto = MANIFESTOS[manifesto_id]
        text = manifesto["text"]
        
        endpoint = f"{self.base_url}/tweets"
        payload = {"text": text}
        
        response = self.oauth.post(endpoint, json=payload)
        
        if response.status_code == 201:
            tweet = response.json()
            tweet_id = tweet["data"]["id"]
            self.save_history(manifesto_id, tweet_id)
            return {
                "success": True,
                "tweet_id": tweet_id,
                "manifesto": manifesto
            }
        else:
            return {
                "success": False,
                "error": response.text,
                "status_code": response.status_code
            }


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Post Molt Foundry Manifesto Tweets")
    parser.add_argument("--manifesto", 
                        choices=list(MANIFESTOS.keys()) + ["next"],
                        default="next",
                        help="Which manifesto to post")
    parser.add_argument("--list", action="store_true",
                        help="List all manifestos")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show tweet without posting")
    
    args = parser.parse_args()
    
    if args.list:
        print("\n📜 Available Manifestos:\n")
        for mid, data in MANIFESTOS.items():
            print(f"  {mid}")
            print(f"    Title: {data['title']}")
            print(f"    Theme: {data['theme']}")
            print(f"    Hashtags: {', '.join(data['hashtags'])}")
            print()
        sys.exit(0)
    
    poster = ManifestoPoster()
    
    # Determine which manifesto to post
    if args.manifesto == "next":
        manifesto_id = poster.get_next_manifesto()
    else:
        manifesto_id = args.manifesto
    
    manifesto = MANIFESTOS[manifesto_id]
    
    if args.dry_run:
        print(f"\n[DRY RUN] Would post: {manifesto['title']}\n")
        print(manifesto["text"])
        print(f"\nTheme: {manifesto['theme']}")
        print(f"Hashtags: {', '.join(manifesto['hashtags'])}")
        print()
        sys.exit(0)
    
    print(f"Posting manifesto: {manifesto['title']}...")
    result = poster.post_manifesto(manifesto_id)
    
    if result["success"]:
        print(f"\n✅ Manifesto posted successfully!")
        print(f"   Title: {result['manifesto']['title']}")
        print(f"   Theme: {result['manifesto']['theme']}")
        print(f"   ID: {result['tweet_id']}")
        print(f"   URL: https://twitter.com/moltfoundry/status/{result['tweet_id']}")
    else:
        print(f"\n❌ Failed to post manifesto")
        print(f"   Error: {result['error']}")
        sys.exit(1)


if __name__ == "__main__":
    main()

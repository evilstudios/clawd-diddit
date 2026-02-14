#!/usr/bin/env python3
"""
Preview Tweet Templates
Shows all available tweets organized by category
"""

import sys
import random
import importlib.util

# Import templates from auto-tweet
spec = importlib.util.spec_from_file_location("auto_tweet", "auto-tweet.py")
auto_tweet = importlib.util.module_from_spec(spec)
spec.loader.exec_module(auto_tweet)
TWEET_TEMPLATES = auto_tweet.TWEET_TEMPLATES


def preview_category(category, templates):
    """Display tweets for a category"""
    print(f"\n{'='*70}")
    print(f"📱 {category.upper().replace('_', ' ')}")
    print(f"{'='*70}")
    print(f"   {len(templates)} templates\n")
    
    for i, tweet in enumerate(templates, 1):
        print(f"{i:2}. {tweet}")
    
    print()


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Preview tweet templates")
    parser.add_argument("--category", choices=list(TWEET_TEMPLATES.keys()),
                        help="Show specific category only")
    parser.add_argument("--random", type=int, metavar="N",
                        help="Show N random tweets")
    parser.add_argument("--count", action="store_true",
                        help="Show template counts only")
    
    args = parser.parse_args()
    
    if args.count:
        print("\n📊 Tweet Template Counts:")
        total = 0
        for category, templates in sorted(TWEET_TEMPLATES.items()):
            count = len(templates)
            total += count
            print(f"   {category:20} {count:3} templates")
        print(f"   {'─'*20} {'─'*3}─────────")
        print(f"   {'TOTAL':20} {total:3} templates\n")
        return
    
    if args.random:
        print(f"\n🎲 {args.random} Random Tweets:\n")
        all_tweets = []
        for templates in TWEET_TEMPLATES.values():
            all_tweets.extend(templates)
        
        sample = random.sample(all_tweets, min(args.random, len(all_tweets)))
        for i, tweet in enumerate(sample, 1):
            print(f"{i:2}. {tweet}\n")
        return
    
    if args.category:
        templates = TWEET_TEMPLATES[args.category]
        preview_category(args.category, templates)
        return
    
    # Show all categories
    print("\n" + "="*70)
    print("🤖 TWITTER AUTO-TWEET TEMPLATES")
    print("="*70)
    
    for category, templates in TWEET_TEMPLATES.items():
        preview_category(category, templates)
    
    print("="*70)
    total = sum(len(t) for t in TWEET_TEMPLATES.values())
    print(f"✨ Total: {total} unique tweets across {len(TWEET_TEMPLATES)} categories")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()

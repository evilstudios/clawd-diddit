#!/usr/bin/env python3
"""
Afoodable Content Preview Tool
Browse and preview social media content templates
"""

import argparse
import random
import os
import sys

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from afoodable_content_library import CONTENT_LIBRARY, format_content, list_categories, LANDING_PAGE_URL

def print_divider(char="=", length=70):
    print(char * length)

def print_content(content, index=None):
    """Pretty print a content template"""
    prefix = f"[{index}] " if index is not None else ""
    
    if 'tweets' in content:
        # Thread
        print(f"\n{prefix}🧵 THREAD - Category: {content['category']}")
        print_divider("-")
        tweets = format_content(content, LANDING_PAGE_URL)
        for i, tweet in enumerate(tweets, 1):
            print(f"\nTweet {i}/{len(tweets)}:")
            print(tweet)
            if i < len(tweets):
                print_divider("·", 40)
    else:
        # Single post
        category = content.get('category', 'unknown')
        print(f"\n{prefix}📄 Category: {category}")
        print_divider("-")
        
        # Format and display main content
        if 'copy' in content:
            print(format_content(content, LANDING_PAGE_URL))
        elif 'text' in content:
            print(format_content(content, LANDING_PAGE_URL))
        elif 'caption' in content:
            print(format_content(content, LANDING_PAGE_URL))
        
        # Show metadata
        if 'hashtags' in content:
            print(f"\n📌 {content['hashtags']}")
        if 'image_suggestion' in content:
            print(f"\n🖼️  Image: {content['image_suggestion']}")

def list_all_platforms():
    """List all available platforms and their stats"""
    print("\n📱 Available Platforms & Content\n")
    print_divider()
    
    total = 0
    for platform in CONTENT_LIBRARY:
        categories = list_categories(platform)
        count = len(CONTENT_LIBRARY[platform])
        total += count
        
        print(f"\n{platform.upper().replace('_', ' ')}")
        print(f"  • Total templates: {count}")
        print(f"  • Categories: {', '.join(categories)}")
    
    print_divider()
    print(f"\n✅ Total content templates: {total}\n")

def show_platform(platform):
    """Show all content for a specific platform"""
    if platform not in CONTENT_LIBRARY:
        print(f"\n❌ Platform '{platform}' not found.")
        print(f"\nAvailable platforms: {', '.join(CONTENT_LIBRARY.keys())}\n")
        return
    
    content_list = CONTENT_LIBRARY[platform]
    
    print(f"\n📱 {platform.upper().replace('_', ' ')}")
    print(f"   {len(content_list)} templates available\n")
    print_divider()
    
    for i, content in enumerate(content_list, 1):
        print_content(content, index=i)
        print_divider()

def show_category(platform, category):
    """Show specific category from a platform"""
    if platform not in CONTENT_LIBRARY:
        print(f"\n❌ Platform '{platform}' not found.\n")
        return
    
    content_list = [c for c in CONTENT_LIBRARY[platform] if c.get('category') == category]
    
    if not content_list:
        available = list_categories(platform)
        print(f"\n❌ Category '{category}' not found in {platform}.")
        print(f"\nAvailable categories: {', '.join(available)}\n")
        return
    
    print(f"\n📱 {platform.upper()} - Category: {category}")
    print_divider()
    
    for content in content_list:
        print_content(content)
        print_divider()

def show_random(count=3):
    """Show random content samples"""
    all_content = []
    for platform, content_list in CONTENT_LIBRARY.items():
        for content in content_list:
            all_content.append((platform, content))
    
    samples = random.sample(all_content, min(count, len(all_content)))
    
    print(f"\n🎲 {len(samples)} Random Content Samples\n")
    print_divider()
    
    for i, (platform, content) in enumerate(samples, 1):
        print(f"\nPlatform: {platform.upper().replace('_', ' ')}")
        print_content(content, index=i)
        print_divider()

def main():
    parser = argparse.ArgumentParser(
        description="Preview Afoodable social media content templates",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --list                           # List all platforms
  %(prog)s --platform facebook_linkedin     # Show all Facebook content
  %(prog)s --platform twitter --category case_study_thread
  %(prog)s --random 5                       # Show 5 random samples
  %(prog)s --count                          # Count templates by platform
        """
    )
    
    parser.add_argument('--list', action='store_true',
                        help='List all platforms and stats')
    parser.add_argument('--platform', type=str,
                        help='Show content for specific platform')
    parser.add_argument('--category', type=str,
                        help='Filter by category (requires --platform)')
    parser.add_argument('--random', type=int, metavar='N',
                        help='Show N random content samples')
    parser.add_argument('--count', action='store_true',
                        help='Count templates by platform')
    
    args = parser.parse_args()
    
    # Default to --list if no args
    if not any(vars(args).values()):
        args.list = True
    
    if args.list or args.count:
        list_all_platforms()
    elif args.random:
        show_random(args.random)
    elif args.platform:
        if args.category:
            show_category(args.platform, args.category)
        else:
            show_platform(args.platform)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

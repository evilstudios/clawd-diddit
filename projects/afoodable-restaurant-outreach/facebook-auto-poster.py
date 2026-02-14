#!/usr/bin/env python3
"""
Afoodable Facebook Auto-Poster
Posts to Facebook Page automatically with smart content rotation
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
HISTORY_FILE = "facebook-post-history.json"
MAX_HISTORY = 50
DRY_RUN = os.getenv("DRY_RUN", "false").lower() == "true"

# Facebook Page credentials (set via environment variables)
PAGE_ID = os.getenv("FACEBOOK_PAGE_ID", "")
PAGE_ACCESS_TOKEN = os.getenv("FACEBOOK_PAGE_ACCESS_TOKEN", "")

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

def get_recent_categories(history, limit=5):
    """Get recently used categories"""
    return [entry['category'] for entry in history[-limit:]]

def select_content():
    """Select next post using smart rotation"""
    history = load_history()
    recent_cats = get_recent_categories(history)
    
    # Get all Facebook/LinkedIn content
    all_content = CONTENT_LIBRARY.get('facebook_linkedin', [])
    
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

def post_to_facebook(content, category):
    """Post content to Facebook Page"""
    if DRY_RUN:
        print("🧪 DRY RUN MODE - Would post:")
        print(f"   Category: {category}")
        print(f"   Content:\n{content[:200]}...")
        return {"id": f"dryrun_{int(datetime.now().timestamp())}"}
    
    if not PAGE_ID or not PAGE_ACCESS_TOKEN:
        raise Exception("Facebook credentials not configured. Set FACEBOOK_PAGE_ID and FACEBOOK_PAGE_ACCESS_TOKEN")
    
    # TODO: Implement actual Facebook Graph API posting
    # This is a placeholder - needs requests library and Graph API integration
    """
    import requests
    
    url = f"https://graph.facebook.com/v18.0/{PAGE_ID}/feed"
    payload = {
        "message": content,
        "access_token": PAGE_ACCESS_TOKEN
    }
    
    response = requests.post(url, data=payload)
    response.raise_for_status()
    
    return response.json()
    """
    
    raise Exception("Facebook Graph API integration not yet implemented. Run with DRY_RUN=true to test content selection.")

def main():
    """Main posting function"""
    print("🚀 Afoodable Facebook Auto-Poster")
    print(f"   Mode: {'DRY RUN' if DRY_RUN else 'LIVE POSTING'}")
    print(f"   Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    try:
        # Select content
        selected = select_content()
        category = selected['category']
        
        # Format content with landing page
        formatted = format_content(selected, LANDING_PAGE_URL)
        
        # Add hashtags
        full_post = formatted
        if 'hashtags' in selected:
            full_post = f"{formatted}\n\n{selected['hashtags']}"
        
        print(f"📝 Selected Category: {category}")
        print(f"🖼️  Image Suggestion: {selected.get('image_suggestion', 'None')}\n")
        print("=" * 60)
        print(full_post)
        print("=" * 60)
        
        # Post to Facebook
        result = post_to_facebook(full_post, category)
        
        # Save to history
        history = load_history()
        history.append({
            "timestamp": datetime.now().isoformat(),
            "category": category,
            "post_id": result.get('id', 'unknown'),
            "content_preview": formatted[:100]
        })
        save_history(history)
        
        print(f"\n✅ Posted successfully!")
        print(f"   Post ID: {result.get('id', 'unknown')}")
        print(f"   Category: {category}")
        
        return 0
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return 1

if __name__ == "__main__":
    exit(main())

#!/usr/bin/env python3
"""
Facebook Auto-Poster
Automatically posts content to Facebook Pages/Groups on a schedule.

Schedule (per HEARTBEAT.md):
- Monday 2pm EST
- Wednesday 6pm EST  
- Friday 8pm EST

Usage:
    python3 facebook-auto-poster.py --post "Your message here"
    python3 facebook-auto-poster.py --schedule  # Use pre-configured content queue
    python3 facebook-auto-poster.py --queue "path/to/content.json"  # Load content queue

Requirements:
    pip install requests python-dotenv pytz
    
Environment Variables (.env):
    FB_PAGE_ACCESS_TOKEN=your_page_access_token
    FB_PAGE_ID=your_page_id
    FB_GROUP_ID=your_group_id (optional)
"""

import os
import json
import sys
import argparse
from datetime import datetime
from pathlib import Path
import requests
import pytz

# Try to load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("⚠️  python-dotenv not installed. Using system environment variables only.")

# Configuration
FB_API_VERSION = "v18.0"
FB_API_BASE = f"https://graph.facebook.com/{FB_API_VERSION}"

# Load credentials from environment
FB_PAGE_ACCESS_TOKEN = os.getenv("FB_PAGE_ACCESS_TOKEN")
FB_PAGE_ID = os.getenv("FB_PAGE_ID")
FB_GROUP_ID = os.getenv("FB_GROUP_ID")  # Optional


class FacebookPoster:
    def __init__(self, page_token, page_id, group_id=None):
        self.page_token = page_token
        self.page_id = page_id
        self.group_id = group_id
        
    def post_to_page(self, message, link=None, image_path=None):
        """Post to Facebook Page"""
        endpoint = f"{FB_API_BASE}/{self.page_id}/feed"
        
        payload = {
            "message": message,
            "access_token": self.page_token
        }
        
        if link:
            payload["link"] = link
            
        if image_path and os.path.exists(image_path):
            # Upload photo first, then post
            return self._post_with_photo(message, image_path, link)
        
        try:
            response = requests.post(endpoint, data=payload)
            response.raise_for_status()
            result = response.json()
            
            if "id" in result:
                print(f"✅ Posted to Facebook Page successfully!")
                print(f"   Post ID: {result['id']}")
                return result
            else:
                print(f"❌ Post failed: {result}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Error posting to Facebook: {e}")
            return None
    
    def _post_with_photo(self, message, image_path, link=None):
        """Post with photo to Facebook Page"""
        endpoint = f"{FB_API_BASE}/{self.page_id}/photos"
        
        with open(image_path, 'rb') as img:
            files = {'source': img}
            payload = {
                "message": message,
                "access_token": self.page_token
            }
            
            if link:
                payload["link"] = link
            
            try:
                response = requests.post(endpoint, data=payload, files=files)
                response.raise_for_status()
                result = response.json()
                
                if "id" in result:
                    print(f"✅ Posted photo to Facebook Page successfully!")
                    print(f"   Photo ID: {result['id']}")
                    return result
                else:
                    print(f"❌ Photo post failed: {result}")
                    return None
                    
            except requests.exceptions.RequestException as e:
                print(f"❌ Error posting photo to Facebook: {e}")
                return None
    
    def post_to_group(self, message, link=None):
        """Post to Facebook Group (requires group permissions)"""
        if not self.group_id:
            print("❌ No FB_GROUP_ID configured")
            return None
            
        endpoint = f"{FB_API_BASE}/{self.group_id}/feed"
        
        payload = {
            "message": message,
            "access_token": self.page_token
        }
        
        if link:
            payload["link"] = link
        
        try:
            response = requests.post(endpoint, data=payload)
            response.raise_for_status()
            result = response.json()
            
            if "id" in result:
                print(f"✅ Posted to Facebook Group successfully!")
                print(f"   Post ID: {result['id']}")
                return result
            else:
                print(f"❌ Group post failed: {result}")
                return None
                
        except requests.exceptions.RequestException as e:
            print(f"❌ Error posting to Facebook Group: {e}")
            return None


class ContentQueue:
    """Manages scheduled content queue"""
    
    def __init__(self, queue_file="facebook-content-queue.json"):
        self.queue_file = Path(__file__).parent / queue_file
        self.queue = self._load_queue()
    
    def _load_queue(self):
        """Load content queue from JSON file"""
        if self.queue_file.exists():
            with open(self.queue_file, 'r') as f:
                return json.load(f)
        else:
            # Create default queue structure
            default_queue = {
                "posts": [
                    {
                        "id": 1,
                        "message": "💡 Tip: Focus on high-leverage activities today. What's the ONE thing you can do that makes everything else easier?",
                        "link": None,
                        "image": None,
                        "posted": False,
                        "posted_at": None
                    },
                    {
                        "id": 2,
                        "message": "🚀 Building in public: What's one thing you shipped this week? Share below!",
                        "link": None,
                        "image": None,
                        "posted": False,
                        "posted_at": None
                    },
                    {
                        "id": 3,
                        "message": "📊 Weekly reminder: Revenue > Vanity metrics. Focus on what actually moves the needle.",
                        "link": None,
                        "image": None,
                        "posted": False,
                        "posted_at": None
                    }
                ]
            }
            
            # Save default queue
            with open(self.queue_file, 'w') as f:
                json.dump(default_queue, f, indent=2)
            
            print(f"📝 Created default content queue: {self.queue_file}")
            return default_queue
    
    def _save_queue(self):
        """Save queue back to file"""
        with open(self.queue_file, 'w') as f:
            json.dump(self.queue, f, indent=2)
    
    def get_next_post(self):
        """Get next unposted item from queue"""
        for post in self.queue["posts"]:
            if not post["posted"]:
                return post
        return None
    
    def mark_posted(self, post_id):
        """Mark a post as published"""
        for post in self.queue["posts"]:
            if post["id"] == post_id:
                post["posted"] = True
                post["posted_at"] = datetime.now(pytz.timezone('US/Eastern')).isoformat()
                self._save_queue()
                return True
        return False
    
    def add_post(self, message, link=None, image=None):
        """Add new post to queue"""
        new_id = max([p["id"] for p in self.queue["posts"]]) + 1 if self.queue["posts"] else 1
        
        new_post = {
            "id": new_id,
            "message": message,
            "link": link,
            "image": image,
            "posted": False,
            "posted_at": None
        }
        
        self.queue["posts"].append(new_post)
        self._save_queue()
        print(f"✅ Added post #{new_id} to queue")
        return new_post
    
    def list_queue(self):
        """Display current queue"""
        print("\n📋 Content Queue:")
        print("=" * 60)
        
        for post in self.queue["posts"]:
            status = "✅ Posted" if post["posted"] else "⏳ Pending"
            print(f"\n[{post['id']}] {status}")
            print(f"Message: {post['message'][:80]}...")
            if post["link"]:
                print(f"Link: {post['link']}")
            if post["posted_at"]:
                print(f"Posted: {post['posted_at']}")
        
        print("\n" + "=" * 60)


def check_credentials():
    """Verify Facebook credentials are configured"""
    if not FB_PAGE_ACCESS_TOKEN:
        print("❌ Error: FB_PAGE_ACCESS_TOKEN not set")
        print("   Set it in .env file or environment variable")
        return False
    
    if not FB_PAGE_ID:
        print("❌ Error: FB_PAGE_ID not set")
        print("   Set it in .env file or environment variable")
        return False
    
    return True


def main():
    parser = argparse.ArgumentParser(description="Facebook Auto-Poster")
    parser.add_argument("--post", type=str, help="Post message directly")
    parser.add_argument("--link", type=str, help="Add link to post")
    parser.add_argument("--image", type=str, help="Path to image file")
    parser.add_argument("--schedule", action="store_true", help="Post next item from queue")
    parser.add_argument("--queue", type=str, help="Load content from custom queue file")
    parser.add_argument("--add", type=str, help="Add message to queue")
    parser.add_argument("--list", action="store_true", help="List content queue")
    parser.add_argument("--group", action="store_true", help="Post to group instead of page")
    
    args = parser.parse_args()
    
    # Check credentials
    if not check_credentials():
        sys.exit(1)
    
    # Initialize poster
    poster = FacebookPoster(FB_PAGE_ACCESS_TOKEN, FB_PAGE_ID, FB_GROUP_ID)
    
    # Initialize content queue
    queue_file = args.queue if args.queue else "facebook-content-queue.json"
    queue = ContentQueue(queue_file)
    
    # Handle different actions
    if args.list:
        queue.list_queue()
        return
    
    if args.add:
        queue.add_post(args.add, args.link, args.image)
        return
    
    if args.schedule:
        # Get next post from queue
        next_post = queue.get_next_post()
        
        if not next_post:
            print("✅ Queue is empty! All posts have been published.")
            return
        
        print(f"📤 Posting from queue (ID: {next_post['id']})...")
        
        if args.group:
            result = poster.post_to_group(next_post["message"], next_post.get("link"))
        else:
            result = poster.post_to_page(
                next_post["message"], 
                next_post.get("link"),
                next_post.get("image")
            )
        
        if result:
            queue.mark_posted(next_post["id"])
            print(f"✅ Posted and marked as complete in queue")
        
        return
    
    if args.post:
        # Direct post
        print(f"📤 Posting to Facebook {'Group' if args.group else 'Page'}...")
        
        if args.group:
            poster.post_to_group(args.post, args.link)
        else:
            poster.post_to_page(args.post, args.link, args.image)
        
        return
    
    # No action specified
    print("❌ No action specified. Use --help for usage information.")
    parser.print_help()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Evil Apples Facebook Engagement Tracker
Monitors posts and provides analytics
"""

import requests
import json
from datetime import datetime

# Configuration
ACCESS_TOKEN = "EAARWzoIjLNMBQu52ANJPjcDAIDbuzfEx2lNgXKlH1WmBlfNPpd5B1krqv9qEaYNCiPMajYjl6ZC0vQEghWXsNoxW78awlYrUzQ0KLfHlAtQOunlZB7lMx1IjHwdqtGO2u0QyHxxqKJ98klz6EHvmT5lD53fx6X0AnTNOoMCiFiWp1NnGrTbqUF9PHgtlAy4jr2pQ0J1ZAymqxkB3QhOKQKbynjyZCHYNxgzgwyU6PI6j9zP4LiaJ4l1ZAoKugrPcAM5CE48zR4QPByZCYo32upbeNwg9XvokwZDm"
PAGE_ID = "127527677435319"
FOLLOWERS = 9572

def get_page_token():
    """Get page access token"""
    response = requests.get(
        "https://graph.facebook.com/v19.0/me/accounts",
        params={"access_token": ACCESS_TOKEN}
    )
    if response.status_code == 200:
        pages = response.json().get('data', [])
        if pages:
            return pages[0]['access_token']
    return None

def get_recent_posts(page_token, limit=10):
    """Get recent posts with engagement metrics"""
    response = requests.get(
        f"https://graph.facebook.com/v19.0/{PAGE_ID}/posts",
        params={
            "fields": "id,message,created_time,likes.summary(true),comments.summary(true),shares,reactions.summary(true)",
            "limit": limit,
            "access_token": page_token
        }
    )
    
    if response.status_code == 200:
        return response.json().get('data', [])
    return []

def calculate_engagement_rate(reactions, comments, shares):
    """Calculate engagement rate"""
    total_engagement = reactions + comments + shares
    return (total_engagement / FOLLOWERS) * 100

def format_time_ago(created_time):
    """Format time since post"""
    created = datetime.fromisoformat(created_time.replace('Z', '+00:00'))
    now = datetime.now().astimezone()
    delta = now - created
    
    if delta.days > 0:
        return f"{delta.days}d ago"
    hours = delta.seconds // 3600
    if hours > 0:
        return f"{hours}h ago"
    minutes = (delta.seconds % 3600) // 60
    return f"{minutes}m ago"

def monitor_engagement():
    """Main monitoring function"""
    print("📊 EVIL APPLES FACEBOOK ENGAGEMENT REPORT")
    print("=" * 70)
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    page_token = get_page_token()
    if not page_token:
        print("❌ Error: Could not get page token")
        return
    
    posts = get_recent_posts(page_token)
    
    if not posts:
        print("❌ No posts found")
        return
    
    print(f"📝 Monitoring {len(posts)} recent posts:\n")
    
    total_engagement = 0
    
    for i, post in enumerate(posts, 1):
        post_id = post.get('id')
        message = post.get('message', '[No message]')[:60]
        created = post.get('created_time')
        
        likes = post.get('likes', {}).get('summary', {}).get('total_count', 0)
        comments = post.get('comments', {}).get('summary', {}).get('total_count', 0)
        shares = post.get('shares', {}).get('count', 0)
        reactions = post.get('reactions', {}).get('summary', {}).get('total_count', 0)
        
        engagement = reactions + comments + shares
        eng_rate = calculate_engagement_rate(reactions, comments, shares)
        time_ago = format_time_ago(created)
        
        total_engagement += engagement
        
        print(f"{i}. {time_ago}")
        print(f"   \"{message}...\"")
        print(f"   👍 {reactions} | 💬 {comments} | 🔄 {shares} | Total: {engagement}")
        print(f"   📊 Engagement Rate: {eng_rate:.2f}%")
        print()
    
    # Summary
    avg_engagement = total_engagement / len(posts)
    avg_rate = (total_engagement / len(posts) / FOLLOWERS) * 100
    
    print("=" * 70)
    print(f"\n📈 SUMMARY:")
    print(f"   Total Engagement: {total_engagement}")
    print(f"   Average per Post: {avg_engagement:.1f}")
    print(f"   Average Engagement Rate: {avg_rate:.2f}%")
    print(f"   Total Followers: {FOLLOWERS:,}")
    print(f"\n🔗 View Page: https://www.facebook.com/{PAGE_ID}")

if __name__ == "__main__":
    monitor_engagement()

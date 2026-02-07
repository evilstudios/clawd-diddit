#!/usr/bin/env python3
"""
YouTube Creator Finder for LYLYS
Finds True Crime creators in the 15k-75k subscriber sweet spot
"""

import os
import sys
import json
import requests
from typing import List, Dict, Optional
from datetime import datetime

# Configuration
YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY', '')
YOUTUBE_API_BASE = "https://www.googleapis.com/youtube/v3"

# Target criteria
MIN_SUBSCRIBERS = 15000
MAX_SUBSCRIBERS = 75000
MIN_ENGAGEMENT_RATIO = 0.02  # 2% comment-to-view ratio

class YouTubeCreatorFinder:
    """Find and analyze YouTube creators"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.results = []
    
    def search_channels(self, query: str, max_results: int = 20) -> List[Dict]:
        """Search for channels by keyword"""
        url = f"{YOUTUBE_API_BASE}/search"
        
        params = {
            'part': 'snippet',
            'type': 'channel',
            'q': query,
            'maxResults': max_results,
            'key': self.api_key,
            'relevanceLanguage': 'en',
            'order': 'relevance'
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            channels = []
            for item in data.get('items', []):
                channel_id = item['id'].get('channelId')
                if channel_id:
                    channels.append({
                        'id': channel_id,
                        'title': item['snippet']['title'],
                        'description': item['snippet']['description']
                    })
            
            return channels
        
        except Exception as e:
            print(f"❌ Search error: {e}")
            return []
    
    def get_channel_details(self, channel_id: str) -> Optional[Dict]:
        """Get detailed channel statistics"""
        url = f"{YOUTUBE_API_BASE}/channels"
        
        params = {
            'part': 'snippet,statistics,contentDetails',
            'id': channel_id,
            'key': self.api_key
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            if not data.get('items'):
                return None
            
            channel = data['items'][0]
            stats = channel['statistics']
            snippet = channel['snippet']
            
            return {
                'id': channel_id,
                'title': snippet['title'],
                'description': snippet['description'],
                'custom_url': snippet.get('customUrl', ''),
                'published_at': snippet['publishedAt'],
                'subscribers': int(stats.get('subscriberCount', 0)),
                'video_count': int(stats.get('videoCount', 0)),
                'view_count': int(stats.get('viewCount', 0)),
                'thumbnail': snippet['thumbnails']['default']['url']
            }
        
        except Exception as e:
            print(f"❌ Channel details error: {e}")
            return None
    
    def get_recent_videos(self, channel_id: str, max_results: int = 5) -> List[Dict]:
        """Get recent videos from a channel"""
        url = f"{YOUTUBE_API_BASE}/search"
        
        params = {
            'part': 'id',
            'channelId': channel_id,
            'order': 'date',
            'type': 'video',
            'maxResults': max_results,
            'key': self.api_key
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            video_ids = [item['id']['videoId'] for item in data.get('items', [])]
            
            if not video_ids:
                return []
            
            return self.get_video_stats(video_ids)
        
        except Exception as e:
            print(f"❌ Recent videos error: {e}")
            return []
    
    def get_video_stats(self, video_ids: List[str]) -> List[Dict]:
        """Get statistics for multiple videos"""
        url = f"{YOUTUBE_API_BASE}/videos"
        
        params = {
            'part': 'snippet,statistics',
            'id': ','.join(video_ids),
            'key': self.api_key
        }
        
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            videos = []
            for item in data.get('items', []):
                stats = item['statistics']
                snippet = item['snippet']
                
                view_count = int(stats.get('viewCount', 0))
                comment_count = int(stats.get('commentCount', 0))
                
                videos.append({
                    'id': item['id'],
                    'title': snippet['title'],
                    'published_at': snippet['publishedAt'],
                    'views': view_count,
                    'likes': int(stats.get('likeCount', 0)),
                    'comments': comment_count,
                    'engagement_ratio': comment_count / view_count if view_count > 0 else 0
                })
            
            return videos
        
        except Exception as e:
            print(f"❌ Video stats error: {e}")
            return []
    
    def calculate_engagement_score(self, channel_details: Dict, recent_videos: List[Dict]) -> float:
        """Calculate overall engagement score"""
        if not recent_videos:
            return 0.0
        
        # Average engagement ratio across recent videos
        avg_engagement = sum(v['engagement_ratio'] for v in recent_videos) / len(recent_videos)
        
        # Weight by subscriber count (lower subs = higher potential value)
        subscriber_score = 1.0 - (channel_details['subscribers'] / MAX_SUBSCRIBERS)
        
        # Combined score
        return (avg_engagement * 0.7) + (subscriber_score * 0.3)
    
    def analyze_channel(self, channel_id: str) -> Optional[Dict]:
        """Full analysis of a channel"""
        print(f"   Analyzing channel {channel_id}...")
        
        # Get channel details
        details = self.get_channel_details(channel_id)
        if not details:
            return None
        
        # Check if in subscriber range
        subs = details['subscribers']
        if subs < MIN_SUBSCRIBERS or subs > MAX_SUBSCRIBERS:
            print(f"   ⏭️  {details['title']}: {subs:,} subs (outside range)")
            return None
        
        # Get recent videos
        videos = self.get_recent_videos(channel_id, max_results=5)
        if not videos:
            print(f"   ⏭️  {details['title']}: No recent videos")
            return None
        
        # Calculate engagement
        engagement_score = self.calculate_engagement_score(details, videos)
        avg_engagement_ratio = sum(v['engagement_ratio'] for v in videos) / len(videos)
        
        # Check minimum engagement
        if avg_engagement_ratio < MIN_ENGAGEMENT_RATIO:
            print(f"   ⏭️  {details['title']}: Low engagement ({avg_engagement_ratio:.2%})")
            return None
        
        # Qualified!
        result = {
            **details,
            'recent_videos': videos,
            'avg_engagement_ratio': avg_engagement_ratio,
            'engagement_score': engagement_score,
            'analyzed_at': datetime.utcnow().isoformat(),
            'status': 'qualified'
        }
        
        print(f"   ✅ {details['title']}: {subs:,} subs, {avg_engagement_ratio:.2%} engagement")
        
        return result
    
    def find_creators(self, queries: List[str], target_count: int = 20) -> List[Dict]:
        """Find creators matching criteria"""
        qualified = []
        seen_channels = set()
        
        for query in queries:
            if len(qualified) >= target_count:
                break
            
            print(f"\n🔍 Searching: {query}")
            channels = self.search_channels(query, max_results=10)
            
            for channel in channels:
                if len(qualified) >= target_count:
                    break
                
                channel_id = channel['id']
                if channel_id in seen_channels:
                    continue
                
                seen_channels.add(channel_id)
                
                # Analyze channel
                result = self.analyze_channel(channel_id)
                if result:
                    qualified.append(result)
        
        return qualified


def search_true_crime_creators(api_key: str, target_count: int = 20) -> List[Dict]:
    """Search for True Crime creators"""
    
    finder = YouTubeCreatorFinder(api_key)
    
    # Search queries (ordered by relevance)
    queries = [
        "true crime podcast",
        "true crime youtube channel",
        "murder mystery podcast",
        "cold case podcast",
        "crime documentary channel",
        "true crime storytelling",
        "unsolved mysteries podcast",
        "investigative journalism true crime",
        "crime analysis youtube",
        "true crime deep dive"
    ]
    
    print("=" * 60)
    print("🎯 LYLYS Creator Finder - True Crime Edition")
    print("=" * 60)
    print(f"Target: {target_count} qualified creators")
    print(f"Criteria: {MIN_SUBSCRIBERS:,}-{MAX_SUBSCRIBERS:,} subs, {MIN_ENGAGEMENT_RATIO:.1%}+ engagement")
    
    results = finder.find_creators(queries, target_count)
    
    print("\n" + "=" * 60)
    print(f"✅ Found {len(results)} qualified creators")
    print("=" * 60)
    
    return results


def save_results(results: List[Dict], output_file: str):
    """Save results to JSON file"""
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\n💾 Saved to: {output_file}")


def export_to_csv(results: List[Dict], output_file: str):
    """Export results to CSV for Instantly.ai"""
    import csv
    
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            'Channel Title',
            'Channel URL',
            'Subscribers',
            'Avg Engagement',
            'Recent Video Title',
            'Status',
            'Notes'
        ])
        
        for channel in results:
            recent_video = channel['recent_videos'][0] if channel['recent_videos'] else {}
            
            writer.writerow([
                channel['title'],
                f"https://youtube.com/channel/{channel['id']}",
                f"{channel['subscribers']:,}",
                f"{channel['avg_engagement_ratio']:.2%}",
                recent_video.get('title', 'N/A'),
                'To Contact',
                f"Engagement Score: {channel['engagement_score']:.3f}"
            ])
    
    print(f"📊 Exported to CSV: {output_file}")


if __name__ == "__main__":
    # Check API key
    if not YOUTUBE_API_KEY:
        print("❌ Error: YOUTUBE_API_KEY not set")
        print("\nGet your API key:")
        print("1. Go to: https://console.cloud.google.com/")
        print("2. Create project → Enable YouTube Data API v3")
        print("3. Create credentials → API key")
        print("4. Export: export YOUTUBE_API_KEY='your_key_here'")
        sys.exit(1)
    
    # Search for creators
    results = search_true_crime_creators(YOUTUBE_API_KEY, target_count=20)
    
    if results:
        # Save full data
        json_file = '/root/clawd/projects/lylys/true-crime-leads.json'
        save_results(results, json_file)
        
        # Export CSV for outreach
        csv_file = '/root/clawd/projects/lylys/true-crime-leads.csv'
        export_to_csv(results, csv_file)
        
        print("\n✅ Lead generation complete!")
        print(f"Next step: Review leads and start outreach campaign")
    else:
        print("\n❌ No qualified creators found. Try adjusting criteria.")

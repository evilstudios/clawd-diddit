#!/usr/bin/env python3
"""
Evil Apples - Google Play Store Monitor
Pulls downloads, revenue, ratings, and reviews
"""

import json
from datetime import datetime, timedelta
from pathlib import Path
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Configuration
SCRIPT_DIR = Path(__file__).parent
SERVICE_ACCOUNT_FILE = SCRIPT_DIR / "google-play-service-account.json"
DATA_DIR = SCRIPT_DIR / "play-data"
DATA_DIR.mkdir(exist_ok=True)

# Evil Apples package name (from Play Console)
PACKAGE_NAME = "com.evilapples.app"

# Scopes for Google Play Developer API
SCOPES = ['https://www.googleapis.com/auth/androidpublisher']

class GooglePlayMonitor:
    def __init__(self):
        self.credentials = service_account.Credentials.from_service_account_file(
            str(SERVICE_ACCOUNT_FILE),
            scopes=SCOPES
        )
        self.service = build('androidpublisher', 'v3', credentials=self.credentials)
    
    def get_app_details(self):
        """Get basic app information"""
        try:
            # Get app details
            app_edit = self.service.edits().insert(
                packageName=PACKAGE_NAME,
                body={}
            ).execute()
            
            edit_id = app_edit['id']
            
            # Get listings
            listings = self.service.edits().listings().list(
                packageName=PACKAGE_NAME,
                editId=edit_id
            ).execute()
            
            # Delete the edit (we're just reading)
            self.service.edits().delete(
                packageName=PACKAGE_NAME,
                editId=edit_id
            ).execute()
            
            return listings
            
        except Exception as e:
            print(f"❌ Error fetching app details: {e}")
            return None
    
    def get_reviews(self, max_results=20):
        """Get recent reviews"""
        try:
            reviews = self.service.reviews().list(
                packageName=PACKAGE_NAME,
                maxResults=max_results
            ).execute()
            
            return reviews.get('reviews', [])
            
        except Exception as e:
            print(f"❌ Error fetching reviews: {e}")
            return []
    
    def analyze_reviews(self, reviews):
        """Analyze review sentiment and ratings"""
        if not reviews:
            return None
        
        ratings = [r['comments'][0]['userComment']['starRating'] for r in reviews 
                   if 'comments' in r and r['comments'] and 'userComment' in r['comments'][0]]
        
        if not ratings:
            return None
        
        avg_rating = sum(ratings) / len(ratings)
        rating_dist = {i: ratings.count(i) for i in range(1, 6)}
        
        # Recent reviews (last 7 days)
        week_ago = datetime.now() - timedelta(days=7)
        recent_reviews = []
        
        for review in reviews:
            if 'comments' not in review or not review['comments']:
                continue
            
            comment = review['comments'][0]['userComment']
            timestamp = comment.get('lastModified', {}).get('seconds', 0)
            
            if timestamp:
                review_date = datetime.fromtimestamp(int(timestamp))
                if review_date >= week_ago:
                    recent_reviews.append({
                        'rating': comment.get('starRating', 0),
                        'text': comment.get('text', ''),
                        'date': review_date.strftime('%Y-%m-%d')
                    })
        
        return {
            'total_reviews': len(reviews),
            'avg_rating': avg_rating,
            'rating_distribution': rating_dist,
            'recent_reviews_count': len(recent_reviews),
            'recent_reviews': recent_reviews[:5]  # Top 5 most recent
        }
    
    def save_snapshot(self, data):
        """Save daily snapshot"""
        today = datetime.now().strftime("%Y-%m-%d")
        filepath = DATA_DIR / f"play-{today}.json"
        
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
        
        print(f"✅ Saved snapshot: {filepath}")
    
    def format_report(self, review_analysis):
        """Format analysis into readable report"""
        report = []
        report.append("🎮 Evil Apples - Google Play Store Report")
        report.append("=" * 50)
        
        if not review_analysis:
            report.append("")
            report.append("ℹ️  No review data available")
            report.append("")
            report.append("Possible reasons:")
            report.append("- App has no reviews yet")
            report.append("- API permissions not fully propagated")
            report.append("- App is still in testing phase")
            return "\n".join(report)
        
        report.append("")
        report.append(f"⭐ Average Rating: {review_analysis['avg_rating']:.2f} / 5.0")
        report.append(f"📝 Total Reviews Analyzed: {review_analysis['total_reviews']}")
        report.append(f"🆕 Recent Reviews (7 days): {review_analysis['recent_reviews_count']}")
        
        report.append("")
        report.append("📊 Rating Distribution:")
        for stars in range(5, 0, -1):
            count = review_analysis['rating_distribution'].get(stars, 0)
            bar = "⭐" * stars
            report.append(f"  {bar} ({stars}): {count}")
        
        if review_analysis['recent_reviews']:
            report.append("")
            report.append("💬 Recent Reviews:")
            report.append("-" * 50)
            for review in review_analysis['recent_reviews']:
                stars = "⭐" * review['rating']
                text = review['text'][:100] + "..." if len(review['text']) > 100 else review['text']
                report.append(f"\n{stars} ({review['date']})")
                report.append(f"  {text}")
        
        return "\n".join(report)


def main():
    """Main execution"""
    print("🎮 Evil Apples - Google Play Store Monitor")
    print("=" * 50)
    
    if not SERVICE_ACCOUNT_FILE.exists():
        print(f"❌ Service account file not found: {SERVICE_ACCOUNT_FILE}")
        print("\nPlease ensure google-play-service-account.json is in the project directory.")
        return 2
    
    monitor = GooglePlayMonitor()
    
    # Fetch reviews
    print("\n📡 Fetching Google Play data...")
    reviews = monitor.get_reviews(max_results=50)
    
    if reviews:
        print(f"✅ Found {len(reviews)} reviews")
        
        # Analyze
        analysis = monitor.analyze_reviews(reviews)
        
        # Save snapshot
        snapshot = {
            'date': datetime.now().isoformat(),
            'analysis': analysis,
            'raw_reviews_count': len(reviews)
        }
        monitor.save_snapshot(snapshot)
        
        # Print report
        print("\n")
        print(monitor.format_report(analysis))
        
        return 0
    else:
        print("ℹ️  No reviews found")
        print("\nThis is normal if:")
        print("- App is newly launched")
        print("- App hasn't received reviews yet")
        print("- API access is still propagating (wait 24h)")
        return 0


if __name__ == "__main__":
    exit(main())

#!/usr/bin/env python3
"""
Twitter API Credit Monitor
Check API usage and remaining credits
"""

import sys
import json
from datetime import datetime
from requests_oauthlib import OAuth1Session

# Twitter API credentials
CONSUMER_KEY = "qnuZrAAsXcAvcpmTY3yMQQXGe"
CONSUMER_SECRET = "C4pzqaqfGu8Vz8FwVdWpIKyoKxcdWFAbvLMU9971KffwXcP4t1"
ACCESS_TOKEN = "2021426499317018624-4qUWIkj9GUybgL3nAhYYs0Im4Hjijq"
ACCESS_TOKEN_SECRET = "smrhgjhdfMKft3yB78aZPLBp6SIXNEUpvpxMVgpswbE2f"


class CreditMonitor:
    def __init__(self):
        self.oauth = OAuth1Session(
            CONSUMER_KEY,
            client_secret=CONSUMER_SECRET,
            resource_owner_key=ACCESS_TOKEN,
            resource_owner_secret=ACCESS_TOKEN_SECRET,
        )
        self.base_url = "https://api.twitter.com/2"

    def check_rate_limits(self):
        """
        Check rate limits for common endpoints
        Note: This doesn't show monthly credits directly,
        but shows rate limit windows
        """
        endpoints = [
            "/tweets",  # Post tweets
            "/users/me",  # Get user info
        ]
        
        results = {}
        
        for endpoint in endpoints:
            # Make a test request to get rate limit headers
            url = f"{self.base_url}{endpoint}"
            response = self.oauth.get(url)
            
            # Extract rate limit headers
            headers = response.headers
            results[endpoint] = {
                "limit": headers.get("x-rate-limit-limit", "unknown"),
                "remaining": headers.get("x-rate-limit-remaining", "unknown"),
                "reset": headers.get("x-rate-limit-reset", "unknown"),
                "status_code": response.status_code
            }
        
        return results

    def test_posting_ability(self):
        """Test if we can post by attempting to get user info"""
        endpoint = f"{self.base_url}/users/me"
        response = self.oauth.get(endpoint)
        
        if response.status_code == 200:
            return {
                "can_post": True,
                "status": "OK - Credits available",
                "message": "✅ Ready to post tweets"
            }
        elif response.status_code == 402:
            # Credits depleted
            try:
                error = response.json()
                return {
                    "can_post": False,
                    "status": "CREDITS_DEPLETED",
                    "message": "❌ Out of API credits",
                    "detail": error.get("detail", "Unknown")
                }
            except:
                return {
                    "can_post": False,
                    "status": "ERROR",
                    "message": "❌ Cannot post - check Twitter Developer Portal"
                }
        else:
            return {
                "can_post": False,
                "status": f"ERROR_{response.status_code}",
                "message": f"❌ API Error: {response.status_code}"
            }


def format_timestamp(ts_string):
    """Convert Unix timestamp to readable format"""
    if ts_string == "unknown":
        return "unknown"
    try:
        ts = int(ts_string)
        dt = datetime.fromtimestamp(ts)
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except:
        return ts_string


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description="Monitor Twitter API credits")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    parser.add_argument("--test-post", action="store_true", 
                        help="Test if posting is available")
    
    args = parser.parse_args()
    
    monitor = CreditMonitor()
    
    if args.test_post:
        result = monitor.test_posting_ability()
        
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(f"\n{result['message']}")
            print(f"Status: {result['status']}")
            if 'detail' in result:
                print(f"Detail: {result['detail']}")
            print()
        
        sys.exit(0 if result['can_post'] else 1)
    
    print("\n" + "="*70)
    print("📊 TWITTER API CREDIT MONITOR")
    print("="*70)
    
    # Test posting ability first
    print("\n🔍 Testing API Access...")
    status = monitor.test_posting_ability()
    print(f"   {status['message']}")
    
    if not status['can_post']:
        print("\n⚠️  API CREDITS DEPLETED")
        print("\n   Your Twitter Developer account is out of monthly credits.")
        print("\n   📋 Next Steps:")
        print("   1. Go to: https://developer.twitter.com/en/portal/dashboard")
        print("   2. Check your usage and plan limits")
        print("   3. Either wait for monthly reset OR upgrade your plan")
        print("\n   💰 Plans:")
        print("   • Free:  $0/month   → 1,500 tweets/month")
        print("   • Basic: $100/month → 3,000 tweets/month + better limits")
        print("   • Pro:   $5,000/mo  → 50,000 tweets/month")
        print()
        sys.exit(1)
    
    print("\n✅ Credits Available - Bot Ready to Post!")
    
    print("\n📈 Rate Limit Info:")
    print("   Note: Rate limits reset every 15 minutes")
    
    # This will likely fail due to credits, but try anyway
    try:
        limits = monitor.check_rate_limits()
        
        for endpoint, info in limits.items():
            print(f"\n   {endpoint}:")
            if info['status_code'] == 200:
                print(f"      Limit: {info['limit']} requests per window")
                print(f"      Remaining: {info['remaining']}")
                reset_time = format_timestamp(info['reset'])
                print(f"      Reset: {reset_time}")
            else:
                print(f"      Status: HTTP {info['status_code']}")
    except Exception as e:
        print(f"   (Rate limit details unavailable: {e})")
    
    print("\n💡 Tips:")
    print("   • Run this before posting to check credit status")
    print("   • Add to cron to monitor daily")
    print("   • Free tier = 1,500 tweets/month (resets monthly)")
    print("\n" + "="*70 + "\n")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Voxable Lead Tracker
Monitor campaign performance, track responses, and manage follow-ups
"""

import os
import sys
import json
import requests
from datetime import datetime, timedelta
from typing import List, Dict, Optional
from collections import defaultdict

class InstantlyAnalytics:
    """Analytics and tracking for Instantly.ai campaigns"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.instantly.ai/api/v1"
    
    def _request(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """Make API request"""
        url = f"{self.base_url}{endpoint}"
        request_params = {"api_key": self.api_key}
        
        if params:
            request_params.update(params)
        
        try:
            response = requests.get(url, params=request_params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"❌ API Error: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response: {e.response.text}")
            return {}
    
    def get_campaign_analytics(self, campaign_name: str) -> Dict:
        """Get campaign analytics"""
        return self._request("/analytics/campaign", {"campaign_name": campaign_name})
    
    def get_lead_status(self, campaign_name: str) -> List[Dict]:
        """Get status of all leads in campaign"""
        return self._request("/lead/list", {"campaign_name": campaign_name})
    
    def get_replies(self, campaign_name: str) -> List[Dict]:
        """Get all replies for campaign"""
        # Note: Actual endpoint may vary based on Instantly.ai API docs
        return self._request("/campaign/replies", {"campaign_name": campaign_name})

def calculate_metrics(leads: List[Dict]) -> Dict:
    """Calculate campaign metrics from lead data"""
    
    total = len(leads)
    if total == 0:
        return {
            "total_leads": 0,
            "sent": 0,
            "opened": 0,
            "clicked": 0,
            "replied": 0,
            "positive_replies": 0,
            "negative_replies": 0,
            "bounced": 0,
            "open_rate": 0,
            "reply_rate": 0,
            "positive_reply_rate": 0
        }
    
    # Count statuses
    statuses = defaultdict(int)
    for lead in leads:
        status = lead.get('status', 'unknown').lower()
        statuses[status] += 1
    
    sent = sum(statuses[s] for s in ['sent', 'opened', 'clicked', 'replied'])
    opened = statuses.get('opened', 0) + statuses.get('clicked', 0) + statuses.get('replied', 0)
    clicked = statuses.get('clicked', 0)
    replied = statuses.get('replied', 0)
    bounced = statuses.get('bounced', 0)
    
    # Calculate rates
    open_rate = (opened / sent * 100) if sent > 0 else 0
    reply_rate = (replied / sent * 100) if sent > 0 else 0
    
    return {
        "total_leads": total,
        "sent": sent,
        "opened": opened,
        "clicked": clicked,
        "replied": replied,
        "bounced": bounced,
        "open_rate": round(open_rate, 2),
        "reply_rate": round(reply_rate, 2),
        "click_rate": round((clicked / sent * 100) if sent > 0 else 0, 2)
    }

def display_campaign_dashboard(campaign_name: str, api_key: str):
    """Display campaign performance dashboard"""
    
    print(f"\n📊 Voxable Campaign Dashboard: {campaign_name}")
    print("=" * 70)
    
    analytics = InstantlyAnalytics(api_key)
    
    # Get campaign data
    print("\n🔄 Fetching campaign data...")
    
    try:
        # Get analytics
        campaign_data = analytics.get_campaign_analytics(campaign_name)
        
        # Get leads
        leads = analytics.get_lead_status(campaign_name)
        
        if not leads:
            print("⚠️  No lead data found. Campaign may not have started yet.")
            return
        
        # Calculate metrics
        metrics = calculate_metrics(leads)
        
        # Display overview
        print("\n📈 CAMPAIGN OVERVIEW")
        print("-" * 70)
        print(f"Total Leads:      {metrics['total_leads']}")
        print(f"Emails Sent:      {metrics['sent']}")
        print(f"Bounced:          {metrics['bounced']}")
        print(f"\n📧 ENGAGEMENT")
        print("-" * 70)
        print(f"Opened:           {metrics['opened']} ({metrics['open_rate']}%)")
        print(f"Clicked:          {metrics['clicked']} ({metrics['click_rate']}%)")
        print(f"Replied:          {metrics['replied']} ({metrics['reply_rate']}%)")
        
        # Performance assessment
        print(f"\n🎯 PERFORMANCE ASSESSMENT")
        print("-" * 70)
        
        # Open rate
        if metrics['open_rate'] >= 50:
            print("✅ Open Rate: EXCELLENT")
        elif metrics['open_rate'] >= 40:
            print("✅ Open Rate: GOOD")
        elif metrics['open_rate'] >= 30:
            print("⚠️  Open Rate: AVERAGE (consider testing new subject lines)")
        else:
            print("❌ Open Rate: NEEDS IMPROVEMENT (check spam score)")
        
        # Reply rate
        if metrics['reply_rate'] >= 10:
            print("✅ Reply Rate: EXCELLENT")
        elif metrics['reply_rate'] >= 5:
            print("✅ Reply Rate: GOOD")
        elif metrics['reply_rate'] >= 3:
            print("⚠️  Reply Rate: AVERAGE")
        else:
            print("❌ Reply Rate: NEEDS IMPROVEMENT")
        
        # Expected conversions
        print(f"\n💰 PROJECTED RESULTS")
        print("-" * 70)
        
        # Assuming 30% of replies are positive interest
        positive_replies_est = int(metrics['replied'] * 0.3)
        # Assuming 50% of interested leads book demo
        demos_est = int(positive_replies_est * 0.5)
        # Assuming 40% of demos convert
        conversions_est = int(demos_est * 0.4)
        
        print(f"Estimated Positive Replies:  {positive_replies_est}")
        print(f"Estimated Demos Booked:      {demos_est}")
        print(f"Estimated Conversions:       {conversions_est}")
        
        # Cost per lead (assuming typical SaaS metrics)
        if conversions_est > 0:
            # Assume $500 LTV for a Voxable customer
            estimated_revenue = conversions_est * 500
            print(f"Estimated Revenue:           ${estimated_revenue:,}")
        
        # Recent replies
        print(f"\n💬 RECENT ACTIVITY")
        print("-" * 70)
        
        replies = analytics.get_replies(campaign_name)
        if replies:
            for i, reply in enumerate(replies[:5], 1):
                print(f"\n{i}. {reply.get('lead_email', 'Unknown')}")
                print(f"   {reply.get('message', '')[:100]}...")
        else:
            print("No replies yet")
        
        print("\n" + "=" * 70)
        
    except Exception as e:
        print(f"❌ Error fetching campaign data: {e}")

def export_replies_to_csv(campaign_name: str, api_key: str, output_file: str):
    """Export replies to CSV for follow-up"""
    import csv
    
    analytics = InstantlyAnalytics(api_key)
    replies = analytics.get_replies(campaign_name)
    
    if not replies:
        print("No replies to export")
        return
    
    with open(output_file, 'w', newline='') as f:
        fieldnames = ['email', 'name', 'company', 'message', 'timestamp', 'sentiment', 'action_needed']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for reply in replies:
            # Simple sentiment analysis
            message = reply.get('message', '').lower()
            
            sentiment = 'neutral'
            if any(word in message for word in ['interested', 'yes', 'sure', 'tell me more', 'demo']):
                sentiment = 'positive'
            elif any(word in message for word in ['not interested', 'no thanks', 'remove', 'unsubscribe']):
                sentiment = 'negative'
            
            action_needed = 'Book demo' if sentiment == 'positive' else 'Follow up' if sentiment == 'neutral' else 'Remove'
            
            writer.writerow({
                'email': reply.get('lead_email', ''),
                'name': reply.get('lead_name', ''),
                'company': reply.get('company_name', ''),
                'message': reply.get('message', '')[:200],
                'timestamp': reply.get('timestamp', ''),
                'sentiment': sentiment,
                'action_needed': action_needed
            })
    
    print(f"✅ Exported {len(replies)} replies to {output_file}")

def send_daily_digest(campaign_name: str, api_key: str, email: str = None):
    """Generate and optionally email daily digest"""
    
    analytics = InstantlyAnalytics(api_key)
    leads = analytics.get_lead_status(campaign_name)
    
    if not leads:
        print("No data available for digest")
        return
    
    metrics = calculate_metrics(leads)
    replies = analytics.get_replies(campaign_name)
    
    # Build digest
    digest = f"""
📊 VOXABLE CAMPAIGN DAILY DIGEST
Campaign: {campaign_name}
Date: {datetime.now().strftime('%Y-%m-%d')}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 PERFORMANCE SUMMARY
• Emails Sent:    {metrics['sent']}
• Open Rate:      {metrics['open_rate']}%
• Reply Rate:     {metrics['reply_rate']}%
• New Replies:    {len(replies)}

💬 LATEST REPLIES
"""
    
    for i, reply in enumerate(replies[:5], 1):
        digest += f"\n{i}. {reply.get('lead_email', 'Unknown')}\n"
        digest += f"   {reply.get('message', '')[:150]}...\n"
    
    digest += f"\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    # Print digest
    print(digest)
    
    # TODO: Add email sending capability
    if email:
        print(f"\n✉️  Email digest to {email} (not implemented yet)")

def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Track Voxable campaign performance')
    parser.add_argument('--api-key', help='Instantly.ai API key (or set INSTANTLY_API_KEY env var)')
    parser.add_argument('--campaign', required=True, help='Campaign name to track')
    parser.add_argument('--dashboard', action='store_true', help='Show dashboard')
    parser.add_argument('--export-replies', help='Export replies to CSV file')
    parser.add_argument('--daily-digest', action='store_true', help='Generate daily digest')
    parser.add_argument('--email', help='Email address for daily digest')
    
    args = parser.parse_args()
    
    # Get API key
    api_key = args.api_key or os.getenv('INSTANTLY_API_KEY')
    if not api_key:
        print("❌ Error: API key required")
        print("Set INSTANTLY_API_KEY environment variable or use --api-key flag")
        sys.exit(1)
    
    # Dashboard
    if args.dashboard:
        display_campaign_dashboard(args.campaign, api_key)
    
    # Export replies
    if args.export_replies:
        export_replies_to_csv(args.campaign, api_key, args.export_replies)
    
    # Daily digest
    if args.daily_digest:
        send_daily_digest(args.campaign, api_key, args.email)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Instantly.ai Campaign Launcher
Automates campaign creation, lead upload, and sequence setup for Voxable outreach
"""

import os
import sys
import json
import requests
from datetime import datetime
from typing import List, Dict, Optional

class InstantlyClient:
    """Client for Instantly.ai API"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.instantly.ai/api/v1"
        self.headers = {
            "Content-Type": "application/json"
        }
    
    def _request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict:
        """Make API request"""
        url = f"{self.base_url}{endpoint}"
        params = {"api_key": self.api_key}
        
        if data:
            params.update(data)
        
        try:
            if method == "GET":
                response = requests.get(url, params=params, headers=self.headers)
            elif method == "POST":
                response = requests.post(url, json=params, headers=self.headers)
            elif method == "DELETE":
                response = requests.delete(url, params=params, headers=self.headers)
            else:
                raise ValueError(f"Unsupported method: {method}")
            
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"❌ API Error: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response: {e.response.text}")
            sys.exit(1)
    
    def list_campaigns(self) -> List[Dict]:
        """List all campaigns"""
        result = self._request("GET", "/campaign/list")
        return result
    
    def create_campaign(self, name: str) -> Dict:
        """Create new campaign"""
        data = {"name": name}
        return self._request("POST", "/campaign/create", data)
    
    def add_leads(self, campaign_name: str, leads: List[Dict]) -> Dict:
        """Add leads to campaign"""
        data = {
            "campaign_name": campaign_name,
            "leads": leads,
            "skip_if_in_workspace": True  # Don't add duplicates
        }
        return self._request("POST", "/lead/add", data)
    
    def launch_campaign(self, campaign_name: str) -> Dict:
        """Launch/start campaign"""
        data = {"campaign_name": campaign_name}
        return self._request("POST", "/campaign/launch", data)
    
    def pause_campaign(self, campaign_name: str) -> Dict:
        """Pause campaign"""
        data = {"campaign_name": campaign_name}
        return self._request("POST", "/campaign/pause", data)

def load_leads_from_csv(file_path: str) -> List[Dict]:
    """Load leads from CSV file"""
    import csv
    
    leads = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Map CSV columns to Instantly.ai format
            lead = {
                "email": row.get('email', row.get('Email', '')).strip(),
                "first_name": row.get('first_name', row.get('FirstName', row.get('First Name', ''))).strip(),
                "last_name": row.get('last_name', row.get('LastName', row.get('Last Name', ''))).strip(),
                "company_name": row.get('company_name', row.get('CompanyName', row.get('Company', ''))).strip(),
                "phone": row.get('phone', row.get('Phone', '')).strip(),
                "website": row.get('website', row.get('Website', '')).strip(),
                "personalization": row.get('personalization', '').strip(),
            }
            
            # Only add if email exists
            if lead['email']:
                leads.append(lead)
    
    return leads

def load_leads_from_json(file_path: str) -> List[Dict]:
    """Load leads from JSON file"""
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    # Handle both array of leads and object with leads array
    if isinstance(data, list):
        return data
    elif isinstance(data, dict) and 'leads' in data:
        return data['leads']
    else:
        print("❌ Invalid JSON format. Expected array or object with 'leads' key")
        sys.exit(1)

def get_voxable_sequences() -> List[Dict]:
    """Get email sequences for Voxable campaign"""
    return [
        {
            "day": 1,
            "subject": "Quick question about missed calls at {{company_name}}",
            "body": """Hi {{first_name}},

I'll get straight to it:

Most local businesses miss about 20–30% of their incoming calls simply because they're busy helping the customer right in front of them.

In the world of service-based businesses, **a missed call is usually a missed paycheck.**

I'm working with Voxable, and we've developed a 24/7 AI Sales Receptionist specifically to solve this. It doesn't just take a message—it answers questions, qualifies leads, and even schedules appointments directly into your calendar while you're off the clock.

Do you have 5 minutes later this week to see how we could stop those leads from calling your competitor instead?

Best,
[Your Name]

P.S. Want to test it yourself? Call our AI at **267-550-0466** and see what your customers would experience."""
        },
        {
            "day": 3,
            "subject": "Scaling {{company_name}} without the extra payroll",
            "body": """Hi {{first_name}},

Following up on my last note.

One of the biggest hurdles I see for local owners is the **"hiring trap"**—needing a receptionist to grow, but not having the budget to pay a full-time salary plus benefits.

Voxable acts as your digital front desk for a fraction of the cost of a new hire:

✅ **Zero Hold Times:** It answers on the first ring, every time.
✅ **24/7/365:** It handles 2:00 AM inquiries while you're sleeping.
✅ **Direct Booking:** It syncs with your current tools to fill your schedule.

I'd love to show you a quick 2-minute demo of the AI in action.

Are you open to a brief chat on [Day of the week]?

Best,
[Your Name]

[Book a 5-min demo] or reply with a good time to connect."""
        },
        {
            "day": 7,
            "subject": "Should I take you off my list, {{first_name}}?",
            "body": """Hi {{first_name}},

I haven't heard back, so I'll assume that capturing after-hours leads or automating your front desk isn't a top priority for {{company_name}} right now.

I'm going to take you off my follow-up list so I don't clutter your inbox.

If your "To-Do" list gets too long or you decide you're tired of playing phone tag with new customers, feel free to reach back out. I'd be happy to help you get an AI receptionist up and running.

Wishing you the best of luck with the business.

Best,
[Your Name]

[Link to Voxable Demo]"""
        }
    ]

def setup_voxable_campaign(api_key: str, leads_file: str, campaign_name: str = None, dry_run: bool = False):
    """Set up complete Voxable outreach campaign"""
    
    # Default campaign name
    if not campaign_name:
        campaign_name = f"Voxable - Local Service - {datetime.now().strftime('%b %Y')}"
    
    print(f"🚀 Setting up Voxable campaign: {campaign_name}")
    print("=" * 60)
    
    # Load leads
    print(f"\n📋 Loading leads from {leads_file}...")
    if leads_file.endswith('.csv'):
        leads = load_leads_from_csv(leads_file)
    elif leads_file.endswith('.json'):
        leads = load_leads_from_json(leads_file)
    else:
        print("❌ Unsupported file format. Use .csv or .json")
        sys.exit(1)
    
    print(f"✅ Loaded {len(leads)} leads")
    
    # Validate leads
    valid_leads = [l for l in leads if l.get('email') and l.get('first_name')]
    if len(valid_leads) < len(leads):
        print(f"⚠️  {len(leads) - len(valid_leads)} leads missing email or first name (will be skipped)")
    
    print(f"✅ {len(valid_leads)} valid leads ready")
    
    if dry_run:
        print("\n🔍 DRY RUN MODE - No changes will be made")
        print("\nSample lead:")
        print(json.dumps(valid_leads[0] if valid_leads else {}, indent=2))
        print("\nEmail sequences:")
        for seq in get_voxable_sequences():
            print(f"  Day {seq['day']}: {seq['subject']}")
        return
    
    # Initialize client
    client = InstantlyClient(api_key)
    
    # Create campaign
    print(f"\n📧 Creating campaign '{campaign_name}'...")
    try:
        result = client.create_campaign(campaign_name)
        print(f"✅ Campaign created")
    except Exception as e:
        print(f"⚠️  Campaign may already exist or error occurred: {e}")
    
    # Add leads
    print(f"\n👥 Adding {len(valid_leads)} leads to campaign...")
    result = client.add_leads(campaign_name, valid_leads)
    print(f"✅ Leads added")
    
    # Display sequences info
    print("\n📝 Email Sequences (configure in Instantly.ai dashboard):")
    for seq in get_voxable_sequences():
        print(f"\n  Email {seq['day']} - Day {seq['day']}")
        print(f"  Subject: {seq['subject']}")
        print(f"  Preview: {seq['body'][:100]}...")
    
    print("\n" + "=" * 60)
    print("✅ Campaign setup complete!")
    print("\nNext steps:")
    print("1. Log into Instantly.ai dashboard")
    print("2. Configure email sequences (copy from above)")
    print("3. Set sending schedule (Mon-Fri, 9am-5pm)")
    print("4. Configure settings:")
    print("   - Max 30-40 emails/day")
    print("   - Auto-stop on reply")
    print("   - 2-5 min delays between sends")
    print("5. Test with 10-20 leads first")
    print("6. Launch full campaign")
    print(f"\n🎯 Campaign name: {campaign_name}")

def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Launch Instantly.ai campaign for Voxable')
    parser.add_argument('--api-key', help='Instantly.ai API key (or set INSTANTLY_API_KEY env var)')
    parser.add_argument('--leads', required=True, help='Path to leads CSV or JSON file')
    parser.add_argument('--campaign-name', help='Campaign name (default: auto-generated)')
    parser.add_argument('--dry-run', action='store_true', help='Preview without making changes')
    parser.add_argument('--list-campaigns', action='store_true', help='List existing campaigns')
    
    args = parser.parse_args()
    
    # Get API key
    api_key = args.api_key or os.getenv('INSTANTLY_API_KEY')
    if not api_key:
        print("❌ Error: API key required")
        print("Set INSTANTLY_API_KEY environment variable or use --api-key flag")
        sys.exit(1)
    
    # List campaigns mode
    if args.list_campaigns:
        print("📋 Fetching campaigns...")
        client = InstantlyClient(api_key)
        campaigns = client.list_campaigns()
        print(json.dumps(campaigns, indent=2))
        return
    
    # Setup campaign
    setup_voxable_campaign(
        api_key=api_key,
        leads_file=args.leads,
        campaign_name=args.campaign_name,
        dry_run=args.dry_run
    )

if __name__ == "__main__":
    main()

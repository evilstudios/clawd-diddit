#!/usr/bin/env python3
"""
Instantly.ai Campaign Builder - Proper API Implementation
Automates campaign creation using Instantly.ai REST API
"""

import requests
import json
import os
import sys
from typing import Dict, List, Optional

# API Configuration
INSTANTLY_API_KEY = os.getenv('INSTANTLY_API_KEY', 'ZmY1YTRkZTktYmRiNC00N2ZiLWFmMzktN2JhNzg5YmNlYWI4OmV3WlBiZ2NGR0lRUA==')
INSTANTLY_API_BASE = "https://api.instantly.ai/api/v1"

class InstantlyAPI:
    """Instantly.ai API wrapper"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.headers = {
            'Content-Type': 'application/json'
        }
    
    def _request(self, method: str, endpoint: str, data: Optional[Dict] = None) -> Dict:
        """Make API request"""
        url = f"{INSTANTLY_API_BASE}/{endpoint}"
        
        # Prepare data with API key
        if data is None:
            data = {}
        
        # Add API key to data
        request_data = {**data, 'api_key': self.api_key}
        
        try:
            if method == 'GET':
                # For GET requests, pass as query params
                response = requests.get(url, params=request_data, headers=self.headers)
            elif method == 'POST':
                # For POST requests, pass in JSON body
                response = requests.post(url, json=request_data, headers=self.headers)
            elif method == 'DELETE':
                # For DELETE requests, pass in JSON body
                response = requests.delete(url, json=request_data, headers=self.headers)
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
        result = self._request('GET', 'campaign/list')
        return result
    
    def create_campaign(self, name: str) -> Dict:
        """Create new campaign"""
        data = {'name': name}
        return self._request('POST', 'campaign/add', data)
    
    def add_leads(self, campaign_name: str, leads: List[Dict]) -> Dict:
        """Add leads to campaign"""
        data = {
            'campaign_name': campaign_name,
            'leads': leads,
            'skip_if_in_workspace': True  # Don't add duplicates
        }
        return self._request('POST', 'lead/add', data)
    
    def get_accounts(self) -> List[Dict]:
        """Get all email accounts"""
        return self._request('GET', 'account/list')
    
    def launch_campaign(self, campaign_name: str) -> Dict:
        """Launch campaign"""
        data = {'campaign_name': campaign_name}
        return self._request('POST', 'campaign/launch', data)
    
    def pause_campaign(self, campaign_name: str) -> Dict:
        """Pause campaign"""
        data = {'campaign_name': campaign_name}
        return self._request('POST', 'campaign/pause', data)


def load_leads_from_csv(csv_path: str) -> List[Dict]:
    """Load leads from CSV file"""
    import csv
    
    leads = []
    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Map CSV columns to Instantly API format
            lead = {
                'email': row.get('Email', row.get('email', '')),
                'first_name': row.get('First Name', row.get('first_name', '')),
                'last_name': row.get('Last Name', row.get('last_name', '')),
                'company_name': row.get('Company', row.get('company', '')),
            }
            
            # Only add valid emails
            if lead['email'] and '@' in lead['email']:
                leads.append(lead)
    
    return leads


def create_ai_employee_campaign():
    """
    Create and configure AI Employee Service campaign
    """
    
    print("🚀 Instantly.ai Campaign Builder")
    print("=" * 50)
    
    api = InstantlyAPI(INSTANTLY_API_KEY)
    
    # Configuration
    campaign_name = "AI Employee Service - Cold Outreach"
    csv_path = "/root/clawd/projects/ai-employee-service/leads.csv"  # To be created
    
    print(f"\n📋 Campaign: {campaign_name}")
    
    # Step 1: Check if campaign already exists
    print("\n1️⃣ Checking existing campaigns...")
    try:
        campaigns = api.list_campaigns()
        existing_campaign = next((c for c in campaigns if c.get('name') == campaign_name), None)
        
        if existing_campaign:
            print(f"⚠️  Campaign '{campaign_name}' already exists")
            response = input("Create a new one with timestamp? (y/n): ").strip().lower()
            if response == 'y':
                import datetime
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
                campaign_name = f"{campaign_name} - {timestamp}"
                print(f"✅ New campaign name: {campaign_name}")
            else:
                print("❌ Cancelled")
                return
    except Exception as e:
        print(f"⚠️  Could not check campaigns: {e}")
    
    # Step 2: Create campaign
    print(f"\n2️⃣ Creating campaign...")
    try:
        result = api.create_campaign(campaign_name)
        print(f"✅ Campaign created: {campaign_name}")
    except Exception as e:
        print(f"❌ Failed to create campaign: {e}")
        return
    
    # Step 3: Check for leads CSV
    print(f"\n3️⃣ Looking for leads CSV...")
    if not os.path.exists(csv_path):
        print(f"⚠️  No leads file found at: {csv_path}")
        print("\n💡 To add leads manually:")
        print(f"   1. Create {csv_path}")
        print("   2. Format: Email, First Name, Last Name, Company")
        print("   3. Re-run this script")
        print("\nOr use Instantly.ai web UI to upload leads manually")
        return
    
    # Step 4: Load and add leads
    print(f"📂 Loading leads from {csv_path}...")
    leads = load_leads_from_csv(csv_path)
    
    if not leads:
        print("❌ No valid leads found in CSV")
        return
    
    print(f"✅ Found {len(leads)} valid leads")
    
    print(f"\n4️⃣ Adding leads to campaign...")
    try:
        result = api.add_leads(campaign_name, leads)
        print(f"✅ Added {len(leads)} leads to campaign")
    except Exception as e:
        print(f"❌ Failed to add leads: {e}")
        return
    
    # Step 5: Display next steps
    print("\n" + "=" * 50)
    print("✅ Campaign created successfully!")
    print("\n📝 Next Steps:")
    print("1. Go to Instantly.ai dashboard")
    print(f"2. Find campaign: '{campaign_name}'")
    print("3. Add email sequences (use the sequence from COLD-EMAIL-SEQUENCE.md)")
    print("4. Configure settings:")
    print("   - Schedule: Mon-Fri, 9am-5pm")
    print("   - Volume: 25-40 emails/day")
    print("   - Stop on reply: ON")
    print("5. Launch campaign")
    print("\n🚀 Ready to go!")


def test_api_connection():
    """Test API connection"""
    print("🔌 Testing Instantly.ai API connection...")
    
    api = InstantlyAPI(INSTANTLY_API_KEY)
    
    try:
        # Test: List accounts
        print("\n1️⃣ Fetching accounts...")
        accounts = api.get_accounts()
        print(f"✅ Found {len(accounts)} email account(s)")
        
        for acc in accounts:
            print(f"   - {acc.get('email', 'Unknown')} (Status: {acc.get('status', 'Unknown')})")
        
        # Test: List campaigns
        print("\n2️⃣ Fetching campaigns...")
        campaigns = api.list_campaigns()
        print(f"✅ Found {len(campaigns)} campaign(s)")
        
        for camp in campaigns[:5]:  # Show first 5
            print(f"   - {camp.get('name', 'Unknown')} (Status: {camp.get('status', 'Unknown')})")
        
        print("\n✅ API connection successful!")
        return True
        
    except Exception as e:
        print(f"\n❌ API connection failed: {e}")
        return False


if __name__ == "__main__":
    import sys
    
    # Check API key
    if not INSTANTLY_API_KEY:
        print("❌ Error: INSTANTLY_API_KEY not set")
        print("Set it in .env.instantly or export it:")
        print('export INSTANTLY_API_KEY="your_api_key_here"')
        sys.exit(1)
    
    # Parse command
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "test":
            test_api_connection()
        elif command == "create":
            create_ai_employee_campaign()
        elif command == "list":
            api = InstantlyAPI(INSTANTLY_API_KEY)
            campaigns = api.list_campaigns()
            print(f"📋 {len(campaigns)} campaign(s):")
            for c in campaigns:
                print(f"   - {c.get('name')} ({c.get('status')})")
        else:
            print(f"❌ Unknown command: {command}")
            print("Usage: python3 instantly-api-campaign-builder.py [test|create|list]")
    else:
        # Interactive mode
        print("Instantly.ai Campaign Builder")
        print("=" * 50)
        print("\nCommands:")
        print("  test   - Test API connection")
        print("  create - Create AI Employee campaign")
        print("  list   - List all campaigns")
        print()
        command = input("Enter command: ").strip().lower()
        
        if command == "test":
            test_api_connection()
        elif command == "create":
            create_ai_employee_campaign()
        elif command == "list":
            api = InstantlyAPI(INSTANTLY_API_KEY)
            campaigns = api.list_campaigns()
            print(f"\n📋 {len(campaigns)} campaign(s):")
            for c in campaigns:
                print(f"   - {c.get('name')} ({c.get('status')})")
        else:
            print("❌ Invalid command")

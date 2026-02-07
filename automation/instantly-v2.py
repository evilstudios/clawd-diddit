#!/usr/bin/env python3
"""
Instantly.ai API V2 Wrapper
Complete automation for campaign management and lead uploads.
"""

import os
import sys
import json
import requests
from typing import Dict, List, Optional
from pathlib import Path

class InstantlyV2:
    """Clean wrapper for Instantly.ai API V2"""
    
    def __init__(self, api_key: Optional[str] = None):
        # Try multiple sources for API key
        self.api_key = api_key or os.getenv('INSTANTLY_API_KEY')
        
        if not self.api_key:
            # Try loading from .env.instantly
            env_file = Path(__file__).parent.parent / '.env.instantly'
            if env_file.exists():
                content = env_file.read_text()
                for line in content.split('\n'):
                    if 'INSTANTLY_API_KEY=' in line:
                        self.api_key = line.split('"')[1]
                        break
        
        if not self.api_key:
            raise ValueError("INSTANTLY_API_KEY not found. Set it in .env.instantly or environment.")
        
        self.base_url = "https://api.instantly.ai/api/v2"
        self.headers = {"Authorization": f"Bearer {self.api_key}"}
    
    def _request(self, method: str, endpoint: str, **kwargs) -> Dict:
        """Make API request with error handling"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            response = requests.request(method, url, headers=self.headers, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"❌ API Error: {e}")
            print(f"Response: {response.text}")
            raise
    
    # Campaign Management
    
    def list_campaigns(self) -> List[Dict]:
        """List all campaigns"""
        data = self._request('GET', '/campaigns')
        return data.get('items', [])
    
    def get_campaign(self, campaign_id: str) -> Dict:
        """Get campaign details"""
        return self._request('GET', f'/campaigns/{campaign_id}')
    
    def create_campaign(self, name: str, from_email: str, **kwargs) -> Dict:
        """
        Create a new campaign.
        
        Args:
            name: Campaign name
            from_email: Sender email address
            **kwargs: Additional campaign settings (daily_limit, schedules, etc.)
        """
        payload = {
            "name": name,
            "email_list": [from_email],
            **kwargs
        }
        return self._request('POST', '/campaigns', json=payload)
    
    def update_campaign(self, campaign_id: str, **kwargs) -> Dict:
        """Update campaign settings"""
        return self._request('PATCH', f'/campaigns/{campaign_id}', json=kwargs)
    
    def delete_campaign(self, campaign_id: str) -> Dict:
        """Delete a campaign"""
        return self._request('DELETE', f'/campaigns/{campaign_id}')
    
    # Lead Management
    
    def add_lead(self, campaign_id: str, email: str, **kwargs) -> Dict:
        """
        Add a lead to a campaign.
        
        Args:
            campaign_id: Target campaign ID
            email: Lead email address
            **kwargs: Additional fields (first_name, last_name, company, etc.)
        """
        payload = {
            "campaign": campaign_id,
            "email": email,
            "skip_if_in_workspace": True,
            **kwargs
        }
        return self._request('POST', '/leads', json=payload)
    
    def add_leads_bulk(self, campaign_id: str, leads: List[Dict]) -> List[Dict]:
        """
        Add multiple leads to a campaign.
        
        Args:
            campaign_id: Target campaign ID
            leads: List of lead dicts with email + custom fields
        
        Returns:
            List of results (success/failure for each lead)
        """
        results = []
        for lead in leads:
            try:
                result = self.add_lead(campaign_id, **lead)
                results.append({"email": lead['email'], "status": "success", "data": result})
            except Exception as e:
                results.append({"email": lead['email'], "status": "error", "error": str(e)})
        return results
    
    def list_leads(self, campaign_id: str, limit: int = 100) -> List[Dict]:
        """List leads in a campaign"""
        data = self._request('GET', f'/campaigns/{campaign_id}/leads', params={"limit": limit})
        return data.get('items', [])
    
    def delete_lead(self, lead_id: str) -> Dict:
        """Delete a lead"""
        return self._request('DELETE', f'/leads/{lead_id}')
    
    # Account Management
    
    def list_accounts(self) -> List[Dict]:
        """List email accounts"""
        data = self._request('GET', '/accounts')
        return data.get('items', [])
    
    # Analytics
    
    def get_campaign_analytics(self, campaign_id: str) -> Dict:
        """Get campaign performance analytics"""
        return self._request('GET', f'/campaigns/{campaign_id}/analytics')


# CLI Interface
def main():
    if len(sys.argv) < 2:
        print("""
Instantly.ai V2 API Manager
============================

Usage:
  python3 instantly-v2.py <command> [args]

Commands:
  test                                  - Test API connection
  campaigns                             - List all campaigns
  campaign <id>                         - Get campaign details
  leads <campaign_id>                   - List leads in campaign
  add-lead <campaign_id> <email>        - Add single lead
  bulk-upload <campaign_id> <csv_file>  - Upload leads from CSV
  analytics <campaign_id>               - Get campaign analytics
  accounts                              - List email accounts

Examples:
  python3 instantly-v2.py test
  python3 instantly-v2.py campaigns
  python3 instantly-v2.py add-lead abc123 john@example.com --first_name=John --last_name=Doe
  python3 instantly-v2.py bulk-upload abc123 leads.csv
""")
        sys.exit(1)
    
    command = sys.argv[1]
    api = InstantlyV2()
    
    try:
        if command == "test":
            print("🔌 Testing Instantly.ai API V2...\n")
            campaigns = api.list_campaigns()
            print(f"✅ Connection successful!")
            print(f"   Found {len(campaigns)} campaigns\n")
            
            if campaigns:
                print("Campaigns:")
                for c in campaigns[:5]:
                    print(f"   - {c['name']}")
                    print(f"     ID: {c['id']}")
                    print(f"     Status: {'Active' if c['status'] == 1 else 'Paused'}")
                    print()
        
        elif command == "campaigns":
            campaigns = api.list_campaigns()
            print(f"Found {len(campaigns)} campaigns:\n")
            for c in campaigns:
                print(f"📧 {c['name']}")
                print(f"   ID: {c['id']}")
                print(f"   Status: {'Active' if c['status'] == 1 else 'Paused'}")
                print(f"   Daily Limit: {c.get('daily_limit', 'N/A')}")
                print()
        
        elif command == "campaign":
            if len(sys.argv) < 3:
                print("Usage: python3 instantly-v2.py campaign <campaign_id>")
                sys.exit(1)
            campaign_id = sys.argv[2]
            campaign = api.get_campaign(campaign_id)
            print(json.dumps(campaign, indent=2))
        
        elif command == "leads":
            if len(sys.argv) < 3:
                print("Usage: python3 instantly-v2.py leads <campaign_id>")
                sys.exit(1)
            campaign_id = sys.argv[2]
            leads = api.list_leads(campaign_id)
            print(f"Found {len(leads)} leads:\n")
            for lead in leads[:20]:
                print(f"📨 {lead.get('email')}")
                print(f"   Name: {lead.get('first_name', '')} {lead.get('last_name', '')}")
                print(f"   Status: {lead.get('status', 'N/A')}")
                print()
        
        elif command == "add-lead":
            if len(sys.argv) < 4:
                print("Usage: python3 instantly-v2.py add-lead <campaign_id> <email> [--first_name=John] [--last_name=Doe]")
                sys.exit(1)
            
            campaign_id = sys.argv[2]
            email = sys.argv[3]
            
            # Parse optional args
            kwargs = {}
            for arg in sys.argv[4:]:
                if arg.startswith('--'):
                    key, value = arg[2:].split('=', 1)
                    kwargs[key] = value
            
            result = api.add_lead(campaign_id, email, **kwargs)
            print(f"✅ Lead added: {email}")
            print(json.dumps(result, indent=2))
        
        elif command == "bulk-upload":
            if len(sys.argv) < 4:
                print("Usage: python3 instantly-v2.py bulk-upload <campaign_id> <csv_file>")
                sys.exit(1)
            
            import csv
            campaign_id = sys.argv[2]
            csv_file = sys.argv[3]
            
            leads = []
            with open(csv_file, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    leads.append(row)
            
            print(f"📤 Uploading {len(leads)} leads to campaign {campaign_id}...\n")
            results = api.add_leads_bulk(campaign_id, leads)
            
            success = sum(1 for r in results if r['status'] == 'success')
            failed = len(results) - success
            
            print(f"\n✅ Success: {success}")
            print(f"❌ Failed: {failed}")
            
            if failed > 0:
                print("\nFailed leads:")
                for r in results:
                    if r['status'] == 'error':
                        print(f"   - {r['email']}: {r['error']}")
        
        elif command == "analytics":
            if len(sys.argv) < 3:
                print("Usage: python3 instantly-v2.py analytics <campaign_id>")
                sys.exit(1)
            
            campaign_id = sys.argv[2]
            analytics = api.get_campaign_analytics(campaign_id)
            print(json.dumps(analytics, indent=2))
        
        elif command == "accounts":
            accounts = api.list_accounts()
            print(f"Found {len(accounts)} email accounts:\n")
            for acc in accounts:
                print(f"📧 {acc.get('email')}")
                print(f"   Status: {acc.get('status', 'N/A')}")
                print(f"   Warmup: {acc.get('warmup_enabled', False)}")
                print()
        
        else:
            print(f"❌ Unknown command: {command}")
            print("Run without arguments to see usage.")
            sys.exit(1)
    
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Instantly.ai API V1 - Simple Campaign Manager
Works with existing V1 API key
"""

import requests
import json
import os
import sys
from typing import Dict, List, Optional

# API Configuration
INSTANTLY_API_KEY = os.getenv('INSTANTLY_API_KEY', 'ZmY1YTRkZTktYmRiNC00N2ZiLWFmMzktN2JhNzg5YmNlYWI4OmV3WlBiZ2NGR0lRUA==')
INSTANTLY_API_BASE = "https://api.instantly.ai/api/v1"

def api_request(endpoint: str, data: Dict = None) -> Dict:
    """Make API request to Instantly V1"""
    url = f"{INSTANTLY_API_BASE}/{endpoint}"
    
    if data is None:
        data = {}
    
    # V1 API uses api_key in request body/params
    data['api_key'] = INSTANTLY_API_KEY
    
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"❌ API Error: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print(f"Response: {e.response.text}")
        return {"error": str(e)}

def list_campaigns():
    """List all campaigns"""
    print("📋 Fetching campaigns...")
    result = api_request("campaign/list")
    
    if "error" in result:
        print(f"❌ Failed: {result['error']}")
        return
    
    # V1 API response format varies - handle it gracefully
    campaigns = result if isinstance(result, list) else result.get('campaigns', [])
    
    print(f"✅ Found {len(campaigns)} campaign(s):\n")
    for camp in campaigns:
        name = camp.get('name', 'Unknown')
        status = camp.get('status', 'Unknown')
        print(f"   • {name} ({status})")

def list_accounts():
    """List email accounts"""
    print("📧 Fetching email accounts...")
    result = api_request("account/list")
    
    if "error" in result:
        print(f"❌ Failed: {result['error']}")
        return
    
    accounts = result if isinstance(result, list) else result.get('accounts', [])
    
    print(f"✅ Found {len(accounts)} account(s):\n")
    for acc in accounts:
        email = acc.get('email', 'Unknown')
        status = acc.get('status', acc.get('active', 'Unknown'))
        print(f"   • {email} (Status: {status})")

def test_connection():
    """Test API connection"""
    print("🔌 Testing Instantly.ai API V1 connection...")
    print("=" * 50)
    
    # Try accounts first
    print("\n1️⃣ Testing account endpoint...")
    accounts_result = api_request("account/list")
    
    if "error" not in accounts_result:
        accounts = accounts_result if isinstance(accounts_result, list) else accounts_result.get('accounts', [])
        print(f"✅ Account endpoint working - {len(accounts)} account(s) found")
    else:
        print(f"❌ Account endpoint failed")
        print(f"   Error: {accounts_result.get('error')}")
    
    # Try campaigns
    print("\n2️⃣ Testing campaign endpoint...")
    campaigns_result = api_request("campaign/list")
    
    if "error" not in campaigns_result:
        campaigns = campaigns_result if isinstance(campaigns_result, list) else campaigns_result.get('campaigns', [])
        print(f"✅ Campaign endpoint working - {len(campaigns)} campaign(s) found")
    else:
        print(f"❌ Campaign endpoint failed")
        print(f"   Error: {campaigns_result.get('error')}")
    
    print("\n" + "=" * 50)
    
    if "error" not in accounts_result or "error" not in campaigns_result:
        print("✅ API connection functional!")
        return True
    else:
        print("❌ API connection failed on all endpoints")
        print("\n💡 Troubleshooting:")
        print("   1. Check your API key in .env.instantly")
        print("   2. Verify it's a V1 API key (base64 format)")
        print("   3. Try regenerating the key at instantly.ai/settings")
        return False

def create_campaign(name: str):
    """Create a new campaign"""
    print(f"📝 Creating campaign: {name}")
    result = api_request("campaign/add", {"name": name})
    
    if "error" in result:
        print(f"❌ Failed: {result['error']}")
        return False
    
    print(f"✅ Campaign created successfully!")
    return True

if __name__ == "__main__":
    if not INSTANTLY_API_KEY:
        print("❌ Error: INSTANTLY_API_KEY not set")
        print('Export it: export INSTANTLY_API_KEY="your_key"')
        sys.exit(1)
    
    print("Instantly.ai API V1 - Simple Manager")
    print("=" * 50)
    print("\nCommands:")
    print("  test      - Test API connection")
    print("  accounts  - List email accounts")
    print("  campaigns - List campaigns")
    print("  create    - Create a new campaign")
    print()
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
    else:
        command = input("Enter command: ").strip().lower()
    
    if command == "test":
        test_connection()
    elif command == "accounts":
        list_accounts()
    elif command == "campaigns":
        list_campaigns()
    elif command == "create":
        if len(sys.argv) > 2:
            campaign_name = " ".join(sys.argv[2:])
        else:
            campaign_name = input("Campaign name: ").strip()
        create_campaign(campaign_name)
    else:
        print(f"❌ Unknown command: {command}")

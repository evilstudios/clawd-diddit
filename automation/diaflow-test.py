#!/usr/bin/env python3
"""
Diaflow API Test - Explore capabilities
"""

import requests
import json

# Diaflow credentials
API_KEY = "sk-7444719b94144c27ae335dea6a628443"
BASE_URL = "https://atlantica.diaflow.app"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def test_connection():
    """Test basic API connectivity"""
    print("🔌 Testing Diaflow API connection...")
    
    # Try to get account/workspace info
    endpoints_to_try = [
        "/api/v1/me",
        "/api/v1/account",
        "/api/v1/workspaces",
        "/api/v1/workflows",
        "/api/v1/executions",
        "/api/user",
        "/api/workflows"
    ]
    
    for endpoint in endpoints_to_try:
        url = f"{BASE_URL}{endpoint}"
        try:
            response = requests.get(url, headers=headers, timeout=10)
            print(f"\n📍 {endpoint}")
            print(f"Status: {response.status_code}")
            if response.status_code == 200:
                print(f"✅ Success!")
                print(f"Response: {json.dumps(response.json(), indent=2)[:500]}")
                return response.json()
            else:
                print(f"❌ Error: {response.text[:200]}")
        except Exception as e:
            print(f"❌ Failed: {e}")
    
    return None

def list_workflows():
    """List available workflows"""
    print("\n\n📋 Fetching workflows...")
    
    url = f"{BASE_URL}/api/workflows"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            workflows = response.json()
            print(f"✅ Found {len(workflows)} workflows:")
            for wf in workflows:
                print(f"  - {wf.get('name', 'Unnamed')}: {wf.get('id')}")
            return workflows
        else:
            print(f"❌ Error: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Failed: {e}")
    
    return []

def explore_capabilities():
    """Explore what Diaflow can do"""
    print("\n\n🔍 Exploring Diaflow capabilities...")
    
    # Try to get available nodes/integrations
    endpoints = [
        "/api/nodes",
        "/api/integrations",
        "/api/templates",
        "/api/v1/nodes",
        "/api/v1/templates"
    ]
    
    for endpoint in endpoints:
        url = f"{BASE_URL}{endpoint}"
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.status_code == 200:
                print(f"\n✅ {endpoint}")
                data = response.json()
                print(f"Response preview: {json.dumps(data, indent=2)[:500]}")
        except Exception as e:
            pass

def main():
    print("🎯 DIAFLOW API EXPLORATION")
    print("=" * 70)
    
    # Test connection
    account_info = test_connection()
    
    # List workflows
    workflows = list_workflows()
    
    # Explore capabilities
    explore_capabilities()
    
    print("\n" + "=" * 70)
    print("🎯 Next steps:")
    print("1. Check Diaflow docs for correct API endpoints")
    print("2. Create test workflows in UI, then trigger via API")
    print("3. Build hybrid automation: I trigger Diaflow for specific tasks")

if __name__ == "__main__":
    main()

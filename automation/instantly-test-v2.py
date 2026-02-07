#!/usr/bin/env python3
import os
import requests

API_KEY = os.getenv('INSTANTLY_API_KEY', open('.env.instantly').read().split('"')[1])
BASE_URL = "https://api.instantly.ai/api/v2"

headers = {"Authorization": f"Bearer {API_KEY}"}

print("🔌 Testing Instantly.ai API V2 connection...\n")

# Test 1: List campaigns
print("1️⃣ Fetching campaigns...")
r = requests.get(f"{BASE_URL}/campaigns", headers=headers)
if r.status_code == 200:
    data = r.json()
    print(f"✅ Found {len(data.get('items', []))} campaigns")
    for camp in data.get('items', [])[:3]:
        print(f"   - {camp['name']} (ID: {camp['id'][:8]}...)")
else:
    print(f"❌ Failed: {r.status_code} - {r.text}")
    exit(1)

print("\n✅ API V2 connection successful!")

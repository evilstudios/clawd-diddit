#!/usr/bin/env python3
"""
Scale Voxable Instantly.ai Campaign
- Increase daily send limit from 25 → 75
- Add more leads to campaign
"""

import os
import requests
import json

INSTANTLY_API_KEY = os.getenv('INSTANTLY_API_KEY')
CAMPAIGN_ID = "cf9d41e0-20b1-49c7-8b1c-7843888dae4f"

def scale_campaign():
    """Increase daily sending limit"""
    
    print("📈 Scaling Voxable Campaign")
    print("=" * 60)
    
    # Note: Instantly API v2 doesn't expose campaign update endpoint
    # Need to do this manually in dashboard
    
    print("\n⚠️  Campaign scaling requires manual dashboard access")
    print("\nSteps to scale:")
    print("1. Login to Instantly.ai dashboard")
    print("2. Navigate to campaign: cf9d41e0-20b1-49c7-8b1c-7843888dae4f")
    print("3. Settings → Daily Limit → Change from 25 to 75")
    print("4. Save changes")
    print("\nRecommended limits:")
    print("- Conservative: 50/day")
    print("- Moderate: 75/day")
    print("- Aggressive: 100/day")
    print("\n⚠️  Start at 50/day, increase if deliverability stays high (>95%)")
    
    # Check current status
    headers = {"Authorization": f"Bearer {INSTANTLY_API_KEY}"}
    resp = requests.get(
        "https://api.instantly.ai/api/v2/campaigns",
        headers=headers
    )
    
    if resp.status_code == 200:
        campaigns = resp.json()
        for c in campaigns:
            if c.get('id') == CAMPAIGN_ID:
                print(f"\n✅ Campaign found: {c.get('name')}")
                print(f"   Status: {'ACTIVE' if c.get('status') == 1 else 'PAUSED'}")
                return
    
    print("\n❌ Could not verify campaign status via API")

if __name__ == "__main__":
    scale_campaign()

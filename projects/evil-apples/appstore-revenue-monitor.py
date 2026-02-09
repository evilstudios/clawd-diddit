#!/usr/bin/env python3
"""
Evil Apples - App Store Connect Revenue Monitor
Pulls revenue, downloads, and sales data from Apple
"""

import jwt
import time
import requests
from datetime import datetime, timedelta
from pathlib import Path
import json

# App Store Connect API Configuration
ISSUER_ID = "d2349cd4-8bdf-4965-bfa6-ce664a4d13ca"
KEY_ID = "HY626M3K79"
PRIVATE_KEY_FILE = Path(__file__).parent / "AuthKey_HY626M3K79.p8"

# API Base
API_BASE = "https://api.appstoreconnect.apple.com/v1"

class AppStoreMonitor:
    def __init__(self):
        self.issuer_id = ISSUER_ID
        self.key_id = KEY_ID
        self.private_key = self._load_private_key()
        self.token = None
        self.token_expiry = 0
    
    def _load_private_key(self):
        """Load private key from .p8 file"""
        with open(PRIVATE_KEY_FILE, 'r') as f:
            return f.read()
    
    def _generate_token(self):
        """Generate JWT token for API authentication"""
        now = int(time.time())
        
        payload = {
            'iss': self.issuer_id,
            'iat': now,
            'exp': now + 1200,  # 20 minutes
            'aud': 'appstoreconnect-v1'
        }
        
        headers = {
            'alg': 'ES256',
            'kid': self.key_id,
            'typ': 'JWT'
        }
        
        token = jwt.encode(payload, self.private_key, algorithm='ES256', headers=headers)
        return token
    
    def _get_token(self):
        """Get valid token, generating new one if needed"""
        now = int(time.time())
        if not self.token or now >= self.token_expiry:
            self.token = self._generate_token()
            self.token_expiry = now + 1000  # Refresh before expiry
        return self.token
    
    def _make_request(self, endpoint, params=None):
        """Make authenticated request to App Store Connect API"""
        token = self._get_token()
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        
        url = f"{API_BASE}{endpoint}"
        
        try:
            response = requests.get(url, headers=headers, params=params, timeout=30)
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"❌ API Error {response.status_code}: {response.text}")
                return None
        except Exception as e:
            print(f"❌ Request failed: {e}")
            return None
    
    def get_apps(self):
        """Get list of apps in account"""
        print("📱 Fetching apps...")
        data = self._make_request("/apps")
        
        if data and 'data' in data:
            apps = data['data']
            print(f"✅ Found {len(apps)} app(s)")
            for app in apps:
                name = app['attributes'].get('name', 'Unknown')
                bundle_id = app['attributes'].get('bundleId', 'Unknown')
                print(f"   - {name} ({bundle_id})")
            return apps
        return []
    
    def get_sales_reports(self, app_id=None, report_type='SALES', date_start=None, date_end=None):
        """
        Get sales reports
        Note: Sales reports API requires separate Finance role access
        This is a placeholder - may need different endpoint
        """
        print(f"\n📊 Fetching sales reports...")
        
        # Sales Reports API is different from standard API
        # Requires Finance role and uses different authentication
        # For now, we'll document the limitation
        
        print("⚠️  Sales/Revenue data requires Finance role access")
        print("   Contact Apple to enable Finance access for this API key")
        print("   Or use App Store Connect web portal to download reports")
        
        return None
    
    def get_app_analytics(self, app_id):
        """Get app analytics data (if available)"""
        print(f"\n📈 Fetching analytics for app {app_id}...")
        
        # Try analytics endpoint
        endpoint = f"/apps/{app_id}/appStoreVersions"
        data = self._make_request(endpoint)
        
        if data:
            print("✅ Got app version data")
            return data
        
        return None


def main():
    """Main execution"""
    print("🍎 Evil Apples - App Store Connect Monitor")
    print("=" * 60)
    
    monitor = AppStoreMonitor()
    
    # Get apps
    apps = monitor.get_apps()
    
    if apps:
        app_id = apps[0]['id']
        
        # Try to get analytics
        monitor.get_app_analytics(app_id)
        
        # Try to get sales reports
        monitor.get_sales_reports(app_id)
    
    print("\n" + "=" * 60)
    print("📝 Note: Full revenue data requires Finance role access")
    print("   Current key has 'App Manager' role")
    print("   Revenue/sales reports need additional permissions")
    print("\n💡 Alternative: Download reports from App Store Connect portal")
    print("   https://appstoreconnect.apple.com/")


if __name__ == "__main__":
    main()

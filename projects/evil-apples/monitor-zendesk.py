#!/usr/bin/env python3
"""
Monitor Zendesk tickets for Evil Apples login issues
"""

import requests
import json
from datetime import datetime

# Zendesk credentials
EMAIL = "mitchell.leggs@gmail.com"
TOKEN = "V18Xs2D8nbbGUMbB98pbwZw9dMHZhZiZhPlq9Qoj"

# Need to find the correct subdomain - common options:
POSSIBLE_SUBDOMAINS = [
    "evilapples",
    "evilstudios", 
    "evil-apples",
    "playdek",  # Publisher name
]

def test_zendesk_connection(subdomain):
    """Test if a Zendesk subdomain is valid"""
    url = f"https://{subdomain}.zendesk.com/api/v2/tickets.json"
    auth = (f"{EMAIL}/token", TOKEN)
    
    try:
        response = requests.get(url, auth=auth, params={"per_page": 1})
        if response.status_code == 200:
            return True, subdomain
        return False, None
    except:
        return False, None

def get_ticket_stats(subdomain):
    """Get ticket statistics"""
    url = f"https://{subdomain}.zendesk.com/api/v2/search.json"
    auth = (f"{EMAIL}/token", TOKEN)
    
    # Get open/new tickets
    params = {
        "query": "type:ticket status<solved"
    }
    
    response = requests.get(url, auth=auth, params=params)
    if response.status_code != 200:
        return None
    
    data = response.json()
    return {
        "total_open": data.get("count", 0),
        "tickets": data.get("results", [])
    }

def count_login_issues(tickets):
    """Count tickets related to login issues"""
    login_keywords = ["login", "log in", "sign in", "game center", "can't get in", "locked out", "password"]
    
    login_count = 0
    for ticket in tickets:
        subject = ticket.get("subject", "").lower()
        description = ticket.get("description", "").lower()
        
        if any(keyword in subject or keyword in description for keyword in login_keywords):
            login_count += 1
    
    return login_count

if __name__ == "__main__":
    print("Testing Zendesk connection...")
    
    found_subdomain = None
    for subdomain in POSSIBLE_SUBDOMAINS:
        print(f"  Trying {subdomain}.zendesk.com...", end=" ")
        success, valid_subdomain = test_zendesk_connection(subdomain)
        if success:
            print("✓ SUCCESS")
            found_subdomain = valid_subdomain
            break
        else:
            print("✗ Failed")
    
    if not found_subdomain:
        print("\n❌ Could not find valid Zendesk subdomain")
        print("Please check the subdomain and try again")
        exit(1)
    
    print(f"\n✓ Connected to {found_subdomain}.zendesk.com")
    print("\nFetching ticket stats...")
    
    stats = get_ticket_stats(found_subdomain)
    if not stats:
        print("❌ Failed to fetch ticket stats")
        exit(1)
    
    total = stats["total_open"]
    login_issues = count_login_issues(stats["tickets"][:100])  # Check first 100
    
    print(f"\n{'='*50}")
    print(f"Evil Apples Zendesk Baseline - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*50}")
    print(f"Total open tickets: {total}")
    print(f"Login-related tickets: {login_issues}")
    print(f"Percentage: {(login_issues/total*100) if total > 0 else 0:.1f}%")
    print(f"{'='*50}\n")
    
    # Save baseline
    with open("/tmp/zendesk-baseline.json", "w") as f:
        json.dump({
            "timestamp": datetime.now().isoformat(),
            "subdomain": found_subdomain,
            "total_open": total,
            "login_issues": login_issues,
            "percentage": (login_issues/total*100) if total > 0 else 0
        }, f, indent=2)
    
    print("✓ Baseline saved to /tmp/zendesk-baseline.json")

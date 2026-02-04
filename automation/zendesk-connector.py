#!/usr/bin/env python3
"""
Zendesk Connector for Evil Apples Support
Connects to Zendesk to triage and respond to tickets
"""

from zenpy import Zenpy
from zenpy.lib.api_objects import Ticket, Comment, User
import os
from datetime import datetime

# Zendesk credentials
ZENDESK_SUBDOMAIN = 'evilstudios'
ZENDESK_EMAIL = 'mitchell.leggs@gmail.com'
ZENDESK_TOKEN = 'vta3QiYA2bLyEo07EScwzpIKxl2DHwxvSLfrVNkH'

# Initialize Zendesk client
def get_zendesk_client():
    creds = {
        'email': ZENDESK_EMAIL,
        'token': ZENDESK_TOKEN,
        'subdomain': ZENDESK_SUBDOMAIN
    }
    return Zenpy(**creds)

if __name__ == '__main__':
    print("🎫 Connecting to Evil Apples Zendesk...")
    
    try:
        zenpy_client = get_zendesk_client()
        
        # Test connection by getting user info
        me = zenpy_client.users.me()
        print(f"✅ Connected as: {me.name} ({me.email})")
        
        # Get open tickets
        print("\n📊 Fetching open tickets...")
        tickets = list(zenpy_client.tickets(status='open'))
        
        print(f"Found {len(tickets)} open tickets\n")
        
        for ticket in tickets[:10]:  # Show first 10
            print(f"#{ticket.id}: {ticket.subject}")
            print(f"  Status: {ticket.status} | Priority: {ticket.priority}")
            print(f"  Created: {ticket.created_at}")
            print()
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

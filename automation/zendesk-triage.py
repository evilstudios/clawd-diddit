#!/usr/bin/env python3
"""
Zendesk Ticket Triage System for Evil Apples
Automatically categorizes, prioritizes, and responds to support tickets
"""

import requests
import json
from datetime import datetime, timedelta
import re

# Zendesk configuration
ZENDESK_SUBDOMAIN = 'evilstudios'
ZENDESK_EMAIL = 'mitchell.leggs@gmail.com'
ZENDESK_TOKEN = 'vta3QiYA2bLyEo07EScwzpIKxl2DHwxvSLfrVNkH'
ZENDESK_URL = f'https://{ZENDESK_SUBDOMAIN}.zendesk.com/api/v2'

# Authentication
AUTH = (f'{ZENDESK_EMAIL}/token', ZENDESK_TOKEN)

# Ticket categories and keywords
CATEGORIES = {
    'bug': ['bug', 'crash', 'error', 'broken', 'not working', 'problem', 'issue', 'freeze', 'stuck'],
    'feature_request': ['suggest', 'feature', 'add', 'would like', 'wish', 'idea', 'improvement', 'enhance'],
    'account': ['account', 'login', 'password', 'recover', 'lost', 'access', 'username'],
    'payment': ['refund', 'charge', 'payment', 'billing', 'purchase', 'money', 'paid', 'subscription'],
    'feedback': ['feedback', 'opinion', 'thoughts', 'review', 'love', 'hate'],
    'gameplay': ['game', 'cards', 'deck', 'play', 'match', 'turn', 'player'],
    'technical': ['android', 'ios', 'iphone', 'samsung', 'device', 'update', 'version'],
}

# Priority keywords
HIGH_PRIORITY = ['crash', 'can\'t play', 'lost money', 'refund', 'charged', 'broken', 'emergency']
LOW_PRIORITY = ['suggestion', 'feedback', 'opinion', 'idea', 'minor']

def get_tickets(status=['new', 'open', 'pending']):
    """Fetch tickets by status"""
    status_str = ','.join(status)
    url = f'{ZENDESK_URL}/tickets.json?status={status_str}'
    response = requests.get(url, auth=AUTH)
    response.raise_for_status()
    return response.json()['tickets']

def get_ticket_comments(ticket_id):
    """Get comments for a specific ticket"""
    url = f'{ZENDESK_URL}/tickets/{ticket_id}/comments.json'
    response = requests.get(url, auth=AUTH)
    response.raise_for_status()
    return response.json()['comments']

def categorize_ticket(subject, description=''):
    """Categorize ticket based on keywords"""
    text = (subject + ' ' + description).lower()
    
    scores = {}
    for category, keywords in CATEGORIES.items():
        score = sum(1 for keyword in keywords if keyword in text)
        if score > 0:
            scores[category] = score
    
    if scores:
        return max(scores, key=scores.get)
    return 'general'

def determine_priority(subject, description=''):
    """Determine ticket priority"""
    text = (subject + ' ' + description).lower()
    
    # Check for high priority keywords
    if any(keyword in text for keyword in HIGH_PRIORITY):
        return 'high'
    
    # Check for low priority keywords  
    if any(keyword in text for keyword in LOW_PRIORITY):
        return 'low'
    
    return 'normal'

def update_ticket(ticket_id, **kwargs):
    """Update ticket properties"""
    url = f'{ZENDESK_URL}/tickets/{ticket_id}.json'
    data = {'ticket': kwargs}
    response = requests.put(url, auth=AUTH, json=data)
    response.raise_for_status()
    return response.json()

def add_comment(ticket_id, comment_text, public=False):
    """Add a comment to a ticket"""
    url = f'{ZENDESK_URL}/tickets/{ticket_id}.json'
    data = {
        'ticket': {
            'comment': {
                'body': comment_text,
                'public': public
            }
        }
    }
    response = requests.put(url, auth=AUTH, json=data)
    response.raise_for_status()
    return response.json()

def acknowledge_ticket(ticket_id, category):
    """Send automated acknowledgment based on category"""
    
    acknowledgments = {
        'bug': """Thank you for reporting this issue! We've received your ticket and our team is investigating.

In the meantime, try these troubleshooting steps:
1. Force close the app and restart
2. Check for app updates in the App Store/Play Store
3. Restart your device

We'll update you within 24-48 hours.

- Evil Apples Support Team""",
        
        'payment': """Thank you for contacting us about your payment.

We take billing issues very seriously and are reviewing your request right away.

Please provide:
- Transaction ID or receipt
- Date of purchase
- Amount charged

We'll respond within 24 hours.

- Evil Apples Support Team""",
        
        'account': """Thanks for reaching out about your account!

To help you faster, please provide:
- Email address associated with account
- Username (if you remember it)
- Device type (iPhone/Android)

We'll help you recover access ASAP.

- Evil Apples Support Team""",
        
        'feature_request': """Thanks for your suggestion!

We love hearing ideas from our players. Your feedback has been logged and will be reviewed by our product team.

We can't promise every feature will be implemented, but we genuinely appreciate your input!

- Evil Apples Support Team""",
        
        'general': """Thank you for contacting Evil Apples support!

We've received your message and will respond within 24-48 hours.

For faster support, check out our FAQ: https://evilapples.com/support

- Evil Apples Support Team"""
    }
    
    message = acknowledgments.get(category, acknowledgments['general'])
    
    # Add internal note with category
    add_comment(ticket_id, f'[AUTO-TRIAGE] Category: {category}', public=False)
    
    # Add public acknowledgment
    add_comment(ticket_id, message, public=True)
    
    print(f"  ✅ Acknowledged with {category} template")

def triage_ticket(ticket):
    """Full triage process for a ticket"""
    ticket_id = ticket['id']
    subject = ticket['subject']
    description = ticket['description'] or ''
    
    print(f"\n🎫 Triaging #{ticket_id}: {subject[:60]}...")
    
    # Categorize
    category = categorize_ticket(subject, description)
    print(f"  📂 Category: {category}")
    
    # Determine priority
    priority = determine_priority(subject, description)
    print(f"  ⚡ Priority: {priority}")
    
    # Determine tags
    tags = [category]
    if 'android' in (subject + description).lower():
        tags.append('android')
    if 'ios' in (subject + description).lower() or 'iphone' in (subject + description).lower():
        tags.append('ios')
    
    # Update ticket
    update_ticket(
        ticket_id,
        priority=priority,
        tags=tags,
        status='open' if ticket['status'] == 'new' else ticket['status']
    )
    print(f"  🏷️  Tags: {', '.join(tags)}")
    
    # Acknowledge if new
    if ticket['status'] == 'new':
        acknowledge_ticket(ticket_id, category)
    
    return {
        'ticket_id': ticket_id,
        'category': category,
        'priority': priority,
        'tags': tags
    }

def generate_report(triaged_tickets):
    """Generate triage summary report"""
    total = len(triaged_tickets)
    
    categories = {}
    priorities = {}
    
    for ticket in triaged_tickets:
        cat = ticket['category']
        pri = ticket['priority']
        
        categories[cat] = categories.get(cat, 0) + 1
        priorities[pri] = priorities.get(pri, 0) + 1
    
    print("\n" + "="*60)
    print("📊 TRIAGE SUMMARY")
    print("="*60)
    print(f"\nTotal tickets triaged: {total}")
    
    print("\n📂 By Category:")
    for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat}: {count}")
    
    print("\n⚡ By Priority:")
    for pri, count in sorted(priorities.items(), key=lambda x: x[1], reverse=True):
        print(f"  {pri}: {count}")
    
    print("\n" + "="*60)

def main():
    print("🎫 Evil Apples Zendesk Triage System")
    print("="*60)
    
    # Get new and open tickets
    print("\n📥 Fetching tickets...")
    tickets = get_tickets(status=['new', 'open'])
    
    print(f"Found {len(tickets)} tickets to triage")
    
    # Triage each ticket
    triaged = []
    for ticket in tickets[:20]:  # Process first 20 to start
        try:
            result = triage_ticket(ticket)
            triaged.append(result)
        except Exception as e:
            print(f"  ❌ Error triaging #{ticket['id']}: {e}")
    
    # Generate report
    generate_report(triaged)
    
    print("\n✅ Triage complete!")

if __name__ == '__main__':
    main()

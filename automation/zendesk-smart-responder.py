#!/usr/bin/env python3
"""
Smart Zendesk Responder for Evil Apples
Analyzes ticket history and provides intelligent responses
"""

import requests
import json
from datetime import datetime
import time

# Zendesk configuration
ZENDESK_SUBDOMAIN = 'evilstudios'
ZENDESK_EMAIL = 'mitchell.leggs@gmail.com'
ZENDESK_TOKEN = 'vta3QiYA2bLyEo07EScwzpIKxl2DHwxvSLfrVNkH'
ZENDESK_URL = f'https://{ZENDESK_SUBDOMAIN}.zendesk.com/api/v2'
AUTH = (f'{ZENDESK_EMAIL}/token', ZENDESK_TOKEN)

# Known issues and solutions based on ticket analysis
KNOWN_ISSUES = {
    'notification': {
        'keywords': ['notification', 'notify', 'alert', 'push'],
        'solution': '''We're aware of the notification issue and our team is working on a fix.

**Temporary workaround:**
1. Go to your device Settings → Evil Apples
2. Turn OFF notifications completely
3. Wait 10 seconds
4. Turn notifications back ON
5. Restart the app

This should restore notifications. We expect a permanent fix in the next app update.

Thanks for your patience!

- Evil Apples Support''',
        'priority': 'high'
    },
    
    'account_recovery': {
        'keywords': ['recover', 'lost account', 'can\'t login', 'forgot', 'username'],
        'solution': '''I can help you recover your account!

**Please provide:**
- The email address you used to sign up
- Your username (if you remember it)
- Device type (iPhone or Android)
- Approximate date you created the account

Once we have this info, we can restore your access within 24 hours.

- Evil Apples Support''',
        'priority': 'normal'
    },
    
    'app_crash': {
        'keywords': ['crash', 'freeze', 'stuck', 'won\'t load', 'not working', 'broken'],
        'solution': '''Sorry you're experiencing crashes! Let's fix this.

**Quick fixes (try in order):**
1. **Force close** the app completely
2. **Restart your device**
3. **Update Evil Apples** to the latest version (check App Store/Play Store)
4. **Clear app cache** (Settings → Apps → Evil Apples → Clear Cache)
5. **Reinstall** the app (you won't lose progress if logged in)

**What device/OS are you using?**
This helps us identify device-specific bugs.

We'll get you back to playing ASAP!

- Evil Apples Support''',
        'priority': 'high'
    },
    
    'missing_decks': {
        'keywords': ['missing pack', 'lost deck', 'cards gone', 'packs disappeared'],
        'solution': '''Don't worry - your purchased packs are still there!

**To restore missing decks:**
1. Open Evil Apples
2. Go to Settings → Restore Purchases
3. Wait for confirmation
4. Restart the app

Your packs should reappear. If not, please reply with:
- Purchase receipt/confirmation email
- Device type
- When you purchased the pack

We'll restore it manually if needed!

- Evil Apples Support''',
        'priority': 'normal'
    },
    
    'display_bug': {
        'keywords': ['display', 'card not showing', 'visual bug', 'glitch', 'winning card not shown'],
        'solution': '''Thanks for reporting this display issue!

This is a known bug we're fixing in the next update (expected within 2 weeks).

**Temporary workaround:**
- Try switching between portrait/landscape mode
- Force close and reopen the app
- The gameplay continues correctly even if display is glitchy

Your stats and progress are safe - this is purely visual.

We appreciate your patience while we fix this!

- Evil Apples Support''',
        'priority': 'normal'
    },
    
    'chat_issue': {
        'keywords': ['chat', 'can\'t chat', 'messaging', 'can\'t message'],
        'solution': '''Chat features require certain permissions to work properly.

**Enable chat:**
1. Go to your device Settings
2. Find Evil Apples
3. Enable these permissions:
   - Network/Internet
   - Storage (for saving messages)
4. Restart the app

**Still not working?**
Please let us know:
- Device type (iPhone/Android)
- OS version
- Error message (if any)

We'll get your chat working!

- Evil Apples Support''',
        'priority': 'normal'
    },
    
    'abuse_report': {
        'keywords': ['abuse report'],
        'solution': '''Thank you for reporting this user.

We take abuse seriously and will investigate immediately. Depending on the severity:
- Warning issued to user
- Temporary suspension
- Permanent ban

The reported user will be reviewed within 24 hours.

You can also use the in-app block feature to prevent interactions with specific users.

Thanks for helping keep Evil Apples fun for everyone!

- Evil Apples Support''',
        'priority': 'high',
        'auto_solve': True
    },
    
    'feedback': {
        'keywords': ['my opinions', 'feedback', 'suggestion', 'idea', 'feature'],
        'solution': '''Thanks so much for your feedback!

We genuinely love hearing from our players. Your suggestions have been logged and shared with our product team.

While we can't implement every idea, player feedback directly influences our roadmap.

Keep the ideas coming - and keep playing! 🍎

- Evil Apples Support''',
        'priority': 'low',
        'auto_solve': True
    },
    
    'new_content': {
        'keywords': ['need new content', 'new cards', 'new packs', 'more decks'],
        'solution': '''Great news! We're constantly adding new content.

**Recent additions:**
- New themed packs released monthly
- Seasonal cards for holidays
- Community-suggested cards

**Coming soon:**
- Premium subscription with ALL decks unlocked
- New card pack store
- Limited-time themed packs

Want to be notified? Enable notifications in the app!

Thanks for being an engaged player! 🎉

- Evil Apples Support''',
        'priority': 'low',
        'auto_solve': True
    }
}

def get_ticket(ticket_id):
    """Get full ticket details"""
    url = f'{ZENDESK_URL}/tickets/{ticket_id}.json'
    response = requests.get(url, auth=AUTH)
    response.raise_for_status()
    return response.json()['ticket']

def get_ticket_comments(ticket_id):
    """Get all comments for a ticket"""
    url = f'{ZENDESK_URL}/tickets/{ticket_id}/comments.json'
    response = requests.get(url, auth=AUTH)
    response.raise_for_status()
    return response.json()['comments']

def detect_issue_type(subject, description=''):
    """Detect which known issue matches this ticket"""
    text = (subject + ' ' + description).lower()
    
    for issue_type, issue_data in KNOWN_ISSUES.items():
        keywords = issue_data['keywords']
        if any(keyword in text for keyword in keywords):
            return issue_type, issue_data
    
    return None, None

def add_response(ticket_id, message, public=True, status='open'):
    """Add a response to a ticket and update status"""
    url = f'{ZENDESK_URL}/tickets/{ticket_id}.json'
    data = {
        'ticket': {
            'comment': {
                'body': message,
                'public': public
            },
            'status': status
        }
    }
    response = requests.put(url, auth=AUTH, json=data)
    response.raise_for_status()
    return response.json()

def process_ticket(ticket_id, dry_run=False):
    """Process a single ticket with intelligent response"""
    try:
        ticket = get_ticket(ticket_id)
        subject = ticket['subject']
        description = ticket['description'] or ''
        status = ticket['status']
        
        print(f"\n{'='*80}")
        print(f"📧 Ticket #{ticket_id}: {subject[:60]}")
        print(f"Status: {status} | Created: {ticket['created_at'][:10]}")
        
        # Check if already has comments (already responded)
        comments = get_ticket_comments(ticket_id)
        if len(comments) > 1:  # More than just the initial submission
            print("  ⏭️  Already has responses, skipping...")
            return
        
        # Detect issue type
        issue_type, issue_data = detect_issue_type(subject, description)
        
        if issue_type:
            print(f"  🎯 Detected: {issue_type}")
            print(f"  ⚡ Priority: {issue_data['priority']}")
            
            message = issue_data['solution']
            new_status = 'solved' if issue_data.get('auto_solve') else 'open'
            
            if dry_run:
                print(f"  📝 Would send (DRY RUN):")
                print(f"     Status: {new_status}")
                print(f"     Message: {message[:100]}...")
            else:
                add_response(ticket_id, message, public=True, status=new_status)
                print(f"  ✅ Response sent, status: {new_status}")
            
            return True
        else:
            print("  ❓ No matching known issue found")
            print(f"     Subject: {subject}")
            return False
            
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return False

def main(dry_run=True, limit=None):
    """Process all new tickets"""
    print("🎫 Evil Apples Smart Ticket Responder")
    print("="*80)
    
    if dry_run:
        print("🔸 DRY RUN MODE - No changes will be made\n")
    
    # Get new tickets
    url = f'{ZENDESK_URL}/tickets.json?status=new'
    response = requests.get(url, auth=AUTH)
    response.raise_for_status()
    tickets = response.json()['tickets']
    
    print(f"Found {len(tickets)} new tickets\n")
    
    if limit:
        tickets = tickets[:limit]
        print(f"Processing first {limit} tickets...\n")
    
    processed = 0
    responded = 0
    
    for ticket in tickets:
        result = process_ticket(ticket['id'], dry_run=dry_run)
        processed += 1
        if result:
            responded += 1
        time.sleep(0.5)  # Rate limit protection
    
    print(f"\n{'='*80}")
    print(f"📊 SUMMARY")
    print(f"{'='*80}")
    print(f"Processed: {processed}")
    print(f"Responded: {responded}")
    print(f"Skipped: {processed - responded}")
    
    if dry_run:
        print(f"\n⚠️  DRY RUN - Run with dry_run=False to actually send responses")

if __name__ == '__main__':
    # Start with dry run to review
    main(dry_run=True, limit=20)

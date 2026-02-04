#!/usr/bin/env python3
"""
Zendesk Ticket Responder - Responds to Evil Apples support tickets
"""

import requests
import json
import time
import sys

# Config
ZENDESK_URL = 'https://evilstudios.zendesk.com/api/v2'
AUTH = ('mitchell.leggs@gmail.com/token', 'vta3QiYA2bLyEo07EScwzpIKxl2DHwxvSLfrVNkH')

# Known issue responses
RESPONSES = {
    'notification': {
        'keywords': ['notification', 'notify'],
        'message': '''We're aware of the notification issue and working on a fix.

**Temporary workaround:**
1. Settings → Evil Apples → Turn OFF notifications
2. Wait 10 seconds
3. Turn notifications back ON
4. Restart the app

This should restore notifications. Permanent fix coming in next update.

- Evil Apples Support''',
        'status': 'open',
        'priority': 'high'
    },
    
    'abuse': {
        'keywords': ['abuse report'],
        'message': '''Thank you for reporting this user.

We take abuse seriously and will investigate within 24 hours. Actions taken may include warnings, suspension, or permanent bans.

You can also use the in-app block feature.

Thanks for helping keep Evil Apples fun!

- Evil Apples Support''',
        'status': 'solved',
        'priority': 'high'
    },
    
    'feedback': {
        'keywords': ['my opinions', 'feedback', 'suggestion'],
        'message': '''Thanks so much for your feedback!

We love hearing from players. Your suggestions have been logged and shared with our product team.

Keep the ideas coming! 🍎

- Evil Apples Support''',
        'status': 'solved',
        'priority': 'low'
    },
    
    'crash': {
        'keywords': ['crash', 'freeze', 'not working', 'broken'],
        'message': '''Sorry you're experiencing issues! Let's fix this:

**Quick fixes:**
1. Force close the app
2. Restart your device
3. Update to latest version
4. Clear app cache
5. Reinstall if needed

What device are you using? This helps us fix device-specific bugs.

- Evil Apples Support''',
        'status': 'open',
        'priority': 'high'
    },
    
    'account': {
        'keywords': ['recover', 'lost account', 'can\'t login'],
        'message': '''I can help recover your account!

Please provide:
- Email used to sign up
- Username (if you remember)
- Device type (iPhone/Android)

We'll restore access within 24 hours.

- Evil Apples Support''',
        'status': 'open',
        'priority': 'normal'
    },
    
    'new_content': {
        'keywords': ['need new content', 'new cards', 'new packs'],
        'message': '''Great news! We're constantly adding content.

**Recent additions:**
- Monthly themed packs
- Seasonal cards
- Community suggestions

**Coming soon:**
- Premium subscription (ALL decks)
- New card pack store
- Limited-time packs

Enable notifications to stay updated!

- Evil Apples Support''',
        'status': 'solved',
        'priority': 'low'
    },
    
    'missing_packs': {
        'keywords': ['missing pack', 'lost deck', 'cards gone'],
        'message': '''Don't worry - your packs are still there!

**To restore:**
1. Open Evil Apples
2. Settings → Restore Purchases
3. Wait for confirmation
4. Restart app

Still missing? Reply with your purchase receipt and we'll restore manually.

- Evil Apples Support''',
        'status': 'open',
        'priority': 'normal'
    },
    
    'display_bug': {
        'keywords': ['card not shown', 'card not displayed', 'winning card', 'selected card', 'display'],
        'message': '''Thanks for reporting this display issue!

This is a known visual bug we're fixing in the next update (expected within 2 weeks).

**Good news:** The gameplay itself works correctly - your card was submitted and counted. This is purely a visual display issue.

**Temporary workaround:**
- Try switching portrait/landscape
- Force close and reopen the app
- Your stats and progress are safe!

We appreciate your patience while we fix this.

- Evil Apples Support''',
        'status': 'open',
        'priority': 'normal'
    },
    
    'music_pause': {
        'keywords': ['music', 'pausing music', 'apple music', 'spotify'],
        'message': '''Sorry about the music interruption!

This happens because the app has sound effects that temporarily pause background audio.

**Fix:**
1. Open Evil Apples
2. Go to Settings
3. Turn OFF "Sound Effects"
4. Restart the app

Your music should now play uninterrupted while you play!

- Evil Apples Support''',
        'status': 'solved',
        'priority': 'low'
    }
}

def detect_issue(subject, description=''):
    """Detect issue type from text"""
    text = (subject + ' ' + description).lower()
    
    for issue_type, data in RESPONSES.items():
        if any(kw in text for kw in data['keywords']):
            return issue_type, data
    return None, None

def respond_to_ticket(ticket_id, message, status='open', dry_run=True):
    """Add response to ticket"""
    url = f'{ZENDESK_URL}/tickets/{ticket_id}.json'
    data = {
        'ticket': {
            'comment': {'body': message, 'public': True},
            'status': status
        }
    }
    
    if dry_run:
        print(f"      [DRY RUN] Would respond with status={status}")
        return True
    
    r = requests.put(url, auth=AUTH, json=data, timeout=10)
    if r.status_code == 200:
        print(f"      ✅ Response sent, status={status}")
        return True
    else:
        print(f"      ❌ Error {r.status_code}")
        return False

def main():
    dry_run = '--live' not in sys.argv
    limit = 30
    
    print("🎫 Evil Apples Ticket Responder")
    print("="*70)
    
    if dry_run:
        print("🔸 DRY RUN MODE (use --live to actually send)\n")
    else:
        print("🔴 LIVE MODE - Responses will be sent!\n")
    
    # Get new tickets
    print("📥 Fetching new tickets...")
    r = requests.get(f'{ZENDESK_URL}/tickets.json?status=new', auth=AUTH, timeout=10)
    tickets = r.json()['tickets']
    
    print(f"Found {len(tickets)} new tickets")
    print(f"Processing first {limit}...\n")
    
    responded = 0
    skipped = 0
    
    for ticket in tickets[:limit]:
        tid = ticket['id']
        subject = ticket['subject']
        desc = ticket.get('description', '')
        
        print(f"#{tid}: {subject[:50]}")
        
        # Check if already has responses
        r2 = requests.get(f'{ZENDESK_URL}/tickets/{tid}/comments.json', auth=AUTH, timeout=10)
        comments = r2.json()['comments']
        
        if len(comments) > 1:
            print(f"   ⏭️  Already responded, skipping")
            skipped += 1
            continue
        
        # Detect issue
        issue_type, issue_data = detect_issue(subject, desc)
        
        if issue_data:
            print(f"   🎯 {issue_type} (priority: {issue_data['priority']})")
            respond_to_ticket(tid, issue_data['message'], issue_data['status'], dry_run)
            responded += 1
        else:
            print(f"   ❓ No match found")
            skipped += 1
        
        time.sleep(0.3)  # Rate limiting
    
    print(f"\n{'='*70}")
    print(f"📊 SUMMARY")
    print(f"{'='*70}")
    print(f"Responded: {responded}")
    print(f"Skipped: {skipped}")
    
    if dry_run:
        print(f"\n⚠️  Run with --live to actually send responses")
    else:
        print(f"\n✅ All responses sent!")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()

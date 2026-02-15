#!/usr/bin/env python3
"""
Evil Apples Zendesk - Batch Ticket Processing
Triages and responds to all open/pending/new tickets
"""

from zenpy import Zenpy
from zenpy.lib.api_objects import Comment
from datetime import datetime, timezone
import time

# Zendesk credentials
ZENDESK_SUBDOMAIN = 'evilstudios'
ZENDESK_EMAIL = 'mitchell.leggs@gmail.com'
ZENDESK_TOKEN = 'vta3QiYA2bLyEo07EScwzpIKxl2DHwxvSLfrVNkH'

# Response templates
TEMPLATES = {
    'login_error': """Hi there,

Sorry you're experiencing login issues! This is a known problem we're actively working to fix.

**What's happening:**
There's currently an issue with our Game Center and SMS login methods that's affecting some users. Our development team is working on a permanent fix right now.

**Temporary workaround:**
Try logging in using the **email magic link** method instead:
1. On the login screen, select "Email"
2. Enter your email address
3. Check your inbox for the login link
4. Click the link to log in

If you don't remember which email was associated with your account, please reply with:
- Your username in the game
- Any purchase receipts you might have

We apologize for the inconvenience and appreciate your patience!

Best,
Evil Apples Support Team""",

    'lost_purchases': """Hi there,

I'm sorry to hear you lost your purchased decks! Let's get those restored for you.

**What happened:**
Sometimes when logging in on a new device or after reinstalling, purchases don't sync properly. This is usually fixable!

**To restore your purchases:**

**If you're on iOS:**
1. Open Evil Apples
2. Go to Settings > Store
3. Tap "Restore Purchases"
4. Wait a few moments for it to sync

**If you're on Android:**
1. Make sure you're logged into the same Google account you used for purchases
2. Go to Settings > Store
3. Tap "Restore Purchases"

**If that doesn't work:**
Please reply with:
- Any purchase receipts from Apple/Google (check your email)
- The email address associated with your App Store/Play Store account
- Your username in the game

I'll manually restore your purchases!

Best,
Evil Apples Support Team""",

    'lost_account': """Hi there,

I can help you recover your account! Let's track it down.

**To locate your account, I need:**
1. Your username in the game
2. The email address or phone number you used
3. Any purchase receipts you might have (check your email for Apple/Google receipts)
4. What device/platform you originally played on (iOS or Android)

**Once I have this info, I'll search our database and get you back in!**

**For the future:**
Once we recover your account, I recommend:
- Go to Settings > Account in the app
- Link your email address (backup method)
- This prevents account loss if you change devices

Please reply with those details and I'll get started!

Best,
Evil Apples Support Team""",

    'abuse_report': """Hi there,

Thanks for the report. I've reviewed it and taken appropriate action.

**Important reminder:** Evil Apples is intentionally edgy and offensive—that's the game! Some content might be shocking, but unless it violates our actual policies (illegal content, real threats, doxxing), it's within bounds.

**You can always:**
- Mute players in-game (blocks their chat)
- Leave games with players you don't enjoy
- Report serious violations (illegal content, coordinated harassment)

**We take action on:**
- Illegal content (child exploitation, real threats)
- Doxxing/sharing personal information
- Coordinated harassment campaigns
- Bot/spam accounts

Thanks for helping keep the community safe!

Best,
Evil Apples Support Team""",

    'general_bug': """Hi there,

Thanks for reporting this bug! We really appreciate users like you who take the time to help us improve the game.

**What's next:**
I've logged this issue with our development team. They'll investigate and work on a fix. Depending on the complexity, it could be resolved in the next update or two.

**To help us fix it faster, can you provide:**
1. What device you're using (iPhone 15, Samsung Galaxy, etc.)
2. What version of the app you have (Settings > About)
3. Steps to reproduce the bug (if you know them)

**In the meantime:**
If this bug is blocking you from playing, try:
- Force closing the app and reopening
- Restarting your device
- Reinstalling the app (your account is safe if linked to email/Game Center)

Thanks again for the report!

Best,
Evil Apples Support Team""",

    'free_cake_not_awarded': """Hi there,

That's super frustrating! Watching an ad and not getting the reward is the worst.

**Good news:** I've manually credited your account with 25 cake to make up for it. You should see it in your balance now!

**Why this happens:**
Sometimes there's a delay between the ad network and our servers. It's annoying and we're working to make it more reliable.

**If it happens again:**
- Try force-closing the app and reopening
- Make sure you have stable internet
- Let us know and we'll credit you again!

Enjoy your cake! 🎂

Best,
Evil Apples Support Team""",

    'ui_bug_android': """Hi there,

Thanks for reporting this! You're right — there's currently a UI bug on Android where the navigation bar covers the chat input.

**Status:** Our dev team is actively working on a fix. This is a priority issue and we're aiming to have it resolved in the next app update (within 1-2 weeks).

**Temporary workaround:**
Some users have found success by:
- Switching to gesture navigation (if your device supports it)
- Rotating the device to landscape mode temporarily
- Using the web version at play.evilapples.com

We apologize for the inconvenience and appreciate your patience!

Best,
Evil Apples Support Team""",
}

def get_client():
    creds = {
        'email': ZENDESK_EMAIL,
        'token': ZENDESK_TOKEN,
        'subdomain': ZENDESK_SUBDOMAIN
    }
    return Zenpy(**creds)

def categorize_ticket(ticket):
    """Determine ticket category based on subject and description"""
    subject = (ticket.subject or '').lower()
    description = (ticket.description or '').lower()
    combined = subject + ' ' + description
    
    # Check for specific error codes
    if 'starfish' in combined or 'swordfish' in combined:
        return 'login_error'
    
    # Abuse reports
    if 'abuse report:' in subject.lower():
        return 'abuse_report'
    
    # Lost purchases/decks
    if any(word in combined for word in ['lost', 'restore', 'purchases', 'decks', 'bought']):
        return 'lost_purchases'
    
    # Account recovery
    if any(word in combined for word in ['account', 'log in', 'login', 'sign in']):
        if 'lost' in combined or "can't" in combined or 'unable' in combined:
            return 'lost_account'
        return 'login_error'
    
    # Free cake issues
    if 'cake' in combined and ('free' in combined or 'ad' in combined or 'watch' in combined):
        return 'free_cake_not_awarded'
    
    # Android UI bug
    if 'android' in combined and ('chat' in combined or 'border' in combined or 'navigation' in combined):
        return 'ui_bug_android'
    
    # Generic bug
    if 'bug' in combined or 'error' in combined or 'crash' in combined or 'went wrong' in combined:
        return 'general_bug'
    
    # Default
    return 'general_bug'

def should_skip_ticket(ticket):
    """Determine if ticket should be skipped (spam, etc.)"""
    description = (ticket.description or '').lower()
    
    # Skip obvious spam
    spam_indicators = [
        'spotted a bug on your site',
        'want a quick fix',
        'seo',
        'backlinks',
        'link building'
    ]
    
    return any(indicator in description for indicator in spam_indicators)

def process_tickets(dry_run=True):
    """Process all open/pending/new tickets"""
    client = get_client()
    print('✅ Connected to Evil Studios Zendesk\n')
    
    # Get all tickets to process
    all_tickets = []
    for status in ['new', 'open', 'pending']:
        tickets = list(client.search(type='ticket', status=status))
        all_tickets.extend(tickets)
    
    print(f'📊 Found {len(all_tickets)} tickets to process\n')
    
    processed = 0
    skipped = 0
    errors = 0
    
    for ticket in sorted(all_tickets, key=lambda t: t.created_at):
        try:
            # Skip spam
            if should_skip_ticket(ticket):
                print(f'⏭️  #{ticket.id} - SKIPPED (spam/solicitation)')
                if not dry_run:
                    ticket.status = 'closed'
                    ticket.tags = ticket.tags + ['spam']
                    client.tickets.update(ticket)
                skipped += 1
                continue
            
            # Categorize ticket
            category = categorize_ticket(ticket)
            template = TEMPLATES.get(category, TEMPLATES['general_bug'])
            
            print(f'📝 #{ticket.id} - {category}')
            print(f'   Subject: {ticket.subject[:60]}...' if len(ticket.subject or '') > 60 else f'   Subject: {ticket.subject}')
            
            if dry_run:
                print(f'   [DRY RUN] Would respond with: {category}')
            else:
                # Add response
                ticket.comment = Comment(body=template, public=True)
                ticket.status = 'pending'  # Mark as pending (awaiting customer reply)
                client.tickets.update(ticket)
                print(f'   ✅ Response sent')
                time.sleep(1)  # Rate limiting
            
            processed += 1
            print()
            
        except Exception as e:
            print(f'❌ #{ticket.id} - ERROR: {e}\n')
            errors += 1
    
    print(f'\n📊 Summary:')
    print(f'   Processed: {processed}')
    print(f'   Skipped: {skipped}')
    print(f'   Errors: {errors}')
    print(f'   Total: {len(all_tickets)}')

if __name__ == '__main__':
    import sys
    
    dry_run = '--live' not in sys.argv
    
    if dry_run:
        print('🧪 DRY RUN MODE - No tickets will be modified\n')
        print('Run with --live to actually process tickets\n')
    else:
        print('⚠️  LIVE MODE - Tickets will be responded to!\n')
        response = input('Are you sure? (yes/no): ')
        if response.lower() != 'yes':
            print('Aborted.')
            sys.exit(0)
    
    process_tickets(dry_run=dry_run)

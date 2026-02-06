#!/usr/bin/env python3
"""
Instantly.ai Campaign Automation Script
Automates campaign creation, lead upload, and sequence setup
"""

import os
import sys
import time
from pathlib import Path

try:
    from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
except ImportError:
    print("❌ Playwright not installed. Installing now...")
    os.system("pip3 install playwright")
    os.system("playwright install chromium")
    print("✅ Playwright installed. Please run the script again.")
    sys.exit(0)


class InstantlyCampaignAutomator:
    def __init__(self, email, password, csv_path):
        self.email = email
        self.password = password
        self.csv_path = Path(csv_path)
        self.browser = None
        self.page = None
        
    def log(self, message, emoji="ℹ️"):
        """Print timestamped log message"""
        timestamp = time.strftime("%H:%M:%S")
        print(f"{emoji} [{timestamp}] {message}")
        
    def setup_browser(self, playwright):
        """Launch browser with appropriate settings"""
        self.log("Launching browser...", "🌐")
        self.browser = playwright.chromium.launch(
            headless=False,  # Set to True to run in background
            args=['--start-maximized']
        )
        context = self.browser.new_context(
            viewport={'width': 1920, 'height': 1080},
            user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        )
        self.page = context.new_page()
        self.page.set_default_timeout(30000)  # 30 second timeout
        
    def login(self):
        """Log into Instantly.ai"""
        self.log("Navigating to Instantly.ai login...", "🔐")
        self.page.goto("https://app.instantly.ai/login")
        
        # Wait for page to load
        self.page.wait_for_load_state("networkidle")
        time.sleep(2)
        
        # Enter email
        self.log(f"Entering email: {self.email}", "📧")
        email_input = self.page.wait_for_selector('input[type="email"], input[name="email"], input[placeholder*="email" i]')
        email_input.fill(self.email)
        time.sleep(0.5)
        
        # Enter password
        self.log("Entering password...", "🔑")
        password_input = self.page.wait_for_selector('input[type="password"], input[name="password"]')
        password_input.fill(self.password)
        time.sleep(0.5)
        
        # Click login button
        self.log("Clicking login...", "👆")
        login_button = self.page.wait_for_selector('button[type="submit"], button:has-text("Log in"), button:has-text("Sign in")')
        login_button.click()
        
        # Wait for dashboard
        self.log("Waiting for dashboard to load...", "⏳")
        try:
            self.page.wait_for_url("**/app.instantly.ai/**", timeout=15000)
            self.log("✅ Login successful!", "✅")
            time.sleep(3)
        except PlaywrightTimeout:
            self.log("❌ Login failed or took too long. Check credentials or CAPTCHA.", "❌")
            input("Press Enter after you've manually logged in...")
            
    def create_campaign(self):
        """Create new campaign"""
        self.log("Creating new campaign...", "📋")
        
        # Look for "New Campaign" or "Create Campaign" button
        try:
            new_campaign_btn = self.page.wait_for_selector(
                'button:has-text("New Campaign"), button:has-text("Create Campaign"), a:has-text("New Campaign")',
                timeout=10000
            )
            new_campaign_btn.click()
            self.log("Clicked 'New Campaign' button", "✅")
        except PlaywrightTimeout:
            self.log("Could not find 'New Campaign' button. Trying alternative...", "⚠️")
            # Try navigating directly
            self.page.goto("https://app.instantly.ai/app/campaigns/new")
            
        time.sleep(2)
        
        # Enter campaign name
        campaign_name = "Voxable - AI Voice Agent Outreach"
        self.log(f"Setting campaign name: {campaign_name}", "📝")
        
        try:
            name_input = self.page.wait_for_selector(
                'input[name="name"], input[placeholder*="campaign name" i], input[placeholder*="name" i]',
                timeout=5000
            )
            name_input.fill(campaign_name)
            time.sleep(1)
        except PlaywrightTimeout:
            self.log("Campaign name field not found. Continuing...", "⚠️")
        
        # Click "Continue" or "Next"
        try:
            continue_btn = self.page.wait_for_selector(
                'button:has-text("Continue"), button:has-text("Next"), button:has-text("Create")',
                timeout=5000
            )
            continue_btn.click()
            self.log("Clicked 'Continue'", "✅")
            time.sleep(2)
        except PlaywrightTimeout:
            self.log("No 'Continue' button found. Moving on...", "⚠️")
            
    def upload_leads(self):
        """Upload CSV file with leads"""
        self.log(f"Uploading leads from: {self.csv_path}", "📤")
        
        if not self.csv_path.exists():
            self.log(f"❌ CSV file not found: {self.csv_path}", "❌")
            return False
            
        try:
            # Look for file upload input or "Upload CSV" button
            upload_btn = self.page.wait_for_selector(
                'button:has-text("Upload"), button:has-text("Add Leads"), input[type="file"]',
                timeout=10000
            )
            
            # If it's a button, click it first to reveal file input
            if upload_btn.evaluate("el => el.tagName") == "BUTTON":
                upload_btn.click()
                time.sleep(1)
                
            # Find the actual file input
            file_input = self.page.wait_for_selector('input[type="file"]', timeout=5000)
            file_input.set_input_files(str(self.csv_path.absolute()))
            
            self.log("✅ CSV uploaded!", "✅")
            time.sleep(3)
            
            # Click "Continue" or "Import"
            try:
                import_btn = self.page.wait_for_selector(
                    'button:has-text("Import"), button:has-text("Continue"), button:has-text("Upload")',
                    timeout=5000
                )
                import_btn.click()
                self.log("Clicked 'Import'", "✅")
                time.sleep(3)
            except PlaywrightTimeout:
                pass
                
            return True
            
        except PlaywrightTimeout:
            self.log("❌ Could not find upload button", "❌")
            return False
            
    def setup_sequences(self):
        """Set up email sequences"""
        self.log("Setting up email sequences...", "✉️")
        
        sequences = [
            {
                "subject": "{{firstName}}, quick question about {{company}}'s customer support",
                "body": """Hi {{firstName}},

I noticed {{company}} is growing fast, and I'm guessing your team is getting slammed with customer calls.

Most teams handle this by:
1. Hiring more reps (expensive)
2. Letting calls go to voicemail (bad experience)
3. Using chatbots (frustrating for customers)

There's a fourth option: AI voice agents that actually sound human.

They handle:
- After-hours calls
- Overflow during busy times
- Simple questions (so your team can focus on complex issues)

**Real use case:** One of our clients went from 40% missed calls to 0% in 30 days.

Interested in a 5-min demo?

Best,
Mitch""",
                "delay": 0
            },
            {
                "subject": "Re: {{firstName}}, quick question about {{company}}'s customer support",
                "body": """Hi {{firstName}},

Following up on my email from Tuesday.

Just to clarify – this isn't a chatbot. It's a voice AI that:
- Answers calls like a real person
- Handles FAQs, scheduling, and routing
- Works 24/7 (no breaks, no sick days)

**Quick stats:**
- 90% of callers can't tell it's AI
- $500-$1,500/month (vs $3,000+/month for a human)
- Set up in 48 hours

Worth a quick chat?

Best,
Mitch""",
                "delay": 3
            },
            {
                "subject": "Last note - AI for {{company}}",
                "body": """Hi {{firstName}},

I'll keep this short.

If you're dealing with:
- Missed calls hurting revenue
- Long hold times frustrating customers
- Support costs eating your margins

We should talk.

15-minute demo, zero pressure.

Here's my calendar: [YOUR CALENDLY LINK]

Best,
Mitch

P.S. If this isn't a priority right now, just let me know and I'll check back in Q3.""",
                "delay": 4
            }
        ]
        
        self.log(f"⚠️  Manual step required: Add {len(sequences)} email sequences", "⚠️")
        self.log("The script will pause here. Please add the sequences manually.", "📝")
        
        print("\n" + "="*80)
        print("EMAIL SEQUENCES TO ADD:")
        print("="*80)
        
        for i, seq in enumerate(sequences, 1):
            print(f"\n📧 Email {i} (Wait: {seq['delay']} days)")
            print(f"\nSubject: {seq['subject']}")
            print(f"\nBody:\n{seq['body']}")
            print("\n" + "-"*80)
            
        input("\n✅ Press Enter once you've added all 3 email sequences...")
        
    def configure_settings(self):
        """Configure campaign settings"""
        self.log("Configuring campaign settings...", "⚙️")
        
        settings = {
            "daily_limit": 40,
            "schedule": "Mon-Fri, 9am-5pm",
            "stop_on_reply": True,
            "track_opens": True,
            "track_clicks": True
        }
        
        self.log(f"Target settings: {settings}", "📊")
        self.log("⚠️  Please verify settings manually:", "⚠️")
        print("\n  - Daily limit: 40 emails/day")
        print("  - Schedule: Monday-Friday, 9am-5pm")
        print("  - Stop on reply: YES")
        print("  - Track opens: YES")
        print("  - Track clicks: YES")
        
        input("\n✅ Press Enter once settings are configured...")
        
    def launch_campaign(self):
        """Launch the campaign"""
        self.log("Looking for 'Launch' button...", "🚀")
        
        try:
            launch_btn = self.page.wait_for_selector(
                'button:has-text("Launch"), button:has-text("Start"), button:has-text("Activate")',
                timeout=10000
            )
            
            self.log("Found 'Launch' button! Ready to launch...", "✅")
            confirm = input("\n🚨 Launch campaign now? (y/n): ")
            
            if confirm.lower() == 'y':
                launch_btn.click()
                self.log("🎉 CAMPAIGN LAUNCHED! 🎉", "🎉")
                time.sleep(3)
            else:
                self.log("Campaign not launched. You can launch manually.", "ℹ️")
                
        except PlaywrightTimeout:
            self.log("Could not find 'Launch' button. Please launch manually.", "⚠️")
            
    def run(self):
        """Main execution flow"""
        print("\n" + "="*80)
        print("🤖 INSTANTLY.AI CAMPAIGN AUTOMATION")
        print("="*80 + "\n")
        
        with sync_playwright() as p:
            try:
                self.setup_browser(p)
                self.login()
                self.create_campaign()
                self.upload_leads()
                self.setup_sequences()
                self.configure_settings()
                self.launch_campaign()
                
                self.log("✅ Automation complete!", "✅")
                self.log("Campaign should be live or ready to launch.", "🎯")
                
                input("\nPress Enter to close browser...")
                
            except KeyboardInterrupt:
                self.log("Script interrupted by user", "⚠️")
            except Exception as e:
                self.log(f"Error occurred: {e}", "❌")
                import traceback
                traceback.print_exc()
            finally:
                if self.browser:
                    self.browser.close()


def main():
    """Entry point"""
    print("\n🔐 INSTANTLY.AI LOGIN CREDENTIALS")
    print("="*80)
    
    # Get credentials
    email = input("Enter your Instantly.ai email: ").strip()
    password = input("Enter your Instantly.ai password: ").strip()
    
    # Get CSV path
    default_csv = "/root/clawd/projects/voxable-cold-outreach/voxable-leads-instantly-export.csv"
    csv_input = input(f"\nCSV file path (default: {default_csv}): ").strip()
    csv_path = csv_input if csv_input else default_csv
    
    print("\n")
    
    # Create and run automator
    automator = InstantlyCampaignAutomator(email, password, csv_path)
    automator.run()


if __name__ == "__main__":
    main()

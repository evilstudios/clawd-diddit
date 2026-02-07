#!/usr/bin/env python3
"""
Email Finder for Restaurant Contacts
Finds missing emails using multiple methods:
1. Website scraping
2. Common pattern guessing
3. Hunter.io API (optional)
"""

import csv
import json
import re
import requests
from typing import Optional, List, Dict
from urllib.parse import urlparse
import time

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("⚠️  BeautifulSoup not installed. Run: pip install beautifulsoup4")
    BeautifulSoup = None

class EmailFinder:
    def __init__(self, hunter_api_key: Optional[str] = None):
        self.hunter_api_key = hunter_api_key
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def extract_email_from_website(self, website_url: str) -> Optional[str]:
        """Scrape website for email addresses"""
        if not website_url or not BeautifulSoup:
            return None
        
        try:
            # Clean URL
            if not website_url.startswith('http'):
                website_url = 'https://' + website_url
            
            response = self.session.get(website_url, timeout=10)
            response.raise_for_status()
            
            # Extract domain for filtering
            domain = urlparse(website_url).netloc.replace('www.', '')
            
            # Search page content for emails
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            emails = re.findall(email_pattern, response.text)
            
            # Filter and prioritize
            excluded = ['example.com', 'gmail.com', 'yahoo.com', 'hotmail.com']
            
            # Prefer emails matching the domain
            for email in emails:
                if domain in email and not any(ex in email for ex in excluded):
                    return email
            
            # Return first non-excluded email
            for email in emails:
                if not any(ex in email for ex in excluded):
                    return email
            
            # Try contact page
            contact_urls = [
                f"{website_url}/contact",
                f"{website_url}/about",
                f"{website_url}/contact-us"
            ]
            
            for url in contact_urls:
                try:
                    resp = self.session.get(url, timeout=5)
                    emails = re.findall(email_pattern, resp.text)
                    for email in emails:
                        if domain in email:
                            return email
                except:
                    continue
        
        except Exception as e:
            print(f"      ⚠️ Error scraping website: {e}")
        
        return None
    
    def guess_email_patterns(self, name: str, website: str) -> List[str]:
        """Generate common email patterns"""
        if not name or not website:
            return []
        
        # Extract domain
        try:
            if not website.startswith('http'):
                website = 'https://' + website
            domain = urlparse(website).netloc.replace('www.', '')
        except:
            return []
        
        # Clean and parse name
        name_parts = re.sub(r'[^\w\s]', '', name.lower()).split()
        if len(name_parts) < 2:
            name_parts = name.lower().split()[:2]
        
        if len(name_parts) < 2:
            return []
        
        first = name_parts[0]
        last = name_parts[-1]
        
        # Common patterns
        patterns = [
            f"info@{domain}",
            f"contact@{domain}",
            f"hello@{domain}",
            f"orders@{domain}",
            f"{first}@{domain}",
            f"{first}.{last}@{domain}",
            f"{first[0]}{last}@{domain}",
            f"{last}@{domain}"
        ]
        
        return patterns
    
    def find_with_hunter(self, domain: str) -> Optional[str]:
        """Use Hunter.io API to find email"""
        if not self.hunter_api_key:
            return None
        
        try:
            url = f"https://api.hunter.io/v2/domain-search"
            params = {
                'domain': domain,
                'api_key': self.hunter_api_key,
                'limit': 1
            }
            
            response = self.session.get(url, params=params, timeout=10)
            data = response.json()
            
            if data.get('data', {}).get('emails'):
                return data['data']['emails'][0]['value']
        
        except Exception as e:
            print(f"      ⚠️ Hunter.io error: {e}")
        
        return None
    
    def find_email(self, name: str, website: str, phone: str = None) -> Dict:
        """Try all methods to find an email"""
        result = {
            'email': None,
            'method': None,
            'confidence': 'none'
        }
        
        # Method 1: Scrape website
        if website:
            email = self.extract_email_from_website(website)
            if email:
                result['email'] = email
                result['method'] = 'website_scrape'
                result['confidence'] = 'high'
                return result
        
        # Method 2: Hunter.io
        if website and self.hunter_api_key:
            try:
                domain = urlparse(website).netloc.replace('www.', '')
                email = self.find_with_hunter(domain)
                if email:
                    result['email'] = email
                    result['method'] = 'hunter_io'
                    result['confidence'] = 'high'
                    return result
            except:
                pass
        
        # Method 3: Pattern guessing (lowest confidence)
        if website:
            patterns = self.guess_email_patterns(name, website)
            if patterns:
                result['email'] = patterns[0]  # Most common: info@domain
                result['method'] = 'pattern_guess'
                result['confidence'] = 'low'
                return result
        
        return result
    
    def process_csv(self, input_csv: str, output_csv: str):
        """Process CSV and add emails"""
        print("\n📧 Finding emails for restaurants...")
        print("="*60)
        
        restaurants = []
        with open(input_csv, 'r') as f:
            reader = csv.DictReader(f)
            restaurants = list(reader)
        
        total = len(restaurants)
        found = 0
        
        for i, restaurant in enumerate(restaurants, 1):
            name = restaurant.get('Restaurant Name', '')
            website = restaurant.get('Website', '')
            current_email = restaurant.get('Email', '')
            
            print(f"\n{i}/{total}: {name}")
            
            # Skip if already has email
            if current_email:
                print("   ✅ Already has email")
                continue
            
            # Find email
            result = self.find_email(name, website)
            
            if result['email']:
                restaurant['Email'] = result['email']
                restaurant['Email Method'] = result['method']
                restaurant['Email Confidence'] = result['confidence']
                found += 1
                print(f"   ✅ Found: {result['email']} (via {result['method']})")
            else:
                print(f"   ❌ No email found")
            
            time.sleep(0.5)  # Be nice to servers
        
        # Save updated CSV
        with open(output_csv, 'w', newline='') as f:
            fieldnames = list(restaurants[0].keys())
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(restaurants)
        
        print("\n" + "="*60)
        print(f"✅ Processed {total} restaurants")
        print(f"📧 Found {found} new emails")
        print(f"💾 Saved to: {output_csv}")
        print("="*60)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Find emails for restaurants')
    parser.add_argument('--input', type=str, required=True, help='Input CSV file')
    parser.add_argument('--output', type=str, help='Output CSV file (default: input_with_emails.csv)')
    parser.add_argument('--hunter-key', type=str, help='Hunter.io API key (optional)')
    
    args = parser.parse_args()
    
    if not args.output:
        base = args.input.replace('.csv', '')
        args.output = f"{base}_with_emails.csv"
    
    finder = EmailFinder(hunter_api_key=args.hunter_key)
    finder.process_csv(args.input, args.output)
    
    print("\n✅ Email finding complete!")
    print(f"\nNext steps:")
    print(f"1. Review: {args.output}")
    print(f"2. Manually verify low-confidence emails")
    print(f"3. Upload to Instantly.ai")


if __name__ == "__main__":
    main()

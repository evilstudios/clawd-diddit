#!/usr/bin/env python3
"""
Voxable Lead Generator - Google Maps Scraper
Targets: Local service businesses (plumbers, HVAC, electricians, etc.)
Output: CSV with business name, owner, email, phone, location
"""

import csv
import json
import time
import requests
from datetime import datetime
from pathlib import Path

# Target industries and cities
INDUSTRIES = [
    "plumber",
    "electrician", 
    "hvac",
    "locksmith",
    "contractor",
    "roofing contractor",
    "painting contractor",
    "pest control",
    "cleaning service",
    "landscaping",
    "auto repair",
    "salon",
    "barber shop",
    "handyman"
]

# Major US cities for broader reach
CITIES = [
    "New York, NY",
    "Los Angeles, CA",
    "Chicago, IL",
    "Houston, TX",
    "Phoenix, AZ",
    "Philadelphia, PA",
    "San Antonio, TX",
    "San Diego, CA",
    "Dallas, TX",
    "San Jose, CA",
    "Austin, TX",
    "Jacksonville, FL",
    "Fort Worth, TX",
    "Columbus, OH",
    "Charlotte, NC",
    "San Francisco, CA",
    "Indianapolis, IN",
    "Seattle, WA",
    "Denver, CO",
    "Boston, MA",
    "Nashville, TN",
    "Detroit, MI",
    "Portland, OR",
    "Las Vegas, NV",
    "Miami, FL"
]

class GoogleMapsLeadScraper:
    """Scrapes Google Maps for local service businesses"""
    
    def __init__(self):
        self.output_file = Path(__file__).parent / f"voxable-leads-{datetime.now().strftime('%Y%m%d')}.csv"
        self.leads = []
        
    def scrape_outscraper(self):
        """
        Uses Outscraper API (if configured)
        Get API key from: https://outscraper.com/
        """
        api_key = os.getenv('OUTSCRAPER_API_KEY')
        if not api_key:
            print("⚠️  OUTSCRAPER_API_KEY not set - skipping Outscraper method")
            return []
        
        # Outscraper implementation here
        print("📡 Scraping via Outscraper API...")
        return []
    
    def scrape_apify(self):
        """
        Uses Apify Google Maps Scraper
        Get API token from: https://apify.com/
        """
        api_token = os.getenv('APIFY_API_TOKEN')
        if not api_token:
            print("⚠️  APIFY_API_TOKEN not set - skipping Apify method")
            return []
            
        print("📡 Scraping via Apify...")
        # Apify implementation here
        return []
    
    def build_manual_search_queries(self):
        """Generate search queries for manual scraping"""
        queries = []
        for industry in INDUSTRIES[:5]:  # Start with top 5 industries
            for city in CITIES[:10]:  # Top 10 cities
                queries.append(f"{industry} {city}")
        
        print(f"\n📋 Generated {len(queries)} search queries")
        print("\n🔍 Top 10 queries to scrape:")
        for i, q in enumerate(queries[:10], 1):
            print(f"   {i}. {q}")
        
        return queries
    
    def generate_email_guesses(self, business_name, owner_name=None):
        """Generate common email patterns"""
        domain_guess = business_name.lower().replace(' ', '').replace('&', 'and')[:20]
        
        patterns = [
            f"info@{domain_guess}.com",
            f"contact@{domain_guess}.com",
            f"hello@{domain_guess}.com",
        ]
        
        if owner_name:
            first = owner_name.split()[0].lower()
            patterns.extend([
                f"{first}@{domain_guess}.com",
                f"{owner_name.replace(' ', '').lower()}@{domain_guess}.com"
            ])
        
        return patterns
    
    def export_csv(self, leads):
        """Export leads to CSV format for Instantly.ai"""
        fieldnames = [
            'firstName',
            'lastName', 
            'email',
            'companyName',
            'businessType',
            'phone',
            'city',
            'state',
            'website',
            'customField1'  # For notes
        ]
        
        with open(self.output_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(leads)
        
        print(f"\n✅ Exported {len(leads)} leads to {self.output_file}")
        return self.output_file
    
    def create_sample_leads(self):
        """Create sample leads for testing (manual entry template)"""
        samples = [
            {
                'firstName': 'Mike',
                'lastName': 'Johnson',
                'email': 'mike@quickplumbingtx.com',
                'companyName': 'Quick Plumbing TX',
                'businessType': 'plumber',
                'phone': '512-555-0123',
                'city': 'Austin',
                'state': 'TX',
                'website': 'quickplumbingtx.com',
                'customField1': 'Google Maps - 4.8 stars, 89 reviews'
            },
            {
                'firstName': 'Sarah',
                'lastName': 'Martinez',
                'email': 'sarah@elitehvacla.com',
                'companyName': 'Elite HVAC LA',
                'businessType': 'hvac',
                'phone': '323-555-0456',
                'city': 'Los Angeles',
                'state': 'CA',
                'website': 'elitehvacla.com',
                'customField1': 'Google Maps - 4.6 stars, 124 reviews'
            },
            {
                'firstName': 'Tom',
                'lastName': 'Wilson',
                'email': 'info@wilsonelectricnyc.com',
                'companyName': 'Wilson Electric NYC',
                'businessType': 'electrician',
                'phone': '212-555-0789',
                'city': 'New York',
                'state': 'NY',
                'website': 'wilsonelectricnyc.com',
                'customField1': 'Google Maps - 4.9 stars, 203 reviews'
            }
        ]
        
        return samples

def main():
    print("🎯 Voxable Lead Generator - Google Maps Edition")
    print("=" * 60)
    
    scraper = GoogleMapsLeadScraper()
    
    # Try API methods first
    leads = []
    leads.extend(scraper.scrape_outscraper())
    leads.extend(scraper.scrape_apify())
    
    # If no API leads, generate manual search guide
    if not leads:
        print("\n⚠️  No API keys configured - generating manual scraping guide")
        queries = scraper.build_manual_search_queries()
        
        print("\n" + "=" * 60)
        print("📖 MANUAL SCRAPING GUIDE")
        print("=" * 60)
        print("\n1. Install Chrome Extension: 'Instant Data Scraper'")
        print("   https://chrome.google.com/webstore/detail/instant-data-scraper/")
        print("\n2. For each query above:")
        print("   a. Search Google Maps")
        print("   b. Click extension icon")
        print("   c. Auto-detect listings")
        print("   d. Export CSV")
        print("\n3. Combine all CSVs into one file")
        print("\n4. Clean data (remove duplicates, validate emails)")
        
        print("\n" + "=" * 60)
        print("📦 RECOMMENDED TOOLS")
        print("=" * 60)
        print("\n💰 Outscraper ($49/mo - 5,000 credits):")
        print("   https://outscraper.com/")
        print("   Best for: Bulk automated scraping")
        print("\n🤖 Apify Google Maps Scraper ($49/mo):")
        print("   https://apify.com/compass/google-maps-scraper")
        print("   Best for: Large-scale data extraction")
        print("\n🆓 Instant Data Scraper (Chrome - Free):")
        print("   Manual but works immediately")
        
        # Create sample file for template
        sample_leads = scraper.create_sample_leads()
        sample_file = scraper.export_csv(sample_leads)
        
        print(f"\n✅ Created sample template: {sample_file}")
        print("   Use this format when adding real leads")
    else:
        scraper.export_csv(leads)
        print(f"\n🎉 Success! Scraped {len(leads)} leads")
    
    print("\n" + "=" * 60)
    print("NEXT STEPS:")
    print("1. Get leads (scraper API or manual)")
    print("2. Validate emails (hunter.io, neverbounce.com)")
    print("3. Upload to Instantly.ai")
    print("4. Launch campaign")
    print("=" * 60)

if __name__ == "__main__":
    import os
    main()

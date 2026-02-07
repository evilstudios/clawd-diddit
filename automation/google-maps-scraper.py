#!/usr/bin/env python3
"""
Google Maps Restaurant Scraper for Afoodable
Scrapes restaurant data from Google Maps for cold outreach campaigns
"""

import os
import json
import csv
import time
import re
from typing import List, Dict, Optional
from datetime import datetime

try:
    from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
except ImportError:
    print("❌ Playwright not installed. Run: pip install playwright && playwright install")
    exit(1)

class GoogleMapsScraper:
    def __init__(self, headless: bool = True):
        self.headless = headless
        self.results = []
        
    def extract_email_from_text(self, text: str) -> Optional[str]:
        """Extract email from text using regex"""
        if not text:
            return None
        
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        matches = re.findall(email_pattern, text)
        
        # Filter out common non-business emails
        excluded_domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com']
        for email in matches:
            domain = email.split('@')[1].lower()
            if domain not in excluded_domains:
                return email
        
        return matches[0] if matches else None
    
    def scrape_search(self, query: str, location: str, max_results: int = 50) -> List[Dict]:
        """Scrape Google Maps search results"""
        
        search_query = f"{query} in {location}"
        url = f"https://www.google.com/maps/search/{search_query.replace(' ', '+')}"
        
        print(f"\n🔍 Searching: {search_query}")
        print(f"   URL: {url}")
        
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=self.headless)
            page = browser.new_page()
            
            try:
                # Navigate to search
                page.goto(url, wait_until="networkidle", timeout=30000)
                time.sleep(3)  # Let results load
                
                # Scroll the results panel to load more
                results_panel = page.locator('[role="feed"]').first
                
                collected = 0
                scroll_attempts = 0
                max_scroll_attempts = 20
                
                while collected < max_results and scroll_attempts < max_scroll_attempts:
                    # Get all visible result cards
                    cards = page.locator('div[role="article"]').all()
                    
                    print(f"   Found {len(cards)} cards (target: {max_results})")
                    
                    for card in cards[collected:]:
                        try:
                            # Click the card to open details
                            card.click(timeout=2000)
                            time.sleep(1.5)
                            
                            # Extract data
                            data = self.extract_place_data(page)
                            
                            if data and data.get('name'):
                                self.results.append(data)
                                collected += 1
                                print(f"   ✅ {collected}/{max_results}: {data['name']}")
                                
                                if collected >= max_results:
                                    break
                        
                        except Exception as e:
                            print(f"   ⏭️  Skipped card: {e}")
                            continue
                    
                    # Scroll to load more results
                    try:
                        results_panel.evaluate("el => el.scrollTop = el.scrollHeight")
                        time.sleep(2)
                        scroll_attempts += 1
                    except:
                        break
                
                print(f"\n✅ Collected {len(self.results)} restaurants")
                
            except Exception as e:
                print(f"❌ Error during scraping: {e}")
            
            finally:
                browser.close()
        
        return self.results
    
    def extract_place_data(self, page) -> Optional[Dict]:
        """Extract data from the place details panel"""
        
        try:
            data = {
                'timestamp': datetime.now().isoformat(),
                'name': None,
                'address': None,
                'phone': None,
                'website': None,
                'email': None,
                'rating': None,
                'reviews_count': None,
                'category': None,
                'hours': None,
                'price_level': None
            }
            
            # Name
            try:
                name_el = page.locator('h1[class*="fontHeadline"]').first
                data['name'] = name_el.inner_text(timeout=2000).strip()
            except:
                pass
            
            # Category
            try:
                category_el = page.locator('button[jsaction*="category"]').first
                data['category'] = category_el.inner_text(timeout=2000).strip()
            except:
                pass
            
            # Rating
            try:
                rating_el = page.locator('span[role="img"][aria-label*="stars"]').first
                rating_text = rating_el.get_attribute('aria-label')
                if rating_text:
                    rating_match = re.search(r'([\d.]+)\s*stars?', rating_text)
                    if rating_match:
                        data['rating'] = float(rating_match.group(1))
            except:
                pass
            
            # Reviews count
            try:
                reviews_el = page.locator('span[aria-label*="review"]').first
                reviews_text = reviews_el.get_attribute('aria-label')
                if reviews_text:
                    reviews_match = re.search(r'([\d,]+)\s*review', reviews_text)
                    if reviews_match:
                        data['reviews_count'] = int(reviews_match.group(1).replace(',', ''))
            except:
                pass
            
            # Address
            try:
                address_el = page.locator('button[data-item-id="address"]').first
                data['address'] = address_el.inner_text(timeout=2000).strip()
            except:
                pass
            
            # Phone
            try:
                phone_el = page.locator('button[data-item-id*="phone"]').first
                phone_text = phone_el.get_attribute('aria-label')
                if phone_text:
                    phone_match = re.search(r'[\d\s\(\)\-\+]+', phone_text)
                    if phone_match:
                        data['phone'] = phone_match.group(0).strip()
            except:
                pass
            
            # Website
            try:
                website_el = page.locator('a[data-item-id="authority"]').first
                data['website'] = website_el.get_attribute('href')
            except:
                pass
            
            # Try to extract email from website button or description
            try:
                # Check "About" tab or description for email
                about_text = page.locator('div[class*="section-editorial"]').first.inner_text(timeout=2000)
                data['email'] = self.extract_email_from_text(about_text)
            except:
                pass
            
            # Hours (simplified - just check if open)
            try:
                hours_el = page.locator('div[aria-label*="hours"]').first
                data['hours'] = hours_el.inner_text(timeout=2000).strip()
            except:
                pass
            
            # Price level
            try:
                price_el = page.locator('span[aria-label*="Price"]').first
                price_text = price_el.get_attribute('aria-label')
                if price_text:
                    data['price_level'] = price_text
            except:
                pass
            
            return data
        
        except Exception as e:
            print(f"   ❌ Error extracting data: {e}")
            return None
    
    def save_results(self, filename: str = 'restaurants.json'):
        """Save results to JSON file"""
        output_path = f"/root/clawd/projects/afoodable-restaurant-outreach/{filename}"
        
        with open(output_path, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        print(f"\n💾 Saved {len(self.results)} results to: {output_path}")
        return output_path
    
    def export_csv(self, filename: str = 'restaurants.csv'):
        """Export results to CSV for Instantly"""
        output_path = f"/root/clawd/projects/afoodable-restaurant-outreach/{filename}"
        
        if not self.results:
            print("❌ No results to export")
            return None
        
        # CSV headers for Instantly.ai
        headers = [
            'Restaurant Name',
            'Email',
            'Phone',
            'Address',
            'Website',
            'Category',
            'Rating',
            'Reviews',
            'Status',
            'Notes'
        ]
        
        with open(output_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            
            for place in self.results:
                writer.writerow([
                    place.get('name', ''),
                    place.get('email', ''),
                    place.get('phone', ''),
                    place.get('address', ''),
                    place.get('website', ''),
                    place.get('category', ''),
                    place.get('rating', ''),
                    place.get('reviews_count', ''),
                    'To Contact',
                    f"Scraped: {datetime.now().strftime('%Y-%m-%d')}"
                ])
        
        print(f"📊 Exported CSV to: {output_path}")
        return output_path
    
    def print_summary(self):
        """Print summary statistics"""
        if not self.results:
            print("\n❌ No results collected")
            return
        
        total = len(self.results)
        with_email = sum(1 for r in self.results if r.get('email'))
        with_phone = sum(1 for r in self.results if r.get('phone'))
        with_website = sum(1 for r in self.results if r.get('website'))
        
        avg_rating = sum(r.get('rating', 0) for r in self.results if r.get('rating')) / max(1, sum(1 for r in self.results if r.get('rating')))
        
        print("\n" + "="*60)
        print("📊 SCRAPING SUMMARY")
        print("="*60)
        print(f"Total restaurants: {total}")
        print(f"With email: {with_email} ({with_email/total*100:.1f}%)")
        print(f"With phone: {with_phone} ({with_phone/total*100:.1f}%)")
        print(f"With website: {with_website} ({with_website/total*100:.1f}%)")
        print(f"Average rating: {avg_rating:.1f}⭐")
        print("="*60)


def main():
    import argparse
    
    parser = argparse.ArgumentParser(description='Scrape Google Maps for restaurant data')
    parser.add_argument('--city', type=str, default='Philadelphia, PA', help='City to search')
    parser.add_argument('--query', type=str, action='append', help='Search query (can be repeated)')
    parser.add_argument('--max-per-query', type=int, default=35, help='Max results per query')
    parser.add_argument('--headless', action='store_true', help='Run in headless mode')
    parser.add_argument('--output-json', type=str, default='philadelphia-restaurants.json', help='Output JSON filename')
    parser.add_argument('--output-csv', type=str, default='philadelphia-restaurants.csv', help='Output CSV filename')
    
    args = parser.parse_args()
    
    # Default queries for Afoodable target restaurants
    if not args.query:
        args.query = [
            'bakery',
            'cafe',
            'fast casual restaurant',
        ]
    
    print("🚀 Afoodable Restaurant Scraper")
    print("="*60)
    print(f"Target city: {args.city}")
    print(f"Queries: {', '.join(args.query)}")
    print(f"Max per query: {args.max_per_query}")
    print("="*60)
    
    scraper = GoogleMapsScraper(headless=args.headless)
    
    # Run searches for each query
    for query in args.query:
        scraper.scrape_search(query, args.city, max_results=args.max_per_query)
        time.sleep(3)  # Pause between queries
    
    # Save results
    scraper.save_results(args.output_json)
    scraper.export_csv(args.output_csv)
    scraper.print_summary()
    
    print("\n✅ Scraping complete!")
    print(f"\nNext steps:")
    print(f"1. Review: {args.output_csv}")
    print(f"2. Find missing emails (see email-finder tool)")
    print(f"3. Upload to Instantly.ai")
    print(f"4. Launch campaign")


if __name__ == "__main__":
    main()

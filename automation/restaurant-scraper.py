#!/usr/bin/env python3
"""
Restaurant Lead Scraper - Google Maps Edition
Extracts restaurant data for cold outreach campaigns
Built for Afoodable Philadelphia launch (and future SaaS product)
"""

import os
import sys
import json
import time
import re
import csv
from typing import List, Dict, Optional
from datetime import datetime
import requests
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout

class RestaurantScraper:
    """Scrapes restaurant data from Google Maps"""
    
    def __init__(self, headless: bool = True):
        self.headless = headless
        self.results = []
        
    def scrape_google_maps(self, query: str, location: str, max_results: int = 50) -> List[Dict]:
        """
        Scrape Google Maps for restaurants
        
        Args:
            query: Search query (e.g., "bakery", "cafe", "fast casual restaurant")
            location: City/location (e.g., "Philadelphia, PA")
            max_results: Maximum number of results to scrape
            
        Returns:
            List of restaurant data dictionaries
        """
        
        search_query = f"{query} in {location}"
        print(f"🔍 Searching: {search_query}")
        
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=self.headless)
            page = browser.new_page()
            
            try:
                # Navigate to Google Maps
                maps_url = f"https://www.google.com/maps/search/{search_query.replace(' ', '+')}"
                print(f"📍 Loading Google Maps...")
                page.goto(maps_url, timeout=30000)
                
                # Wait for results to load
                time.sleep(3)
                
                # Scroll to load more results
                print(f"📜 Scrolling to load results...")
                results_panel = page.query_selector('div[role="feed"]')
                
                if not results_panel:
                    print("❌ Could not find results panel")
                    browser.close()
                    return []
                
                # Scroll multiple times to load more results
                for i in range(max_results // 10):
                    page.evaluate("""
                        (selector) => {
                            const panel = document.querySelector(selector);
                            if (panel) {
                                panel.scrollTop = panel.scrollHeight;
                            }
                        }
                    """, 'div[role="feed"]')
                    time.sleep(1)
                
                # Get all result links
                print(f"🎯 Extracting restaurant data...")
                result_links = page.query_selector_all('a[href*="/maps/place/"]')
                
                restaurants = []
                processed = 0
                
                for link in result_links[:max_results]:
                    if processed >= max_results:
                        break
                    
                    try:
                        # Click to open details
                        link.click()
                        time.sleep(2)
                        
                        # Extract data
                        restaurant = self._extract_restaurant_data(page)
                        
                        if restaurant:
                            restaurants.append(restaurant)
                            processed += 1
                            print(f"  ✓ {processed}/{max_results}: {restaurant['name']}")
                        
                    except Exception as e:
                        print(f"  ⚠️  Error processing result: {e}")
                        continue
                
                browser.close()
                return restaurants
                
            except Exception as e:
                print(f"❌ Error during scraping: {e}")
                browser.close()
                return []
    
    def _extract_restaurant_data(self, page) -> Optional[Dict]:
        """Extract restaurant data from Google Maps detail page"""
        
        try:
            # Name
            name_element = page.query_selector('h1')
            name = name_element.inner_text() if name_element else None
            
            if not name:
                return None
            
            # Address
            address_element = page.query_selector('button[data-item-id="address"]')
            address = address_element.inner_text() if address_element else None
            
            # Phone
            phone_element = page.query_selector('button[data-item-id*="phone"]')
            phone = phone_element.inner_text() if phone_element else None
            
            # Website
            website_element = page.query_selector('a[data-item-id="authority"]')
            website = website_element.get_attribute('href') if website_element else None
            
            # Rating
            rating_element = page.query_selector('div[jsaction*="pane.rating"]')
            rating = None
            if rating_element:
                rating_text = rating_element.inner_text()
                rating_match = re.search(r'(\d+\.?\d*)', rating_text)
                if rating_match:
                    rating = float(rating_match.group(1))
            
            # Review count
            review_count = None
            review_element = page.query_selector('span[aria-label*="reviews"]')
            if review_element:
                review_text = review_element.inner_text()
                review_match = re.search(r'(\d+)', review_text.replace(',', ''))
                if review_match:
                    review_count = int(review_match.group(1))
            
            # Hours
            hours = None
            hours_element = page.query_selector('div[aria-label*="Hours"]')
            if hours_element:
                hours = hours_element.inner_text()
            
            # Category/Type
            category_element = page.query_selector('button[jsaction*="category"]')
            category = category_element.inner_text() if category_element else None
            
            # Extract email from website if available
            email = self._find_email_from_website(website) if website else None
            
            return {
                'name': name,
                'address': address,
                'phone': phone,
                'website': website,
                'email': email,
                'rating': rating,
                'review_count': review_count,
                'hours': hours,
                'category': category,
                'lead_score': self._calculate_lead_score(rating, review_count, category),
                'scraped_at': datetime.now().isoformat()
            }
            
        except Exception as e:
            print(f"    Error extracting data: {e}")
            return None
    
    def _find_email_from_website(self, website_url: str, timeout: int = 5) -> Optional[str]:
        """Try to find email address from restaurant website"""
        
        try:
            response = requests.get(website_url, timeout=timeout)
            html = response.text
            
            # Common email patterns
            email_patterns = [
                r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
            ]
            
            for pattern in email_patterns:
                matches = re.findall(pattern, html)
                if matches:
                    # Filter out common non-contact emails
                    filtered = [e for e in matches if not any(x in e.lower() for x in 
                               ['@example', '@domain', '@yourcompany', '@test', 'noreply', 'donotreply'])]
                    if filtered:
                        return filtered[0]
            
            return None
            
        except:
            return None
    
    def _calculate_lead_score(self, rating: Optional[float], review_count: Optional[int], category: Optional[str]) -> int:
        """
        Calculate lead quality score (1-10)
        
        Factors:
        - Rating (higher = better)
        - Review count (more = more popular/busy)
        - Category match (bakery/cafe = higher score)
        """
        
        score = 5  # Base score
        
        # Rating factor
        if rating:
            if rating >= 4.5:
                score += 2
            elif rating >= 4.0:
                score += 1
            elif rating < 3.5:
                score -= 1
        
        # Review count factor (popularity = likely to have surplus)
        if review_count:
            if review_count >= 500:
                score += 2
            elif review_count >= 200:
                score += 1
            elif review_count < 50:
                score -= 1
        
        # Category factor
        if category:
            category_lower = category.lower()
            if any(x in category_lower for x in ['bakery', 'cafe', 'coffee']):
                score += 1
            elif 'fast casual' in category_lower or 'counter service' in category_lower:
                score += 1
        
        return max(1, min(10, score))  # Clamp between 1-10
    
    def guess_email_patterns(self, restaurant_name: str, website: Optional[str] = None) -> List[str]:
        """
        Generate likely email patterns for a restaurant
        
        Returns list of probable email addresses to try
        """
        
        if not website:
            return []
        
        # Extract domain from website
        domain_match = re.search(r'https?://(?:www\.)?([^/]+)', website)
        if not domain_match:
            return []
        
        domain = domain_match.group(1)
        
        # Generate common patterns
        patterns = [
            f'info@{domain}',
            f'contact@{domain}',
            f'hello@{domain}',
            f'owner@{domain}',
            f'manager@{domain}',
            f'orders@{domain}',
            f'catering@{domain}'
        ]
        
        return patterns
    
    def export_to_csv(self, restaurants: List[Dict], filename: str):
        """Export restaurant data to CSV for Instantly.ai"""
        
        if not restaurants:
            print("⚠️  No restaurants to export")
            return
        
        # Parse names for personalization
        processed = []
        for r in restaurants:
            # Try to extract owner name from website or use generic
            first_name = "Owner"
            last_name = ""
            
            # Generate email guesses if none found
            if not r['email'] and r['website']:
                email_guesses = self.guess_email_patterns(r['name'], r['website'])
                r['email_guesses'] = ', '.join(email_guesses[:3])
            else:
                r['email_guesses'] = ''
            
            processed.append({
                'restaurant_name': r['name'],
                'first_name': first_name,
                'last_name': last_name,
                'email': r['email'] or '',
                'email_guesses': r['email_guesses'],
                'phone': r['phone'] or '',
                'website': r['website'] or '',
                'address': r['address'] or '',
                'category': r['category'] or '',
                'rating': r['rating'] or '',
                'review_count': r['review_count'] or '',
                'hours': (r['hours'] or '').replace('\n', ' | '),
                'lead_score': r['lead_score'],
                'notes': f"Scraped from Google Maps on {datetime.now().strftime('%Y-%m-%d')}"
            })
        
        # Write CSV
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['restaurant_name', 'first_name', 'last_name', 'email', 'email_guesses',
                         'phone', 'website', 'address', 'category', 'rating', 'review_count',
                         'hours', 'lead_score', 'notes']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(processed)
        
        print(f"✅ Exported {len(processed)} restaurants to {filename}")
        
        # Show summary
        with_email = len([r for r in processed if r['email']])
        with_phone = len([r for r in processed if r['phone']])
        avg_score = sum(r['lead_score'] for r in processed) / len(processed)
        
        print(f"\n📊 Summary:")
        print(f"  Total restaurants: {len(processed)}")
        print(f"  With email: {with_email} ({with_email/len(processed)*100:.1f}%)")
        print(f"  With phone: {with_phone} ({with_phone/len(processed)*100:.1f}%)")
        print(f"  Avg lead score: {avg_score:.1f}/10")


def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Scrape restaurant leads from Google Maps')
    parser.add_argument('--query', required=True, help='Search query (e.g., "bakery", "cafe")')
    parser.add_argument('--location', required=True, help='Location (e.g., "Philadelphia, PA")')
    parser.add_argument('--max', type=int, default=50, help='Maximum results (default: 50)')
    parser.add_argument('--output', default='restaurants.csv', help='Output CSV filename')
    parser.add_argument('--visible', action='store_true', help='Show browser (not headless)')
    
    args = parser.parse_args()
    
    print("🍎 Restaurant Lead Scraper")
    print("=" * 60)
    
    scraper = RestaurantScraper(headless=not args.visible)
    restaurants = scraper.scrape_google_maps(args.query, args.location, args.max)
    
    if restaurants:
        scraper.export_to_csv(restaurants, args.output)
        print(f"\n✅ Done! Ready to upload to Instantly.ai")
    else:
        print("\n❌ No restaurants found")


if __name__ == "__main__":
    main()

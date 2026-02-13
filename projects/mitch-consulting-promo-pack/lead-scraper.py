#!/usr/bin/env python3
"""
Consulting Lead Scraper
Target: 3PL/Logistics, Home Service Franchises, Engineering Firms
Criteria: $5M-$30M revenue, 50-500 employees, owner/exec contact
"""

import csv
import json
import time
from typing import List, Dict
import requests
from datetime import datetime

class ConsultingLeadScraper:
    """Scrape high-ticket consulting prospects"""
    
    def __init__(self):
        self.leads = []
        
    def scrape_apollo_io(self, search_params: Dict) -> List[Dict]:
        """
        Use Apollo.io API to find prospects
        Free tier: 50 credits/month
        
        Args:
            search_params: Search criteria
            
        Returns:
            List of prospects
        """
        # Apollo.io API endpoint
        api_key = "YOUR_APOLLO_API_KEY"  # Get from https://app.apollo.io/#/settings/integrations/api
        
        url = "https://api.apollo.io/v1/mixed_people/search"
        
        headers = {
            "Content-Type": "application/json",
            "Cache-Control": "no-cache",
            "X-Api-Key": api_key
        }
        
        payload = {
            "page": 1,
            "per_page": 25,
            "person_titles": search_params.get("titles", []),
            "q_organization_domains": search_params.get("domains", []),
            "organization_num_employees_ranges": ["51-200", "201-500", "501-1000"],
            "revenue_range": {
                "min": 5000000,
                "max": 50000000
            }
        }
        
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            return data.get("people", [])
        else:
            print(f"Apollo API error: {response.status_code}")
            return []
    
    def scrape_google_search(self, query: str, num_results: int = 20) -> List[Dict]:
        """
        Scrape Google search results for company websites
        
        Args:
            query: Search query (e.g., "3PL logistics companies USA")
            num_results: Number of results to return
            
        Returns:
            List of company data
        """
        # Using SerpAPI (Google Search API)
        api_key = "YOUR_SERPAPI_KEY"  # Get from https://serpapi.com/
        
        url = "https://serpapi.com/search"
        
        params = {
            "q": query,
            "api_key": api_key,
            "num": num_results,
            "gl": "us"
        }
        
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            results = []
            
            for result in data.get("organic_results", []):
                results.append({
                    "company_name": result.get("title", "").split("-")[0].strip(),
                    "website": result.get("link", ""),
                    "description": result.get("snippet", "")
                })
            
            return results
        else:
            print(f"SerpAPI error: {response.status_code}")
            return []
    
    def enrich_with_hunter_io(self, domain: str) -> Dict:
        """
        Find email addresses at domain using Hunter.io
        Free tier: 25 searches/month
        
        Args:
            domain: Company domain (e.g., "example.com")
            
        Returns:
            Dict with emails and contacts
        """
        api_key = "YOUR_HUNTER_API_KEY"  # Get from https://hunter.io/
        
        url = f"https://api.hunter.io/v2/domain-search"
        
        params = {
            "domain": domain,
            "api_key": api_key,
            "limit": 10
        }
        
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            return {
                "emails": [email.get("value") for email in data.get("data", {}).get("emails", [])],
                "pattern": data.get("data", {}).get("pattern", ""),
                "organization": data.get("data", {}).get("organization", "")
            }
        else:
            return {"emails": [], "pattern": "", "organization": ""}
    
    def scrape_3pl_logistics(self) -> List[Dict]:
        """Scrape 3PL and logistics companies"""
        print("🚚 Scraping 3PL/Logistics companies...")
        
        # Google search queries
        queries = [
            "3PL logistics companies USA",
            "freight forwarding companies",
            "warehousing and distribution companies",
            "third party logistics providers"
        ]
        
        companies = []
        
        for query in queries:
            results = self.scrape_google_search(query, num_results=10)
            companies.extend(results)
            time.sleep(2)  # Rate limiting
        
        print(f"✓ Found {len(companies)} 3PL/Logistics companies")
        return companies
    
    def scrape_home_services(self) -> List[Dict]:
        """Scrape home service franchise companies"""
        print("🏠 Scraping Home Service Franchises...")
        
        queries = [
            "HVAC franchise companies USA",
            "plumbing franchise companies",
            "home repair franchise",
            "restoration services franchise",
            "multi-location home services"
        ]
        
        companies = []
        
        for query in queries:
            results = self.scrape_google_search(query, num_results=10)
            companies.extend(results)
            time.sleep(2)
        
        print(f"✓ Found {len(companies)} Home Service Franchises")
        return companies
    
    def scrape_engineering_firms(self) -> List[Dict]:
        """Scrape engineering consulting firms"""
        print("⚙️ Scraping Engineering Firms...")
        
        queries = [
            "engineering consulting firms USA",
            "civil engineering companies",
            "mechanical engineering firms",
            "environmental engineering companies"
        ]
        
        companies = []
        
        for query in queries:
            results = self.scrape_google_search(query, num_results=10)
            companies.extend(results)
            time.sleep(2)
        
        print(f"✓ Found {len(companies)} Engineering Firms")
        return companies
    
    def find_decision_makers(self, company_website: str) -> List[Dict]:
        """
        Find CEO/COO/Owner contact info
        
        Args:
            company_website: Company domain
            
        Returns:
            List of decision-maker contacts
        """
        # Extract domain from URL
        domain = company_website.replace("https://", "").replace("http://", "").split("/")[0]
        
        # Get emails from Hunter.io
        email_data = self.enrich_with_hunter_io(domain)
        
        # Try to identify decision-makers (CEO, COO, Owner, President)
        decision_makers = []
        
        for email in email_data.get("emails", []):
            # Simple heuristic: look for executive titles in email patterns
            if any(title in email.lower() for title in ["ceo", "coo", "owner", "president", "founder"]):
                decision_makers.append({
                    "email": email,
                    "company": email_data.get("organization", ""),
                    "website": company_website
                })
        
        return decision_makers
    
    def export_to_csv(self, filename: str):
        """Export leads to CSV"""
        if not self.leads:
            print("No leads to export!")
            return
        
        with open(filename, 'w', newline='') as f:
            fieldnames = ['company_name', 'website', 'industry', 'email', 'title', 'phone', 'linkedin', 'notes']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            writer.writeheader()
            for lead in self.leads:
                writer.writerow(lead)
        
        print(f"\n✓ Exported {len(self.leads)} leads to {filename}")
    
    def run(self):
        """Main scraping workflow"""
        print("🎯 Starting Consulting Lead Scraper")
        print("=" * 60)
        
        all_companies = []
        
        # Scrape each category
        all_companies.extend([{**c, "industry": "3PL/Logistics"} for c in self.scrape_3pl_logistics()])
        all_companies.extend([{**c, "industry": "Home Services"} for c in self.scrape_home_services()])
        all_companies.extend([{**c, "industry": "Engineering"} for c in self.scrape_engineering_firms()])
        
        print(f"\n📊 Total companies found: {len(all_companies)}")
        print("🔍 Finding decision-maker contacts...")
        
        # Enrich with decision-maker contacts
        for company in all_companies[:20]:  # Limit to 20 for free tier
            if company.get("website"):
                print(f"  → {company.get('company_name')}")
                
                contacts = self.find_decision_makers(company.get("website"))
                
                for contact in contacts:
                    self.leads.append({
                        "company_name": company.get("company_name", ""),
                        "website": company.get("website", ""),
                        "industry": company.get("industry", ""),
                        "email": contact.get("email", ""),
                        "title": "Executive",  # Placeholder
                        "phone": "",  # TODO: Add phone lookup
                        "linkedin": "",  # TODO: Add LinkedIn lookup
                        "notes": company.get("description", "")[:200]
                    })
                
                time.sleep(3)  # Rate limiting for Hunter.io
        
        # Export results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"consulting-leads-{timestamp}.csv"
        self.export_to_csv(filename)
        
        print("\n✅ Scraping complete!")
        print(f"📧 Found {len(self.leads)} decision-maker contacts")
        print(f"💾 Saved to: {filename}")


def main():
    """Run the scraper"""
    scraper = ConsultingLeadScraper()
    scraper.run()


if __name__ == "__main__":
    main()

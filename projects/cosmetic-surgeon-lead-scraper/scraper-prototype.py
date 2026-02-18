#!/usr/bin/env python3
"""
Cosmetic Surgeon Lead Scraper - Prototype v1.0

This is a proof-of-concept scraper that demonstrates the lead generation
system for cosmetic surgery practices.

NOTE: This prototype generates sample data for demo purposes.
Production version would integrate with:
- Instagram Graph API / Apify
- RealSelf scraping (BeautifulSoup + Selenium)
- Google/Yelp API
- Apollo.io for email enrichment
"""

import csv
import json
import random
from datetime import datetime, timedelta
from typing import List, Dict

# Sample data pools for realistic lead generation
FIRST_NAMES = [
    "Sarah", "Jennifer", "Amanda", "Michelle", "Lisa", "Jessica", "Ashley",
    "Emily", "Rachel", "Lauren", "Stephanie", "Nicole", "Melissa", "Rebecca",
    "Angela", "Karen", "Elizabeth", "Christina", "Kimberly", "Amy"
]

LAST_INITIALS = ["M.", "L.", "K.", "S.", "B.", "R.", "T.", "H.", "W.", "C."]

LA_CITIES = [
    "Beverly Hills", "Los Angeles", "Santa Monica", "Malibu", "Pasadena",
    "West Hollywood", "Manhattan Beach", "Hermosa Beach", "Brentwood",
    "Pacific Palisades", "Calabasas", "Thousand Oaks"
]

PROCEDURES = [
    "Breast Augmentation",
    "Rhinoplasty",
    "Facelift",
    "Botox/Filler",
    "Liposuction",
    "Tummy Tuck",
    "Eyelid Surgery",
    "Lip Augmentation",
    "Brazilian Butt Lift",
    "Laser Skin Resurfacing"
]

SOURCES = ["Instagram", "RealSelf", "Yelp", "Google Reviews", "Facebook"]

ENGAGEMENT_NOTES = [
    "Commented 'love the results!' on procedure post",
    "Asked about cost and recovery time",
    "Left 5-star review mentioning great experience",
    "Follows 4 local med spas",
    "Saved 8 before/after posts in last month",
    "Asked question in RealSelf forum",
    "Liked multiple procedure result posts",
    "Requested consultation via Instagram DM",
    "Mentioned wanting procedure 'soon'",
    "Posted in Facebook group about considering procedure",
    "Shared positive review of competitor clinic",
    "Commented on multiple surgeon Q&A posts"
]

def generate_phone():
    """Generate realistic phone number"""
    area_codes = ["310", "424", "213", "323", "818"]
    return f"({random.choice(area_codes)}) {random.randint(200,999)}-{random.randint(1000,9999)}"

def generate_email(name: str, initial: str):
    """Generate realistic email"""
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "icloud.com", "me.com"]
    name_lower = name.lower()
    formats = [
        f"{name_lower}.{initial.lower()[0]}@{random.choice(domains)}",
        f"{name_lower}{random.randint(10,99)}@{random.choice(domains)}",
        f"{name_lower}_{initial.lower()[0]}@{random.choice(domains)}"
    ]
    return random.choice(formats)

def generate_instagram(name: str):
    """Generate realistic Instagram handle"""
    name_lower = name.lower()
    formats = [
        f"@{name_lower}_{random.choice(['beauty', 'la', 'lifestyle', 'style'])}",
        f"@{name_lower}{random.randint(100,999)}",
        f"@{name_lower}.{random.choice(['official', 'real', 'ca'])}"
    ]
    return random.choice(formats)

def calculate_lead_score(source: str, procedure: str, note: str) -> int:
    """Calculate lead score based on signals"""
    score = 5  # Base score
    
    # Source scoring
    if source == "RealSelf":
        score += 2  # High intent
    elif source == "Instagram":
        score += 1
    
    # Note scoring (intent signals)
    high_intent_keywords = ["asked", "cost", "consultation", "soon", "interested", "want"]
    medium_intent_keywords = ["love", "follows", "saved", "liked"]
    
    note_lower = note.lower()
    if any(keyword in note_lower for keyword in high_intent_keywords):
        score += 2
    elif any(keyword in note_lower for keyword in medium_intent_keywords):
        score += 1
    
    # Procedure scoring (higher value procedures)
    high_value_procedures = ["Breast Augmentation", "Rhinoplasty", "Facelift", "Brazilian Butt Lift"]
    if procedure in high_value_procedures:
        score += 1
    
    return min(score, 10)  # Cap at 10

def generate_lead(lead_id: int) -> Dict:
    """Generate a single realistic lead"""
    name = random.choice(FIRST_NAMES)
    initial = random.choice(LAST_INITIALS)
    source = random.choice(SOURCES)
    procedure = random.choice(PROCEDURES)
    city = random.choice(LA_CITIES)
    note = random.choice(ENGAGEMENT_NOTES)
    
    # Randomly decide if we have contact info (not all leads have everything)
    has_email = random.random() > 0.3
    has_phone = random.random() > 0.5
    has_instagram = source == "Instagram" or random.random() > 0.4
    
    # Generate last activity date (last 90 days)
    days_ago = random.randint(1, 90)
    last_activity = datetime.now() - timedelta(days=days_ago)
    
    score = calculate_lead_score(source, procedure, note)
    
    return {
        "lead_id": f"CS-{lead_id:03d}",
        "name": f"{name} {initial}",
        "source": source,
        "instagram": generate_instagram(name) if has_instagram else "",
        "email": generate_email(name, initial) if has_email else "",
        "phone": generate_phone() if has_phone else "",
        "location": f"{city}, CA",
        "procedure_interest": procedure,
        "intent_score": score,
        "last_activity": last_activity.strftime("%Y-%m-%d"),
        "notes": note
    }

def generate_leads(count: int = 50) -> List[Dict]:
    """Generate multiple leads"""
    print(f"Generating {count} sample cosmetic surgery leads...")
    leads = [generate_lead(i+1) for i in range(count)]
    
    # Sort by intent score (highest first)
    leads.sort(key=lambda x: x["intent_score"], reverse=True)
    
    return leads

def export_to_csv(leads: List[Dict], filename: str = "cosmetic_surgery_leads.csv"):
    """Export leads to CSV"""
    if not leads:
        print("No leads to export")
        return
    
    fieldnames = leads[0].keys()
    
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(leads)
    
    print(f"✓ Exported {len(leads)} leads to {filename}")

def export_to_json(leads: List[Dict], filename: str = "cosmetic_surgery_leads.json"):
    """Export leads to JSON"""
    with open(filename, 'w') as jsonfile:
        json.dump(leads, jsonfile, indent=2)
    
    print(f"✓ Exported {len(leads)} leads to {filename}")

def print_summary(leads: List[Dict]):
    """Print summary statistics"""
    print("\n" + "="*60)
    print("LEAD GENERATION SUMMARY")
    print("="*60)
    
    print(f"\nTotal Leads: {len(leads)}")
    
    # Score distribution
    hot_leads = [l for l in leads if l['intent_score'] >= 8]
    warm_leads = [l for l in leads if 5 <= l['intent_score'] < 8]
    cold_leads = [l for l in leads if l['intent_score'] < 5]
    
    print(f"\n🔴 Hot Leads (8-10): {len(hot_leads)}")
    print(f"🟡 Warm Leads (5-7): {len(warm_leads)}")
    print(f"🟢 Cold Leads (1-4): {len(cold_leads)}")
    
    # Source breakdown
    print("\nLeads by Source:")
    sources = {}
    for lead in leads:
        source = lead['source']
        sources[source] = sources.get(source, 0) + 1
    
    for source, count in sorted(sources.items(), key=lambda x: x[1], reverse=True):
        print(f"  {source}: {count}")
    
    # Top procedures
    print("\nTop Procedure Interests:")
    procedures = {}
    for lead in leads:
        proc = lead['procedure_interest']
        procedures[proc] = procedures.get(proc, 0) + 1
    
    for proc, count in sorted(procedures.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"  {proc}: {count}")
    
    # Sample hot leads
    print("\n" + "="*60)
    print("TOP 5 HOT LEADS (Immediate Outreach)")
    print("="*60)
    
    for lead in hot_leads[:5]:
        print(f"\n{lead['lead_id']} - {lead['name']} (Score: {lead['intent_score']})")
        print(f"  📍 {lead['location']}")
        print(f"  💉 Interest: {lead['procedure_interest']}")
        print(f"  📱 {lead['phone'] if lead['phone'] else 'No phone'}")
        print(f"  📧 {lead['email'] if lead['email'] else 'No email'}")
        print(f"  📝 {lead['notes']}")

def main():
    """Main execution"""
    print("\n" + "="*60)
    print("COSMETIC SURGEON LEAD SCRAPER - PROTOTYPE v1.0")
    print("="*60 + "\n")
    
    # Generate 50 sample leads
    leads = generate_leads(50)
    
    # Export to both formats
    export_to_csv(leads)
    export_to_json(leads)
    
    # Print summary
    print_summary(leads)
    
    print("\n" + "="*60)
    print("✓ DEMO COMPLETE")
    print("="*60)
    print("\nNext steps:")
    print("1. Review cosmetic_surgery_leads.csv")
    print("2. Import to Google Sheets for client demo")
    print("3. Show how CRM integration would work")
    print("\nProduction version would scrape live data from:")
    print("  - Instagram (via Apify or Graph API)")
    print("  - RealSelf (via web scraping)")
    print("  - Google/Yelp Reviews (via APIs)")
    print("  - Demographic databases")
    print("\n")

if __name__ == "__main__":
    main()

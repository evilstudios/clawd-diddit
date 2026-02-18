#!/usr/bin/env python3
"""
Philadelphia Med Spa & Cosmetic Surgery Lead Scraper - Prototype v1.0

Generates sample leads for Philadelphia area (40-mile radius) including:
- Cosmetic surgeons
- Med spas offering Botox, CoolSculpting, fillers, etc.

NOTE: This prototype generates sample data for demo purposes.
Production version would integrate with live APIs/scraping.
"""

import csv
import json
import random
from datetime import datetime, timedelta
from typing import List, Dict

# Philadelphia area cities (40-mile radius)
PHILLY_CITIES = [
    "Philadelphia", "Center City", "Society Hill", "Rittenhouse Square",
    "Chestnut Hill", "Manayunk", "Old City", "University City",
    "Bryn Mawr", "Wayne", "Ardmore", "Radnor", "Villanova",
    "King of Prussia", "Conshohocken", "Blue Bell", "Fort Washington",
    "Cherry Hill, NJ", "Haddonfield, NJ", "Moorestown, NJ",
    "Wilmington, DE", "Media", "Newtown Square", "West Chester"
]

FIRST_NAMES = [
    "Sarah", "Jennifer", "Amanda", "Michelle", "Lisa", "Jessica", "Ashley",
    "Emily", "Rachel", "Lauren", "Stephanie", "Nicole", "Melissa", "Rebecca",
    "Angela", "Karen", "Elizabeth", "Christina", "Kimberly", "Amy",
    "Heather", "Danielle", "Brittany", "Courtney", "Samantha"
]

LAST_INITIALS = ["M.", "L.", "K.", "S.", "B.", "R.", "T.", "H.", "W.", "C.", "D.", "P.", "F."]

# Med Spa & Cosmetic Surgery Procedures
PROCEDURES = [
    # Injectable Treatments
    "Botox",
    "Dysport",
    "Jeuveau (Newtox)",
    "Dermal Fillers (Juvederm)",
    "Lip Fillers",
    "Restylane",
    "Sculptra",
    "Kybella (Double Chin)",
    
    # Body Contouring
    "CoolSculpting",
    "EmSculpt",
    "SculpSure",
    "Liposuction",
    "Tummy Tuck",
    "Brazilian Butt Lift",
    
    # Skin Treatments
    "Laser Hair Removal",
    "Laser Skin Resurfacing",
    "Chemical Peels",
    "Microneedling",
    "HydraFacial",
    "IPL Photofacial",
    "RF Microneedling (Morpheus8)",
    
    # Surgical Procedures
    "Breast Augmentation",
    "Rhinoplasty",
    "Facelift",
    "Eyelid Surgery",
    "Mommy Makeover"
]

SOURCES = ["Instagram", "RealSelf", "Yelp", "Google Reviews", "Facebook", "TikTok"]

ENGAGEMENT_NOTES = [
    "Asked about Botox pricing in DMs",
    "Commented 'need this!' on CoolSculpting before/after",
    "Left 5-star review for med spa",
    "Follows 6 local med spas",
    "Saved multiple filler result posts",
    "Asked about CoolSculpting consultation",
    "Liked every laser hair removal post",
    "Requested pricing via Instagram",
    "Mentioned wanting treatment 'before summer'",
    "Posted in Facebook group about considering procedure",
    "Shared positive review of competitor",
    "Commented on Q&A about recovery time",
    "Asked 'does this hurt?' on procedure video",
    "Tagged 3 friends in before/after post",
    "Requested consultation via website form",
    "Called asking about same-day appointments",
    "Watched full YouTube consultation video",
    "Clicked 'Book Now' but didn't complete",
    "Asked about financing options",
    "Mentioned wanting subtle, natural results"
]

def generate_phone():
    """Generate realistic Philadelphia area phone"""
    area_codes = ["215", "267", "610", "484", "856"]  # Philly + South Jersey
    return f"({random.choice(area_codes)}) {random.randint(200,999)}-{random.randint(1000,9999)}"

def generate_email(name: str, initial: str):
    """Generate realistic email"""
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "icloud.com", "me.com", "comcast.net"]
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
        f"@{name_lower}_{random.choice(['beauty', 'philly', 'lifestyle', 'style', 'glam'])}",
        f"@{name_lower}{random.randint(100,999)}",
        f"@{name_lower}.{random.choice(['official', 'real', 'pa', 'xo'])}"
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
    elif source == "TikTok":
        score += 1  # Younger, engaged audience
    
    # Note scoring (intent signals)
    high_intent_keywords = ["asked", "pricing", "cost", "consultation", "before summer", "book", "appointment", "financing"]
    medium_intent_keywords = ["love", "need this", "follows", "saved", "liked"]
    
    note_lower = note.lower()
    if any(keyword in note_lower for keyword in high_intent_keywords):
        score += 2
    elif any(keyword in note_lower for keyword in medium_intent_keywords):
        score += 1
    
    # Procedure scoring (higher urgency/value procedures)
    high_urgency = ["Botox", "Dermal Fillers", "Lip Fillers", "CoolSculpting", "Kybella"]
    high_value = ["Breast Augmentation", "Rhinoplasty", "Facelift", "Mommy Makeover", "Brazilian Butt Lift"]
    
    if procedure in high_urgency:
        score += 1
    if procedure in high_value:
        score += 2
    
    return min(score, 10)  # Cap at 10

def generate_lead(lead_id: int) -> Dict:
    """Generate a single realistic lead"""
    name = random.choice(FIRST_NAMES)
    initial = random.choice(LAST_INITIALS)
    source = random.choice(SOURCES)
    procedure = random.choice(PROCEDURES)
    city = random.choice(PHILLY_CITIES)
    note = random.choice(ENGAGEMENT_NOTES)
    
    # Randomly decide if we have contact info
    has_email = random.random() > 0.25
    has_phone = random.random() > 0.45
    has_instagram = source in ["Instagram", "TikTok"] or random.random() > 0.4
    
    # Generate last activity date (last 90 days)
    days_ago = random.randint(1, 90)
    last_activity = datetime.now() - timedelta(days=days_ago)
    
    score = calculate_lead_score(source, procedure, note)
    
    return {
        "lead_id": f"PHI-{lead_id:03d}",
        "name": f"{name} {initial}",
        "source": source,
        "instagram": generate_instagram(name) if has_instagram else "",
        "email": generate_email(name, initial) if has_email else "",
        "phone": generate_phone() if has_phone else "",
        "location": city,
        "procedure_interest": procedure,
        "intent_score": score,
        "last_activity": last_activity.strftime("%Y-%m-%d"),
        "notes": note
    }

def generate_leads(count: int = 75) -> List[Dict]:
    """Generate multiple leads"""
    print(f"Generating {count} sample Philadelphia area med spa/cosmetic surgery leads...")
    leads = [generate_lead(i+1) for i in range(count)]
    
    # Sort by intent score (highest first)
    leads.sort(key=lambda x: x["intent_score"], reverse=True)
    
    return leads

def export_to_csv(leads: List[Dict], filename: str = "philadelphia_medspa_leads.csv"):
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

def export_to_json(leads: List[Dict], filename: str = "philadelphia_medspa_leads.json"):
    """Export leads to JSON"""
    with open(filename, 'w') as jsonfile:
        json.dump(leads, jsonfile, indent=2)
    
    print(f"✓ Exported {len(leads)} leads to {filename}")

def print_summary(leads: List[Dict]):
    """Print summary statistics"""
    print("\n" + "="*60)
    print("PHILADELPHIA MED SPA LEAD GENERATION SUMMARY")
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
    
    for proc, count in sorted(procedures.items(), key=lambda x: x[1], reverse=True)[:10]:
        print(f"  {proc}: {count}")
    
    # Location breakdown
    print("\nTop Locations:")
    locations = {}
    for lead in leads:
        loc = lead['location']
        locations[loc] = locations.get(loc, 0) + 1
    
    for loc, count in sorted(locations.items(), key=lambda x: x[1], reverse=True)[:8]:
        print(f"  {loc}: {count}")
    
    # Sample hot leads
    print("\n" + "="*60)
    print("TOP 10 HOT LEADS (Immediate Outreach)")
    print("="*60)
    
    for lead in hot_leads[:10]:
        print(f"\n{lead['lead_id']} - {lead['name']} (Score: {lead['intent_score']})")
        print(f"  📍 {lead['location']}")
        print(f"  💉 Interest: {lead['procedure_interest']}")
        print(f"  📱 {lead['phone'] if lead['phone'] else 'No phone'}")
        print(f"  📧 {lead['email'] if lead['email'] else 'No email'}")
        print(f"  📝 {lead['notes']}")

def main():
    """Main execution"""
    print("\n" + "="*60)
    print("PHILADELPHIA MED SPA LEAD SCRAPER - PROTOTYPE v1.0")
    print("Coverage: Philadelphia + 40-mile radius")
    print("="*60 + "\n")
    
    # Generate 75 sample leads
    leads = generate_leads(75)
    
    # Export to both formats
    export_to_csv(leads)
    export_to_json(leads)
    
    # Print summary
    print_summary(leads)
    
    print("\n" + "="*60)
    print("✓ DEMO COMPLETE")
    print("="*60)
    print("\nNext steps:")
    print("1. Review philadelphia_medspa_leads.csv")
    print("2. Import to Google Sheets for client demo")
    print("3. Show how targeting works for local market")
    print("\nProduction version would scrape live data from:")
    print("  - Instagram (via Apify or Graph API)")
    print("  - RealSelf (via web scraping)")
    print("  - Google/Yelp Reviews (via APIs)")
    print("  - TikTok (beauty/aesthetic content)")
    print("  - Local demographic databases")
    print("\n")

if __name__ == "__main__":
    main()

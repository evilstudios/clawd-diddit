#!/usr/bin/env python3
"""
Evil Apples Facebook Auto-Poster
Posts random card combos 3x per week at optimal times
"""

import requests
import random
from datetime import datetime

# Facebook credentials
ACCESS_TOKEN = "EAARWzoIjLNMBQkwARGHZA8ZAcfxiThpJYMswdyuI5msYnYmueqoqaZB1GiR9IiKkZBHpZAuztZBH1EwHMcHR7ZBMJvZCMKUVZCav9xGYk3LuK8TBlqCT7iI6egC8lZAZBbg3ItolYazOSlbwaglV55BejtwRm7uDNuZAIWO1UJnbBGaAl99TVkb0AHZCeoeZAxSmfWpcjkbNfLl3vAzst3MIregvFf"
PAGE_ID = "127527677435319"

# Prompt cards
PROMPTS = [
    "Netflix just released a documentary titled \"The Dark Side of __________.\"",
    "My Uber driver was great, until he started talking about __________.",
    "The real reason the Wi-Fi is down is actually __________.",
    "I'm not saying I'm rich, but I do use __________ as toilet paper.",
    "In a shocking twist, the next Marvel superhero's only power is __________.",
    "Most people go to Vegas for the gambling, but I go for the __________.",
    "What's the newest TikTok trend that's sending Gen Z to the ER?",
    "My dating profile says I'm \"outdoorsy,\" but it really means I enjoy __________.",
    "For only $9.99 a month, you can subscribe to my OnlyFans for exclusive content of __________.",
    "The secret to a long, happy marriage is a healthy dose of __________.",
    "I'm sorry, Officer, I didn't know it was illegal to possess __________.",
    "What's the last thing you want to find in your kid's Trick-or-Treat bag?",
    "During the apocalypse, the new global currency will be __________.",
    "My therapist says I need to find a healthier outlet for my __________.",
    "Forget the 10 Commandments. The 11th Commandment is \"Thou shalt not __________.\"",
    "Heaven is great and all, but it's seriously lacking __________.",
    "I didn't lose my job; I was \"professionally liberated\" due to __________.",
    "What's that smell? It's a mix of wet dog and __________.",
    "Kids, I'm going to tell you a story. It's the story of how I lost my finger to __________.",
    "The autopsy report was inconclusive, but it definitely involved __________.",
    "Nothing says \"I love you\" like a gift-wrapped __________.",
    "I'm not crying, I just have __________ in my eye.",
    "The worst thing to say during a eulogy is \"At least they finally got __________.\"",
    "My grandmother's secret ingredient in her famous cookies is __________.",
    "\"Honey, we need to talk. I think our son is addicted to __________.\"",
    "First date tip: Always bring __________ just in case things get weird.",
    "_________ is why I'm sticky.",
    "I get a weird sense of satisfaction from __________.",
    "If you look up \"regret\" in the dictionary, you'll see a picture of __________.",
    "__________ the most inappropriate thing to bring to a baby shower.",
    "My LinkedIn bio used to say \"Thought Leader,\" but now it just says \"__________ Enthusiast.\"",
    "The HR department had a meltdown today after discovering __________ in the breakroom.",
    "My boss called me into his office to discuss my inappropriate use of __________.",
    "During my performance review, I was told I need to work on my __________.",
    "The key to successful networking is a firm handshake and a pocket full of __________.",
    "I'm not saying I'm a workaholic, but I did bring __________ to my cousin's wedding.",
    "The company retreat was going great until we started the team-building exercise involving __________.",
    "I didn't get the promotion because I'm \"too focused on __________.\"",
    "\"Does this count as a tax write-off?\" I asked, while holding __________.",
    "The secret to surviving a Monday morning is a double espresso and __________.",
    "My ex-boyfriend's biggest red flag was definitely his obsession with __________.",
    "\"It's not you, it's __________.\"",
    "Nothing ruins a first kiss like the taste of __________.",
    "I knew we were soulmates when I saw your collection of __________.",
    "My Tinder bio is just a high-res photo of __________.",
    "\"Will you marry me?\" \"Only if we can have __________ at the reception.\"",
    "I tried to be \"spontaneous\" in the bedroom, but it just resulted in __________.",
    "The most romantic thing a man can do is buy me __________.",
    "We broke up because he refused to stop __________ in public.",
    "My dream wedding involves a chocolate fountain filled with __________.",
    "\"Mom, where do babies come from?\" \"Well, honey, when a man and a woman love __________ very much...\"",
    "I'm writing a memoir called \"Growing Up with __________.\"",
    "The worst part of being an adult is having to pay for your own __________.",
    "My parents didn't believe in \"time-outs\"; they preferred __________.",
    "My childhood imaginary friend was actually just __________.",
    "I'm not saying my family is weird, but our Thanksgiving tradition involves __________.",
    "The most embarrassing thing my mom ever caught me doing was __________.",
    "\"And this is the room where we keep __________,\" said the creepy tour guide.",
    "I was banned from the PTA for suggesting __________ as a fundraiser.",
    "___________ is the real reason Grandpa isn't allowed at the zoo anymore.",
    "I'm currently \"ghosting\" my responsibilities to focus on __________.",
    "The latest iPhone update includes a controversial feature that tracks your __________.",
    "My targeted ads are getting weirdly specific. Today I saw an ad for __________.",
    "I accidentally sent a screenshot of __________ to the group chat.",
    "The Metaverse is basically just a virtual world where you can experience __________.",
    "I'm starting a podcast dedicated entirely to the history of __________.",
    "My \"Screen Time\" report says I spent 14 hours this week looking at __________.",
    "I tried to \"unplug\" from technology, but I realized I can't live without __________.",
    "The most liked photo on Instagram is currently a picture of __________.",
    "My AI assistant is becoming sentient and keeps demanding __________.",
    "___________ is the one thing you should never bring to a knife fight.",
    "I'm not a doctor, but I'm pretty sure __________ is the cure for everything.",
    "The newest Olympic sport is actually just __________.",
    "My spirit animal is __________.",
    "The secret ingredient in the local diner's \"Mystery Meat\" is definitely __________.",
    "I have a 5-step plan to take over the world using only __________.",
    "What's the first thing you'd buy if you won the lottery and lost your mind?",
    "I'm allergic to peanuts, shellfish, and __________.",
    "\"Trust me, I've done this before,\" I said, as I grabbed __________.",
    "The four horsemen of the apocalypse: War, Famine, Pestilence, and __________.",
    "My \"prepper\" bunker is stocked with 500 gallons of __________.",
    "If the world ends tomorrow, I'm spending my last hour __________.",
    "The aliens finally landed, and their first words were \"Take us to __________.\"",
    "Who knew the zombie apocalypse would be started by __________?",
    "My post-apocalyptic nickname is \"The Sultan of __________.\"",
    "In the new world order, the most powerful person is whoever owns __________.",
    "I'm not saying I'm the Antichrist, but I do enjoy __________.",
    "The last remaining human on Earth spent their final moments __________.",
    "________ is the true meaning of life."
]

# Answer cards
ANSWERS = [
    "flight attendant lap dances", "airplane restroom gloryhole", "licking tray tables",
    "duty-free lube", "cockpit dutch oven", "farting on a greyhound bus",
    "The Bipolar Express", "Cannibal Cruise Line buffet", "truck stop love",
    "STDs on the Love Boat", "Boner-cycle", "airline pilots tripping on acid",
    "zombie TSA agents", "bus station blowjobs", "Cocaine Train",
    "cruise ship cougars", "A colonoscopy sundae", "The Big Booty brigade",
    "drinking Whoopi Goldberg's dirty bath water", "A smegma soufflé",
    "Golden showers by The Golden Girls", "A hand job in a hot tub",
    "a clown hooker bordello", "Masturbating to 'The Walking Dead'",
    "Butt plugs and crumpets", "Grandma's nipple clamp collection",
    "A hot sauce rim job", "A nursing home orgy", "a virtual reality hand job",
    "Bill Gates' pocket pussy collection", "a time travel orgy",
    "a cyborg lap dance", "a hard drive, a very hard drive",
    "a glass of wine, bottle of lube, and ChatGPT", "dildos by delivery drone",
    "an army of robot hookers", "Oppenheimer's tighty-whities",
    "Einstein, Darwin, and a bottle of Viagra", "A stupid smartphone",
    "light bulbs and gerbils", "an electronic butt sex doll",
    "pansexual travel agents", "A three way with Kim Jong Un",
    "Sasquatch hookers on ecstasy", "Mom's sex robot fantasy",
    "a programmable penis", "f*ckin' Control ALT Delete",
    "Sir Isaac Newton's \"apple juice\"", "a solar-powered enema"
]

def get_page_token():
    """Get page access token"""
    response = requests.get(
        "https://graph.facebook.com/v19.0/me/accounts",
        params={"access_token": ACCESS_TOKEN}
    )
    if response.status_code == 200:
        pages = response.json().get('data', [])
        if pages:
            return pages[0]['access_token']
    return None

def generate_post():
    """Generate random Evil Apples card combo"""
    prompt = random.choice(PROMPTS)
    answer_a = random.choice(ANSWERS)
    answer_b = random.choice([a for a in ANSWERS if a != answer_a])
    
    post = f"""{prompt}

A) {answer_a}
B) {answer_b}

Vote for the funniest answer! Drop A or B in the comments 👇

Download Evil Apples:
🔗 https://www.evilapples.com

#EvilApples #CardGame #DarkHumor #GameNight #VoteNow"""
    
    return post

def post_to_facebook(message):
    """Post message to Facebook page"""
    # ACCESS_TOKEN is already the page token
    response = requests.post(
        f"https://graph.facebook.com/v19.0/{PAGE_ID}/feed",
        data={
            "message": message,
            "access_token": ACCESS_TOKEN
        }
    )
    
    if response.status_code == 200:
        post_id = response.json().get('id')
        return {"success": True, "post_id": post_id}
    else:
        return {"success": False, "error": response.text}

def main():
    """Main posting function"""
    print("🍎 EVIL APPLES AUTO-POSTER")
    print("=" * 70)
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Generate post
    post_content = generate_post()
    print("📝 Generated Post:")
    print("-" * 70)
    print(post_content)
    print("-" * 70)
    
    # Post to Facebook
    print("\n📤 Posting to Facebook...")
    result = post_to_facebook(post_content)
    
    if result["success"]:
        print(f"✅ SUCCESS! Post ID: {result['post_id']}")
        print(f"🔗 View: https://www.facebook.com/{PAGE_ID}")
    else:
        print(f"❌ ERROR: {result.get('error', 'Unknown error')}")
    
    print("\n" + "=" * 70)

if __name__ == "__main__":
    main()

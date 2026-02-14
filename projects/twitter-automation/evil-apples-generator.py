#!/usr/bin/env python3
"""
Evil Apples Content Generator
Generate random prompt + answer combos from Evil Apples card database
"""

import random
import sys

# Evil Apples Prompts (from TOOLS.md)
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
]

# Evil Apples Answers (sample from TOOLS.md)
ANSWERS = [
    "flight attendant lap dances",
    "airplane restroom gloryhole",
    "licking tray tables",
    "duty-free lube",
    "cockpit dutch oven",
    "naked on a hot air balloon",
    "farting on a greyhound bus",
    "The Bipolar Express",
    "truck stop love",
    "STDs on the Love Boat",
    "a train ride through the Toberlerone tunnel",
    "Boner-cycle",
    "airline pilots tripping on acid",
    "zombie TSA agents",
    "a helicopter ride to Temptation Island",
    "watersports on the cruise ship poop deck",
    "a plane full of rabid weasels",
    "bus station blowjobs",
    "flying first class on Cunnilingus Airlines",
    "driving to Humptulips, Washington",
    "a SpaceX flight on Ecstasy",
    "bicycling with hemorrhoids",
    "Cocaine Train",
    "pansexual travel agents",
    "dropping a deuce in a motorcoach bathroom",
    "an orgy on the Orient Express",
    "joining the 'Mile High Club' alone",
    "cruise ship cougars",
    "The Captain Kirk circle jerk",
    "A colonoscopy sundae",
    "Slurping a Sticky Ricky",
    "The Big Booty brigade",
    "A jizz and tonic, shaken, not stirred",
    "drinking Whoopi Goldberg's dirty bath water",
    "A sack of stretchy vaginas",
    "A smegma soufflé",
    "A gray pube omelet",
    "Golden showers by The Golden Girls",
    "A jug of Beyoncé's booty sweat",
    "A platter of weeping penises",
    "Two nuns, one cup",
    "A hand job in a hot tub",
    "A three way with Kim Jong Un",
    "a clown hooker bordello",
    "Your mama's favorite dildo",
    "Masturbating to 'The Walking Dead'",
    "Butt plugs and crumpets",
    "A dopplebanger",
    "An old-fashioned zombie mask",
    "Grandma's nipple clamp collection",
    "Sasquatch hookers on ecstasy",
    "A hot sauce rim job",
    "A thrift store pocket pussy",
    "A nursing home orgy",
    "A hermit crab hand job",
    "Snatchchatting",
    "Mom's sex robot fantasy",
    "Dad's sex robot fantasy",
    "Grandpa's sex robot fantasy",
    "a virtual reality hand job",
    "Arti-f*kin-ficial Intelligence",
    "Bill Gates' pocket pussy collection",
    "The IT bitty titty committee",
    "a time travel orgy",
    "a programmable penis",
    "virtual reality vaginas",
    "a cyborg lap dance",
    "an anal sex algorithm",
    "a hard drive, a very hard drive",
    "a database of d1ck pics",
    "a cloud-based porn collection",
    "cybersex on a public library computer",
    "dildos by delivery drone",
    "a Taylor Swift robot",
    "f*ckin' Control ALT Delete",
    "a Pornhub computer course",
    "an army of robot hookers",
]


def generate_combo():
    """Generate a random prompt + 2 answer combo"""
    prompt = random.choice(PROMPTS)
    answers = random.sample(ANSWERS, 2)
    
    return {
        "prompt": prompt,
        "answer_a": answers[0],
        "answer_b": answers[1]
    }


def format_tweet(combo, include_cta=True):
    """Format combo as a tweet"""
    tweet = f"**{combo['prompt']}**\n\n"
    tweet += f"A) {combo['answer_a']}\n"
    tweet += f"B) {combo['answer_b']}\n"
    
    if include_cta:
        tweet += "\nWhich is funnier? 😈🍎\n\nPlay Evil Apples: evilapples.com"
    
    return tweet


def format_for_twitter(combo, include_cta=True):
    """Format combo for actual Twitter posting (no markdown bold)"""
    tweet = f"{combo['prompt']}\n\n"
    tweet += f"A) {combo['answer_a']}\n"
    tweet += f"B) {combo['answer_b']}\n"
    
    if include_cta:
        tweet += "\n🤔 Which is funnier? Vote below!\n\n😈 Play Evil Apples: evilapples.com"
    
    return tweet


def main():
    import argparse
    import json
    
    parser = argparse.ArgumentParser(description="Generate Evil Apples content")
    parser.add_argument("--count", type=int, default=1,
                        help="Number of combos to generate")
    parser.add_argument("--no-cta", action="store_true",
                        help="Skip call-to-action")
    parser.add_argument("--twitter-format", action="store_true",
                        help="Format for Twitter (no markdown)")
    parser.add_argument("--json", action="store_true",
                        help="Output JSON")
    
    args = parser.parse_args()
    
    combos = [generate_combo() for _ in range(args.count)]
    
    if args.json:
        print(json.dumps(combos, indent=2))
    else:
        for i, combo in enumerate(combos, 1):
            if args.count > 1:
                print(f"\n{'='*70}")
                print(f"Combo {i}")
                print('='*70)
            
            if args.twitter_format:
                print(format_for_twitter(combo, not args.no_cta))
            else:
                print(format_tweet(combo, not args.no_cta))
            
            if i < len(combos):
                print()


if __name__ == "__main__":
    main()

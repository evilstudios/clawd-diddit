#!/usr/bin/env python3
"""
Social Media Content Generator
Creates engaging posts for Twitter, LinkedIn, Instagram, TikTok
"""

import json
from datetime import datetime, timedelta
from typing import List, Dict

class SocialMediaGenerator:
    """Generate social media content for all products"""
    
    @staticmethod
    def generate_wellplate_posts():
        """Social posts for WellPlate AI"""
        return {
            'twitter': [
                {
                    'text': 'Nutritionist visit: $150\n\nAI nutritionist in your pocket: $9.99/month\n\nSame expert advice, 93% cheaper.\n\nTry WellPlate AI free → [link]',
                    'type': 'value_prop',
                    'hashtags': ['#Nutrition', '#HealthTech', '#AI']
                },
                {
                    'text': 'Stop counting calories manually.\n\nJust take a photo. Our AI does the rest.\n\n7-day free trial 👇',
                    'type': 'feature_highlight',
                },
                {
                    'text': 'Things that cost more than WellPlate AI:\n\n• 2 Starbucks lattes\n• Netflix\n• A single salad at Sweetgreen\n• One nutrition book\n\nBut somehow people think they can\'t afford a nutritionist 🤔',
                    'type': 'objection_handler',
                },
                {
                    'text': 'Your body deserves a meal plan designed FOR YOU.\n\nNot some generic "eat 1,500 calories" BS.\n\nGet a personalized plan in 60 seconds → [link]',
                    'type': 'pain_point',
                },
            ],
            'linkedin': [
                {
                    'text': 'We built an AI nutritionist that costs less than a single consultation.\n\nHere\'s how we did it and what we learned about democratizing health expertise 🧵',
                    'type': 'thought_leadership',
                },
            ],
            'instagram': [
                {
                    'caption': 'POV: You\'re eating healthy without spending 3 hours meal prepping 🥗✨\n\n#HealthyEating #MealPlanning #Nutrition #WellPlateAI',
                    'content_idea': 'Carousel: Before/After of someone\'s meal planning routine',
                    'type': 'lifestyle',
                },
            ],
            'tiktok': [
                {
                    'hook': 'This app reads nutrition labels so you don\'t have to',
                    'content': 'Demo: Scan food with phone, AI instantly shows macros/nutrition',
                    'cta': 'Link in bio',
                    'type': 'feature_demo',
                },
            ],
        }
    
    @staticmethod
    def generate_afoodable_posts():
        """Social posts for Afoodable AI"""
        return {
            'twitter': [
                {
                    'text': 'You\'re throwing away $125/month in food.\n\nAfoodable costs $7.99/month.\n\nDo the math 📊',
                    'type': 'roi_focused',
                },
                {
                    'text': 'Random ingredients in your fridge:\n• Half an onion\n• 2 eggs\n• Random vegetables\n• Leftover rice\n\nAfoodable AI: "Here\'s 5 delicious recipes you can make right now"\n\nThis is the future.',
                    'type': 'feature_demo',
                },
                {
                    'text': 'The guilt of throwing away food is real.\n\nWe built an app that helps you actually USE everything you buy.\n\nTry it free → [link]',
                    'type': 'emotional',
                },
            ],
            'instagram': [
                {
                    'caption': 'Saved $89 this month by not wasting food 🎉\n\nAfoodable helps you use EVERYTHING in your fridge\n\n#ZeroWaste #SaveMoney #FoodWaste',
                    'content_idea': 'Before/after of fridge organization + monthly savings tracker',
                },
            ],
            'tiktok': [
                {
                    'hook': 'POV: You\'re about to throw away food',
                    'content': '*Opens Afoodable app* *Gets 3 recipe ideas* *Makes delicious dinner*',
                    'sound': 'Trending sound',
                    'type': 'pov',
                },
            ],
        }
    
    @staticmethod
    def generate_wine_monkey_posts():
        """Social posts for Wine Monkey"""
        return {
            'twitter': [
                {
                    'text': 'Wine pairing doesn\'t have to be pretentious.\n\n"What wine goes with pizza?"\n\nWine Monkey: "Chianti or Barbera"\n\nDone. Easy. Delicious.',
                    'type': 'approachable',
                },
                {
                    'text': 'Your phone knows:\n• The weather\n• Your schedule\n• How many steps you took\n\nBut it can\'t tell you what wine to order?\n\nFixed that → [link]',
                    'type': 'problem_solution',
                },
            ],
        }
    
    @staticmethod
    def generate_evil_apples_posts():
        """Social posts for Evil Apples"""
        return {
            'twitter': [
                {
                    'text': 'If Cards Against Humanity and your phone had a baby, it would be Evil Apples.\n\n8,000+ offensive cards. Free to play.\n\nDownload: [link]',
                    'type': 'value_prop',
                },
                {
                    'text': 'Evil Apples drinking game:\n\nTake a shot every time you laugh.\n\n*Disclaimer: You will die*',
                    'type': 'viral/funny',
                },
            ],
            'tiktok': [
                {
                    'hook': 'Playing Evil Apples with my friends and...',
                    'content': '*Shows hilarious card combination* *Everyone loses it*',
                    'type': 'gameplay',
                },
            ],
            'instagram': [
                {
                    'caption': 'Game night but make it FILTHY 🍎\n\n#EvilApples #PartyGames #AdultHumor',
                    'content_idea': 'Friends playing together, reactions',
                },
            ],
        }
    
    @staticmethod
    def generate_content_calendar(days=30):
        """Generate 30-day posting schedule"""
        start_date = datetime.now()
        
        schedule = []
        
        for day in range(days):
            date = start_date + timedelta(days=day)
            
            # Post 3x per day per product (aggressive growth phase)
            schedule.append({
                'date': date.strftime('%Y-%m-%d'),
                'posts': {
                    'wellplate': [
                        {'time': '08:00', 'platform': 'twitter', 'type': 'educational'},
                        {'time': '13:00', 'platform': 'instagram', 'type': 'lifestyle'},
                        {'time': '19:00', 'platform': 'tiktok', 'type': 'feature_demo'},
                    ],
                    'afoodable': [
                        {'time': '09:00', 'platform': 'twitter', 'type': 'value_prop'},
                        {'time': '15:00', 'platform': 'instagram', 'type': 'user_story'},
                    ],
                    'wine_monkey': [
                        {'time': '17:00', 'platform': 'twitter', 'type': 'tip'},
                    ],
                    'evil_apples': [
                        {'time': '12:00', 'platform': 'twitter', 'type': 'viral'},
                        {'time': '20:00', 'platform': 'tiktok', 'type': 'gameplay'},
                    ],
                }
            })
        
        return schedule


def generate_all_social_content():
    """Generate complete social media strategy"""
    gen = SocialMediaGenerator()
    
    return {
        'post_library': {
            'wellplate': gen.generate_wellplate_posts(),
            'afoodable': gen.generate_afoodable_posts(),
            'wine_monkey': gen.generate_wine_monkey_posts(),
            'evil_apples': gen.generate_evil_apples_posts(),
        },
        'content_calendar': gen.generate_content_calendar(30),
        'posting_strategy': {
            'frequency': {
                'twitter': '3x per product per day',
                'instagram': '1-2x per product per day',
                'tiktok': '1x per product per day',
                'linkedin': '3x per week (WellPlate/Afoodable only)',
            },
            'best_times': {
                'twitter': ['8am', '1pm', '7pm'],
                'instagram': ['9am', '3pm', '8pm'],
                'tiktok': ['12pm', '7pm', '9pm'],
            },
            'hashtag_strategy': 'Use 3-5 relevant hashtags on Instagram, 1-2 on Twitter',
            'engagement': 'Respond to all comments within 2 hours',
        },
        'automation_tools': [
            'Buffer or Hootsuite for scheduling',
            'Canva for graphics',
            'CapCut for TikTok editing',
        ]
    }


if __name__ == '__main__':
    print("📱 Generating social media content strategy...\n")
    
    content = generate_all_social_content()
    
    output_file = '/root/clawd/marketing/social_media_strategy.json'
    with open(output_file, 'w') as f:
        json.dump(content, f, indent=2)
    
    print(f"✅ Social media strategy saved to: {output_file}\n")
    
    print("📋 Content Library Summary:")
    for product, platforms in content['post_library'].items():
        total_posts = sum(len(posts) for posts in platforms.values())
        print(f"  {product.upper()}: {total_posts} posts across {len(platforms)} platforms")
    
    print(f"\n📅 30-day content calendar generated")
    print(f"   Total scheduled posts: {len(content['content_calendar']) * 10} (approx)")
    
    print("\n💡 Next steps:")
    print("  1. Set up social media accounts for each product")
    print("  2. Use Buffer/Hootsuite to schedule posts")
    print("  3. Create visual content (graphics, videos)")
    print("  4. Monitor engagement and iterate")

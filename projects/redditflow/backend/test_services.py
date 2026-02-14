#!/usr/bin/env python3
"""
Quick test script for Reddit and AI services
Tests thread discovery and comment generation
"""

import os
import sys
from dotenv import load_dotenv

# Add parent directory to path
sys.path.insert(0, os.path.dirname(__file__))

from services.reddit import RedditService, RedditAccountManager
from services.ai import AIService

load_dotenv()

def test_reddit_discovery():
    """Test Reddit thread discovery"""
    print("\n=== Testing Reddit Thread Discovery ===\n")
    
    reddit = RedditService(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT", "RedditFlow/1.0")
    )
    
    # Test search
    keywords = ["food waste", "restaurant sustainability"]
    subreddits = ["restaurant", "smallbusiness"]
    
    print(f"Searching for: {keywords}")
    print(f"In subreddits: {subreddits}\n")
    
    threads = reddit.discover_threads(
        keywords=keywords,
        subreddits=subreddits,
        time_filter="week",
        limit=5
    )
    
    print(f"Found {len(threads)} threads:\n")
    
    for i, thread in enumerate(threads[:3], 1):
        print(f"{i}. r/{thread['subreddit']}")
        print(f"   Title: {thread['title']}")
        print(f"   Score: {thread['score']} | Comments: {thread['num_comments']}")
        print(f"   URL: {thread['url']}")
        
        # Calculate relevance
        relevance = reddit.calculate_relevance_score(thread, keywords)
        print(f"   Relevance: {relevance:.2f}")
        print()
    
    return threads[0] if threads else None

def test_ai_comment_generation(thread):
    """Test AI comment generation"""
    print("\n=== Testing AI Comment Generation ===\n")
    
    if not thread:
        print("No thread to test with")
        return
    
    ai = AIService(
        anthropic_api_key=os.getenv("ANTHROPIC_API_KEY")
    )
    
    # Test comment generation
    print(f"Generating comment for thread:")
    print(f"Title: {thread['title']}\n")
    
    comment = ai.generate_comment(
        thread_title=thread['title'],
        thread_body=thread.get('selftext', ''),
        subreddit=thread['subreddit'],
        brand_name="Afoodable",
        brand_description="A platform that helps restaurants turn food waste into revenue by connecting them with customers looking for discounted end-of-day meals",
        brand_url="https://afoodable.ai"
    )
    
    if comment:
        print("Generated Comment:")
        print("=" * 60)
        print(comment)
        print("=" * 60)
        print()
        
        # Check quality
        quality = ai.check_comment_quality(comment, "Afoodable")
        print(f"Quality Score: {quality['quality_score']:.2f}")
        print(f"Recommendation: {quality['recommendation']}")
        print()
        
        return comment
    else:
        print("Failed to generate comment")
        return None

def test_relevance_scoring(thread):
    """Test AI relevance scoring"""
    print("\n=== Testing AI Relevance Scoring ===\n")
    
    if not thread:
        print("No thread to test with")
        return
    
    ai = AIService(
        anthropic_api_key=os.getenv("ANTHROPIC_API_KEY")
    )
    
    score = ai.score_thread_relevance(
        thread_title=thread['title'],
        thread_body=thread.get('selftext', ''),
        brand_description="Platform that helps restaurants reduce food waste and recover revenue",
        keywords=["food waste", "restaurant", "sustainability"]
    )
    
    print(f"AI Relevance Score: {score:.2f}")
    print()

def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("RedditFlow Service Tests")
    print("=" * 60)
    
    # Check environment variables
    required_vars = [
        "REDDIT_CLIENT_ID",
        "REDDIT_CLIENT_SECRET",
        "ANTHROPIC_API_KEY"
    ]
    
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print(f"\n❌ Missing environment variables: {', '.join(missing_vars)}")
        print("   Copy .env.example to .env and fill in your credentials")
        return
    
    try:
        # Test Reddit discovery
        thread = test_reddit_discovery()
        
        if thread:
            # Test AI comment generation
            comment = test_ai_comment_generation(thread)
            
            # Test AI relevance scoring
            test_relevance_scoring(thread)
        
        print("\n" + "=" * 60)
        print("✅ All tests completed!")
        print("=" * 60 + "\n")
        
    except Exception as e:
        print(f"\n❌ Error during tests: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

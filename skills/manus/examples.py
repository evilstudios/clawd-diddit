#!/usr/bin/env python3
"""
Examples of using the Manus client for various tasks
"""

import os
from manus_client import ManusClient

# Initialize client
client = ManusClient()


def example_quick_research():
    """Example: Quick research task"""
    print("Example 1: Quick research on 3PL industry...")
    
    result = client.quick_task(
        prompt="Research the top 5 key trends in the 3PL (third-party logistics) industry for 2026. Focus on technology adoption and automation.",
        agent_profile="manus-1.6-lite",
        max_wait=120
    )
    
    print(f"Result:\n{result}\n")


def example_linkedin_scraping():
    """Example: LinkedIn lead generation"""
    print("Example 2: LinkedIn lead scraping...")
    
    # Note: This requires LinkedIn connector to be configured in your Manus account
    result = client.create_task(
        prompt="""Find 10 companies in Pennsylvania that specialize in cold storage logistics.
        
For each company provide:
- Company name
- LinkedIn URL
- Key decision maker (if available)
- Company size
- Brief description

Export as a CSV file.""",
        agent_profile="manus-1.6",
        connectors=["linkedin"],  # Requires connector setup
        wait_for_completion=False  # This will take longer, check URL manually
    )
    
    print(f"Task created: {result['task_url']}")
    print(f"Check status at: {result['task_url']}\n")


def example_competitive_analysis():
    """Example: App store competitive analysis"""
    print("Example 3: Competitive analysis...")
    
    result = client.create_task(
        prompt="""Analyze the game "Cards Against Humanity" on the iOS App Store.

Provide:
1. Current rating and number of reviews
2. Top 5 most common complaints from recent reviews (last 30 days)
3. Top 3 most praised features
4. Any mentions of push notifications or engagement features
5. Recent update history

Format as a structured report.""",
        agent_profile="manus-1.6",
        wait_for_completion=False
    )
    
    print(f"Task created: {result['task_url']}\n")


def example_data_processing():
    """Example: Data cleaning and analysis"""
    print("Example 4: Data processing...")
    
    result = client.quick_task(
        prompt="""Create a Python script that:
1. Generates 100 sample restaurant names
2. Categorizes them by cuisine type (Italian, Mexican, American, Asian, etc.)
3. Exports to CSV with columns: name, cuisine, fake_email, phone

Just show me the script, don't execute it.""",
        agent_profile="manus-1.6-lite",
        max_wait=90
    )
    
    print(f"Result:\n{result}\n")


def example_async_batch():
    """Example: Create multiple tasks asynchronously"""
    print("Example 5: Batch task creation...")
    
    prompts = [
        "What are the top 3 benefits of AI agents?",
        "List 5 ways to improve customer service with automation",
        "Explain the difference between RPA and AI agents in 2 sentences"
    ]
    
    tasks = []
    for prompt in prompts:
        result = client.create_task(
            prompt=prompt,
            agent_profile="manus-1.6-lite",
            wait_for_completion=False
        )
        tasks.append(result)
        print(f"Created task: {result['task_id']}")
    
    print(f"\nCreated {len(tasks)} tasks. Check them manually or poll for completion.\n")


if __name__ == '__main__':
    print("Manus Client Examples\n" + "="*50 + "\n")
    
    # Run quick examples (comment out the slow ones for testing)
    example_quick_research()
    example_data_processing()
    example_async_batch()
    
    # These create tasks but don't wait (check URLs manually)
    # example_linkedin_scraping()
    # example_competitive_analysis()
    
    print("\n" + "="*50)
    print("Examples completed!")

#!/usr/bin/env python3
"""
Diaflow Client - Trigger and manage Diaflow workflows from Python
"""

import requests
import json
from typing import Dict, Any, Optional
from datetime import datetime

class DiaflowClient:
    """Wrapper for triggering Diaflow workflows via webhooks"""
    
    def __init__(self, api_key: str = "sk-7444719b94144c27ae335dea6a628443"):
        self.api_key = api_key
        self.base_url = "https://atlantica.diaflow.app"
        
        # Workflow webhook URLs (populated after workflows are created in UI)
        self.workflows = {
            # Add workflow webhooks here as they're created
            # "lead-scraper": "https://atlantica.diaflow.app/api/webhook/xxxxx",
            # "data-processor": "https://atlantica.diaflow.app/api/webhook/yyyyy",
        }
    
    def trigger_workflow(self, workflow_name: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Trigger a Diaflow workflow by name
        
        Args:
            workflow_name: Name of the workflow (must be registered in self.workflows)
            payload: Data to send to the workflow
            
        Returns:
            Dict with response from Diaflow
        """
        if workflow_name not in self.workflows:
            return {
                "success": False,
                "error": f"Workflow '{workflow_name}' not registered. Available: {list(self.workflows.keys())}"
            }
        
        webhook_url = self.workflows[workflow_name]
        
        try:
            response = requests.post(
                webhook_url,
                json=payload,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.api_key}"
                },
                timeout=60
            )
            
            if response.status_code == 200:
                return {
                    "success": True,
                    "data": response.json() if response.content else None,
                    "workflow": workflow_name,
                    "timestamp": datetime.now().isoformat()
                }
            else:
                return {
                    "success": False,
                    "error": f"HTTP {response.status_code}: {response.text}",
                    "workflow": workflow_name
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "workflow": workflow_name
            }
    
    def register_workflow(self, name: str, webhook_url: str):
        """Register a new workflow webhook"""
        self.workflows[name] = webhook_url
        print(f"✅ Registered workflow: {name}")
        print(f"   Webhook: {webhook_url}")
    
    def list_workflows(self):
        """List all registered workflows"""
        if not self.workflows:
            print("⚠️  No workflows registered yet")
            print("\nTo register a workflow:")
            print("1. Create workflow in Diaflow UI")
            print("2. Add HTTP Trigger node")
            print("3. Copy webhook URL")
            print("4. Call: client.register_workflow('name', 'webhook_url')")
            return
        
        print("📋 Registered Diaflow Workflows:")
        for name, url in self.workflows.items():
            print(f"  - {name}: {url}")


# Example use cases

class LeadScraperWorkflow:
    """Wrapper for lead scraping workflows"""
    
    def __init__(self, client: DiaflowClient):
        self.client = client
    
    def scrape_restaurants(self, city: str, business_type: str = "bakery", limit: int = 50):
        """
        Scrape restaurants from Google Maps
        
        Returns: List of leads with name, email, phone, address
        """
        payload = {
            "city": city,
            "business_type": business_type,
            "limit": limit,
            "include_email": True,
            "include_phone": True
        }
        
        result = self.client.trigger_workflow("restaurant-scraper", payload)
        
        if result.get("success"):
            leads = result.get("data", {}).get("leads", [])
            print(f"✅ Scraped {len(leads)} leads for {business_type} in {city}")
            return leads
        else:
            print(f"❌ Scraping failed: {result.get('error')}")
            return []
    
    def scrape_service_businesses(self, city: str, service_type: str, limit: int = 100):
        """
        Scrape service businesses (plumbers, HVAC, etc.)
        
        Returns: List of leads
        """
        payload = {
            "city": city,
            "service_type": service_type,
            "limit": limit
        }
        
        result = self.client.trigger_workflow("service-business-scraper", payload)
        
        if result.get("success"):
            leads = result.get("data", {}).get("leads", [])
            print(f"✅ Scraped {len(leads)} {service_type} leads in {city}")
            return leads
        else:
            print(f"❌ Scraping failed: {result.get('error')}")
            return []


class DataProcessorWorkflow:
    """Wrapper for data processing workflows"""
    
    def __init__(self, client: DiaflowClient):
        self.client = client
    
    def enrich_leads(self, leads: list):
        """
        Enrich lead data with additional info (social profiles, etc.)
        """
        payload = {
            "leads": leads,
            "enrichments": ["email_verification", "social_profiles", "company_info"]
        }
        
        result = self.client.trigger_workflow("lead-enricher", payload)
        
        if result.get("success"):
            enriched = result.get("data", {}).get("leads", [])
            print(f"✅ Enriched {len(enriched)} leads")
            return enriched
        else:
            print(f"❌ Enrichment failed: {result.get('error')}")
            return leads  # Return original if enrichment fails


# Example usage
def example_usage():
    """Example of how to use Diaflow integration"""
    
    # Initialize client
    client = DiaflowClient()
    
    # Register workflows (do this once, after creating in Diaflow UI)
    # client.register_workflow("restaurant-scraper", "https://atlantica.diaflow.app/api/webhook/XXXXX")
    # client.register_workflow("service-business-scraper", "https://atlantica.diaflow.app/api/webhook/YYYYY")
    
    # List available workflows
    client.list_workflows()
    
    # Use workflow wrappers
    # scraper = LeadScraperWorkflow(client)
    # leads = scraper.scrape_restaurants(city="Austin", business_type="bakery", limit=50)
    
    # Process results
    # processor = DataProcessorWorkflow(client)
    # enriched_leads = processor.enrich_leads(leads)
    
    print("\n💡 Next steps:")
    print("1. Create workflows in Diaflow UI")
    print("2. Register webhook URLs")
    print("3. Start triggering workflows!")


if __name__ == "__main__":
    example_usage()

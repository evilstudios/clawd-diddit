#!/usr/bin/env python3
"""
Manus.im API Client
Wrapper for interacting with Manus AI tasks
"""

import os
import json
import time
import requests
from typing import Optional, Dict, List, Any

class ManusClient:
    """Client for Manus.im API"""
    
    def __init__(self, api_key: Optional[str] = None):
        """Initialize Manus client
        
        Args:
            api_key: Manus API key (or use MANUS_API_KEY env var)
        """
        self.api_key = api_key or os.getenv('MANUS_API_KEY')
        if not self.api_key:
            raise ValueError("Manus API key required (set MANUS_API_KEY or pass api_key)")
        
        self.base_url = "https://api.manus.ai/v1"
        self.headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "API_KEY": self.api_key
        }
    
    def create_task(
        self,
        prompt: str,
        agent_profile: str = "manus-1.6",
        task_mode: Optional[str] = None,
        attachments: Optional[List[Dict]] = None,
        connectors: Optional[List[str]] = None,
        interactive_mode: bool = False,
        project_id: Optional[str] = None,
        wait_for_completion: bool = False,
        poll_interval: int = 5,
        max_wait: int = 300
    ) -> Dict[str, Any]:
        """Create a new Manus task
        
        Args:
            prompt: Task instruction
            agent_profile: manus-1.6 (default), manus-1.6-lite, or manus-1.6-max
            task_mode: chat, adaptive, or agent
            attachments: List of file attachments
            connectors: List of connector IDs to enable
            interactive_mode: Allow Manus to ask follow-up questions
            project_id: Associate with a project
            wait_for_completion: Poll until task completes
            poll_interval: Seconds between polls
            max_wait: Max seconds to wait
        
        Returns:
            Task response dict with task_id, task_title, task_url
        """
        payload = {
            "prompt": prompt,
            "agentProfile": agent_profile
        }
        
        if task_mode:
            payload["taskMode"] = task_mode
        if attachments:
            payload["attachments"] = attachments
        if connectors:
            payload["connectors"] = connectors
        if project_id:
            payload["projectId"] = project_id
        if interactive_mode:
            payload["interactiveMode"] = True
        
        response = requests.post(
            f"{self.base_url}/tasks",
            headers=self.headers,
            json=payload
        )
        response.raise_for_status()
        result = response.json()
        
        if wait_for_completion:
            task_id = result.get('task_id')
            if task_id:
                completed_task = self.wait_for_task(task_id, poll_interval, max_wait)
                result['full_task'] = completed_task
        
        return result
    
    def get_task(self, task_id: str) -> Dict[str, Any]:
        """Get task details by ID
        
        Args:
            task_id: Task ID
        
        Returns:
            Task details dict
        """
        # List recent tasks and find the matching one
        response = requests.get(
            f"{self.base_url}/tasks",
            headers=self.headers,
            params={"limit": 50}
        )
        response.raise_for_status()
        data = response.json()
        
        # Return first matching task
        tasks = data.get('data', [])
        for task in tasks:
            if task.get('id') == task_id:
                return task
        
        return {}
    
    def list_tasks(
        self,
        limit: int = 10,
        status: Optional[str] = None,
        before: Optional[str] = None,
        after: Optional[str] = None
    ) -> Dict[str, Any]:
        """List tasks with optional filters
        
        Args:
            limit: Max tasks to return
            status: Filter by status (pending, in_progress, completed, failed)
            before: Task ID for pagination
            after: Task ID for pagination
        
        Returns:
            List response with tasks
        """
        params = {"limit": limit}
        if status:
            params["status"] = status
        if before:
            params["before"] = before
        if after:
            params["after"] = after
        
        response = requests.get(
            f"{self.base_url}/tasks",
            headers=self.headers,
            params=params
        )
        response.raise_for_status()
        return response.json()
    
    def wait_for_task(
        self,
        task_id: str,
        poll_interval: int = 5,
        max_wait: int = 300
    ) -> Dict[str, Any]:
        """Wait for task to complete
        
        Args:
            task_id: Task ID to wait for
            poll_interval: Seconds between polls
            max_wait: Max seconds to wait
        
        Returns:
            Completed task dict
        
        Raises:
            TimeoutError: If task doesn't complete in max_wait seconds
        """
        start_time = time.time()
        
        while time.time() - start_time < max_wait:
            task = self.get_task(task_id)
            status = task.get('status', 'unknown')
            
            if status in ['completed', 'failed']:
                return task
            
            time.sleep(poll_interval)
        
        raise TimeoutError(f"Task {task_id} did not complete within {max_wait} seconds")
    
    def extract_result(self, task: Dict[str, Any]) -> str:
        """Extract text result from completed task
        
        Args:
            task: Task dict from get_task or wait_for_task
        
        Returns:
            Extracted text result
        """
        output = task.get('output', [])
        result_parts = []
        
        for msg in output:
            if msg.get('role') == 'assistant':
                content = msg.get('content', [])
                for item in content:
                    if item.get('type') == 'output_text':
                        result_parts.append(item.get('text', ''))
        
        return '\n\n'.join(result_parts)
    
    def quick_task(
        self,
        prompt: str,
        agent_profile: str = "manus-1.6",
        max_wait: int = 300
    ) -> str:
        """Create task and wait for text result
        
        Args:
            prompt: Task instruction
            agent_profile: Agent profile to use
            max_wait: Max seconds to wait
        
        Returns:
            Text result from completed task
        """
        result = self.create_task(
            prompt=prompt,
            agent_profile=agent_profile,
            wait_for_completion=True,
            max_wait=max_wait
        )
        
        full_task = result.get('full_task', {})
        return self.extract_result(full_task)


def main():
    """Test the client"""
    client = ManusClient()
    
    print("Testing Manus client...")
    print("\nCreating task...")
    
    result = client.create_task(
        prompt="List 3 benefits of using AI agents in business automation",
        agent_profile="manus-1.6-lite",
        wait_for_completion=True,
        max_wait=60
    )
    
    print(f"\nTask ID: {result.get('task_id')}")
    print(f"Task URL: {result.get('task_url')}")
    
    full_task = result.get('full_task', {})
    if full_task:
        print(f"\nStatus: {full_task.get('status')}")
        print(f"Credit usage: {full_task.get('credit_usage')}")
        
        text_result = client.extract_result(full_task)
        print(f"\nResult:\n{text_result}")


if __name__ == '__main__':
    main()

"""
AI Service - Comment generation and relevance scoring
Uses Claude for natural language generation
"""

import anthropic
import logging
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)


class AIService:
    """
    AI-powered comment generation and analysis
    """
    
    def __init__(self, anthropic_api_key: str):
        self.client = anthropic.Anthropic(api_key=anthropic_api_key)
        self.model = "claude-sonnet-4-20250514"
    
    def generate_comment(
        self,
        thread_title: str,
        thread_body: str,
        subreddit: str,
        brand_name: str,
        brand_description: str,
        brand_url: str,
        top_comments: Optional[List[Dict]] = None,
        subreddit_rules: Optional[List[str]] = None
    ) -> Optional[str]:
        """
        Generate a natural, helpful comment that mentions the brand
        
        Args:
            thread_title: Thread title
            thread_body: Thread content
            subreddit: Subreddit name
            brand_name: User's brand/product name
            brand_description: What the product does
            brand_url: Product website
            top_comments: Existing comments (for context)
            subreddit_rules: Rules to avoid violating
            
        Returns:
            Generated comment text or None if failed
        """
        
        # Build context
        context = f"""You are helping create a helpful, natural Reddit comment.

**Thread Title:** {thread_title}

**Thread Content:**
{thread_body if thread_body else "(No body text)"}

**Subreddit:** r/{subreddit}
"""

        if top_comments:
            context += "\n**Top Comments:**\n"
            for i, comment in enumerate(top_comments[:3], 1):
                context += f"{i}. u/{comment['author']}: {comment['body'][:200]}...\n"
        
        if subreddit_rules:
            context += f"\n**Subreddit Rules to Respect:**\n"
            for rule in subreddit_rules[:5]:
                context += f"- {rule}\n"
        
        # Build prompt
        prompt = f"""{context}

**Your Brand:**
- Name: {brand_name}
- Description: {brand_description}
- URL: {brand_url}

**Task:** Write a genuinely helpful Reddit comment that:
1. Addresses the original post naturally
2. Provides actual value (advice, insights, etc.)
3. Casually mentions {brand_name} if it's relevant
4. Sounds like a real person (not promotional)
5. Respects subreddit rules and culture
6. Is 2-4 paragraphs long

**Important:**
- Don't be salesy or promotional
- Don't force the brand mention if it doesn't fit naturally
- Match the tone of the subreddit (casual vs professional)
- Add value first, mention the brand second
- Use conversational language

Write the comment now (just the comment text, no meta-commentary):"""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1024,
                messages=[{
                    "role": "user",
                    "content": prompt
                }]
            )
            
            comment_text = response.content[0].text.strip()
            
            # Basic quality checks
            if len(comment_text) < 50:
                logger.warning("Generated comment too short, rejecting")
                return None
            
            if comment_text.count(brand_name) > 2:
                logger.warning("Generated comment mentions brand too many times, rejecting")
                return None
            
            logger.info(f"Generated comment ({len(comment_text)} chars)")
            return comment_text
            
        except Exception as e:
            logger.error(f"Error generating comment: {e}")
            return None
    
    def score_thread_relevance(
        self,
        thread_title: str,
        thread_body: str,
        brand_description: str,
        keywords: List[str]
    ) -> float:
        """
        Use AI to score how relevant a thread is to the brand
        
        Returns: Score from 0.0 to 1.0
        """
        
        prompt = f"""Rate how relevant this Reddit thread is to a brand/product.

**Thread Title:** {thread_title}

**Thread Content:**
{thread_body[:500] if thread_body else "(No body text)"}

**Brand/Product:**
{brand_description}

**Target Keywords:**
{', '.join(keywords)}

**Task:** Rate the relevance on a scale of 0-100:
- 0-20: Not relevant at all
- 21-40: Slightly relevant
- 41-60: Moderately relevant
- 61-80: Highly relevant
- 81-100: Perfect fit

Consider:
- Does the thread discuss problems the brand solves?
- Would mentioning the brand be helpful and natural?
- Is the audience a good fit?

Respond with just a number (0-100):"""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=10,
                messages=[{
                    "role": "user",
                    "content": prompt
                }]
            )
            
            score_text = response.content[0].text.strip()
            score = int(score_text)
            
            # Normalize to 0-1
            return min(max(score / 100, 0.0), 1.0)
            
        except Exception as e:
            logger.error(f"Error scoring relevance: {e}")
            return 0.0
    
    def analyze_subreddit_tone(
        self,
        subreddit_name: str,
        subreddit_description: str,
        sample_comments: List[str]
    ) -> Dict:
        """
        Analyze the tone/culture of a subreddit
        
        Returns dict with tone characteristics
        """
        
        comments_text = "\n\n".join([f"- {c[:200]}" for c in sample_comments[:10]])
        
        prompt = f"""Analyze the tone and culture of this subreddit:

**Subreddit:** r/{subreddit_name}

**Description:**
{subreddit_description}

**Sample Comments:**
{comments_text}

**Task:** Describe the subreddit's tone in a few words. Choose from:
- Formal vs Casual
- Technical vs General
- Serious vs Humorous
- Helpful vs Critical
- Professional vs Conversational

Respond with a JSON object:
{{
  "formality": "formal" or "casual",
  "technicality": "technical" or "general",
  "humor": "serious" or "humorous",
  "helpfulness": "helpful" or "critical",
  "professionalism": "professional" or "conversational",
  "guidelines": ["guideline1", "guideline2", "guideline3"]
}}

Where guidelines are 2-3 specific tips for posting in this subreddit."""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=500,
                messages=[{
                    "role": "user",
                    "content": prompt
                }]
            )
            
            import json
            tone_data = json.loads(response.content[0].text.strip())
            
            logger.info(f"Analyzed r/{subreddit_name} tone: {tone_data}")
            return tone_data
            
        except Exception as e:
            logger.error(f"Error analyzing subreddit tone: {e}")
            return {
                "formality": "casual",
                "technicality": "general",
                "humor": "balanced",
                "helpfulness": "helpful",
                "professionalism": "conversational",
                "guidelines": ["Be helpful", "Add value", "Don't spam"]
            }
    
    def check_comment_quality(
        self,
        comment_text: str,
        brand_name: str
    ) -> Dict:
        """
        Check if a comment is high quality and not spammy
        
        Returns dict with quality assessment
        """
        
        checks = {
            "is_too_short": len(comment_text) < 50,
            "is_too_promotional": comment_text.lower().count(brand_name.lower()) > 2,
            "has_spam_words": any(word in comment_text.lower() for word in [
                "click here", "sign up now", "limited time", "act now", "buy now"
            ]),
            "is_all_caps": comment_text.isupper(),
            "has_excessive_links": comment_text.count("http") > 2
        }
        
        # Calculate quality score
        quality_score = 1.0
        if checks["is_too_short"]:
            quality_score -= 0.3
        if checks["is_too_promotional"]:
            quality_score -= 0.4
        if checks["has_spam_words"]:
            quality_score -= 0.2
        if checks["is_all_caps"]:
            quality_score -= 0.3
        if checks["has_excessive_links"]:
            quality_score -= 0.2
        
        quality_score = max(quality_score, 0.0)
        
        return {
            "quality_score": quality_score,
            "is_acceptable": quality_score >= 0.6,
            "checks": checks,
            "recommendation": "approved" if quality_score >= 0.6 else "rejected"
        }

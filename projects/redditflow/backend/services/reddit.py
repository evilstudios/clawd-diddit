"""
Reddit Service - Core Reddit API integration
Handles thread discovery, comment posting, account management
"""

import praw
import time
import random
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)


class RedditService:
    """
    Reddit API service using PRAW
    """
    
    def __init__(self, client_id: str, client_secret: str, user_agent: str):
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent
        )
        logger.info("Reddit service initialized (read-only mode)")
    
    def discover_threads(
        self,
        keywords: List[str],
        subreddits: List[str],
        time_filter: str = "day",
        limit: int = 50
    ) -> List[Dict]:
        """
        Discover relevant threads based on keywords and subreddits
        
        Args:
            keywords: List of keywords to search for
            subreddits: List of subreddit names
            time_filter: "hour", "day", "week", "month", "year", "all"
            limit: Max threads to return
            
        Returns:
            List of thread dictionaries with metadata
        """
        discovered_threads = []
        
        for subreddit_name in subreddits:
            try:
                subreddit = self.reddit.subreddit(subreddit_name)
                
                # Search for each keyword
                for keyword in keywords:
                    logger.info(f"Searching r/{subreddit_name} for '{keyword}'")
                    
                    search_results = subreddit.search(
                        keyword,
                        time_filter=time_filter,
                        limit=limit
                    )
                    
                    for submission in search_results:
                        thread_data = self._extract_thread_data(submission)
                        thread_data['keyword'] = keyword
                        discovered_threads.append(thread_data)
                        
                    # Respect rate limits
                    time.sleep(1)
                    
            except Exception as e:
                logger.error(f"Error searching r/{subreddit_name}: {e}")
                continue
        
        # Remove duplicates (by reddit_id)
        seen = set()
        unique_threads = []
        for thread in discovered_threads:
            if thread['reddit_id'] not in seen:
                seen.add(thread['reddit_id'])
                unique_threads.append(thread)
        
        logger.info(f"Discovered {len(unique_threads)} unique threads")
        return unique_threads
    
    def get_hot_threads(
        self,
        subreddits: List[str],
        limit: int = 25
    ) -> List[Dict]:
        """
        Get currently hot/trending threads from subreddits
        """
        hot_threads = []
        
        for subreddit_name in subreddits:
            try:
                subreddit = self.reddit.subreddit(subreddit_name)
                
                for submission in subreddit.hot(limit=limit):
                    thread_data = self._extract_thread_data(submission)
                    hot_threads.append(thread_data)
                
                time.sleep(1)
                
            except Exception as e:
                logger.error(f"Error getting hot threads from r/{subreddit_name}: {e}")
                continue
        
        return hot_threads
    
    def _extract_thread_data(self, submission) -> Dict:
        """
        Extract relevant data from a Reddit submission
        """
        return {
            'reddit_id': submission.id,
            'subreddit': submission.subreddit.display_name,
            'title': submission.title,
            'selftext': submission.selftext,
            'url': f"https://reddit.com{submission.permalink}",
            'author': str(submission.author) if submission.author else '[deleted]',
            'score': submission.score,
            'upvote_ratio': submission.upvote_ratio,
            'num_comments': submission.num_comments,
            'created_utc': datetime.fromtimestamp(submission.created_utc),
            'is_self': submission.is_self,
            'link_flair_text': submission.link_flair_text,
        }
    
    def get_thread_details(self, thread_id: str) -> Optional[Dict]:
        """
        Get detailed information about a specific thread
        """
        try:
            submission = self.reddit.submission(id=thread_id)
            
            # Fetch top comments
            submission.comments.replace_more(limit=0)  # Don't fetch "load more" comments
            top_comments = []
            
            for comment in submission.comments[:10]:  # Get top 10 comments
                if hasattr(comment, 'body'):
                    top_comments.append({
                        'author': str(comment.author) if comment.author else '[deleted]',
                        'body': comment.body,
                        'score': comment.score,
                        'created_utc': datetime.fromtimestamp(comment.created_utc)
                    })
            
            thread_data = self._extract_thread_data(submission)
            thread_data['top_comments'] = top_comments
            
            return thread_data
            
        except Exception as e:
            logger.error(f"Error fetching thread {thread_id}: {e}")
            return None
    
    def post_comment(
        self,
        thread_id: str,
        comment_text: str,
        username: str,
        password: str
    ) -> Optional[Dict]:
        """
        Post a comment to a thread using specific account credentials
        
        Args:
            thread_id: Reddit submission ID
            comment_text: Comment body
            username: Reddit username
            password: Reddit password
            
        Returns:
            Dict with comment details or None if failed
        """
        try:
            # Create authenticated Reddit instance for this account
            user_reddit = praw.Reddit(
                client_id=self.reddit.config.client_id,
                client_secret=self.reddit.config.client_secret,
                user_agent=self.reddit.config.user_agent,
                username=username,
                password=password
            )
            
            # Get the submission
            submission = user_reddit.submission(id=thread_id)
            
            # Post comment
            comment = submission.reply(comment_text)
            
            logger.info(f"Successfully posted comment {comment.id} as u/{username}")
            
            return {
                'reddit_comment_id': comment.id,
                'permalink': f"https://reddit.com{comment.permalink}",
                'posted_at': datetime.now(),
                'status': 'posted'
            }
            
        except Exception as e:
            logger.error(f"Error posting comment as u/{username}: {e}")
            return None
    
    def get_account_karma(self, username: str) -> Optional[int]:
        """
        Get total karma for a Reddit account
        """
        try:
            user = self.reddit.redditor(username)
            total_karma = user.link_karma + user.comment_karma
            return total_karma
        except Exception as e:
            logger.error(f"Error fetching karma for u/{username}: {e}")
            return None
    
    def check_shadowban(self, username: str) -> bool:
        """
        Check if a Reddit account is shadowbanned
        
        Returns True if shadowbanned, False if not
        """
        try:
            user = self.reddit.redditor(username)
            # Try to access user attributes
            _ = user.id
            return False  # If we can access, not shadowbanned
        except Exception:
            # If exception (404, etc.), likely shadowbanned
            return True
    
    def get_subreddit_info(self, subreddit_name: str) -> Optional[Dict]:
        """
        Get information about a subreddit (rules, description, etc.)
        """
        try:
            subreddit = self.reddit.subreddit(subreddit_name)
            
            # Get rules
            rules = []
            for rule in subreddit.rules:
                rules.append({
                    'short_name': rule.short_name,
                    'description': rule.description,
                    'kind': rule.kind
                })
            
            return {
                'name': subreddit.display_name,
                'title': subreddit.title,
                'description': subreddit.public_description,
                'subscribers': subreddit.subscribers,
                'rules': rules,
                'over18': subreddit.over18,
                'created_utc': datetime.fromtimestamp(subreddit.created_utc)
            }
            
        except Exception as e:
            logger.error(f"Error fetching subreddit r/{subreddit_name}: {e}")
            return None
    
    def calculate_relevance_score(
        self,
        thread: Dict,
        keywords: List[str]
    ) -> float:
        """
        Calculate relevance score (0-1) for a thread based on keywords
        
        Factors:
        - Keyword presence in title (high weight)
        - Keyword presence in body (medium weight)
        - Score/upvotes (activity indicator)
        - Number of comments (engagement indicator)
        - Recency (newer = higher score)
        """
        score = 0.0
        
        title_lower = thread['title'].lower()
        body_lower = thread.get('selftext', '').lower()
        
        # Keyword matching (60% of score)
        keyword_score = 0
        for keyword in keywords:
            keyword_lower = keyword.lower()
            if keyword_lower in title_lower:
                keyword_score += 30  # Title match = very relevant
            if keyword_lower in body_lower:
                keyword_score += 10  # Body match = somewhat relevant
        
        score += min(keyword_score, 60)  # Cap at 60 points
        
        # Activity score (20% of score)
        # Threads with 10+ upvotes and 5+ comments are "active"
        if thread['score'] >= 10:
            score += 10
        if thread['num_comments'] >= 5:
            score += 10
        
        # Recency score (20% of score)
        # Threads less than 24 hours old get bonus
        age_hours = (datetime.now() - thread['created_utc']).total_seconds() / 3600
        if age_hours < 24:
            score += 20
        elif age_hours < 48:
            score += 10
        
        # Normalize to 0-1
        return min(score / 100, 1.0)


class RedditAccountManager:
    """
    Manages multiple Reddit accounts for posting
    """
    
    def __init__(self):
        self.accounts = []
        self.last_used = {}  # Track when each account was last used
    
    def add_account(self, username: str, password: str, karma: int = 0):
        """
        Add a Reddit account to the pool
        """
        self.accounts.append({
            'username': username,
            'password': password,
            'karma': karma,
            'status': 'active'
        })
        logger.info(f"Added account u/{username} to pool")
    
    def get_next_account(self) -> Optional[Dict]:
        """
        Get next available account (with cooldown logic)
        
        Returns account that hasn't been used recently
        """
        if not self.accounts:
            return None
        
        now = datetime.now()
        cooldown_minutes = 60  # Wait 1 hour between posts per account
        
        available_accounts = []
        for account in self.accounts:
            if account['status'] != 'active':
                continue
            
            username = account['username']
            last_used = self.last_used.get(username)
            
            if not last_used:
                available_accounts.append(account)
            elif (now - last_used).total_seconds() > cooldown_minutes * 60:
                available_accounts.append(account)
        
        if not available_accounts:
            logger.warning("No accounts available (all on cooldown)")
            return None
        
        # Pick random account from available
        account = random.choice(available_accounts)
        self.last_used[account['username']] = now
        
        return account
    
    def mark_account_banned(self, username: str):
        """
        Mark an account as banned/compromised
        """
        for account in self.accounts:
            if account['username'] == username:
                account['status'] = 'banned'
                logger.warning(f"Marked u/{username} as banned")
                break

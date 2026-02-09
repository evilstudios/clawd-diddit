#!/usr/bin/env python3
"""
SEO/AEO Optimizer - Site Crawler
Crawls websites and extracts SEO/AEO relevant data
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import json
import time
from typing import Dict, List, Set
from collections import defaultdict

class SiteCrawler:
    def __init__(self, base_url: str, max_pages: int = 50):
        self.base_url = base_url
        self.max_pages = max_pages
        self.domain = urlparse(base_url).netloc
        self.visited: Set[str] = set()
        self.pages: List[Dict] = []
        
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; PortifoySEOBot/1.0; +https://clawd.bot)'
        }
    
    def is_valid_url(self, url: str) -> bool:
        """Check if URL should be crawled"""
        parsed = urlparse(url)
        
        # Same domain only
        if parsed.netloc != self.domain:
            return False
        
        # Skip common non-content URLs
        skip_extensions = ['.pdf', '.jpg', '.png', '.gif', '.css', '.js', '.xml', '.zip']
        if any(url.lower().endswith(ext) for ext in skip_extensions):
            return False
        
        # Skip common admin/system paths
        skip_paths = ['/admin', '/login', '/logout', '/api/', '/wp-admin']
        if any(path in url.lower() for path in skip_paths):
            return False
        
        return True
    
    def extract_page_data(self, url: str, soup: BeautifulSoup) -> Dict:
        """Extract SEO/AEO relevant data from page"""
        
        # Basic metadata
        title = soup.find('title')
        title_text = title.get_text().strip() if title else ""
        
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        description = meta_desc.get('content', '').strip() if meta_desc else ""
        
        # Headers
        h1_tags = [h.get_text().strip() for h in soup.find_all('h1')]
        h2_tags = [h.get_text().strip() for h in soup.find_all('h2')]
        
        # Schema markup
        schema_scripts = soup.find_all('script', type='application/ld+json')
        schemas = []
        for script in schema_scripts:
            try:
                schema_data = json.loads(script.string)
                schemas.append(schema_data)
            except:
                pass
        
        # Open Graph
        og_tags = {}
        for tag in soup.find_all('meta', property=lambda x: x and x.startswith('og:')):
            og_tags[tag.get('property')] = tag.get('content', '')
        
        # Links
        internal_links = []
        external_links = []
        for link in soup.find_all('a', href=True):
            href = urljoin(url, link['href'])
            if urlparse(href).netloc == self.domain:
                internal_links.append(href)
            else:
                external_links.append(href)
        
        # Images
        images = []
        for img in soup.find_all('img'):
            images.append({
                'src': img.get('src', ''),
                'alt': img.get('alt', ''),
                'has_alt': bool(img.get('alt'))
            })
        
        # Content
        # Remove script and style elements
        for script in soup(['script', 'style']):
            script.decompose()
        
        text_content = soup.get_text()
        # Clean up whitespace
        lines = (line.strip() for line in text_content.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text_content = ' '.join(chunk for chunk in chunks if chunk)
        
        word_count = len(text_content.split())
        
        return {
            'url': url,
            'title': title_text,
            'title_length': len(title_text),
            'meta_description': description,
            'meta_description_length': len(description),
            'h1_tags': h1_tags,
            'h1_count': len(h1_tags),
            'h2_tags': h2_tags[:10],  # First 10 only
            'h2_count': len(h2_tags),
            'schema_markup': schemas,
            'has_schema': len(schemas) > 0,
            'og_tags': og_tags,
            'has_og_tags': len(og_tags) > 0,
            'internal_links': internal_links,
            'internal_link_count': len(internal_links),
            'external_link_count': len(external_links),
            'images': images,
            'image_count': len(images),
            'images_without_alt': sum(1 for img in images if not img['has_alt']),
            'word_count': word_count,
            'text_content': text_content[:1000],  # First 1000 chars for analysis
        }
    
    def crawl_page(self, url: str) -> Dict:
        """Crawl a single page"""
        try:
            print(f"  Crawling: {url}")
            response = requests.get(url, headers=self.headers, timeout=10)
            
            if response.status_code != 200:
                return None
            
            soup = BeautifulSoup(response.content, 'html.parser')
            page_data = self.extract_page_data(url, soup)
            
            # Add response metadata
            page_data['status_code'] = response.status_code
            page_data['load_time'] = response.elapsed.total_seconds()
            
            return page_data
            
        except Exception as e:
            print(f"  ❌ Error crawling {url}: {e}")
            return None
    
    def crawl(self) -> List[Dict]:
        """Crawl the entire site"""
        print(f"\n🕷️  Crawling {self.base_url}")
        print(f"   Max pages: {self.max_pages}")
        
        to_visit = [self.base_url]
        
        while to_visit and len(self.visited) < self.max_pages:
            url = to_visit.pop(0)
            
            if url in self.visited or not self.is_valid_url(url):
                continue
            
            self.visited.add(url)
            page_data = self.crawl_page(url)
            
            if page_data:
                self.pages.append(page_data)
                
                # Add internal links to crawl queue
                for link in page_data['internal_links']:
                    if link not in self.visited and link not in to_visit:
                        to_visit.append(link)
            
            # Be polite - don't hammer the server
            time.sleep(0.5)
        
        print(f"✅ Crawled {len(self.pages)} pages")
        return self.pages
    
    def get_summary(self) -> Dict:
        """Get summary statistics"""
        if not self.pages:
            return {}
        
        return {
            'total_pages': len(self.pages),
            'avg_title_length': sum(p['title_length'] for p in self.pages) / len(self.pages),
            'avg_description_length': sum(p['meta_description_length'] for p in self.pages) / len(self.pages),
            'pages_with_schema': sum(1 for p in self.pages if p['has_schema']),
            'pages_with_og': sum(1 for p in self.pages if p['has_og_tags']),
            'total_images': sum(p['image_count'] for p in self.pages),
            'images_without_alt': sum(p['images_without_alt'] for p in self.pages),
            'avg_word_count': sum(p['word_count'] for p in self.pages) / len(self.pages),
        }


def main():
    """Test crawler"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python crawler.py <url>")
        sys.exit(1)
    
    url = sys.argv[1]
    crawler = SiteCrawler(url, max_pages=20)
    pages = crawler.crawl()
    
    print("\n📊 Summary:")
    summary = crawler.get_summary()
    for key, value in summary.items():
        print(f"  {key}: {value}")
    
    # Save results
    output_file = f"crawl-results-{urlparse(url).netloc}.json"
    with open(output_file, 'w') as f:
        json.dump({
            'url': url,
            'summary': summary,
            'pages': pages
        }, f, indent=2)
    
    print(f"\n✅ Results saved to {output_file}")


if __name__ == "__main__":
    main()

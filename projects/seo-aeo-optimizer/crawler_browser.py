#!/usr/bin/env python3
"""
SEO/AEO Optimizer - Browser-Based Crawler
Uses Playwright to bypass Cloudflare and crawl protected sites
"""

from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import json
import time
from typing import Dict, List, Set

class BrowserCrawler:
    def __init__(self, base_url: str, max_pages: int = 20):
        self.base_url = base_url
        self.max_pages = max_pages
        self.domain = urlparse(base_url).netloc
        self.visited: Set[str] = set()
        self.pages: List[Dict] = []
    
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
    
    def extract_page_data(self, url: str, html_content: str) -> Dict:
        """Extract SEO/AEO relevant data from page"""
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Basic metadata
        title = soup.find('title')
        title_text = title.get_text().strip() if title else ""
        
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        description = meta_desc.get('content', '').strip() if meta_desc else ""
        
        # Headers
        h1_tags = [h.get_text().strip() for h in soup.find_all('h1')]
        h2_tags = [h.get_text().strip() for h in soup.find_all('h2')]
        h3_tags = [h.get_text().strip() for h in soup.find_all('h3')]
        
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
        
        # Twitter Cards
        twitter_tags = {}
        for tag in soup.find_all('meta', attrs={'name': lambda x: x and x.startswith('twitter:')}):
            twitter_tags[tag.get('name')] = tag.get('content', '')
        
        # Links
        internal_links = []
        external_links = []
        for link in soup.find_all('a', href=True):
            href = urljoin(url, link['href'])
            parsed_href = urlparse(href)
            # Clean fragment
            href_clean = f"{parsed_href.scheme}://{parsed_href.netloc}{parsed_href.path}"
            if parsed_href.netloc == self.domain:
                if href_clean not in internal_links:
                    internal_links.append(href_clean)
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
        for script in soup(['script', 'style', 'nav', 'header', 'footer']):
            script.decompose()
        
        text_content = soup.get_text()
        lines = (line.strip() for line in text_content.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text_content = ' '.join(chunk for chunk in chunks if chunk)
        
        word_count = len(text_content.split())
        
        # Canonical URL
        canonical = soup.find('link', rel='canonical')
        canonical_url = canonical.get('href') if canonical else None
        
        return {
            'url': url,
            'title': title_text,
            'title_length': len(title_text),
            'meta_description': description,
            'meta_description_length': len(description),
            'h1_tags': h1_tags,
            'h1_count': len(h1_tags),
            'h2_tags': h2_tags[:10],
            'h2_count': len(h2_tags),
            'h3_count': len(h3_tags),
            'schema_markup': schemas,
            'has_schema': len(schemas) > 0,
            'og_tags': og_tags,
            'has_og_tags': len(og_tags) > 0,
            'twitter_tags': twitter_tags,
            'canonical_url': canonical_url,
            'internal_links': internal_links,
            'internal_link_count': len(internal_links),
            'external_link_count': len(external_links),
            'images': images,
            'image_count': len(images),
            'images_without_alt': sum(1 for img in images if not img['has_alt']),
            'word_count': word_count,
            'text_preview': text_content[:500],
        }
    
    def crawl(self) -> List[Dict]:
        """Crawl the entire site using browser automation"""
        print(f"\n🌐 Crawling {self.base_url} (Browser Mode)")
        print(f"   Max pages: {self.max_pages}")
        
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            to_visit = [self.base_url]
            
            while to_visit and len(self.visited) < self.max_pages:
                url = to_visit.pop(0)
                
                if url in self.visited or not self.is_valid_url(url):
                    continue
                
                self.visited.add(url)
                
                try:
                    print(f"  📄 {url}")
                    page.goto(url, wait_until='networkidle', timeout=15000)
                    
                    # Wait for content to load
                    time.sleep(1)
                    
                    html_content = page.content()
                    page_data = self.extract_page_data(url, html_content)
                    
                    # Add load time (approximate)
                    page_data['status'] = 'success'
                    
                    self.pages.append(page_data)
                    
                    # Add internal links to queue
                    for link in page_data['internal_links'][:10]:  # Limit to avoid explosion
                        if link not in self.visited and link not in to_visit:
                            to_visit.append(link)
                    
                except PlaywrightTimeout:
                    print(f"  ⏱️  Timeout")
                except Exception as e:
                    print(f"  ❌ Error: {str(e)[:50]}")
            
            browser.close()
        
        print(f"✅ Crawled {len(self.pages)} pages\n")
        return self.pages
    
    def get_summary(self) -> Dict:
        """Get summary statistics"""
        if not self.pages:
            return {}
        
        total_pages = len(self.pages)
        
        return {
            'total_pages': total_pages,
            'avg_title_length': round(sum(p['title_length'] for p in self.pages) / total_pages, 1),
            'avg_description_length': round(sum(p['meta_description_length'] for p in self.pages) / total_pages, 1),
            'pages_with_schema': sum(1 for p in self.pages if p['has_schema']),
            'pages_without_schema': total_pages - sum(1 for p in self.pages if p['has_schema']),
            'pages_with_og': sum(1 for p in self.pages if p['has_og_tags']),
            'total_images': sum(p['image_count'] for p in self.pages),
            'images_without_alt': sum(p['images_without_alt'] for p in self.pages),
            'avg_word_count': round(sum(p['word_count'] for p in self.pages) / total_pages, 1),
            'pages_missing_h1': sum(1 for p in self.pages if p['h1_count'] == 0),
            'pages_multiple_h1': sum(1 for p in self.pages if p['h1_count'] > 1),
        }


def main():
    """Test crawler"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python crawler_browser.py <url> [max_pages]")
        sys.exit(1)
    
    url = sys.argv[1]
    max_pages = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    
    crawler = BrowserCrawler(url, max_pages=max_pages)
    pages = crawler.crawl()
    
    print("📊 SUMMARY:")
    print("=" * 50)
    summary = crawler.get_summary()
    for key, value in summary.items():
        print(f"  {key}: {value}")
    
    # Save results
    domain = urlparse(url).netloc.replace('.', '-')
    output_file = f"crawl-{domain}.json"
    
    with open(output_file, 'w') as f:
        json.dump({
            'url': url,
            'crawled_at': time.strftime('%Y-%m-%d %H:%M:%S'),
            'summary': summary,
            'pages': pages
        }, f, indent=2)
    
    print(f"\n✅ Results saved to {output_file}")


if __name__ == "__main__":
    main()

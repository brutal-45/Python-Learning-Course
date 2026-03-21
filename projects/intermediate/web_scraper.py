"""
Project: Web Scraper
Level: Intermediate
Description: A web scraper that extracts data from websites using requests and BeautifulSoup.

This project demonstrates:
- HTTP requests with requests library
- HTML parsing with BeautifulSoup
- Data extraction techniques
- Error handling
- Data storage (CSV, JSON)
- Rate limiting
"""

import time
import json
import csv
import re
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict
from urllib.parse import urljoin, urlparse


# Note: In a real environment, you would need:
# pip install requests beautifulsoup4

# For demonstration, we'll create mock implementations


@dataclass
class Article:
    """Data class for storing article information."""
    title: str
    url: str
    author: Optional[str] = None
    date: Optional[str] = None
    summary: Optional[str] = None
    content: Optional[str] = None


class MockResponse:
    """Mock response for demonstration purposes."""

    def __init__(self, url: str):
        self.url = url
        self.status_code = 200
        self.text = self._generate_mock_html()
        self.headers = {'content-type': 'text/html'}

    def _generate_mock_html(self) -> str:
        """Generate mock HTML content."""
        return """
        <!DOCTYPE html>
        <html>
        <head><title>Mock News Site</title></head>
        <body>
            <div class="article">
                <h2 class="title"><a href="/article/1">Python 3.12 Released</a></h2>
                <span class="author">John Doe</span>
                <span class="date">2024-03-15</span>
                <p class="summary">The latest Python version brings performance improvements.</p>
            </div>
            <div class="article">
                <h2 class="title"><a href="/article/2">Web Scraping Best Practices</a></h2>
                <span class="author">Jane Smith</span>
                <span class="date">2024-03-14</span>
                <p class="summary">Learn how to scrape websites ethically.</p>
            </div>
            <div class="article">
                <h2 class="title"><a href="/article/3">Data Science with Python</a></h2>
                <span class="author">Bob Johnson</span>
                <span class="date">2024-03-13</span>
                <p class="summary">Exploring pandas and numpy for data analysis.</p>
            </div>
        </body>
        </html>
        """


class MockBeautifulSoup:
    """Mock BeautifulSoup for demonstration."""

    def __init__(self, html: str, parser: str):
        self.html = html

    def find_all(self, tag: str, class_: str = None) -> List['MockElement']:
        """Mock find_all method."""
        articles = []

        # Extract articles from mock HTML
        article_pattern = r'<div class="article">(.*?)</div>'
        for match in re.finditer(article_pattern, self.html, re.DOTALL):
            article_html = match.group(1)
            articles.append(MockElement(article_html))

        return articles


class MockElement:
    """Mock element for demonstration."""

    def __init__(self, html: str):
        self.html = html

    def find(self, tag: str, class_: str = None) -> Optional['MockElement']:
        """Mock find method."""
        patterns = {
            'title': r'<h2 class="title"><a href="([^"]+)">([^<]+)</a></h2>',
            'author': r'<span class="author">([^<]+)</span>',
            'date': r'<span class="date">([^<]+)</span>',
            'summary': r'<p class="summary">([^<]+)</p>'
        }

        if class_ in patterns:
            match = re.search(patterns[class_], self.html)
            if match:
                return MockElement(match.group(2) if class_ == 'title' else match.group(1))
        return None

    def get(self, attr: str) -> Optional[str]:
        """Mock get method for attributes."""
        if attr == 'href':
            match = re.search(r'href="([^"]+)"', self.html)
            return match.group(1) if match else None
        return None

    def get_text(self, strip: bool = True) -> str:
        """Mock get_text method."""
        text = re.sub(r'<[^>]+>', '', self.html)
        return text.strip() if strip else text

    @property
    def text(self) -> str:
        return self.get_text()


class WebScraper:
    """
    A web scraper class with rate limiting and error handling.

    Features:
    - Configurable rate limiting
    - Retry logic for failed requests
    - Data extraction from HTML
    - Export to CSV and JSON
    """

    def __init__(self, base_url: str, rate_limit: float = 1.0, max_retries: int = 3):
        """
        Initialize the web scraper.

        Args:
            base_url: Base URL for the website
            rate_limit: Seconds to wait between requests
            max_retries: Maximum retry attempts for failed requests
        """
        self.base_url = base_url
        self.rate_limit = rate_limit
        self.max_retries = max_retries
        self.last_request_time = 0
        self.session = None  # Would be requests.Session() in real use
        self.scraped_data: List[Article] = []

    def _rate_limit_wait(self):
        """Wait if necessary to respect rate limiting."""
        elapsed = time.time() - self.last_request_time
        if elapsed < self.rate_limit:
            time.sleep(self.rate_limit - elapsed)

    def get_page(self, url: str) -> Optional[MockResponse]:
        """
        Fetch a web page with error handling and retries.

        Args:
            url: URL to fetch

        Returns:
            Response object or None if failed
        """
        self._rate_limit_wait()

        for attempt in range(self.max_retries):
            try:
                # In real implementation: response = self.session.get(url)
                response = MockResponse(url)
                self.last_request_time = time.time()

                if response.status_code == 200:
                    return response
                elif response.status_code == 404:
                    print(f"Page not found: {url}")
                    return None
                elif response.status_code == 429:
                    wait_time = 2 ** attempt
                    print(f"Rate limited. Waiting {wait_time} seconds...")
                    time.sleep(wait_time)
                else:
                    print(f"HTTP {response.status_code}: {url}")

            except Exception as e:
                print(f"Error fetching {url}: {e}")
                if attempt < self.max_retries - 1:
                    time.sleep(2 ** attempt)

        return None

    def parse_article(self, element: MockElement, base_url: str) -> Optional[Article]:
        """
        Parse article data from an HTML element.

        Args:
            element: BeautifulSoup element
            base_url: Base URL for resolving relative URLs

        Returns:
            Article object or None if parsing failed
        """
        try:
            title_elem = element.find('h2', class_='title')
            if not title_elem:
                return None

            title = title_elem.get_text()
            url = title_elem.get('href')
            if url:
                url = urljoin(base_url, url)

            author_elem = element.find('span', class_='author')
            author = author_elem.get_text() if author_elem else None

            date_elem = element.find('span', class_='date')
            date = date_elem.get_text() if date_elem else None

            summary_elem = element.find('p', class_='summary')
            summary = summary_elem.get_text() if summary_elem else None

            return Article(
                title=title,
                url=url,
                author=author,
                date=date,
                summary=summary
            )

        except Exception as e:
            print(f"Error parsing article: {e}")
            return None

    def scrape_articles(self, url: str) -> List[Article]:
        """
        Scrape articles from a page.

        Args:
            url: URL to scrape

        Returns:
            List of Article objects
        """
        response = self.get_page(url)
        if not response:
            return []

        # In real implementation: soup = BeautifulSoup(response.text, 'html.parser')
        soup = MockBeautifulSoup(response.text, 'html.parser')

        articles = []
        article_elements = soup.find_all('div', class_='article')

        for elem in article_elements:
            article = self.parse_article(elem, self.base_url)
            if article:
                articles.append(article)

        self.scraped_data.extend(articles)
        return articles

    def export_to_json(self, filename: str) -> None:
        """Export scraped data to JSON file."""
        data = [asdict(article) for article in self.scraped_data]
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Exported {len(data)} articles to {filename}")

    def export_to_csv(self, filename: str) -> None:
        """Export scraped data to CSV file."""
        if not self.scraped_data:
            print("No data to export")
            return

        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['title', 'url', 'author', 'date', 'summary'])
            writer.writeheader()
            for article in self.scraped_data:
                writer.writerow(asdict(article))

        print(f"Exported {len(self.scraped_data)} articles to {filename}")

    def get_statistics(self) -> Dict:
        """Get scraping statistics."""
        return {
            'total_articles': len(self.scraped_data),
            'unique_authors': len(set(a.author for a in self.scraped_data if a.author)),
            'articles_with_dates': sum(1 for a in self.scraped_data if a.date),
        }


def demonstrate_scraper():
    """Demonstrate the web scraper functionality."""
    print("\n" + "=" * 60)
    print("🕷️ WEB SCRAPER DEMONSTRATION")
    print("=" * 60)

    # Create scraper
    scraper = WebScraper(
        base_url="https://mock-news-site.com",
        rate_limit=0.5,
        max_retries=3
    )

    # Scrape articles
    print("\n📄 Scraping articles...")
    articles = scraper.scrape_articles("https://mock-news-site.com/news")

    # Display results
    print(f"\n✅ Found {len(articles)} articles:\n")
    for i, article in enumerate(articles, 1):
        print(f"  Article {i}:")
        print(f"    Title: {article.title}")
        print(f"    URL: {article.url}")
        print(f"    Author: {article.author}")
        print(f"    Date: {article.date}")
        print(f"    Summary: {article.summary}")
        print()

    # Show statistics
    print("📊 Statistics:")
    stats = scraper.get_statistics()
    for key, value in stats.items():
        print(f"  {key}: {value}")

    # Export options (commented out to avoid file creation in demo)
    # scraper.export_to_json('articles.json')
    # scraper.export_to_csv('articles.csv')


# =============================================================================
# BEST PRACTICES FOR WEB SCRAPING
# =============================================================================

SCRAPING_BEST_PRACTICES = """
🕷️ Web Scraping Best Practices:

1. RESPECT ROBOTS.TXT
   - Check robots.txt before scraping
   - Follow the rules specified by the website

2. RATE LIMITING
   - Add delays between requests
   - Don't overwhelm the server

3. IDENTIFY YOURSELF
   - Set a descriptive User-Agent
   - Provide contact information if possible

4. HANDLE ERRORS GRACEFULLY
   - Implement retry logic
   - Log errors for debugging

5. RESPECT COPYRIGHT
   - Don't republish content without permission
   - Use data for personal/educational purposes

6. CHECK FOR APIs
   - Many sites offer official APIs
   - APIs are more reliable and legal

7. BE PREPARED FOR CHANGES
   - Website structures change frequently
   - Write flexible selectors

8. STORAGE
   - Store data efficiently (JSON, CSV, Database)
   - Include metadata like scrape timestamp
"""


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    # Run demonstration
    demonstrate_scraper()

    print("\n" + SCRAPING_BEST_PRACTICES)

    print("\n✅ Web scraper demonstration complete!")

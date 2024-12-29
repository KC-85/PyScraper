from bs4 import BeautifulSoup
from crawler.utils import logger

class SoupParser:
    def parse(self, html_content):
        try:
            logger.info("Parsing HTML content with Beautiful Soup.")
            soup = BeautifulSoup(html_content, "lxml")
            data = []
            for item in soup.select(".example-class"):  # Adjust CSS selector
                data.append({
                    "title": item.get_text(strip=True),
                    "link": item.get("href")
                })
            return data
        except Exception as e:
            logger.error(f"Error parsing content: {e}")
            return []

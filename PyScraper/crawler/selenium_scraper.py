import requests
from crawler.utils import logger
from crawler.config import HEADERS, TIMEOUT

class Scraper:
    def __init__(self, base_url):
        self.base_url = base_url

    def fetch(self, endpoint=""):
        url = f"{self.base_url}{endpoint}"
        try:
            logger.info(f"Fetching URL: {url}")
            response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logger.error(f"Error fetching URL: {e}")
            return None

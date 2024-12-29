from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from crawler.utils import logger
from crawler.config import SELENIUM_DRIVER_PATH

class SeleniumScraper:
    def __init__(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(service=Service(SELENIUM_DRIVER_PATH), options=options)

    def fetch_page(self, url):
        try:
            logger.info(f"Fetching page with Selenium: {url}")
            self.driver.get(url)
            return self.driver.page_source
        except Exception as e:
            logger.error(f"Error in Selenium scraper: {e}")
            return None

    def close(self):
        self.driver.quit()

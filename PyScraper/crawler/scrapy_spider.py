from scrapy_selenium import SeleniumRequest
from scrapy import Spider
from crawler.storage import Storage
from crawler.config import SCRAPY_PAGINATION_SELECTOR
from crawler.utils import logger


class ScrapySpider(Spider):
    name = "scrapy_spider"
    start_urls = ["https://example.com"]  # Replace with your target URL

    def start_requests(self):
        """
        Starts requests with Selenium integration to handle JavaScript-rendered pages.
        """
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=5,  # Adjust the wait time if needed for JavaScript loading
            )

    def parse(self, response):
        """
        Parses the content of the page and yields extracted data.
        Also handles pagination by following next page links dynamically.
        """
        logger.info(f"Scraping: {response.url}")

        # Extract data using CSS selectors
        for item in response.css(".example-class"):  # Adjust the CSS selector
            yield {
                "title": item.css("::text").get(),
                "link": response.urljoin(item.css("::attr(href)").get()),
            }

        # Handle pagination
        next_page = response.css(SCRAPY_PAGINATION_SELECTOR).get()
        if next_page:
            logger.info(f"Following pagination link: {next_page}")
            yield SeleniumRequest(
                url=response.urljoin(next_page),
                callback=self.parse,
                wait_time=5,
            )

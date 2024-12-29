import scrapy
from scrapy_selenium import SeleniumRequest
from crawler.config import SCRAPY_PAGINATION_SELECTOR

class AsyncSpider(scrapy.Spider):
    name = "async_spider"
    start_urls = ["https://example.com"]

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse
            )

    def parse(self, response):
        for item in response.css(".example-class"):  # Adjust CSS selector
            yield {
                "title": item.css("::text").get(),
                "link": item.css("::attr(href)").get(),
            }

        # Handle pagination
        next_page = response.css(SCRAPY_PAGINATION_SELECTOR).get()
        if next_page:
            yield SeleniumRequest(
                url=response.urljoin(next_page),
                callback=self.parse
            )

from scrapy_selenium import SeleniumRequest
from scrapy import Spider
from crawler.storage import Storage
from crawler.utils import logger


class ReedSpider(Spider):
    name = "reed_spider"
    start_urls = ["https://www.reed.co.uk/jobs/python-developer-jobs-in-london"]

    def start_requests(self):
        """
        Starts Selenium requests to render job listing pages.
        """
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url,
                callback=self.parse,
                wait_time=5,  # Allow JavaScript to load fully
            )

    def parse(self, response):
        """
        Parses the job listing page and extracts job details.
        """
        logger.info(f"Scraping: {response.url}")

        # Extract job details
        for job in response.css(".job-result-card"):  # Adjust based on site structure
            yield {
                "title": job.css(".job-title ::text").get(),
                "company": job.css(".job-company ::text").get(),
                "location": job.css(".job-location ::text").get(),
                "salary": job.css(".job-salary ::text").get(),
                "link": response.urljoin(job.css("a::attr(href)").get()),
            }

        # Handle pagination
        next_page = response.css(".pagination-next::attr(href)").get()
        if next_page:
            yield SeleniumRequest(
                url=response.urljoin(next_page),
                callback=self.parse,
                wait_time=5,
            )

from crawler.selenium_scraper import SeleniumScraper
from crawler.soup_parser import SoupParser
from crawler.storage import Storage
from scrapy.crawler import CrawlerProcess
from scrapy_project.scrapy_project.spiders.async_spider import AsyncSpider

def main():
    # Selenium + BeautifulSoup
    selenium_scraper = SeleniumScraper()
    soup_parser = SoupParser()
    storage = Storage()

    html_content = selenium_scraper.fetch_page("https://example.com")
    selenium_scraper.close()

    if html_content:
        data = soup_parser.parse(html_content)
        if data:
            storage.save_to_db(data)

    # Scrapy Async Spider
    process = CrawlerProcess()
    process.crawl(AsyncSpider)
    process.start()

if __name__ == "__main__":
    main()

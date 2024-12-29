BOT_NAME = "scrapy_project"
SPIDER_MODULES = ["scrapy_project.spiders"]
NEWSPIDER_MODULE = "scrapy_project.spiders"

ROBOTSTXT_OBEY = True
SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = 'path/to/chromedriver'  # Update to your ChromeDriver path
SELENIUM_DRIVER_ARGUMENTS = ['--headless']

DOWNLOADER_MIDDLEWARES = {
    'scrapy_project.middlewares.RandomUserAgentMiddleware': 400,
    'scrapy_selenium.SeleniumMiddleware': 800,
}

ITEM_PIPELINES = {
    'scrapy_project.pipelines.ScrapyProjectPipeline': 300,
}

import scrapy

class ScrapyProjectItem(scrapy.Item):
    # Define the fields for your item here
    title = scrapy.Field()
    link = scrapy.Field()
    additional_info = scrapy.Field()  # Add more fields as needed

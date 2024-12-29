from crawler.storage import Storage

class ScrapyProjectPipeline:
    """
    Pipeline to store data in the database using SQLAlchemy.
    """
    def __init__(self):
        self.storage = Storage()

    def process_item(self, item, spider):
        try:
            # Convert Scrapy Item to dictionary for database storage
            data = {
                "title": item.get("title"),
                "link": item.get("link"),
                "additional_info": item.get("additional_info", None),
            }
            self.storage.save_to_db([data])
        except Exception as e:
            spider.logger.error(f"Error saving item: {e}")
        return item

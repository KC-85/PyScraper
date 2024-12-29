from sqlalchemy import create_engine, Column, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from crawler.utils import logger
from crawler.config import DATABASE_URL

Base = declarative_base()

class DataModel(Base):
    __tablename__ = 'scraped_data'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    link = Column(String, nullable=True, unique=True)

    __table_args__ = (
        UniqueConstraint('link', name='unique_link'),
    )

class Storage:
    def __init__(self):
        logger.info(f"Connecting to database at {DATABASE_URL}.")
        self.engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def save_to_db(self, data):
        session = self.Session()
        try:
            logger.info("Saving data to the database.")
            records = [DataModel(**item) for item in data]
            session.add_all(records)
            session.commit()
        except Exception as e:
            logger.error(f"Error saving data to the database: {e}")
            session.rollback()
        finally:
            session.close()

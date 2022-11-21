from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, DateTime
from database import Base



class NewsInfo(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    data_stworzenia = Column(DateTime)
    autor = Column(String)
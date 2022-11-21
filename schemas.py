from pydantic import BaseModel
import datetime
from typing import Optional, List



class CreateAndUpdateNews(BaseModel):
    content: str
    data_stworzenia: datetime.datetime
    autor: str



class News(CreateAndUpdateNews):
    id: int

    class Config:
        orm_mode = True



class PaginatedNewsInfo(BaseModel):
    limit: int
    offset: int
    data: List[News]
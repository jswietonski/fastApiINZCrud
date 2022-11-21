from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from crud import get_all_news, create_news, get_news_info_by_id, update_news_info, delete_news_info
from database import get_db
from exceptions import NewsInfoException
from schemas import News, CreateAndUpdateNews, PaginatedNewsInfo

router = APIRouter()


@cbv(router)
class Newss:
    session: Session = Depends(get_db)


    @router.get("/news", response_model=PaginatedNewsInfo)
    def list_news(self, limit: int = 10, offset: int = 0):

        news_list = get_all_news(self.session, limit, offset)
        response = {"limit": limit, "offset": offset, "data": news_list}

        return response

    @router.post("/news")
    def add_news(self, news_info: CreateAndUpdateNews):

        try:
            news_info = create_news(self.session, news_info)
            return news_info
        except NewsInfoException as cie:
            raise HTTPException(**cie.__dict__)


@router.get("/news/{news_id}", response_model=News)
def get_news_info(news_id: int, session: Session = Depends(get_db)):

    try:
        news_info = get_news_info_by_id(session, news_id)
        return news_info
    except NewsInfoException as cie:
        raise HTTPException(**cie.__dict__)


@router.put("/news/{news_id}", response_model=News)
def update_news(news_id: int, new_info: CreateAndUpdateNews, session: Session = Depends(get_db)):

    try:
        news_info = update_news_info(session, news_id, new_info)
        return news_info
    except NewsInfoException as cie:
        raise HTTPException(**cie.__dict__)


@router.delete("/news/{news_id}")
def delete_news(news_id: int, session: Session = Depends(get_db)):

    try:
        return delete_news_info(session, news_id)
    except NewsInfoException as cie:
        raise HTTPException(**cie.__dict__)
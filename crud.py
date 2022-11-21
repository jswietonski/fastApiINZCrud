from typing import List
from sqlalchemy.orm import Session
from exceptions import NewsInfoInfoAlreadyExistError, NewsInfoNotFoundError
from models import NewsInfo
from schemas import CreateAndUpdateNews


def get_all_news(session: Session, limit: int, offset: int) -> List[NewsInfo]:
    return session.query(NewsInfo).offset(offset).limit(limit).all()


def get_news_info_by_id(session: Session, _id: int) -> NewsInfo:
    news_info = session.query(NewsInfo).get(_id)

    if news_info is None:
        raise NewsInfoNotFoundError

    return news_info


def create_news(session: Session, news_info: CreateAndUpdateNews) -> NewsInfo:
    news_details = session.query(NewsInfo).filter(NewsInfo.content == news_info.content, NewsInfo.autor == news_info.autor).first()
    if news_details is not None:
        raise NewsInfoInfoAlreadyExistError

    new_news_info = NewsInfo(**news_info.dict())
    session.add(new_news_info)
    session.commit()
    session.refresh(new_news_info)
    return new_news_info


def update_news_info(session: Session, _id: int, info_update: CreateAndUpdateNews) -> NewsInfo:
    news_info = get_news_info_by_id(session, _id)

    if news_info is None:
        raise NewsInfoNotFoundError

    news_info.content = info_update.content
    news_info.data_stworzenia = info_update.data_stworzenia
    news_info.autor = info_update.autor

    session.commit()
    session.refresh(news_info)

    return news_info


def delete_news_info(session: Session, _id: int):
    news_info = get_news_info_by_id(session, _id)

    if news_info is None:
        raise NewsInfoNotFoundError

    session.delete(news_info)
    session.commit()

    return
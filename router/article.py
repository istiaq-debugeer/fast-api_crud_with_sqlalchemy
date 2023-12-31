import db.db_user
from schemas import ArticleBase,ArticleDisplay
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_article
from typing import List
from auth.Oauth2 import outh2_schema

router=APIRouter(
    prefix='/article',
    tags=['article']
)
#cretearticle
@router.post('/',response_model=ArticleDisplay)
def create_article(request:ArticleBase,db:Session=Depends(get_db)):
    return db_article.create_article(db,request)


@router.get('/{id}',response_model=ArticleDisplay)
def get_article(id: int,db:Session=Depends(get_db),token: str=Depends(outh2_schema)):
    return db_article.get_article(db,id)
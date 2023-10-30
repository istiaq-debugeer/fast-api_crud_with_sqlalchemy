from fastapi import FastAPI
from router import blog_post
from db import models
from auth import authentication
from db.database import  engine
from router import users,article,product

app = FastAPI()
app.include_router(users.router)
app.include_router(authentication.router)
app.include_router(blog_post.router)
app.include_router(article.router)
app.include_router(product.router)
models.Base.metadata.create_all(engine)
from fastapi import FastAPI
from router import blog_post
from db import models
from db.database import  engine
from router import users,article

app = FastAPI()
app.include_router(users.router)
app.include_router(blog_post.router)
app.include_router(article.router)
models.Base.metadata.create_all(engine)
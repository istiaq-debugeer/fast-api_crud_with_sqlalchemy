from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL="sqlite:///.fastapiproject.db"

engine=create_engine(
    SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False}
)
SessionLoacal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()

def get_db():
    db=SessionLoacal()
    try:
        yield db
    finally:
        db.close_all
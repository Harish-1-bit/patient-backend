from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.utils.setting import setting

base = declarative_base()

engine = create_engine(url=setting.DB_CONNECTION)

localSession = sessionmaker(bind = engine)

def get_db():
    session = localSession()
    try:
        yield session
    finally:
        session.close()
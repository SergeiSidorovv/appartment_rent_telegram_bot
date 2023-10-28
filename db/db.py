from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from config import create_db_uri


engine = create_engine(create_db_uri())

Base = declarative_base()


def create_all():
    Base.metadata.create_all(engine)

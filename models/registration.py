from sqlalchemy import Column, Integer, String

from db.db import Base


class Registration(Base):
    __tablename__ = 'registration'
    id = Column(Integer(), primary_key=True)
    user_name = Column(String(100), nullable=False, unique=True)
    user_telegram_id = Column(String(1000), nullable=False, unique=True)

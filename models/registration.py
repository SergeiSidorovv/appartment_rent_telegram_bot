from sqlalchemy import Column, Integer, String, ForeignKey

from db.db import Base, create_all


class Registration(Base):
    __tablename__ = 'registration'
    id = Column(Integer(), primary_key=True)
    user_name = Column(String(100), nullable=False, unique=True)
    user_telegram_id = Column(Integer(), nullable=False, unique=True)

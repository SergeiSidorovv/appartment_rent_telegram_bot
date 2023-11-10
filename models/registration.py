from sqlalchemy import Column, String, ForeignKey, BIGINT, Integer

from db.db import Base, create_all


class Registration(Base):
    __tablename__ = 'registration'
    id = Column(Integer(), primary_key=True)
    user_name = Column(String(100), nullable=False, unique=True)
    user_telegram_id = Column(BIGINT(), nullable=False, unique=True)

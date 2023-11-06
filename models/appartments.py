from sqlalchemy import Column, Integer, String, ForeignKey

from db.db import Base, create_all


class Appartments(Base):
    __tablename__ = 'appartments'
    id_appartment = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey(
        'registration.user_telegram_id'), nullable=False)
    url = Column(String(), nullable=False)
    info = Column(String(), nullable=False)
    price = Column(String(), nullable=False)

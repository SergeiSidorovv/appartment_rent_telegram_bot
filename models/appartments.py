from sqlalchemy import Column, Integer, String, ForeignKey, BIGINT, VARCHAR

from db.db import Base, create_all


class Appartments(Base):
    __tablename__ = 'appartments'
    id_appartment = Column(Integer(), primary_key=True)
    user_id = Column(BIGINT(), ForeignKey(
        'registration.user_telegram_id'), nullable=False)
    url = Column(VARCHAR(), nullable=False)
    info = Column(VARCHAR(), nullable=False)
    price = Column(VARCHAR(), nullable=False)

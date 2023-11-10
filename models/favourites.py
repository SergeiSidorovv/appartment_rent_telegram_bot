from sqlalchemy import Column, String, ForeignKey, BIGINT, Integer, VARCHAR

from db.db import Base, create_all, engine


class Favourites(Base):
    __tablename__ = 'favourites'
    id = Column(Integer(), primary_key=True)
    user_id = Column(BIGINT(), ForeignKey(
        'registration.user_telegram_id'))
    url = Column(VARCHAR(), nullable=False)
    info = Column(VARCHAR(), nullable=False)
    price = Column(VARCHAR(), nullable=False)


create_all()

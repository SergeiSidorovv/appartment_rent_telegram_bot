from sqlalchemy.orm import Session

from db.db import engine
from models.registration import Registration


def add_user(user_data: dict):
    with Session(autoflush=False, bind=engine) as session:
        user = Registration(
            user_name=user_data['nick_name'],
            user_telegram_id=user_data['user_telegram_id']
        )
        session.add(user)
        session.commit()

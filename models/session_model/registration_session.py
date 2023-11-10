from sqlalchemy.orm import Session

from models.registration import Registration
from db.db import engine


def get_users_telegram_id():
    with Session(autoflush=False, bind=engine) as session:
        users_telegram_id = session.query(Registration.user_telegram_id).all()
        users_telegram_id = [i[0] for i in users_telegram_id]
    return users_telegram_id


def add_user(user_data: dict):
    with Session(autoflush=False, bind=engine) as session:
        user = Registration(
            user_name=user_data['nick_name'],
            user_telegram_id=user_data['user_telegram_id']
        )
        session.add(user)
        session.commit()

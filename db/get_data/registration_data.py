from sqlalchemy.orm import Session

from db.db import engine
from models.registration import Registration


def get_users_telegram_id():
    with Session(autoflush=False, bind=engine) as session:
        users_telegram_id = session.query(Registration.user_telegram_id).all()
        users_telegram_id = [i[0] for i in users_telegram_id]
    return users_telegram_id

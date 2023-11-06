from sqlalchemy.orm import Session

from db.db import engine
from models.appartments import Appartments
from models.registration import Registration


def get_appartment(person_id: int):
    with Session(autoflush=False, bind=engine) as session:
        appartments = session.query(
            Appartments).filter(Appartments.user_id == str(person_id), Appartments.info != '').all()
        for i in appartments:
            advertisement = {}
            advertisement['url'] = i.url
            advertisement['info'] = i.info
            advertisement['price'] = i.price

            yield advertisement
    yield None


def get_user_id():
    with Session(autoflush=False, bind=engine) as session:
        users_id = session.query(Appartments.user_id).all()
        users_id = [i[0] for i in users_id]
    return users_id


def get_users_telegram_id():
    with Session(autoflush=False, bind=engine) as session:
        users_telegram_id = session.query(Registration.user_telegram_id).all()
        users_telegram_id = [i[0] for i in users_telegram_id]
    return users_telegram_id

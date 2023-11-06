from sqlalchemy.orm import Session

from db.db import engine
from models.appartments import Appartments
from models.registration import Registration


def add_appartments(appartments: dict, person_id: int):
    with Session(autoflush=False, bind=engine) as session:
        count_appartments = len(appartments['info'])
        highlighted_id = 50

        for i in range(count_appartments):
            app = Appartments(
                user_id=person_id,
                url=appartments['url'][i],
                info=appartments['info'][i],
                price=appartments['price'][i]
            )
            session.add(app)
            session.commit()

        if count_appartments < highlighted_id:
            for i in range(count_appartments, highlighted_id):
                empty_data = Appartments(
                    user_id=person_id,
                    url='',
                    info='',
                    price=''
                )
                session.add(empty_data)
                session.commit()


def add_user(user_data: dict):
    with Session(autoflush=False, bind=engine) as session:
        user = Registration(
            user_name=user_data['nick_name'],
            user_telegram_id=user_data['user_telegram_id']
        )
        session.add(user)
        session.commit()

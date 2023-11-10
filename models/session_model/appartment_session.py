from sqlalchemy.orm import Session

from db.db import engine
from models.appartments import Appartments


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
        users_id = session.query(Appartments.user_id).distinct(
            Appartments.user_id).all()
        users_id = [i[0] for i in users_id]

    return users_id


def update_person_appartments(appartments: dict, person_id: int):
    with Session(autoflush=False, bind=engine) as session:
        count_id_appartments = session.query(
            Appartments).filter_by(user_id=str(person_id)).count()
        max_id_new_appartment = len(appartments['url']) - 1

        for i in range(count_id_appartments):
            id_appartment = i + 1
            appartment = session.query(Appartments).get(id_appartment)

            if i <= max_id_new_appartment:
                appartment.url = appartments['url'][i]
                appartment.info = appartments['info'][i]
                appartment.price = appartments['price'][i]
                session.commit()
            else:
                appartment.url = ''
                appartment.price = ''
                appartment.info = ''
                session.commit()


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

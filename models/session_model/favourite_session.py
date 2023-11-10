from sqlalchemy.orm import Session

from db.db import engine
from models.favourites import Favourites


def add_favourite(appartment: dict, person_id: int):
    with Session(autoflush=False, bind=engine) as session:
        appartment_favourite = Favourites(
            user_id=person_id,
            url=appartment[2].strip()[1::],
            info=appartment[0].strip()[1::],
            price=appartment[1].strip()[1::]
        )
        session.add(appartment_favourite)
        session.commit()


def delete_favourite(appartment: dict, person_id: int):
    with Session(autoflush=False, bind=engine) as session:
        session.query(Favourites).filter_by(info=appartment[0].strip()[1::],
                                            price=appartment[1].strip()[1::],
                                            user_id=person_id,
                                            url=appartment[2].strip()[1::]).\
            delete(synchronize_session='evaluate')

        session.commit()


def get_favourites(person_id: int):
    with Session(autoflush=False, bind=engine) as session:
        appartments = session.query(
            Favourites).filter(Favourites.user_id == str(person_id)).all()

        return appartments


def get_url_favourites(person_id: int):
    with Session(autoflush=False, bind=engine) as session:
        url_appartments = session.query(
            Favourites.url).filter(Favourites.user_id == str(person_id)).all()

        return url_appartments

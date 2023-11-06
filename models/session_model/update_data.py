from sqlalchemy.orm import Session

from db.db import engine
from models.appartments import Appartments


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

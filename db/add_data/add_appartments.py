from sqlalchemy.orm import Session

from db.db import engine
from models.appartments import Appartments


def add_appartments(appartments: dict, person_id: int):
    with Session(autoflush=False, bind=engine) as session:
        count_appartments = len(appartments['info'])
        for i in range(count_appartments + 1):
            app = Appartments(
                user_id=person_id,
                url=appartments['url'][i],
                info=appartments['info'][i],
                price=appartments['price'][i]
            )
        session.add(app)
        session.commit()

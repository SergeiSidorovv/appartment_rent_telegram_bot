from sqlalchemy.orm import Session

from db.db import engine
from models.appartments import Appartments


def delete_appartments(person_id: int):
    with Session(autoflush=False, bind=engine) as session:
        person_appaprtments = session.query(
            Appartments).filter_by(user_id=str(person_id))
        session.delete(person_appaprtments)
        session.commit()

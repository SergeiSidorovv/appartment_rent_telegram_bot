from sqlalchemy.orm import Session

from db.db import engine
from models.appartments import Appartments


def get_appartment(person_id: int):
    with Session(autoflush=False, bind=engine) as session:
        appartments = session.query(
            Appartments).filter_by(user_id=str(person_id))
        for i in appartments:
            advertisement = {}
            advertisement['url'] = i[1]
            advertisement['info'] = i[2]
            advertisement['price'] = i[3]

            yield advertisement
    yield None

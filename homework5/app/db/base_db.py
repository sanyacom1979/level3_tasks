from sqlalchemy.orm.decl_api import DeclarativeAttributeIntercept
from typing import Union
from app.db.base import get_session


class DbBase:
    data_model: Union[DeclarativeAttributeIntercept, None] = None

    def add(self, data: dict):
        with get_session() as session:
            if self.data_model is not None:
                to_add = self.data_model(**data)
                session.add(to_add)
                session.commit()

    def get(self, filtered_by: dict):
        with get_session() as session:
            return session.query(self.data_model).filter_by(**filtered_by).first()

    def get_many(self, filtered_by: dict):
        with get_session() as session:
            return session.query(self.data_model).filter_by(**filtered_by).all()

    def delete(self, filtered_by: dict):
        with get_session() as session:
            to_delete = session.query(self.data_model).filter_by(**filtered_by).first()
            session.delete(to_delete)
            session.commit()

    def update(self, filtered_by: dict, upd_data: dict):
        with get_session() as session:
            session.query(self.data_model).filter_by(**filtered_by).update(upd_data)
            session.commit()

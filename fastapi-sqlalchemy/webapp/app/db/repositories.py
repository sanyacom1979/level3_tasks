"""Repositories module."""

from contextlib import AbstractContextManager
from typing import Callable, Iterator, Union


from app.db.models import User


class DbRepository:

    data_model = None
   

    def __init__(self, session_factory: Callable[..., AbstractContextManager]) -> None:
        self.session_factory = session_factory

    def get_all(self) -> Iterator:
        with self.session_factory() as session:
            return session.query(self.data_model).all()

    def get_by_id(self, filtered_by: dict) -> User:
        with self.session_factory() as session:
            return session.query(self.data_model).filter_by(**filtered_by).first()
            

    def add(self, data: dict) -> User:
        with self.session_factory() as session:
            to_add = self.data_model(**data)
            session.add(to_add)
            session.commit()
            session.refresh(to_add)
            return to_add

    def delete_by_id(self, filtered_by: dict) -> None:
        with self.session_factory() as session:
            to_delete = session.query(self.data_model).filter_by(**filtered_by).first()
            session.delete(to_delete)
            session.commit()


class NotFoundError(Exception):

    entity_name: str

    def __init__(self, entity_id):
        super().__init__(f"{self.entity_name} not found, id: {entity_id}")


class UserNotFoundError(NotFoundError):

    entity_name: str = "User"


class UserRepository(DbRepository):
    data_model = User

    def get_by_id(self, filtered_by_user: dict) -> User:
        with self.session_factory() as session:
            res = session.query(self.data_model).filter_by(**filtered_by_user).first()
            if not res:
                raise UserNotFoundError(filtered_by_user["id"])
            return res

    def delete_by_id(self, filtered_by_user: dict) -> None:
        with self.session_factory() as session:
            to_delete = session.query(self.data_model).filter_by(**filtered_by_user).first()
            if not to_delete:
                raise UserNotFoundError(filtered_by_user["id"])
            session.delete(to_delete)
            session.commit()
from datetime import datetime

from base_db import DbBase
from db.models import User


# def add_user(session: Session, name: str, birthday: datetime, work_quality: int, password: str) -> None:
#     user = User(name=name, birthday=birthday, work_quality=work_quality, password=password)
#     session.add(user)
#     session.commit()
#
#
# def get_user(session: Session, user_id: int) -> User | None:
#     return session.query(User).filter_by(id=user_id).first()
#
#
# def delete_user(session: Session, user_id: int) -> None:
#     user = session.query(User).filter_by(id=user_id).first()
#     session.delete(user)
#     session.commit()
#
#
# def change_password(session: Session, user_id: int, new_password: str) -> User:
#     user = session.query(User).filter_by(id=user_id).first()
#     user.password = new_password
#     session.add(user)
#     session.commit()
#     return get_user(session, user_id)


class DbUsers(DbBase):
    data_model = User


if __name__ == "__main__":
    
    db = DbUsers()
    """
    d = {"mail": "my5@yandex.ru", "password": "22345", "balance": 0, "registered_date": "2023-03-04" }
    db.add(d)

    d = {"mail": "my6@yandex.ru", "password": "525345", "balance": 0, "registered_date": "2023-03-04" }
    db.add(d)
    """
    print("Получение из таблицы")

    u = db.get({"mail": "max_max@gmail.com"})
    print(f"{u.id}, {u.balance}, {u.password}")

    u = db.get({"mail": "alex1979@gmail.com"})
    print(f"{u.id}, {u.balance}, {u.password}")

    u = db.get({"mail": "my2@mail.ru"})
    print(f"{u.id}, {u.balance}, {u.password}")

    print("__________________________________")

    print("До update")

    u = db.get({"id": 5})
    print(f"{u.id}, {u.balance}, {u.password}")

    u = db.get({"id": 8})
    print(f"{u.id}, {u.balance}, {u.password}")

    lst_id_to_upd = [5, 8]
    for i in lst_id_to_upd:
        db.update({"id": i}, {"password": "55555555", "balance" : 0})
    
    print("__________________________________")

    print("После update")

    u = db.get({"id": 5})
    print(f"{u.id}, {u.balance}, {u.password}")

    u = db.get({"id": 8})
    print(f"{u.id}, {u.balance}, {u.password}")

   
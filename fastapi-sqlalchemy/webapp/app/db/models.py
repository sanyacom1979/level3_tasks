"""Models module."""

from sqlalchemy import Column, String, Boolean, Integer, DateTime

from app.db.database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    mail = Column(String, unique=True)
    password = Column(String)
    balance = Column(Integer)
    registered_date = Column(DateTime)

    def __repr__(self):
        return f"<User(id={self.id}, " \
               f"mail=\"{self.mail}\", " \
               f"password=\"{self.password}\", " \
               f"balance={self.balance}, " \
               f"registered_date=\"{self.registered_date}\")>"

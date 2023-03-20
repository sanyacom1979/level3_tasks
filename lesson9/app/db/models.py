from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    mail = Column(String, unique=True)
    password = Column(String)
    balance = Column(Integer)
    registered_date = Column(DateTime)
    comment = Column(String)

    def to_dict(self):
        return {"mail" : self.mail, "password" : self.password, "balance" : self.balance, "registered_date" : self.registered_date}

    def __str__(self):
        return f"Пользователь: номер {self.id}, e_mail {self.mail}, пароль {self.password}, баланс {self.balance}, дата регистрации {self.registered_date}."

"""
class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    amount = Column(Integer)
    date = Column(DateTime)
    completed = Column(Boolean)
    user = relationship("User", backref="payments_users", lazy="joined")

    def to_dict(self):
        return {"user_id" : self.user_id, "amount" : self.amount, "date" : self.date, "completed" : self.completed}

    def __str__(self):
        return f"Пользователь: номер {self.user_id}, пополнил {self.amount}, дата пополнения {self.date}, завершил {self.completed}."

"""
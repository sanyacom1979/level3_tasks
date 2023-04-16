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

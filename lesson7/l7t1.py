from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


from sqlalchemy import Column, Integer, String, DateTime


from pydantic import BaseSettings




class Base(DeclarativeBase):
	pass


class Users(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True, autoincrement=True)
	mail = Column(String)
	password = Column(DateTime)
	balance = Column(Integer)
	registered_date = Column(DateTime)

	def __str__(self):
		return f"Пользователь: номер {self.id}, e_mail {self.mail}, пароль {self.password}, баланс {self.balance}, дата регистрации {self.registered_date}."



class DatabaseConfig(BaseSettings):
    login: str = "admin"
    password: str = "admin"
    host: str = "localhost"
    port: str = "5432"
    database: str = "my_db"


config = DatabaseConfig()
db_url = f"postgresql://{config.login}:{config.password}@{config.host}:{config.port}/{config.database}"
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)


def get_users():
    session = Session()
    users = session.query(Users).all()
    session.close()
    return users

u = get_users()

for i in u: 
	print(i)



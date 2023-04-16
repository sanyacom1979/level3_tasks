from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from contextlib import contextmanager, AbstractContextManager
from typing import Callable
from config import config

db_url = f"postgresql://{config.login}:{config.password}@{config.host}:{config.port}/{config.database}"
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    ...


@contextmanager
def get_session() -> Session:
    session = Session()
    yield session
    session.close()

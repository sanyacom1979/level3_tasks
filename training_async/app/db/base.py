from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from contextlib import contextmanager, AbstractContextManager
from typing import Callable
from config import config

db_url = f"postgresql+asyncpg://{config.login}:{config.password}@{config.host}:{config.port}/{config.database}"
engine = create_async_engine(db_url)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


class Base(DeclarativeBase):
    ...

"""
@contextmanager
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
        session.close()
"""

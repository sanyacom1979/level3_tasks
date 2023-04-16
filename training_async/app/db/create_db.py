from db.base import engine, Base
from db.models import User


async with engine.begin() as conn:
	await conn.run_sync(Base.metadata.drop_all)
	await conn.run_sync(Base.metadata.create_all(tables=[User.__table__]))
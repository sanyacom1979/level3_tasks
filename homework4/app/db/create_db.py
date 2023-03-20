from db.base import engine, Base
from db.models import User

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine, tables=[city_distances.__table__])
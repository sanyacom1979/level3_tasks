from db.base import engine, Base
from db.models import CityDistance

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine, tables=[CityDistance.__table__])
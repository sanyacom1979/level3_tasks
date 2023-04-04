from app.db.base_db import DbBase
from app.db.models import CityDistance


class DbCityDistances(DbBase):
    data_model = CityDistance

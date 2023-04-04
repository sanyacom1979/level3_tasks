from fastapi import Depends

from app.db.db_cities import DbCityDistances
from app.services.city_services import ServiceCityDistance


def db_dependency() -> DbCityDistances:
    return DbCityDistances()


def city_distance_dependency(
    db: DbCityDistances = Depends(db_dependency),
) -> ServiceCityDistance:
    return ServiceCityDistance(db)

import pytest
from typing import Union

from app.city_distance.city_distance_without_db import min_city_distance
from app.city_distance.city_distance_with_db import min_city_distance_db
from app.services.city_services import ServiceCityDistance
from app.dependencies import city_distance_dependency


class CityDistanceServiceForTest:
    _city_distance_service: Union[ServiceCityDistance, None] = None

    @classmethod
    def get_city_distance_service(cls) -> ServiceCityDistance:
        if cls._city_distance_service is None:
            cls._city_distance_service = city_distance_dependency()
        return cls._city_distance_service


@pytest.mark.parametrize(
    "city_start, city_finish, result",
    [(17, 0, {"body": {"path": [17, 4, 0], "distance": 4}}), (17, 17, None)],
)
def test_min_city_distance(city_start, city_finish, result):
    assert min_city_distance(city_start, city_finish) == result


@pytest.mark.parametrize(
    "city_start, city_finish, city_distance_service, result",
    [
        (
            17,
            0,
            CityDistanceServiceForTest.get_city_distance_service(),
            {"body": {"path": [17, 4, 0], "distance": 4}},
        ),
        (17, 17, CityDistanceServiceForTest.get_city_distance_service(), None),
    ],
)
def test_min_city_distance_db(city_start, city_finish, city_distance_service, result):
    assert (
        min_city_distance_db(city_start, city_finish, city_distance_service) == result
    )

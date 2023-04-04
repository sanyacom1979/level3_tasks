import pytest


@pytest.mark.parametrize(
    "city_start, city_finish, header, resp_status, resp_json",
    [
        (0, 9, "123321", 200, {"body": {"path": [0, 23, 9], "distance": 2}}),
        (0, 9, "", 401, {"detail": "Wrong api key"}),
        (9, 9, "123321", 404, {"detail": "No road"}),
    ],
)
def test_get_city_route_no_db(
    test_client, city_start, city_finish, header, resp_status, resp_json
):
    response = test_client.get(
        "/api/cities_no_db",
        params={"city_start": city_start, "city_finish": city_finish},
        headers={"x-api-key": header},
    )
    assert response.status_code == resp_status
    assert response.json() == resp_json


@pytest.mark.parametrize(
    "city_start, city_finish, header, resp_status, resp_json",
    [
        (0, 9, "123321", 200, {"body": {"path": [0, 23, 9], "distance": 2}}),
        (0, 9, "", 401, {"detail": "Wrong api key"}),
        (9, 9, "123321", 404, {"detail": "No road"}),
    ],
)
def test_get_city_route_with_db(
    test_client, city_start, city_finish, header, resp_status, resp_json
):
    response = test_client.get(
        "/api/cities_with_db",
        params={"city_start": city_start, "city_finish": city_finish},
        headers={"x-api-key": header},
    )
    assert response.status_code == resp_status
    assert response.json() == resp_json

import requests
from app.city_distance.read_matrix import read_matrix


def send_matrix():
    url = "http://127.0.0.1:8080/api/cities_with_db"
    distances = read_matrix()
    for city_from, city_item in enumerate(distances):
        for city_to, dst in enumerate(city_item):
            requests.post(
                url=url,
                json={"city_from": city_from, "city_to": city_to, "distance": int(dst)},
                headers={"x-api-key": "123321"},
            )

from datetime import datetime
from typing import Tuple

from aiohttp import ClientSession
from geopy.geocoders import Nominatim
from pydantic import BaseModel


class Probe(BaseModel):
    time: datetime
    temperature: float
    wind_speed: float


class OpenMeteApi:
    def __init__(self, url: str):
        self.url = url
        self.geolocator = Nominatim(user_agent="meteo-app")

    def _get_city_coordinates(self, city: str) -> Tuple[float, float]:
        location = self.geolocator.geocode(city)
        return location.latitude, location.longitude

    async def forecats(self, city: str) -> list:
        lat, lon = self._get_city_coordinates(city)
        async with ClientSession() as session:
            url = f"{self.url}?latitude={lat}&longitude={lon}&hourly=temperature_2m,windspeed_10m"
            async with session.get(url=url) as resp:
                res = await resp.json()
                result = []
                for time, temp, wind in zip(
                    res["hourly"]["time"],
                    res["hourly"]["temperature_2m"],
                    res["hourly"]["windspeed_10m"],
                ):
                    result.append(Probe(time=time, temperature=temp, wind_speed=wind))
                return result

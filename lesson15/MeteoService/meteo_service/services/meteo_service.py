from integrations.open_meteo_api import OpenMeteApi, Probe


class MeteoService:
    def __init__(self, open_meteo_api: OpenMeteApi):
        self._open_meteo_api = open_meteo_api

    async def __call__(self, city: str) -> list:
        return await self._open_meteo_api.forecats(city)

from fastapi import Depends

from config import Config
from integrations.open_meteo_api import OpenMeteApi
from services.meteo_service import MeteoService


def settings_dependency() -> Config:
    return Config()


def open_meteo_api_dependency(
    config: Config = Depends(settings_dependency),
) -> OpenMeteApi:
    return OpenMeteApi(config.open_meteo_api)


def meteo_service_dependency(
    open_meteo_api: OpenMeteApi = Depends(open_meteo_api_dependency),
) -> MeteoService:
    return MeteoService(open_meteo_api)

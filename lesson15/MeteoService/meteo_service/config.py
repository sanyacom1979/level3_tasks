from pydantic import BaseSettings


class Config(BaseSettings):
    open_meteo_api: str = "https://api.open-meteo.com/v1/forecast"

from fastapi import APIRouter, Depends

from dependencies import meteo_service_dependency
from integrations.open_meteo_api import Probe
from services.meteo_service import MeteoService

router = APIRouter(
    prefix="/api",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/weather", response_model=list)
async def get_weather(
    city: str, meteo_service: MeteoService = Depends(meteo_service_dependency)
) -> list:
    return await meteo_service(city)

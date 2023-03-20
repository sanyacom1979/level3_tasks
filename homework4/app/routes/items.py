from typing import Union

from fastapi import APIRouter, HTTPException, Depends, Header
from pydantic import BaseModel

from app.dependencies import city_distance_dependency
from app.services.city_services import ServiceCityDistance
from app.city_distance.city_distance_without_db import min_city_distance
from app.city_distance.city_distance_with_db import min_city_distance_db

router = APIRouter(
    prefix="/api",
    tags=["cities"],
    responses={404: {"description": "Not found"}},
)


class MinDistanceResponse(BaseModel):
    path : list
    distance : int


class MinDistanceResponseFull(BaseModel):
    body : MinDistanceResponse
    

class BodyToDBMinDistances(BaseModel):
    city_from : int
    city_to : int
    distance : int



@router.get("/cities_no_db", response_model=MinDistanceResponseFull)
def get_city_route_no_db(
    city_start: int,
    city_finish: int,
    x_api_key: Union[str, None] = Header(default=None)
) -> MinDistanceResponseFull:
    if x_api_key != "123321":
        raise HTTPException(status_code=401, detail=f"Wrong api key")
    city_short_route = min_city_distance(city_start, city_finish)
    if city_short_route is None:
        raise HTTPException(status_code=404, detail=f"No road")
    return city_short_route



@router.get("/cities_with_db", response_model=MinDistanceResponseFull)
def get_city_route_with_db(
    city_start: int,
    city_finish: int,
    city_distance_service: ServiceCityDistance=Depends(city_distance_dependency),
    x_api_key: Union[str, None] = Header(default=None)
) -> MinDistanceResponseFull:
    if x_api_key != "123321":
        raise HTTPException(status_code=401, detail=f"Wrong api key")
    city_short_route = min_city_distance_db(city_start, city_finish, city_distance_service)
    if city_short_route is None:
        raise HTTPException(status_code=404, detail=f"No road")
    return city_short_route



@router.post("/cities_with_db")
def add_city_to_db(
    city_item: BodyToDBMinDistances,
    city_distance_service: ServiceCityDistance=Depends(city_distance_dependency),
    x_api_key: Union[str, None] = Header(default=None)
    ):
    if x_api_key != "123321":
        raise HTTPException(status_code=401, detail=f"Wrong api key")
    city_distance_service.add_city_distance({"city_from" : city_item.city_from, "city_to" : city_item.city_to, "distance" : city_item.distance})


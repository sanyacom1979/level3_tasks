"""Endpoints module."""

from datetime import date
from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide
from pydantic import BaseModel 

from app.db.containers import Container
from app.services.services import UserService
from app.db.repositories import NotFoundError

router = APIRouter(
    prefix="/api",
    tags=["users"],
    responses={404: {"description": "Not found"},
        201: {"description": "Created"},
        204: {"description": "No content"}   
    },
)


class UserResponse(BaseModel):
    id: int
    mail: str
    password: str
    balance : int
    registered_date : date

    class Config:
        orm_mode = True


class BodyToAddUser(BaseModel):
    mail: str
    password: str
    balance: int
    registered_date: date


@router.get("/users")
@inject
def get_list(
        user_service: UserService = Depends(Provide[Container.user_service]),
):
    return user_service.get_users()



@router.get("/users/{user_id}", response_model=UserResponse)
@inject
def get_by_id(
        user_id: int,
        user_service: UserService = Depends(Provide[Container.user_service]),
) -> UserResponse:
    try:
        return user_service.get_user_by_id(user_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)



@router.post("/users", status_code=status.HTTP_201_CREATED)
@inject
def add(
        user_item: BodyToAddUser,
        user_service: UserService = Depends(Provide[Container.user_service]),
):
    return user_service.create_user(
        {
            "mail": user_item.mail,
            "password": user_item.password,
            "balance": user_item.balance,
            "registered_date": user_item.registered_date
        }
    )



@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
def remove(
        user_id: int,
        user_service: UserService = Depends(Provide[Container.user_service]),
):
    try:
        user_service.delete_user_by_id(user_id)
    except NotFoundError:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)



@router.get("/status")
def get_status():
    return {"status": "OK"}

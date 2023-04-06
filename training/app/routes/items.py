from datetime import date
from typing import Union

from fastapi import APIRouter, HTTPException, Depends, Header
from pydantic import BaseModel

from app.dependencies import get_user_dependency
from app.dependencies import add_user_dependency

from app.services.user_service import GetUser
from app.services.user_service import AddUser

#from app.db.db_user import db_users

router = APIRouter(
    prefix="/api",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


class UserResponse(BaseModel):
    id: int
    mail: str
    password: str
    balance : int
    registered_date : date
    comment: Union[str, None]

    class Config:
        orm_mode = True


class BodyToAddUser(BaseModel):
    mail: str
    password: str
    balance: int
    registered_date: date


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, 
    get_user_service: GetUser=Depends(get_user_dependency),
    my_header: Union[str, None]=Header(default=None)
) -> UserResponse:
    
    if get_user_service(user_id) is None:
        raise HTTPException(status_code=404, detail=f"User not found")
    return get_user_service(user_id)


@router.post("/users")
def get_user(user_item: BodyToAddUser, 
    add_user_service: AddUser=Depends(add_user_dependency),
) -> None:
    
    add_user_service(
        {
            "mail": user_item.mail,
            "password": user_item.password,
            "balance": user_item.balance,
            "registered_date": user_item.registered_date
        }
    )
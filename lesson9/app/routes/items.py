from datetime import date
from typing import Union

from fastapi import APIRouter, HTTPException, Depends, Header
from pydantic import BaseModel

from app.dependencies import get_user_dependency
from app.services.get_user_service import GetUser

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


@router.get("/users/{user_id}", response_model=UserResponse)
def get_user(user_id: int, 
    get_user_service: GetUser=Depends(get_user_dependency),
    my_header: Union[str, None]=Header(default=None)
) -> UserResponse:
    #user = db_users.get({"id": user_id})
    #if user is None:
    #    raise HTTPException(status_code=404, detail=f"User not found")
    #return user
    if get_user_service(user_id) is None:
        raise HTTPException(status_code=404, detail=f"User not found")
    return get_user_service(user_id)
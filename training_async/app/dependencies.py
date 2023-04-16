from fastapi import Depends

from app.db.db_user import DbUsers
from app.services.user_service import GetUser
from app.services.user_service import AddUser



def db_dependency() -> DbUsers: 
	return DbUsers()


def get_user_dependency(
	db: DbUsers = Depends(db_dependency)
) -> GetUser:
	
	return GetUser(db)


def add_user_dependency(
	db: DbUsers = Depends(db_dependency)
) -> AddUser:

	return AddUser(db)

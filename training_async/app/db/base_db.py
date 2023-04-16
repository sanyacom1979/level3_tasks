#from contextlib import AbstractContextManager
#from typing import Callable

from sqlalchemy.orm import Session

class DbBase():

    data_model = None

    
    def add(self, session, data: dict):
        to_add = self.data_model(**data)
        session.add(to_add)



    async def get(self, session, filtered_by: int):
        return await session.get(self.data_model, filtered_by)

"""

    async def delete(self, session, filtered_by: dict):
        to_delete = await session.query(self.data_model).filter_by(**filtered_by).first()
        session.delete(to_delete)
        await session.commit()


    
    async def update(self, session, filtered_by: dict, upd_data: dict):
        await session.query(self.data_model).filter_by(**filtered_by).update(upd_data)
        await session.commit()
"""


#from contextlib import AbstractContextManager
#from typing import Callable

from sqlalchemy.orm import Session

class DbBase():

    data_model = None

    
    def add(self, session, data: dict):
        to_add = self.data_model(**data)
        session.add(to_add)
        session.commit()



    def get(self, session, filtered_by: dict):
        return session.query(self.data_model).filter_by(**filtered_by).first()



    def delete(self, session, filtered_by: dict):
        to_delete = session.query(self.data_model).filter_by(**filtered_by).first()
        session.delete(to_delete)
        session.commit()


    
    def update(self, session, filtered_by: dict, upd_data: dict):
        session.query(self.data_model).filter_by(**filtered_by).update(upd_data)
        session.commit()


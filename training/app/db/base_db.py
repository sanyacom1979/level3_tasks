

class DbBase():
    data_model = None

    def __init__(self, session):
        self.session = session


    def add(self, data: dict):
        with self.session() as session:
            to_add = self.data_model(**data)
            session.add(to_add)
            session.commit()



    def get(self, filtered_by: dict):
        with self.session() as session:
            return session.query(self.data_model).filter_by(**filtered_by).first()



    def delete(self, filtered_by: dict):
        with self.session() as session:
            to_delete = session.query(self.data_model).filter_by(**filtered_by).first()
            session.delete(to_delete)
            session.commit()


    
    def update(self, filtered_by: dict, upd_data: dict):
        with self.session() as session:
            session.query(self.data_model).filter_by(**filtered_by).update(upd_data)
            session.commit()


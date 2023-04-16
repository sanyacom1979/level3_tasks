from app.db.db_user import DbUsers

class GetUser():

	def __init__(self, db: DbUsers):
		self.db_ = db


	def __call__(self, session, user_id):
		return self.db_.get(session, user_id)


class AddUser():

	def __init__(self, db: DbUsers):
		self.db_ = db


	def __call__(self, session, user_row):
		self.db_.add(session, user_row)
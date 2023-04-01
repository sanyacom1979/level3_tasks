from app.db.db_cities import DbCityDistances

class ServiceCityDistance():

	def __init__(self, db: DbCityDistances):
		self.db_ = db


	def add_city_distance(self, city_distance_record):
		self.db_.add(city_distance_record)

	
	def get_city_distances(self, city_from):
		return self.db_.get_many({"city_from" : city_from})

	
	def get_cities(self):
		return self.db_.get_many({})

	
	
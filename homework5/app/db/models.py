from sqlalchemy import Column, Integer
from app.db.base import Base


class CityDistance(Base):
    __tablename__ = "city_distances"

    id = Column(Integer, primary_key=True, autoincrement=True)
    city_from = Column(Integer, nullable=False)
    city_to = Column(Integer, nullable=False)
    distance = Column(Integer, nullable=False)

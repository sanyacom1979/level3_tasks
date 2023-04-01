import math
from app.city_distance.read_matrix import read_matrix
from app.dependencies import city_distance_dependency
from app.services.city_services import ServiceCityDistance


def min_city_distance_db(
	city_start: int, 
	city_finish: int, 
	city_distance_service: ServiceCityDistance
) -> dict:
	set_cities = set(row.city_from for row in city_distance_service.get_cities())
	route_lst = [[math.inf, False, []] for _ in set_cities]		
	route_lst[city_start][0] = 0
	route_lst[city_start][2].append(city_start)	
	city_temp = city_start
	for _ in set_cities:
		rows = city_distance_service.get_city_distances(city_temp)											
		for city_to, dst in zip((row.city_to for row in rows), (row.distance for row in rows)):
			if dst and not route_lst[city_to][1]:
				if route_lst[city_to][0] > route_lst[city_temp][0] + dst:
					route_lst[city_to][0] = route_lst[city_temp][0] + dst
					route_lst[city_to][2].clear()		
					for el in route_lst[city_temp][2]:
						route_lst[city_to][2].append(el)
					route_lst[city_to][2].append(city_to)					
		route_lst[city_temp][1] = True
		min_item = math.inf
		for i, item in enumerate(route_lst):
			if not item[1]:
				if item[0] < min_item:
					city_next, min_item = i, item[0]	
		city_temp = city_next	
	if len(route_lst[city_finish][2]) < 2:
		return None
	return to_json_db(route_lst[city_finish][2], route_lst[city_finish][0])


def to_json_db(rt: list, dst: int) -> dict:
	return {"body" : {"path" : rt, "distance" : dst}}
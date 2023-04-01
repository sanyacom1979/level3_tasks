import math
from app.city_distance.read_matrix import read_matrix

def min_city_distance(city_start: int, city_finish: int) -> dict:
	distances = read_matrix()
	route_lst = [[math.inf, False, []] for _ in range(len(distances))]
	route_lst[city_start][0] = 0
	route_lst[city_start][2].append(city_start)	
	city_temp = city_start
	for _ in range(len(distances)):
		for i, item in enumerate(distances[city_temp]):
			if item and not route_lst[i][1]:
				if route_lst[i][0] > route_lst[city_temp][0] + item:
					route_lst[i][0] = route_lst[city_temp][0] + item
					route_lst[i][2].clear()		
					for el in route_lst[city_temp][2]:
						route_lst[i][2].append(el)
					route_lst[i][2].append(i)					
		route_lst[city_temp][1] = True
		min_item = math.inf
		for i, item in enumerate(route_lst):
			if not item[1]:
				if item[0] < min_item:
					city_next, min_item = i, item[0]	
		city_temp = city_next	
	if len(route_lst[city_finish][2]) < 2:
		return None
	return to_json(route_lst[city_finish][2], route_lst[city_finish][0])


def to_json(rt: list, dst: int) -> dict:
	return {"body" : {"path" : rt, "distance" : dst}}
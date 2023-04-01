from app.routes.items import get_city_route_no_db

city_start = 0
city_finish = 9

def test_get_city_route_no_db(test_client):
	response = test_client.get("/api/cities_no_db", params={"city_start" : city_start, "city_finish" : city_finish}, headers={"x-api-key" : "123321"} )
	assert response.status_code == 200
	assert response.json() == {"body" : {"path" : [0, 23, 9], "distance" : 2}}



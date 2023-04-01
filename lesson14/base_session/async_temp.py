
import asyncio
import time
from aiohttp import ClientSession


cashe = {}

async def get_my_temp(lat: float, lon: float) -> float:
	async with ClientSession() as session:
		url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
		async with session.get(url=url) as resp:
			res = await resp.json()
			return res["current_weather"]["temperature"]


async def run(lat, lon):

	
	start = time.time()

	if (lat, lon) in cashe:
		print(time.time() - start)
		return cashe[(lat, lon)]

	task = asyncio.create_task(get_my_temp(lat, lon))
	
	
	res = await task

	cashe[(lat, lon)] = res
	
	print(time.time() - start)

	return res
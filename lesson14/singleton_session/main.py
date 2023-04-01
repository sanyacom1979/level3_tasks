
import uvicorn
import asyncio

from fastapi import FastAPI
from fastapi.logger import logger as fastAPI_logger 


from async_temp import run
from singleton_aiohttp import SingletonAiohttp



async def on_start_up() -> None:
    fastAPI_logger.info("on_start_up")
    SingletonAiohttp.get_aiohttp_client()


async def on_shutdown() -> None:
    fastAPI_logger.info("on_shutdown")
    await SingletonAiohttp.close_aiohttp_client()


app = FastAPI(docs_url="/", on_startup=[on_start_up], on_shutdown=[on_shutdown])




@app.get("/temp")
async def get_temp(lat: float, lon: float) -> float:
    return await run(lat, lon)


if __name__ == "__main__":
    uvicorn.run(app, port=8080)

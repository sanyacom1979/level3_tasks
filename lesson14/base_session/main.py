
import uvicorn
import asyncio
from fastapi import FastAPI

from async_temp import get_my_temp, run

app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/temp")
async def get_temp(lat: float, lon: float) -> float:
    return await run(lat, lon)


if __name__ == "__main__":
    uvicorn.run(app, port=8080)

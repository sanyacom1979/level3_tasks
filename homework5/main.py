import uvicorn
from fastapi import FastAPI

from app.routes.items import router
from send_matrix import send_matrix


app = FastAPI()
app.include_router(router)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/")
def send_to_route_cities_with_db():
    send_matrix()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

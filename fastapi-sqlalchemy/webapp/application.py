"""Application module."""
import uvicorn
from fastapi import FastAPI

from app.db.containers import Container
from app.routes.endpoints import router


def create_app() -> FastAPI:
    container = Container()

    db = container.db()
    #db.create_database()

    app = FastAPI()
    app.container = container
    app.include_router(router)
    return app


app = create_app()


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)

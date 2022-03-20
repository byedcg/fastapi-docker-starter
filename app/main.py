import logging
import time
from functools import lru_cache
from logging.config import dictConfig

from fastapi import Depends, FastAPI, Request, Response

from app.routers import background

from . import models
from .config import LogConfig, Settings
from .routers import echo, files


@lru_cache()  # prevent from reading .env file every request
def get_settings():
    return Settings()


app = FastAPI()
app.include_router(echo.router, prefix="/echo")
app.include_router(files.router, prefix="/files")
app.include_router(background.router, prefix="/background")

# Setup logging
dictConfig(LogConfig().dict())
logger = logging.getLogger("app_logging")


@app.on_event("startup")
async def startup():
    logger.info("Starting up")
    # logger.info("Dummy Info")
    # logger.error("Dummy Error")
    # logger.debug("Dummy Debug")
    # logger.warning("Dummy Warning")


@app.on_event("shutdown")
async def shutdown():
    logger.info("Shutting down application")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/info")
async def info(settings: Settings = Depends(get_settings)):
    return {"app_name": settings.app_name}


@app.get("/bye")
async def bye():
    return {"message": "Bye bye!"}


# middleware run on every request
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response: Response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.post("/send")
def send_data(item: models.Item):
    item_dict = item.dict()
    return item_dict


if __name__ == "__main__":
    # debug mode
    import os

    import uvicorn

    logger.setLevel(logging.DEBUG)

    port = int(os.environ.get("DEV_PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

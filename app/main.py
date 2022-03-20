import time
from functools import lru_cache
from typing import Optional

from fastapi import Depends, FastAPI, Request, Response
from pydantic import BaseModel

from .config import Settings


@lru_cache()  # prevent from reading .env file every request
def get_settings():
    return Settings()


app = FastAPI()


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


@app.get("/echo/{message}")
async def echo(message: str, query: Optional[str] = None):
    time.sleep(1)
    return {"message": message, "query": query}


# data model
class Item(BaseModel):
    name: str
    description: Optional[str] = None


@app.post("/send")
async def send_data(item: Item):
    item_dict = item.dict()
    return item_dict


if __name__ == "__main__":
    # debug mode
    import uvicorn
    import os

    port = int(os.environ.get("DEV_PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

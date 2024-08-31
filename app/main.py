from fastapi import FastAPI

from contextlib import asynccontextmanager
import uvicorn

from api.endpoints.product import product_router
from api.endpoints.category import category_router

from database import database

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    try:
      yield
    finally:
      await database.disconnect


app = FastAPI(lifespan=lifespan)


app.include_router(product_router, prefix="/products")
app.include_router(category_router, prefix="/categories")


@app.get("/")
async def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

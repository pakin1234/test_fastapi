from fastapi import FastAPI

from api.endpoints.product import product_router
from api.endpoints.category import category_router

from database import database

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(product_router, prefix="/products")
app.include_router(category_router, prefix="/categories")


@app.get("/")
async def read_root():
    return {"Hello": "World"}
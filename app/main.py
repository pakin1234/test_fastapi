from fastapi import FastAPI

from api.endpoints.product import product_router
from api.endpoints.category import category_router

app = FastAPI()
app.include_router(product_router, prefix="/products")
app.include_router(category_router, prefix="/categories")


@app.get("/")
async def read_root():
    return {"Hello": "World"}
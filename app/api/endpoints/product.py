from fastapi import APIRouter, HTTPException
from api.models.schemas import Product, ProductCreate
import crud

from typing import List

product_router = APIRouter()


@product_router.post("/products/", response_model=Product)
async def create_product(product: ProductCreate):
    return await crud.create_product(product)

@product_router.get("/products/", response_model=List[Product])
async def get_products(skip: int = 0, limit: int = 10):
    return await crud.get_product(skip=skip, limit=limit)

@product_router.get("/products/filter/", response_model=List[Product])
async def get_filtered_products(
    name: str = None,
    min_price: int = None,
    max_price: int = None,
    category_id: int = None,
    skip: int = 0,
    limit: int = 10
):
    return await crud.get_filter_product(
        name=name,
        min_price=min_price,
        max_price=max_price,
        category_id=category_id,
        skip=skip,
        limit=limit
    )

@product_router.put("/products/{product_id}/", response_model=Product)
async def update_product(product_id: int, product: ProductCreate):
    return await crud.update_product(product_id=product_id, new_product_data=product)

@product_router.delete("/products/{product_id}/")
async def delete_product(product_id: int):
    result = await crud.delete_product(product_id)
    if not result:
        raise HTTPException(status_code=404, detail="Product not found")
    return result





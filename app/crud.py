from database import database
from api.models.model import categories, products
from api.models.schemas import Category, CategoryCreate, Product, ProductCreate

from sqlalchemy import and_

from typing import Optional, List

async def create_category(category: CategoryCreate):
    query = categories.insert().values(title=category.title)
    category_id = await database.execute(query)
    return {"id": category_id, "title": category.title}

async def get_category(skip: int = 0, limit: int = 0):
    query = categories.select().offset(skip).limit(limit)
    return await database.fetch_all(query)

async def create_product(product: ProductCreate):
    query = products.insert().values(name=product.name, price=product.price, description=product.description, category_id=product.category_id)
    product_id = await database.execute(query)
    return {**product.model_dump(), "id": product_id}

async def update_product(product_id: int, new_product_data: ProductCreate):
    query = products.update().where(products.c.id == product_id).values(name=new_product_data.name, price=new_product_data.price, description=new_product_data.description, category_id=new_product_data.category_id)
    await database.execute(query)
    return{**new_product_data.model_dump(), "id": product_id}

async def delete_product(product_id: int):
    query = products.select().where(products.c.id == product_id)
    product = await database.fetch_one(query)    
    if not product:
        return None

    delete_query = products.delete().where(products.c.id == product_id)
    await database.execute(delete_query)
    return {"message": f"Product with id {product_id} was deleted"}

async def get_product(skip: int = 0, limit: int = 0):
    query = products.select().offset(skip).limit(limit)
    return await database.fetch_all(query)

async def get_filter_product(
    name: Optional[str] = None,
    min_price: Optional[int] = None,
    max_price: Optional[int] = None,
    category_id: Optional[int] = None,
    skip: int = 0,
    limit: int = 100
    ):
    query = products.select()

    filters = []

    if name:
        filters.append(products.c.name.ilike(f"%{name}%"))
    if min_price:
        filters.append(products.c.price >= min_price)
    if max_price:
        filters.append(products.c.price <= max_price)
    if category_id:
        filters.append(products.c.category_id == category_id)

    if filters:
        query = query.where(and_(*filters))

    query = query.offset(skip).limit(limit)

    return await database.fetch_all(query)
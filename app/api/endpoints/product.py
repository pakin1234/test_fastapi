from fastapi import APIRouter

product_router = APIRouter()

# Добавление продукта
@product_router.post("/add")
async def read_product():
    product = "product"
    return {"new_product": product}

# Обновление продукта
@product_router.put("/update/{id}")
async def read_product(id: int):
    product = "new_name_product"
    return {"new_product": product}

# Удаление продукта
@product_router.delete("/delete/{id}")
async def read_product(id: int):
    product = "product"
    return {"delete_product": product}

# Получение информации о продукте
@product_router.get("/info/{id}")
async def read_product(id: int):
    return {"product_info": "id"}

# Список продуктов с фильтрацией по параметрам
@product_router.get("/info")
async def read_product():
    return {"product_info": "id"}





from fastapi import APIRouter, HTTPException
import crud
from api.models.schemas import CategoryCreate

from typing import List

category_router = APIRouter()

@category_router.get("/", response_model=List[CategoryCreate])
async def read_category(skip: int = 0, limit: int = 100):
    return await crud.get_category(skip=skip, limit=limit)

@category_router.post("/", response_model=CategoryCreate)
async def create_category(category: CategoryCreate):
    return await crud.create_category(category=category)


from fastapi import APIRouter

category_router = APIRouter()

@category_router.get("/info")
async def read_product():
    return {"category_info": "info"}


from fastapi.routing import APIRouter

from domain.models import (
    Category,
    CategoryUpdate,
    CategoryCreate,
)
from domain.data.category import (
    list_categories,
    add_category,
    update_category,
    delete_category,
)

category_router = APIRouter(
    tags=['Category']
)


@category_router.get("/list_categories", response_model=list[Category])
async def list_categories_router() -> list[Category]:
    return list_categories()


@category_router.post("/create_category")
async def create_category_router(category_create: CategoryCreate):
    add_category(category_create)


@category_router.put("/update_category")
async def update_category_router(id_: int, category_update: CategoryUpdate):
    update_category(id_, category_update)


@category_router.delete("/delete_category")
async def delete_category_router(id_: int):
    delete_category(id_)

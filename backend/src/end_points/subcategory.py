from fastapi.routing import APIRouter

from domain.models import (
    Subcategory,
    SubcategoryUpdate,
    SubcategoryCreate
)
from domain.data.subcategory import (
    list_subcategories,
    add_subcategory,
    update_subcategory,
    delete_subcategory
)

subcategory_router = APIRouter(
    tags=['Subcategory']
)


@subcategory_router.get("/subcategories", response_model=list[Subcategory])
async def list_subcategories_router() -> list[Subcategory]:
    return list_subcategories()


@subcategory_router.post("/subcategory")
async def create_subcategory_router(subcategory_create: SubcategoryCreate):
    add_subcategory(subcategory_create)


@subcategory_router.put("/subcategory")
async def update_subcategory_router(id_: int, subcategory_update: SubcategoryUpdate):
    update_subcategory(id_, subcategory_update)


@subcategory_router.delete("/subcategory")
async def delete_subcategory_router(id_: int):
    delete_subcategory(id_)

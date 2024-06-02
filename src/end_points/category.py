import logging
from typing import List
from fastapi.routing import APIRouter
from fastapi.responses import Response

from domain.models import (
    Category,
    CategoryUpdate,
    CategoryCreate
)
from domain.data.category import (
    list_categories,
    add_category,
    update_category,
    delete_category
)

category_router = APIRouter(
    tags=['Category']
)


@category_router.get("/categories", response_model=List[Category])
def list_categories_router() -> List[Category]:
    return list_categories()


@category_router.post("/create_category")
def create_category_router(category_create: CategoryCreate):
    add_category(category_create)


@category_router.put("/update_category")
def update_category_router(id_: int, category_update: CategoryUpdate):
    try:
        update_category(id_, category_update)
        return Response(status_code=200)
    except IndexError:
        logging.exception("IndexError")
        return Response(status_code=422)


@category_router.delete("/delete_category")
def delete_category_router(id_: int):
    try:
        delete_category(id_)
    except IndexError:
        logging.exception("IndexError")
        return Response(status_code=422)

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
def get_all_categories():
    return list_categories()


@category_router.post("/create_category")
def category(category_create: CategoryCreate):
    add_category(
        category_create
    )


@category_router.put("/update_category")
def category(category_update: CategoryUpdate):
    try:
        update_category(
            category_update
        )
    except IndexError:
        logging.exception("IndexError")
        return Response(
            status_code=422
        )


@category_router.delete("/delete_category")
def category(id_: int):
    try:
        delete_category(id_)
    except IndexError:
        logging.exception("IndexError")
        return Response(
            status_code=422
        )



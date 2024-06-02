import logging

from typing import List
from fastapi.routing import APIRouter
from fastapi.responses import Response

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


@subcategory_router.get("/subcategories", response_model=List[Subcategory])
def list_subcategories_router() -> List[Subcategory]:
    return list_subcategories()


@subcategory_router.post("/create_subcategory")
def create_subcategory_router(subcategory_create: SubcategoryCreate):
    add_subcategory(subcategory_create)


@subcategory_router.put("/update_subcategory")
def update_subcategory_router(id_: int, subcategory_update: SubcategoryUpdate):
    try:
        update_subcategory(id_, subcategory_update)
    except IndexError:
        logging.exception("IndexError")
        return Response(status_code=422)


@subcategory_router.delete("/delete_subcategory")
def delete_subcategory_router(id_: int):
    try:
        delete_subcategory(id_)
    except IndexError:
        logging.exception("IndexError")
        return Response(status_code=422)

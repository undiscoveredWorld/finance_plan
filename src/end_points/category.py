import logging
from fastapi.routing import APIRouter
from fastapi.responses import JSONResponse, Response

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
def list_categories_router() -> list[Category]:
    return list_categories()


@category_router.post("/create_category")
def create_category_router(category_create: CategoryCreate) -> JSONResponse:
    try:
        add_category(category_create)
    except RuntimeError as e:
        return JSONResponse(
            content={"Error": e.args[0]},
            status_code=422
        )


@category_router.put("/update_category")
def update_category_router(id_: int, category_update: CategoryUpdate) -> Response:
    try:
        update_category(id_, category_update)
        return Response(status_code=200)
    except IndexError as e:
        logging.exception(IndexError)
        return JSONResponse(
            content={"Error": e.args[0]},
            status_code=422
        )


@category_router.delete("/delete_category")
def delete_category_router(id_: int) -> Response:
    try:
        delete_category(id_)
        return Response(status_code=200)
    except IndexError as e:
        logging.exception(IndexError)
        return JSONResponse(
            content={"Error": e.args[0]},
            status_code=422
        )

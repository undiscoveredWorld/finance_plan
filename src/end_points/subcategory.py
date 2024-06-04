import logging

from fastapi.routing import APIRouter
from fastapi.responses import Response, JSONResponse

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


@subcategory_router.get("/list_subcategories", response_model=list[Subcategory])
async def list_subcategories_router() -> list[Subcategory]:
    return list_subcategories()


@subcategory_router.post("/create_subcategory")
async def create_subcategory_router(subcategory_create: SubcategoryCreate) -> Response:
    try:
        add_subcategory(subcategory_create)
        return Response(status_code=200)
    except RuntimeError as e:
        return JSONResponse(
            content={"Error": e.args[0]},
            status_code=422
        )
    except ValueError as e:
        return JSONResponse(
            content={"Error": e.args[0]},
            status_code=422
        )


@subcategory_router.put("/update_subcategory")
async def update_subcategory_router(id_: int, subcategory_update: SubcategoryUpdate) -> Response:
    try:
        update_subcategory(id_, subcategory_update)
        return Response(status_code=200)
    except IndexError as e:
        logging.exception(IndexError)
        return JSONResponse(
            content={"Error": e.args[0]},
            status_code=422
        )
    except ValueError as e:
        logging.exception(IndexError)
        return JSONResponse(
            content={"Error": e.args[0]},
            status_code=422
        )
    except RuntimeError as e:
        logging.exception(IndexError)
        return JSONResponse(
            content={"Error": e.args[0]},
            status_code=422
        )


@subcategory_router.delete("/delete_subcategory")
async def delete_subcategory_router(id_: int) -> Response:
    try:
        delete_subcategory(id_)
        return Response(status_code=200)
    except IndexError as e:
        logging.exception("IndexError")
        return JSONResponse(
            content={"Error": e.args[0]},
            status_code=422
        )

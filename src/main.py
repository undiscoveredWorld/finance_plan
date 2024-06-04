import logging

from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.responses import Response

from common.data import save_data_to_json_file, load_data_to_ram_from_json_file
from end_points.category import category_router
from end_points.subcategory import subcategory_router

logging.basicConfig(level=logging.INFO)

app = FastAPI()
app.include_router(category_router)
app.include_router(subcategory_router)


@app.post("/save")
async def save():
    save_data_to_json_file()
    return Response(status_code=200)


@app.post("/load")
async def load():
    try:
        load_data_to_ram_from_json_file()
        return Response(status_code=200)
    except FileNotFoundError:
        logging.exception("FileNotFound")
        return Response(status_code=422)


@app.exception_handler(ValueError)
async def value_error_handler(_, exc):
    raise HTTPException(
        detail=exc.args[0],
        status_code=400
    )


@app.exception_handler(IndexError)
async def index_error_handler(_, exc):
    raise HTTPException(
        detail=exc.args[0],
        status_code=404
    )


@app.exception_handler(RuntimeError)
async def runtime_error_handler(_, exc):
    raise HTTPException(
        detail=exc.args[0],
        status_code=422
    )

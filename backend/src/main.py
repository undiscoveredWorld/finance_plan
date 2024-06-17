import logging

from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import IntegrityError, NoResultFound

from end_points.category import category_router
from end_points.subcategory import subcategory_router
from end_points.buy import buy_router

origins = ["http://5.35.88.46:3000"]

logging.basicConfig(level=logging.INFO)

app = FastAPI()
app.include_router(category_router)
app.include_router(subcategory_router)
app.include_router(buy_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"]
)


@app.exception_handler(TypeError)
async def value_error_handler(_, exc):
    raise HTTPException(
        detail=exc.args[0],
        status_code=400
    )


@app.exception_handler(NoResultFound)
async def index_error_handler(_, exc):
    raise HTTPException(
        detail=exc.args[0],
        status_code=404
    )


@app.exception_handler(IntegrityError)
async def runtime_error_handler(_, exc):
    raise HTTPException(
        detail=exc.args[0],
        status_code=422
    )

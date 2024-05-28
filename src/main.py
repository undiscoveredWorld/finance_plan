from typing import List

from fastapi import FastAPI
from fastapi.responses import Response

from common.data import DataFactory
from domain.models import CategoryCreate, Category


app = FastAPI()

data_factory = DataFactory()


@app.post("/create_category")
def create_category(category: CategoryCreate):
    data_factory.add_category(
        category=category
    )


@app.put("/update_category")
def update_category(id_: int, category: CategoryCreate):
    try:
        data_factory.update_category(
            id_,
            new_category=category
        )
    except IndexError:
        return Response(
            status_code=422
        )


@app.delete("/delete_category")
def delete_category(id_: int):
    try:
        data_factory.delete_category(id_)
    except IndexError:
        return Response(
            status_code=422
        )


@app.post("/save")
def save():
    data_factory.save_data()


@app.post("/load")
def load():
    data_factory.load_data()


@app.get("/categories", response_model=List[Category])
def get_categories():
    return data_factory.list_categories()

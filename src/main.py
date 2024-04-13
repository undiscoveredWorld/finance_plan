from typing import List

from fastapi import FastAPI

from common.data import DataFactory
from domain.models import CategoryCreate, Category


app = FastAPI()

data_factory = DataFactory()


@app.post("/create_category")
def create_category(category: CategoryCreate):
    data_factory.add_category(
        category=category
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

from fastapi import FastAPI
from fastapi.responses import Response

from common.data import save_data_to_json_file, load_data_to_ram_from_json_file
from end_points.category import category_router
from end_points.subcategory import subcategory_router

app = FastAPI()
app.include_router(category_router)
app.include_router(subcategory_router)


@app.post("/save")
def save():
    save_data_to_json_file()


@app.post("/load")
def load():
    try:
        load_data_to_ram_from_json_file()
    except FileNotFoundError:
        return Response(status_code=422)

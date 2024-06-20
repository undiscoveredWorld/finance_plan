from fastapi.routing import APIRouter
from fastapi import UploadFile

from domain.data.import_buys import import_buys

import_data_router = APIRouter()


@import_data_router.post("/import")
def import_data(sheet_name: str, ranges: str, file: UploadFile):
    split_ranges = ranges.split(",")
    import_buys(sheet_name, split_ranges, file)
    return {"filename": file.filename}

from fastapi.routing import APIRouter
from fastapi import UploadFile

from domain.data.import_buys import import_buys

import_data_router = APIRouter(prefix="/import")


@import_data_router.post("/xlsx/buys")
def import_buys(sheet_name: str, ranges: str, file: UploadFile):
    split_ranges = ranges.split(",")
    import_buys(sheet_name, split_ranges, file)
    return {"filename": file.filename}

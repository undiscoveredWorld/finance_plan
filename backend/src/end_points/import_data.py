from fastapi.routing import APIRouter
from fastapi import UploadFile

from domain.data.import_buys import import_buys

import_data_router = APIRouter()


@import_data_router.post("/import")
def import_data(sheet_name: str, ranges: list[str], file: UploadFile):
    import_buys(sheet_name, ranges, file)
    return {"filename": file.filename}

from fastapi.routing import APIRouter

from domain.models import (
    ReportsConfig,
    ReportsConfigUpdate,
    ReportsConfigCreate,
)
from domain.data.config import (
    list_reports_configs,
    add_reports_config,
    update_reports_config,
    delete_reports_config,
)

reports_config_router = APIRouter(
    tags=['ReportsConfig'],
)


@reports_config_router.get("/reports", response_model=list[ReportsConfig])
async def list_reports_configs_router() -> list[ReportsConfig]:
    return list_reports_configs()


@reports_config_router.post("/reports")
async def create_reports_config_router(reports_config_create: ReportsConfigCreate):
    add_reports_config(reports_config_create)


@reports_config_router.put("/reports")
async def update_reports_config_router(id_: int, reports_config_update: ReportsConfigUpdate):
    update_reports_config(id_, reports_config_update)


@reports_config_router.delete("/reports")
async def delete_reports_config_router(id_: int):
    delete_reports_config(id_)

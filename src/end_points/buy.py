from fastapi.routing import APIRouter

from domain.models import (
    Buy,
    BuyUpdate,
    BuyCreate,
)
from domain.data.buy import (
    list_buys,
    add_buy,
    update_buy,
    delete_buy,
)

buy_router = APIRouter(
    tags=['Buy']
)


@buy_router.get("/list_buys", response_model=list[Buy])
async def list_categories_router() -> list[Buy]:
    return list_buys()


@buy_router.post("/create_buy")
async def create_buy_router(buy_create: BuyCreate):
    add_buy(buy_create)


@buy_router.put("/update_buy")
async def update_buy_router(id_: int, buy_update: BuyUpdate):
    update_buy(id_, buy_update)


@buy_router.delete("/delete_buy")
async def delete_buy_router(id_: int):
    delete_buy(id_)

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from common.data.db import get_session
from common.data.db_models import Buy as DB_Buy
from common.data.utils import check_object_is_subclass_of_model
from domain.models import (
    BuyCreate,
    BuyUpdate,
    Buy,
)


def add_buy(buy: BuyCreate) -> int:
    """Add buy to db.

    Raises:
        TypeError: if object is not subclass of model
    """
    check_object_is_subclass_of_model(buy, BuyCreate)
    db_session: Session = get_session()

    new_buy = DB_Buy(**buy.model_dump())
    db_session.add(new_buy)
    db_session.commit()

    return new_buy.id


def generate_multiple_adding_buy() -> (callable, callable):
    """Generate two function -- add_one_buy(buy: BuyCreate) and commit all buys.

    Returns:
        add_one_buy callable(buy: BuyCreate), commit: callable()
    """
    db_session: Session = get_session()

    def add_one_buy(buy: BuyCreate) -> int:
        check_object_is_subclass_of_model(buy, BuyCreate)
        new_buy = DB_Buy(**buy.model_dump())
        db_session.add(new_buy)
        db_session.flush()
        return new_buy.id

    return add_one_buy, db_session.commit


def list_buys() -> list[Buy]:
    db_session: Session = get_session()
    db_buys = db_session.query(DB_Buy).all()
    buys = _convert_db_buys_to_buys(db_buys)
    return buys


def _convert_db_buys_to_buys(db_buys):
    result = []
    for buy in db_buys:
        result.append(Buy(
            id=buy.id,
            product=buy.product,
            category_id=buy.category_id,
            subcategory_id=buy.subcategory_id,
            date=buy.date,
            sum=buy.sum,
            category=buy.category,
            subcategory=buy.subcategory
        ))
    return result


def update_buy(id_: int, new_buy: BuyUpdate) -> None:
    """Update buy in db.

    Raises:
        TypeError: if object is not subclass of model
        NoResultFound: if id_ was not found in the db
    """
    check_object_is_subclass_of_model(new_buy, BuyUpdate)
    db_session: Session = get_session()

    buy = db_session.execute(select(DB_Buy).filter_by(id=id_)).scalar_one()
    if buy is None:
        raise NoResultFound(f"Category with id_ {id_} does not found")

    for key, value in new_buy.model_dump().items():
        if value is not None:
            buy.__setattr__(key, value)

    db_session.commit()


def delete_buy(id_: int) -> None:
    """Delete buy."""
    db_session: Session = get_session()
    db_session.query(DB_Buy).filter_by(id=id_).delete()
    db_session.commit()


def clear_buys() -> None:
    db_session: Session = get_session()
    db_session.query(DB_Buy).delete()
    db_session.commit()

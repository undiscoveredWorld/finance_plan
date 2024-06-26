from sqlalchemy import select
from sqlalchemy.orm import (
    Session,
)
from sqlalchemy.exc import NoResultFound

from settings import CACHING_KEYS
from common.data.utils import (
    check_object_is_subclass_of_model
)
from common.data.db import get_session
from common.data.db_models import (
    Subcategory as DB_Subcategory
)
from common.data.utils import convert_return_to_list_of_model
from common.cache.function_cache import (
    invalidate_cache_by_call,
    redis_cache_list_models,
)
from domain.models import (
    SubcategoryCreate,
    SubcategoryUpdate,
    Subcategory
)


@invalidate_cache_by_call(CACHING_KEYS["subcategories"])
def add_subcategory(subcategory: SubcategoryCreate) -> int:
    """Add subcategory to db.

    Raises:
        TypeError: if object is not subclass of model
    """
    check_object_is_subclass_of_model(subcategory, SubcategoryCreate)
    db_session: Session = get_session()

    new_subcategory = DB_Subcategory(**subcategory.model_dump())
    db_session.add(new_subcategory)
    db_session.commit()

    return new_subcategory.id


@redis_cache_list_models(CACHING_KEYS["subcategories"], Subcategory)
@convert_return_to_list_of_model(Subcategory)
def list_subcategories() -> list[type[Subcategory]]:
    db_session: Session = get_session()
    db_subcategories = db_session.query(DB_Subcategory).all()
    return db_subcategories


@invalidate_cache_by_call(CACHING_KEYS["subcategories"])
def update_subcategory(id_: int, new_subcategory: SubcategoryUpdate) -> None:
    """Update subcategory in db.

    Raises:
        TypeError: if object is not subclass of model
        NoResultFound: if id_ was not found in the db
        IntegrityError: if category.name already exists
    """
    check_object_is_subclass_of_model(new_subcategory, SubcategoryUpdate)
    db_session: Session = get_session()

    subcategory = db_session.execute(select(DB_Subcategory).filter_by(id=id_)).scalar_one()
    if subcategory is None:
        raise NoResultFound(f"Subcategory with id {id} was not found in db")

    for key, value in new_subcategory.model_dump().items():
        if value is not None:
            subcategory.__setattr__(key, value)
    db_session.commit()


@invalidate_cache_by_call(CACHING_KEYS["subcategories"])
def delete_subcategory(id_: int) -> None:
    db_session: Session = get_session()
    db_session.query(DB_Subcategory).filter_by(id=id_).delete()
    db_session.commit()


@invalidate_cache_by_call(CACHING_KEYS["subcategories"])
def clear_subcategories() -> None:
    db_session: Session = get_session()
    db_session.query(DB_Subcategory).delete()
    db_session.commit()

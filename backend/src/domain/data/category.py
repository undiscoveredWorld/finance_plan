from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from settings import CACHING_KEYS
from common.data.db import get_session
from common.data.db_models import Category as DB_Category
from common.data.utils import check_object_is_subclass_of_model
from common.cache.function_cache import (
    redis_cache_list_models,
    invalidate_cache_by_call,
)
from domain.models import (
    CategoryCreate,
    CategoryUpdate,
    Category,
)


@invalidate_cache_by_call(CACHING_KEYS["categories"])
def add_category(category: CategoryCreate) -> int:
    """Add category to db.

    Raises:
        TypeError: if object is not subclass of model
    """
    check_object_is_subclass_of_model(category, CategoryCreate)
    db_session: Session = get_session()

    new_category = DB_Category(**category.model_dump())
    db_session.add(new_category)
    db_session.commit()

    return new_category.id


@redis_cache_list_models(CACHING_KEYS["categories"], Category)
def list_categories() -> list[Category]:
    db_session: Session = get_session()
    db_categories = db_session.query(DB_Category).all()

    model_categories: list[Category] = []
    for category in db_categories:
        model_categories.append(Category(
            id=category.id,
            name=category.name,
            subcategories=category.subcategories
        ))

    return model_categories


@invalidate_cache_by_call(CACHING_KEYS["categories"])
def update_category(id_: int, new_category: CategoryUpdate) -> None:
    """Update category in db.

    Raises:
        TypeError: if object is not subclass of model
        NoResultFound: if id_ was not found in the db
        IntegrityError: if category.name already exists
    """
    check_object_is_subclass_of_model(new_category, CategoryUpdate)

    db_session: Session = get_session()
    category = db_session.execute(select(DB_Category).filter_by(id=id_)).scalar_one()
    if category is None:
        raise NoResultFound(f"Category with id_ {id_} does not found")

    for key, value in new_category.model_dump().items():
        if value is not None:
            category.__setattr__(key, value)

    db_session.commit()


@invalidate_cache_by_call(CACHING_KEYS["categories"])
def delete_category(id_: int) -> None:
    """Delete category."""
    db_session: Session = get_session()
    db_session.query(DB_Category).filter_by(id=id_).delete()
    db_session.commit()


@invalidate_cache_by_call(CACHING_KEYS["categories"])
def clear_categories() -> None:
    db_session: Session = get_session()
    db_session.query(DB_Category).delete()
    db_session.commit()

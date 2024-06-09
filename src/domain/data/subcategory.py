import logging

from sqlalchemy import select
from sqlalchemy.orm import (
    Session,
)
from sqlalchemy.exc import NoResultFound

from common.data.utils import (
    check_object_is_subclass_of_model
)
from common.data.db import Session
from common.data.db_models import (
    Subcategory as DB_Subcategory
)
from domain.models import (
    SubcategoryCreate,
    SubcategoryUpdate,
)
from domain.data.category import (
    list_categories,
)


def add_subcategory(subcategory: SubcategoryCreate) -> int:
    """Add subcategory to db.

    Raises:
        TypeError: if object is not subclass of model
    """
    check_object_is_subclass_of_model(subcategory, SubcategoryCreate)

    db_session: Session = Session()
    new_subcategory = DB_Subcategory(**subcategory.model_dump())
    db_session.add(new_subcategory)
    db_session.commit()

    return new_subcategory.id


def list_subcategories() -> list[type[DB_Subcategory]]:
    db_session: Session = Session()
    db_subcategories = db_session.query(DB_Subcategory).all()
    return db_subcategories


def update_subcategory(id_: int, new_subcategory: SubcategoryUpdate) -> None:
    """Update subcategory in db.

    Raises:
        TypeError: if object is not subclass of model
        NoResultFound: if id_ was not found in the db
        IntegrityError: if category.name already exists
    """
    check_object_is_subclass_of_model(new_subcategory, SubcategoryUpdate)

    db_session: Session = Session()
    subcategory = db_session.execute(select(DB_Subcategory).filter_by(id=id_)).scalar_one()
    if subcategory is None:
        raise NoResultFound(f"Subcategory with id {id} was not found in db")

    for key, value in new_subcategory.model_dump().items():
        subcategory.__setattr__(key, value)
    db_session.commit()


def delete_subcategory(id_: int) -> None:
    db_session: Session = Session()
    db_session.query(DB_Subcategory).filter_by(id=id_).delete()
    db_session.commit()


def clear_subcategories() -> None:
    db_session: Session = Session()
    db_session.query(DB_Subcategory).delete()
    db_session.commit()


def _check_category_exists(id_: int) -> None:
    """Raise RuntimeError if category with that id does not exist.

    Raises:
        RuntimeError
    """
    categories = list_categories()
    if id_ > len(categories):
        logging.warning("Trying link subcategory with not existing category")
        raise RuntimeError("Trying link subcategory with not existing category")

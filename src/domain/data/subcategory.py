import logging

from common.data.catalog import Catalog
from common.data.utils import (
    check_unique_of_field_in_catalog,
    check_object_is_subclass_of_model
)
from domain.models import (
    SubcategoryCreate,
    Subcategory,
    SubcategoryUpdate,
)
from domain.data.category import (
    list_categories,
)

subcategories = Catalog("Subcategories")


def add_subcategory(subcategory: SubcategoryCreate) -> None:
    """Add subcategory.

    Raises:
        RuntimeError
        ValueError
    """
    check_object_is_subclass_of_model(subcategory, SubcategoryCreate)
    check_unique_of_field_in_catalog(
        value=subcategory.name,
        field_name="name",
        catalog_name=subcategories.get_catalog_name())
    _check_category_exists(subcategory.category_id)
    subcategories.add_element(subcategory.model_dump())


def list_subcategories() -> list[Subcategory]:
    result_list: list[dict] = subcategories.get_all_elements()

    # Convert list[dict] to list[Subcategory]
    result_list: list[Subcategory] = list(
        map(
            Subcategory.model_validate,
            result_list
        )
    )

    return result_list


def update_subcategory(id_: int, new_subcategory: SubcategoryUpdate) -> None:
    """Update subcategory.

    Raises:
        ValueError
        IndexError
        RuntimeError
    """
    check_object_is_subclass_of_model(new_subcategory, SubcategoryUpdate)
    check_unique_of_field_in_catalog(
        value=new_subcategory.name,
        field_name="name",
        catalog_name=subcategories.get_catalog_name())
    if new_subcategory.category_id is not None:
        _check_category_exists(new_subcategory.category_id)
    subcategories.update_element(id_, new_subcategory.model_dump())


def delete_subcategory(id_: int) -> None:
    """Delete subcategory.

    Raises:
        IndexError
    """
    subcategories.delete_element(id_)


def clear_subcategories() -> None:
    subcategories.clear_catalog()


def _check_category_exists(id_: int) -> None:
    """Raise RuntimeError if category with that id does not exist.

    Raises:
        RuntimeError
    """
    categories = list_categories()
    if id_ > len(categories):
        logging.warning("Trying link subcategory with not existing category")
        raise RuntimeError("Trying link subcategory with not existing category")

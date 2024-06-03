import logging

from typing import (
    List,
    Dict,
)

from common.data import (
    Catalog,
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
    check_object_is_subclass_of_model(subcategory, SubcategoryCreate)
    check_unique_of_field_in_catalog(
        value=subcategory.name,
        field_name="name",
        catalog_name=subcategories.get_catalog_name())
    _check_category_exists(subcategory.category_id)
    subcategories.add_element(subcategory.model_dump())


def list_subcategories() -> List[Subcategory]:
    result_list: List[Dict] = subcategories.get_all_elements()

    # Convert List[BaseModel] to List[Subcategory]
    result_list: List[Subcategory] = list(
        map(
            Subcategory.model_validate,
            result_list
        )
    )

    return result_list


def update_subcategory(id_: int, new_subcategory: SubcategoryUpdate) -> None:
    check_object_is_subclass_of_model(new_subcategory, SubcategoryUpdate)
    check_unique_of_field_in_catalog(
        value=new_subcategory.name,
        field_name="name",
        catalog_name=subcategories.get_catalog_name())
    if new_subcategory.category_id is not None:
        _check_category_exists(new_subcategory.category_id)
    subcategories.update_element(id_, new_subcategory.model_dump())


def delete_subcategory(id_: int) -> None:
    subcategories.delete_element(id_)


def clear_subcategories() -> None:
    subcategories.clear_catalog()


def _check_category_exists(id_: int) -> None:
    """_check_category_exists raises an exception if category with that id does not exist."""
    categories = list_categories()
    if id_ > len(categories):
        logging.warning("Trying link subcategory with not existing category")
        raise ValueError("Trying link subcategory with not existing category")

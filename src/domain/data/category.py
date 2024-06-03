from typing import (
    List,
    Dict,
)

from common.data import (
    Catalog,
    check_object_is_subclass_of_model,
    check_unique_of_field_in_catalog
)
from domain.models import (
    CategoryCreate,
    Category,
    CategoryUpdate,
)

categories = Catalog("Categories")


def add_category(category: CategoryCreate) -> None:
    check_object_is_subclass_of_model(category, CategoryCreate)
    check_unique_of_field_in_catalog(
        value=category.name,
        field_name="name",
        catalog_name=categories.get_catalog_name())
    categories.add_element(category.model_dump())


def list_categories() -> List[Category]:
    result_list: List[Dict] = categories.get_all_elements()

    # Convert List[BaseModel] to List[Category]
    result_list: List[Category] = list(
        map(
            Category.model_validate,
            result_list
        )
    )

    return result_list


def update_category(id_: int, new_category: CategoryUpdate) -> None:
    check_object_is_subclass_of_model(new_category, CategoryUpdate)
    check_unique_of_field_in_catalog(
        value=new_category.name,
        field_name="name",
        catalog_name=categories.get_catalog_name())
    categories.update_element(id_, new_category.model_dump())


def delete_category(id_: int) -> None:
    categories.delete_element(id_)


def clear_categories() -> None:
    categories.clear_catalog()

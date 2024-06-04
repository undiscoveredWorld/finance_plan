from common.data.catalog import Catalog
from common.data.utils import (
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
    """Add category.

    Raises:
        ValueError
        RuntimeError
    """
    check_object_is_subclass_of_model(category, CategoryCreate)
    check_unique_of_field_in_catalog(
        value=category.name,
        field_name="name",
        catalog_name=categories.get_catalog_name()
    )
    categories.add_element(category.model_dump())


def list_categories() -> list[Category]:
    result_list: list[dict] = categories.get_all_elements()

    # Convert list[dict] to list[Category]
    result_list: list[Category] = list(
        map(
            Category.model_validate,
            result_list
        )
    )

    return result_list


def update_category(id_: int, new_category: CategoryUpdate) -> None:
    """Update category.

    Raises:
        ValueError
        IndexError
        RuntimeError
    """
    check_object_is_subclass_of_model(new_category, CategoryUpdate)
    if categories.get_all_elements()[id_]["name"] != new_category.name:
        check_unique_of_field_in_catalog(
            value=new_category.name,
            field_name="name",
            catalog_name=categories.get_catalog_name()
        )
    categories.update_element(id_, new_category.model_dump())


def delete_category(id_: int) -> None:
    """Delete category.

    Raises:
        IndexError
    """
    categories.delete_element(id_)


def clear_categories() -> None:
    categories.clear_catalog()

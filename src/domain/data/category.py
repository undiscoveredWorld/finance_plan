from typing import (
    List,
    Dict
)

from common.data import Catalog
from domain.models import CategoryCreate, Category, CategoryUpdate

categories = Catalog("Categories")


def add_category(category: CategoryCreate) -> None:
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


def update_category(id: int, new_category: CategoryUpdate) -> None:
    categories.update_element(id, new_category.model_dump())


def delete_category(id_: int) -> None:
    categories.delete_element(id_)

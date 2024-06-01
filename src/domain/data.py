from typing import (
    List,
    Dict
)

from common.data import Catalog
from domain.models import CategoryCreate, Category, CategoryUpdate

categories = Catalog("categories", Category)


def add_category(category: CategoryCreate) -> None:
    categories.add_element(category)


def list_categories() -> List[Category]:
    result_list: List[Dict] = categories.get_all_elements()

    # Convert List[BaseModel] to List[Category]
    result_list: List[Category] = list(
        map(
            lambda x: Category.model_validate(x),
            result_list
        )
    )

    return result_list


def update_category(new_category: CategoryUpdate) -> None:
    categories.update_element(new_category.id, new_category.model_dump())


def delete_category(id_: int) -> None:
    categories.delete_element(id_)

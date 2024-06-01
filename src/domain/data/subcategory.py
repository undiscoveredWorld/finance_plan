from typing import (
    List,
    Dict
)

from common.data import Catalog
from domain.models import SubcategoryCreate, Subcategory, SubcategoryUpdate

subcategories = Catalog("Subcategories")


def add_subcategory(category: SubcategoryCreate) -> None:
    subcategories.add_element(category)


def list_subcategories() -> List[Subcategory]:
    result_list: List[Dict] = subcategories.get_all_elements()

    # Convert List[BaseModel] to List[Category]
    result_list: List[Subcategory] = list(
        map(
            lambda x: Subcategory.model_validate(x),
            result_list
        )
    )

    return result_list


def update_subcategory(new_category: SubcategoryUpdate) -> None:
    subcategories.update_element(new_category.id, new_category.model_dump())


def delete_subcategory(id_: int) -> None:
    subcategories.delete_element(id_)

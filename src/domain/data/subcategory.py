from typing import (
    List,
    Dict
)

from common.data import Catalog
from domain.models import SubcategoryCreate, Subcategory, SubcategoryUpdate

subcategories = Catalog("Subcategories")


def add_subcategory(subcategory: SubcategoryCreate) -> None:
    subcategories.add_element(subcategory.model_dump())


def list_subcategories() -> List[Subcategory]:
    result_list: List[Dict] = subcategories.get_all_elements()

    # Convert List[BaseModel] to List[Category]
    result_list: List[Subcategory] = list(
        map(
            Subcategory.model_validate,
            result_list
        )
    )

    return result_list


def update_subcategory(id_: int,new_subcategory: SubcategoryUpdate) -> None:
    subcategories.update_element(id_, new_subcategory.model_dump())


def delete_subcategory(id_: int) -> None:
    subcategories.delete_element(id_)

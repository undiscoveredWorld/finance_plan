import ast
import datetime
import os

from dateutil.parser import parse
from fastapi import UploadFile
from functools import lru_cache

from settings import CACHING_KEYS
from common.cache.redis_connect import invalidate_key
from common.data.utils import create_uploaded_file
from common.data.import_data import (
    read_range_from_sheet,
    open_sheet
)
from domain.models import (
    Category,
    Subcategory,
    CategoryCreate,
    SubcategoryCreate,
    BuyCreate,
)
from domain.data.category import list_categories, add_category
from domain.data.subcategory import list_subcategories, add_subcategory
from domain.data.buy import generate_multiple_adding_buy


class _ImportResolver:
    """Class for resolution some differences from imported data and data inside db."""
    categories: list[Category]
    subcategories: list[Subcategory]

    def __init__(self, categories: list[Category], subcategories: list[Subcategory]):
        self.categories = categories
        self.subcategories = subcategories

    def get_id_category_by_name_or_create_it(self, category_name: str) -> int:
        """Get id of category by name or create it if it doesn't exist.

        Side effect: if the category doesn't exist, will be created category with category_name
        """
        for category in self.categories:
            if category.name == category_name:
                return category.id
        id_ = add_category(CategoryCreate(name=category_name))
        self.categories = list_categories()
        return id_

    def get_id_subcategory_by_name_or_create_it(self, parent_category_id: int, subcategory_name: str) -> int:
        """Get id of subcategory by name or create it if it doesn't exist.

        Side effect: if the subcategory doesn't exist, will be created category with category_name
        """
        for subcategory in self.subcategories:
            if subcategory.name == subcategory_name and subcategory.category_id == parent_category_id:
                return subcategory.id

        id_ = add_subcategory(SubcategoryCreate(name=subcategory_name, category_id=parent_category_id))
        self.subcategories = _convert_db_subcategories_to_model_subcategories(list_subcategories())
        return id_

    def _is_category_id_exist(self, category_id: int) -> bool:
        for category in self.categories:
            if category.id == category_id:
                return True
        return False


@lru_cache
def _get_date_from_str(date_str: str) -> datetime.date:
    return parse(date_str).date()


def _read_ranges(sheet_name: str, ranges: list[str], path_to_file: str):
    rows = []
    sheet = open_sheet(path_to_file, sheet_name)
    for r in ranges:
        for sub_row in read_range_from_sheet(sheet, r):
            rows.append(sub_row)

    return rows


def _get_import_resolver() -> _ImportResolver:
    categories = list_categories()
    db_subcategories = list_subcategories()
    subcategories = _convert_db_subcategories_to_model_subcategories(db_subcategories)
    import_resolver = _ImportResolver(categories, subcategories)
    return import_resolver


def _convert_db_subcategories_to_model_subcategories(db_subcategories):
    subcategories: list[Subcategory] = []
    for subcategory in db_subcategories:
        subcategories.append(Subcategory.model_validate(subcategory.__dict__))
    return subcategories


def _create_buys_from_rows(rows: list[list[str]]):
    """Create buys from rows.

    Side effect: created buy will add to db
    """
    import_resolver = _get_import_resolver()
    add_buy, commit = generate_multiple_adding_buy()
    for row in rows:
        category_id = import_resolver.get_id_category_by_name_or_create_it(row[1])
        subcategory_id = import_resolver.get_id_subcategory_by_name_or_create_it(category_id, row[2])
        add_buy(BuyCreate(
            date=_get_date_from_str(row[0]),
            category_id=category_id,
            subcategory_id=subcategory_id,
            product=row[3],
            sum=int(ast.literal_eval(row[4]))
        ))

    commit()


def import_buys(sheet_name: str, ranges: list[str], file: UploadFile):
    path_to_file = "/tmp/got_file.xlsx"
    create_uploaded_file(file, path_to_file)
    rows = _read_ranges(sheet_name, ranges, path_to_file)
    _invalidate_cache()
    _create_buys_from_rows(rows)
    os.remove(path_to_file)


def import_buys_from_path_to_file(sheet_name: str, ranges: list[str], path_to_file: str):
    rows = _read_ranges(sheet_name, ranges, path_to_file)
    _invalidate_cache()
    _create_buys_from_rows(rows)


def _invalidate_cache():
    invalidate_key(CACHING_KEYS["categories"])
    invalidate_key(CACHING_KEYS["subcategories"])

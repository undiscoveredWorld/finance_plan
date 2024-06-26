import datetime

from domain.data.buy import add_buy
from domain.data.category import add_category
from domain.data.subcategory import add_subcategory
from domain.models import CategoryCreate, SubcategoryCreate, BuyCreate


def create_buy() -> (int, int, int):
    """Create buy and return category_id, subcategory_id and buy_id.

    Returns:
        (category_id, subcategory_id, buy_id)
    """
    category_id = add_category(CategoryCreate(name="test_category"))
    subcategory_id = add_subcategory(SubcategoryCreate(name="test_subcategory", category_id=category_id))
    buy_id = add_buy(
        BuyCreate(
            datetime.date.today(),
            category_id,
            subcategory_id,
            "test_product",
            100
        )
    )
    return category_id, subcategory_id, buy_id


def create_subcategory() -> (int, int):
    """Create subcategory and return category_id and subcategory_id.

    Returns:
        (category_id, subcategory_id)
    """
    category_id = add_category(CategoryCreate(name="test_category"))
    subcategory_id = add_subcategory(SubcategoryCreate(category_id=category_id, name="test_subcategory"))
    return category_id, subcategory_id

import datetime
import unittest
from pydantic import BaseModel, ValidationError
from sqlalchemy.exc import IntegrityError, NoResultFound

from domain.models import (
    CategoryCreate,
    CategoryUpdate,
    SubcategoryCreate,
    Subcategory,
    SubcategoryUpdate,
    BuyCreate,
    BuyUpdate,
    Buy
)
from domain.data.category import (
    add_category,
    list_categories,
    update_category,
    delete_category,
    clear_categories,
)
from domain.data.subcategory import (
    add_subcategory,
    list_subcategories,
    update_subcategory,
    delete_subcategory,
    clear_subcategories,
)
from domain.data.buy import (
    add_buy,
    list_buys,
    update_buy,
    delete_buy,
    clear_buys,
)


class TestModel(BaseModel):
    name: str
    description: str


class DataCategoryTestCase(unittest.TestCase):
    def test_positive_add_category(self):
        add_category(CategoryCreate(name="test_category"))
        categories = list_categories()
        self.assertEqual(
            1,
            len(categories),
        )
        self.assertEqual(
            "test_category",
            categories[0].name,
        )

    def test_add_other_model_in_category_catalog(self):
        with self.assertRaises(TypeError):
            add_category(TestModel(name="test_category", description="test_category"))
        with self.assertRaises(ValidationError):
            add_category(Subcategory(name="test_subcategory"))

    def test_add_a_category_twice(self):
        add_category(CategoryCreate(name="test_category"))
        with self.assertRaises(IntegrityError):
            add_category(CategoryCreate(name="test_category"))

    def test_positive_list_categories(self):
        add_category(CategoryCreate(name="test_category"))
        categories = list_categories()
        self.assertEqual(
            1,
            len(categories),
        )
        self.assertEqual(
            "test_category",
            categories[0].name,
        )

    def test_positive_update_category(self):
        category_id = add_category(CategoryCreate(name="test_category"))
        update_category(category_id, CategoryUpdate(name="Updated"))
        categories = list_categories()
        self.assertEqual(
            1,
            len(categories),
        )
        self.assertEqual(
            "Updated",
            categories[0].name,
        )

    def test_call_update_with_no_changes(self):
        category_id = add_category(CategoryCreate(name="test_category"))
        update_category(category_id, CategoryUpdate())
        categories = list_categories()
        self.assertEqual(
            1,
            len(categories),
        )
        self.assertEqual(
            "test_category",
            categories[0].name,
        )

    def test_update_category_out_index(self):
        with self.assertRaises(NoResultFound):
            update_category(100, CategoryUpdate(name="Updated"))

    def test_update_category_name_on_engaged_name(self):
        add_category(CategoryCreate(name="Engaged"))
        category_id = add_category(CategoryCreate(name="test_category"))
        with self.assertRaises(IntegrityError):
            update_category(category_id, CategoryUpdate(name="Engaged"))

    def test_update_category_by_other_model(self):
        category_id = add_category(CategoryCreate(name="test_category"))
        with self.assertRaises(TypeError):
            update_category(category_id, SubcategoryUpdate(name="Updated"))
        with self.assertRaises(TypeError):
            update_category(category_id, TestModel(name="56%45", description="test"))

    def test_positive_delete_category(self):
        category_id = add_category(CategoryCreate(name="test_category"))
        delete_category(category_id)
        self.assertEqual([], list_categories())

    def test_delete_category_out_index(self):
        delete_category(100)

    def test_positive_clear_categories(self):
        for i in range(4):
            add_category(CategoryCreate(name=f"{i}"))
        clear_categories()
        self.assertEqual([], list_categories())

    def tearDown(self):
        super().tearDown()
        clear_categories()


class DataSubcategoryTest(unittest.TestCase):
    def test_positive_add_subcategory(self):
        category_id = add_category(CategoryCreate(name="test_category"))
        add_subcategory(
            SubcategoryCreate(name="test_subcategory", category_id=category_id)
        )

        categories = list_categories()
        subcategories = list_subcategories()
        self.assertEqual(
            1,
            len(subcategories)
        )
        self.assertEqual(
            "test_subcategory",
            subcategories[0].name
        )
        self.assertEqual(
            categories[0].id,
            subcategories[0].category.id
        )

    def test_add_other_model_in_subcategory_catalog(self):
        with self.assertRaises(TypeError):
            add_subcategory(TestModel(name="test_subcategory", description="test_subcategory"))

    def test_add_a_subcategory_twice(self):
        category_id = add_category(CategoryCreate(name="Test Category"))
        add_subcategory(SubcategoryCreate(name="test", category_id=category_id))
        with self.assertRaises(IntegrityError):
            add_subcategory(SubcategoryCreate(name="test", category_id=0))

    def test_link_subcategory_to_not_exist_category(self):
        with self.assertRaises(IntegrityError):
            add_subcategory(SubcategoryCreate(name="test", category_id=100))

    def test_positive_list_subcategories(self):
        category_id = add_category(CategoryCreate(name="test_category"))
        add_subcategory(SubcategoryCreate(name="test_subcategory", category_id=category_id))

        subcategories = list_subcategories()
        self.assertEqual(
            1,
            len(subcategories)
        )
        self.assertEqual(
            "test_subcategory",
            subcategories[0].name
        )
        self.assertEqual(
            category_id,
            subcategories[0].category.id
        )
        self.assertEqual(
            "test_category",
            subcategories[0].category.name
        )

    def test_positive_update_subcategory(self):
        category_id = add_category(CategoryCreate(name="test_category"))
        subcategory_id = add_subcategory(SubcategoryCreate(name="test_subcategory", category_id=category_id))
        update_subcategory(subcategory_id, SubcategoryUpdate(name="Updated"))
        self.assertEqual(
            "Updated",
            list_subcategories()[0].name
        )

    def test_call_update_subcategory_with_no_changes(self):
        category_id = add_category(CategoryCreate(name="test_category"))
        subcategory_id = add_subcategory(SubcategoryCreate(name="test_subcategory", category_id=category_id))
        update_subcategory(subcategory_id, SubcategoryUpdate())
        self.assertEqual(
            "test_subcategory",
            list_subcategories()[0].name
        )

    def test_update_subcategory_out_index(self):
        with self.assertRaises(NoResultFound):
            update_subcategory(100, SubcategoryUpdate(name="Updated"))

    def test_update_subcategory_name_on_engaged_name(self):
        category_id = add_category(CategoryCreate(name="test_category"))
        add_subcategory(SubcategoryCreate(name="Engaged", category_id=category_id))
        subcategory_id = add_subcategory(SubcategoryCreate(name="test_subcategory", category_id=category_id))
        with self.assertRaises(IntegrityError):
            update_subcategory(subcategory_id, SubcategoryUpdate(name="Engaged"))

    def test_update_subcategory_by_other_model(self):
        category_id = add_category(CategoryCreate(name="test_category"))
        add_subcategory(SubcategoryCreate(name="test_subcategory", category_id=category_id))
        with self.assertRaises(TypeError):
            update_subcategory(0, CategoryUpdate(name="Updated"))

    def test_update_subcategory_link_to_category_on_not_existing_category(self):
        category_id = add_category(CategoryCreate(name="test_category"))
        subcategory_id = add_subcategory(SubcategoryCreate(name="test_subcategory", category_id=category_id))
        with self.assertRaises(IntegrityError):
            update_subcategory(subcategory_id, SubcategoryUpdate(category_id=100))

    def test_positive_delete_subcategory(self):
        category_id = add_category(CategoryCreate(name="test_category"))
        subcaetgory_id = add_subcategory(SubcategoryCreate(name="test_subcategory", category_id=category_id))
        delete_subcategory(subcaetgory_id)
        self.assertEqual([], list_subcategories())

    def test_positive_clear_subcategories(self):
        category_id = add_category(CategoryCreate(name="test_category"))
        for i in range(4):
            add_subcategory(SubcategoryCreate(name=f"{i}", category_id=category_id))
        clear_subcategories()
        self.assertEqual([], list_subcategories())

    def tearDown(self):
        super().tearDown()
        clear_subcategories()
        clear_categories()


class DataBuyTest(unittest.TestCase):
    def test_positive_add_buy(self):
        _create_buy()
        buys = list_buys()
        self.assertEqual(
            1,
            len(buys)
        )
        self.assertEqual(
            "test_product",
            buys[0].product
        )

    def test_add_other_model_in_add_buy(self):
        with self.assertRaises(TypeError):
            add_buy(TestModel(name="test_buy", description="test_buy"))

    def test_link_buy_to_not_exist_category(self):
        with self.assertRaises(IntegrityError):
            category_id = add_category(CategoryCreate(name="test_category"))
            subcategory_id = add_subcategory(SubcategoryCreate(name="test_subcategory", category_id=category_id))
            add_buy(
                BuyCreate(
                    datetime.date.today(),
                    0,
                    subcategory_id,
                    "test_product",
                    100
                )
            )

    def test_link_buy_to_not_exist_subcategory(self):
        with self.assertRaises(IntegrityError):
            category_id = add_category(CategoryCreate(name="test_category"))
            add_subcategory(SubcategoryCreate(name="test_subcategory", category_id=category_id))
            add_buy(
                BuyCreate(
                    datetime.date.today(),
                    category_id,
                    0,
                    "test_product",
                    100
                )
            )

    def test_positive_list_buys(self):
        category_id, subcategory_id, _ = _create_buy()
        buys = list_buys()
        self.assertEqual(
            1,
            len(buys)
        )
        self.assertEqual(
            "test_product",
            buys[0].product
        )
        self.assertEqual(
            category_id,
            buys[0].category.id
        )
        self.assertEqual(
            subcategory_id,
            buys[0].subcategory.id
        )
        self.assertEqual(
            "test_category",
            buys[0].category.name
        )

    def test_positive_update_buy(self):
        _, _, buy_id = _create_buy()
        update_buy(buy_id, BuyUpdate(product="Updated"))
        self.assertEqual(
            "Updated",
            list_buys()[0].product
        )

    def test_update_buy_out_index(self):
        with self.assertRaises(NoResultFound):
            update_buy(100, BuyUpdate(name="Updated"))

    def test_update_buy_by_other_model(self):
        _, _, buy_id = _create_buy()
        with self.assertRaises(TypeError):
            update_buy(buy_id, CategoryUpdate(name="Updated"))

    def test_update_buy_link_to_category_on_not_existing_category(self):
        _, _, buy_id = _create_buy()
        with self.assertRaises(IntegrityError):
            update_buy(buy_id, BuyUpdate(category_id=100))

    def test_positive_delete_buy(self):
        _, _, buy_id = _create_buy()
        delete_buy(buy_id)
        self.assertEqual([], list_buys())

    def test_positive_clear_buys(self):
        category_id = add_category(CategoryCreate(name="test_category"))
        subcategory_id = add_subcategory(SubcategoryCreate(name="test_subcategory", category_id=category_id))
        for i in range(4):
            add_buy(
                BuyCreate(
                    datetime.date.today(),
                    category_id,
                    subcategory_id,
                     "test_product",
                     100
                )
            )

        clear_buys()
        self.assertEqual([], list_buys())

    def tearDown(self):
        super().tearDown()
        clear_buys()
        clear_subcategories()
        clear_categories()


def _create_buy() -> (int, int, int):
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


import unittest
from pydantic import BaseModel

from domain.models import (
    CategoryCreate,
    Category,
    CategoryUpdate,
    SubcategoryCreate,
    Subcategory,
    SubcategoryUpdate,
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


class TestModel(BaseModel):
    name: str
    description: str


class DataCategoryTestCase(unittest.TestCase):
    def test_positive_add_category(self):
        add_category(CategoryCreate(name="test_category"))
        self.assertEqual(
            [Category(id=0, name="test_category")],
            list_categories()
        )

    def test_add_other_model_in_category_catalog(self):
        with self.assertRaises(RuntimeError):
            add_category(TestModel(name="test_category", description="test_category"))

    def test_add_a_category_twice(self):
        add_category(CategoryCreate(name="test_category"))
        with self.assertRaises(RuntimeError):
            add_category(CategoryCreate(name="test_category"))

    def test_positive_list_categories(self):
        add_category(CategoryCreate(name="test_category"))
        self.assertEqual(
            [Category(id=0, name="test_category")],
            list_categories()
        )

    def test_positive_update_category(self):
        add_category(CategoryCreate(name="test_category"))
        update_category(0, CategoryUpdate(name="Updated"))
        self.assertEqual(
            [Category(id=0, name="Updated")],
            list_categories()
        )

    def test_update_category_out_index(self):
        with self.assertRaises(IndexError):
            update_category(100, CategoryUpdate(name="Updated"))

    def test_update_category_name_on_engaged_name(self):
        add_category(CategoryCreate(name="Engaged"))
        add_category(CategoryCreate(name="test_category"))
        with self.assertRaises(RuntimeError):
            update_category(1, CategoryUpdate(name="Engaged"))

    def test_update_category_by_other_model(self):
        add_category(CategoryCreate(name="test_category"))
        with self.assertRaises(RuntimeError):
            update_category(0, SubcategoryUpdate(name="Updated"))

    def test_positive_delete_category(self):
        add_category(CategoryCreate(name="test_category"))
        delete_category(0)
        self.assertEqual([], list_categories())

    def test_delete_category_out_index(self):
        with self.assertRaises(IndexError):
            delete_category(100)

    def test_positive_clear_categories(self):
        for i in range(10):
            add_category(CategoryCreate(name=f"{i}"))
        clear_categories()
        self.assertEqual([], list_categories())

    def tearDown(self):
        super().tearDown()
        clear_categories()


class DataSubcategoryTest(unittest.TestCase):
    def test_positive_add_subcategory(self):
        add_category(CategoryCreate(name="test_category"))
        add_subcategory(
            SubcategoryCreate(name="test_subcategory", category_id=0)
        )
        self.assertEqual(
            [Subcategory(id=0, name="test_subcategory", category_id=0)],
            list_subcategories()
        )

    def test_add_other_model_in_subcategory_catalog(self):
        with self.assertRaises(RuntimeError):
            add_subcategory(TestModel(name="test_subcategory", description="test_subcategory"))

    def test_add_a_subcategory_twice(self):
        add_category(CategoryCreate(name="Test Category"))
        add_subcategory(SubcategoryCreate(name="test", category_id=0))
        with self.assertRaises(RuntimeError):
            add_subcategory(SubcategoryCreate(name="test", category_id=0))

    def test_link_subcategory_to_not_exist_category(self):
        with self.assertRaises(ValueError):
            add_subcategory(SubcategoryCreate(name="test", category_id=100))

    def test_positive_list_subcategories(self):
        add_category(CategoryCreate(name="test_category"))
        add_subcategory(SubcategoryCreate(name="test_subcategory", category_id=0))
        self.assertEqual(
            [Subcategory(id=0, name="test_subcategory", category_id=0)],
            list_subcategories()
        )

    def test_positive_update_subcategory(self):
        add_category(CategoryCreate(name="test_category"))
        add_subcategory(SubcategoryCreate(name="test_subcategory", category_id=0))
        update_subcategory(0, SubcategoryUpdate(name="Updated"))
        self.assertEqual(
            [Subcategory(id=0, name="Updated", category_id=0)],
            list_subcategories()
        )

    def test_update_subcategory_out_index(self):
        with self.assertRaises(IndexError):
            update_subcategory(100, SubcategoryUpdate(name="Updated"))

    def test_update_subcategory_name_on_engaged_name(self):
        add_category(CategoryCreate(name="test_category"))
        add_subcategory(SubcategoryCreate(name="Engaged", category_id=0))
        add_subcategory(SubcategoryCreate(name="test_subcategory", category_id=0))
        with self.assertRaises(RuntimeError):
            update_subcategory(1, SubcategoryUpdate(name="Engaged"))

    def test_update_subcategory_by_other_model(self):
        add_category(CategoryCreate(name="test_category"))
        add_subcategory(SubcategoryCreate(name="test_subcategory", category_id=0))
        with self.assertRaises(RuntimeError):
            update_subcategory(0, CategoryUpdate(name="Updated"))

    def test_update_subcategory_link_to_category_on_not_existing_category(self):
        add_category(CategoryCreate(name="test_category"))
        add_subcategory(SubcategoryCreate(name="test_subcategory", category_id=0))
        with self.assertRaises(ValueError):
            update_subcategory(0, SubcategoryUpdate(category_id=100))

    def test_positive_delete_subcategory(self):
        add_category(CategoryCreate(name="test_category"))
        add_subcategory(SubcategoryCreate(name="test_subcategory", category_id=0))
        delete_subcategory(0)
        self.assertEqual([], list_subcategories())

    def test_delete_subcategory_out_index(self):
        with self.assertRaises(IndexError):
            delete_subcategory(100)

    def test_positive_clear_subcategories(self):
        add_category(CategoryCreate(name="test_category"))
        for i in range(10):
            add_subcategory(SubcategoryCreate(name=f"{i}", category_id=0))
        clear_subcategories()
        self.assertEqual([], list_subcategories())

    def tearDown(self):
        super().tearDown()
        clear_categories()
        clear_subcategories()

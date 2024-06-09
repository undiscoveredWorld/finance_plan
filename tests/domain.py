import unittest
from pydantic import BaseModel, ValidationError
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy.orm import Session

from common.data.db import Session
from domain.models import (
    CategoryCreate,
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
            1,
            len(list_categories()),
        )
        self.assertEqual(
            "test_category",
            list_categories()[0].name,
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
        self.assertEqual(
            1,
            len(list_categories()),
        )
        self.assertEqual(
            "test_category",
            list_categories()[0].name,
        )

    def test_positive_update_category(self):
        category_id = add_category(CategoryCreate(name="test_category"))
        update_category(category_id, CategoryUpdate(name="Updated"))
        self.assertEqual(
            1,
            len(list_categories()),
        )
        self.assertEqual(
            "Updated",
            list_categories()[0].name,
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
        for i in range(10):
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
        self.assertEqual(
            1,
            len(list_subcategories())
        )
        self.assertEqual(
            "test_subcategory",
            list_subcategories()[0].name
        )
        self.assertEqual(
            list_categories()[0].id,
            list_subcategories()[0].category.id
        )
        self.assertEqual(
            list_subcategories()[0].id,
            list_categories()[0].subcategories[0].id
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
        self.assertEqual(
            1,
            len(list_subcategories())
        )
        self.assertEqual(
            "test_subcategory",
            list_subcategories()[0].name
        )
        self.assertEqual(
            category_id,
            list_subcategories()[0].category.id
        )
        self.assertEqual(
            "test_category",
            list_subcategories()[0].category.name
        )

    def test_positive_update_subcategory(self):
        category_id = add_category(CategoryCreate(name="test_category"))
        subcategory_id = add_subcategory(SubcategoryCreate(name="test_subcategory", category_id=category_id))
        update_subcategory(subcategory_id, SubcategoryUpdate(name="Updated"))
        self.assertEqual(
            "Updated",
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
        for i in range(10):
            add_subcategory(SubcategoryCreate(name=f"{i}", category_id=category_id))
        clear_subcategories()
        self.assertEqual([], list_subcategories())

    def tearDown(self):
        super().tearDown()
        clear_subcategories()
        clear_categories()

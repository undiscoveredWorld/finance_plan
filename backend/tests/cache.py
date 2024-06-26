import unittest

from sqlalchemy.orm import Session

from settings import CACHING_KEYS
from common.cache.redis_connect import (
    add_value_to_redis,
    get_value_from_redis,
    invalidate_key,
)
from common.data.db import get_session
from common.data.db_models import (
    Category as DB_Category,
    Subcategory as DB_Subcategory,
)
from domain.data.category import (
    add_category,
    update_category,
    delete_category,
    list_categories,
    clear_categories,
)
from domain.data.subcategory import (
    update_subcategory,
    delete_subcategory,
    list_subcategories,
    clear_subcategories,
)
from domain.data.buy import (
   clear_buys,
)
from domain.models import (
    CategoryUpdate,
    CategoryCreate,
)
from domain.models import (
    SubcategoryUpdate,
)
from utils import create_subcategory


class CategoryCacheTest(unittest.TestCase):
    def test_positive_cache_category(self):
        add_category(CategoryCreate(name="test_category"))
        result1 = list_categories()
        result2 = list_categories()
        self.assertEqual(result1, result2)

    def test_positive_list_categories_with_empty_list(self):
        add_category(CategoryCreate(name="test_category"))
        add_value_to_redis(CACHING_KEYS["categories"], b"[]")
        result = list_categories()
        self.assertEqual([], result)

    def test_positive_get_value_from_cache_on_second_list_categories(self):
        add_category(CategoryCreate(name="Food"))
        list_categories()
        _add_category_avoid_invalidation_cache("test_category")
        result = list_categories()
        self.assertEqual(1, len(result))  # Prove, that list_categories cached

        invalidate_key(CACHING_KEYS["categories"])
        result = list_categories()
        self.assertEqual(2, len(result))

    def test_positive_invalidation_cache_on_add_category(self):
        _add_test_value_to_cache(CACHING_KEYS["categories"])  # Cache will not empty
        add_category(CategoryCreate(name="test_category"))
        self._check_categories_cache_is_empty()

    def test_positive_invalidation_cache_on_update_category(self):
        category_id = add_category(CategoryCreate(name="test_category"))
        _add_test_value_to_cache(CACHING_KEYS["categories"])
        update_category(category_id, CategoryUpdate(name="test_category"))
        self._check_categories_cache_is_empty()

    def test_positive_invalidation_cache_on_delete_category(self):
        category_id = add_category(CategoryCreate(name="test_category"))
        _add_test_value_to_cache(CACHING_KEYS["categories"])
        delete_category(category_id)
        self._check_categories_cache_is_empty()

    def test_positive_invalidation_cache_on_clear_categories(self):
        _add_test_value_to_cache(CACHING_KEYS["categories"])
        clear_categories()
        self._check_categories_cache_is_empty()

    def _check_categories_cache_is_empty(self):
        self.assertEqual(
            None,
            get_value_from_redis(CACHING_KEYS["categories"])
        )

    def test_negative_list_categories_with_invalid_cache(self):
        add_value_to_redis(CACHING_KEYS["categories"], b"")
        result = list_categories()
        self.assertEqual([], result)

    def tearDown(self):
        super().tearDown()
        clear_buys()
        clear_subcategories()
        clear_categories()


class SubcategoryCacheTest(unittest.TestCase):
    def test_positive_cache_subcategory(self):
        create_subcategory()
        result1 = list_subcategories()
        result2 = list_subcategories()
        self.assertEqual(result1, result2)

    def test_positive_list_subcategories_with_empty_list(self):
        create_subcategory()
        add_value_to_redis(CACHING_KEYS["subcategories"], b"[]")
        result = list_subcategories()
        self.assertEqual([], result)

    def test_positive_get_value_from_cache_on_second_list_subcategories(self):
        category_id, _ = create_subcategory()
        list_subcategories()
        _add_subcategory_avoid_invalidation_cache(category_id, "test_subcategory2")
        result = list_subcategories()
        self.assertEqual(1, len(result))

        invalidate_key(CACHING_KEYS["subcategories"])
        result = list_subcategories()
        self.assertEqual(2, len(result))

    def test_positive_invalidation_cache_on_add_subcategory(self):
        _add_test_value_to_cache(CACHING_KEYS["subcategories"])
        create_subcategory()
        self._check_subcategories_cache_is_empty()

    def test_positive_invalidation_cache_on_update_subcategory(self):
        _, subcategory_id = create_subcategory()
        _add_test_value_to_cache(CACHING_KEYS["subcategories"])
        update_subcategory(subcategory_id, SubcategoryUpdate(name="test_subcategory2"))
        self._check_subcategories_cache_is_empty()

    def test_positive_invalidation_cache_on_delete_subcategory(self):
        _, subcategory_id = create_subcategory()
        _add_test_value_to_cache(CACHING_KEYS["subcategories"])
        delete_subcategory(subcategory_id)
        self._check_subcategories_cache_is_empty()

    def test_positive_invalidation_cache_on_clear_subcategories(self):
        _add_test_value_to_cache(CACHING_KEYS["subcategories"])
        clear_subcategories()
        self._check_subcategories_cache_is_empty()

    def _check_subcategories_cache_is_empty(self):
        self.assertEqual(
            None,
            get_value_from_redis(CACHING_KEYS["subcategories"])
        )

    def test_negative_list_subcategories_with_invalid_cache(self):
        add_value_to_redis(CACHING_KEYS["subcategories"], b"")
        result = list_subcategories()
        self.assertEqual([], result)

    def tearDown(self):
        super().tearDown()
        clear_buys()
        clear_subcategories()
        clear_categories()


def _add_category_avoid_invalidation_cache(name):
    session: Session = get_session()
    session.add(DB_Category(name=name))
    session.commit()


def _add_subcategory_avoid_invalidation_cache(category_id, name):
    session: Session = get_session()
    session.add(DB_Subcategory(category_id=category_id, name=name))
    session.commit()


def _add_test_value_to_cache(caching_key):
    add_value_to_redis(caching_key, b"[]")

import unittest
from typing import List, Dict
from pydantic import BaseModel

import common
from common.data import Catalog


class TestModel(BaseModel):
    name: str


class CatalogTestCase(unittest.TestCase):
    test_catalog: Catalog

    def test_positive_create_catalog(self):
        Catalog("Catalog_Positive")

    def test_create_catalog_with_engaged_name(self):
        Catalog("Engaged_Catalog")
        with self.assertRaises(RuntimeError):
            Catalog("Engaged_Catalog")

    def test_positive_list_catalog(self):
        result: List[Dict] = self.test_catalog.get_all_elements()
        self.assertTrue(type(result) is list)
        self.assertEqual([], result)

    def test_safety_data_after_list_catalog(self):
        self.test_catalog.add_element(
            {"name":  "sdaf"}
        )
        self.test_catalog.get_all_elements()
        self.assertEqual(
            [{
                "name": "sdaf"
            }],
            common.data._data[self.test_catalog.get_catalog_name()]
        )

    def test_positive_add_element_to_catalog(self):
        self.test_catalog.add_element(
            TestModel(name="dsf").model_dump()
        )
        result: List[Dict] = self.test_catalog.get_all_elements()
        self.assertEqual(
            [{
                "name": "dsf",
                "id": 0
            }],
            result
        )

    def test_add_element_with_id_to_catalog(self):
        with self.assertRaises(RuntimeError):
            self.test_catalog.add_element(
                {
                    "id": 100,
                    "name": "naasdf"
                }
            )

    def test_positive_update_element_in_catalog(self):
        self.test_catalog.add_element(
            TestModel(name="Original").model_dump()
        )
        self.test_catalog.update_element(
            0,
            TestModel(name="Updated").model_dump()
        )

        result: List[Dict] = self.test_catalog.get_all_elements()
        self.assertEqual(
            [{
                "id": 0,
                "name": "Updated"
            }],
            result
        )

    def test_update_element_with_id_in_catalog(self):
        self.test_catalog.add_element(
            {
                "name": "Original"
            }
        )
        with self.assertRaises(RuntimeError):
            self.test_catalog.update_element(
                0,
                {
                    "id": 100,
                    "name": "Original"
                }
            )

    def test_update_by_free_id(self):
        with self.assertRaises(IndexError):
            self.test_catalog.update_element(100, {})

    def test_positive_delete_element_in_catalog(self):
        self.test_catalog.add_element({})
        self.test_catalog.delete_element(0)
        self.assertEqual(
            0,
            len(self.test_catalog.get_all_elements())
        )

    def test_delete_by_free_id(self):
        with self.assertRaises(IndexError):
            self.test_catalog.delete_element(100)

    def setUp(self):
        super().setUp()
        self.test_catalog = Catalog("Test_catalog")

    def tearDown(self):
        super().tearDown()
        common.data._data = dict()



import unittest

from typing import List, Dict
from pydantic import BaseModel

import common
from common.data import (
    Catalog,
    save_data_to_json_file,
    load_data_to_ram_from_json_file,
    check_object_is_subclass_of_model,
    check_unique_of_field_in_catalog,
)


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
        self.assertTrue(isinstance(result, list))
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
            self.test_catalog.update_element(100, {"name": "q"})

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

    def test_positive_clear_catalog(self):
        for i in range(10):
            self.test_catalog.add_element({"name": "fsdf"})
        self.test_catalog.clear_catalog()

        self.assertEqual(
            [],
            common.data._data[self.test_catalog.get_catalog_name()]
        )

    def setUp(self):
        super().setUp()
        self.test_catalog = Catalog("Test_catalog")

    def tearDown(self):
        super().tearDown()
        common.data._data = {}


class OtherTestCase(unittest.TestCase):
    __original_path_data_file: str
    test_catalog: Catalog

    def test_positive_save_load_data(self):
        self.test_catalog.add_element(
            {
                "name": "sdf"
            }
        )
        save_data_to_json_file()
        self.test_catalog.add_element(
            {
                "name": "sdf"
            }
        )
        load_data_to_ram_from_json_file()

        self.assertEqual(
            [{
                "name": "sdf"
            }],
            common.data._data["Test_catalog"]
        )

    def test_positive_save_load_empty_data(self):
        save_data_to_json_file()
        load_data_to_ram_from_json_file()
        self.assertEqual(
            [],
            common.data._data["Test_catalog"]
        )

    def test_save_with_busy_data(self):
        common.data._data["Test_catalog"] = {}
        with self.assertRaises(RuntimeError):
            save_data_to_json_file()

    def test_positive_check_catalog_name_engaged(self):
        Catalog("Engaged")
        self.assertTrue(common.data._check_catalog_name_engaged("Engaged"))

    def test_positive_check_id_field_exist(self):
        with self.assertRaises(RuntimeError):
            common.data._check_id_field_exist(
                {
                    "id": 2,
                    "name": "sdf"
                }
            )

        common.data._check_id_field_exist(
            {"name": "sdf"}
        )

    def test_positive_check_data_types_valid(self):
        common.data._data = []
        self.assertFalse(common.data._check_data_types_valid())

        common.data._data = {4: []}
        self.assertFalse(common.data._check_data_types_valid())

        common.data._data = {"a": []}
        self.assertTrue(common.data._check_data_types_valid())

        common.data._data = {"a": [324]}
        self.assertFalse(common.data._check_data_types_valid())

        common.data._data = {"a": [{}, {}]}
        self.assertTrue(common.data._check_data_types_valid())

    def test_positive_check_object_is_subclass_of_base_model(self):
        class A(BaseModel):
            name: str

        class B(BaseModel):
            name: str

        class C(B):
            description: str

        a = A(name="A")
        b = B(name="B")
        c = C(name="C", description="")

        check_object_is_subclass_of_model(a, A)
        check_object_is_subclass_of_model(b, B)
        check_object_is_subclass_of_model(c, C)
        check_object_is_subclass_of_model(c, B)

        with self.assertRaises(RuntimeError):
            check_object_is_subclass_of_model(c, A)
        with self.assertRaises(RuntimeError):
            check_object_is_subclass_of_model(b, A)
        with self.assertRaises(RuntimeError):
            check_object_is_subclass_of_model(b, C)

    def test_positive_check_unique_of_field_in_catalog(self):
        self.test_catalog.add_element({"name": "sdf"})
        with self.assertRaises(RuntimeError):
            check_unique_of_field_in_catalog(
                value="sdf",
                field_name="name",
                catalog_name=self.test_catalog.get_catalog_name()
            )

    def test_check_unique_of_field_in_catalog_with_busy_catalog_name(self):
        with self.assertRaises(KeyError):
            check_unique_of_field_in_catalog(
                value="dasf",
                field_name="name",
                catalog_name="busy"
            )

    def setUp(self):
        super().setUp()
        self.test_catalog = Catalog("Test_catalog")

    def tearDown(self):
        super().tearDown()
        common.data._data = {}

import unittest
from pydantic import BaseModel

from common.data.utils import check_object_is_subclass_of_model
from common.data.import_data import read_range_from_sheet


class A(BaseModel):
    name: str


class B(BaseModel):
    name: str


class C(A):
    name: str


class UtilsTest(unittest.TestCase):
    def test_positive_check_object_is_subclass_of_model(self):
        a = A(name="sdf")
        b = B(name="sdf")
        c = C(name="sdf")
        check_object_is_subclass_of_model(a, BaseModel)
        check_object_is_subclass_of_model(a, A)
        check_object_is_subclass_of_model(b, B)
        check_object_is_subclass_of_model(c, A)
        with self.assertRaises(TypeError):
            check_object_is_subclass_of_model(a, B)
        with self.assertRaises(TypeError):
            check_object_is_subclass_of_model(a, C)


class ImportDataTest(unittest.TestCase):
    def test_positive_read_range(self):
        data: list[list[str]] = read_range_from_sheet(
            path_to_file="./test_read_range.xlsx",
            sheet_name="Sheet1",
            range_="A1:E1")
        self.assertEqual(
            [['5', 'string', '2024-12-03 00:00:00', '', '']],
            data
        )


if __name__ == '__main__':
    unittest.main()

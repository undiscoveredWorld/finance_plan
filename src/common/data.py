import ast
import copy
import logging

from typing import List, Dict

from settings import PATH_TO_DATA_FILE


_data: Dict[str, List[Dict]] = {}


class Catalog:
    _catalog_name: str

    def __init__(self, catalog_name: str):
        if _check_catalog_name_engaged(catalog_name):
            logging.warning("Trying to create catalog with engaged name")
            raise RuntimeError("Catalog name is engaged")

        self._catalog_name = catalog_name

        _data[self._catalog_name] = []

    def add_element(self, element: Dict) -> None:
        _check_id_field_exist(element)
        _data[self._catalog_name].append(element)

    def get_all_elements(self) -> List[Dict]:
        result: List[Dict] = copy.deepcopy(_data[self._catalog_name])
        for i in range(len(result)):
            result[i]["id"] = i
        return result

    def update_element(self, id_: int, new_element: Dict) -> None:
        _check_id_field_exist(new_element)
        _data[self._catalog_name][id_] = new_element
        for key, value in new_element.items():
            _data[self._catalog_name][id_][key] = value

    def delete_element(self, id_: int) -> None:
        _data[self._catalog_name].pop(id_)

    def get_catalog_name(self) -> str:
        return self._catalog_name


def save_data_to_json_file() -> None:
    """ save_data_to_json_file opens or creates a json file and writes in it current state of data. """
    with open(PATH_TO_DATA_FILE, 'w', encoding='UTF-8') as file:
        file.write(
            str(_data)
        )


def load_data_to_ram_from_json_file() -> None:
    """
    load_data_to_ram_from_json_file opens file and reads in ram.
    :raises: FileNotFoundError
    """
    with open(PATH_TO_DATA_FILE, 'r', encoding='UTF-8') as file:
        global _data
        data = file.read()
        data_dict = ast.literal_eval(data)
        _data = data_dict


def _check_catalog_name_engaged(catalog_name: str) -> bool:
    """ _check_catalog_name_engaged returns true, if name engaged, and false otherwise. """
    if catalog_name not in _data.keys():
        return False
    return True


def _check_id_field_exist(element: Dict):
    if "id" in element.keys():
        logging.warning("Trying create element with id field")
        raise RuntimeError("Element contains reserved field -- id.")

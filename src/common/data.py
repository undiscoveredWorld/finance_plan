import ast
import os

from pydantic import BaseModel
from typing import List, Dict, Type

from settings import PATH_TO_DATA_FILE


_data: Dict[str, List[Dict]] = dict()


class Catalog:
    _catalog_name: str
    _StorageModel: Type[BaseModel]

    def __init__(self, catalog_name: str, storage_model: Type[BaseModel]):
        self._catalog_name = catalog_name
        self._storage_model = storage_model

        _data[self._catalog_name] = list()

    def add_element(self, element: BaseModel) -> None:
        element_dict = element.model_dump()
        element_dict["id"] = len(_data[self._catalog_name])

        _data[self._catalog_name].append(element_dict)

    def get_all_elements(self) -> List[Dict]:
        return _data[self._catalog_name]

    def update_element(self, id_: int, new_element: Dict) -> None:
        _data[self._catalog_name][id_] = new_element

    def delete_element(self, id_: int) -> None:
        _data[self._catalog_name].pop(id_)


def save_data_to_json_file() -> None:
    """ save_data_to_json_file opens or creates a json file and writes in it current state of data. """
    with open(PATH_TO_DATA_FILE, 'w') as file:
        file.write(
            str(_data)
        )


def load_data_to_ram_from_json_file() -> None:
    """
    load_data_to_ram_from_json_file opens file and reads in ram.
    :raises: FileNotFoundError
    """
    with open(PATH_TO_DATA_FILE, 'r') as file:
        global _data
        data = file.read()
        data_dict = ast.literal_eval(data)
        _data = data_dict

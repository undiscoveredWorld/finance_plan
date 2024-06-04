import ast
import logging

from pydantic import BaseModel

import common.data
from common.data import _data
from settings import PATH_TO_DATA_FILE


def save_data_to_json_file() -> None:
    """Open or create a json file and write in it current state of data.

    Raises:
        RuntimeError
    """
    _check_data_types_valid()
    with open(PATH_TO_DATA_FILE, 'w', encoding='utf-8') as file:
        file.write(
            str(_data)
        )


def _check_data_types_valid():
    """Check _data on type dict[str, list[dict].

    Raises:
         RuntimeError: if type is not valid."""
    if not _is_data_types_valid():
        logging.warning("Data is busy")
        raise RuntimeError("Cannot save data to json file. Data is busy")


def _is_data_types_valid() -> bool:
    """Return true, if _data type is Dict[str, List[Dict]], else false."""
    if not isinstance(_data, dict):
        return False

    for catalog_name in _data.keys():
        if not isinstance(catalog_name, str):
            return False

    for catalog in _data.values():
        if not isinstance(catalog, list):
            return False

        for element in catalog:
            if not isinstance(element, dict):
                return False

    return True


def load_data_to_ram_from_json_file() -> None:
    """Open file and read it in ram.

    Raises:
        FileNotFoundError
    """
    with open(PATH_TO_DATA_FILE, 'r', encoding='UTF-8') as file:
        data = file.read()
        data_dict = ast.literal_eval(data)
        common.data._data = data_dict


def check_object_is_subclass_of_model(object_: BaseModel, model: type[BaseModel]) -> None:
    """Raise ValueError if object is not subclass of model.

    Raises:
        ValueError
    """
    if not issubclass(object_.__class__, model):
        logging.warning(f"Trying create object by invalid model. Got {object_.__class__}, expected {model}")
        raise ValueError(f"Got an invalid model to create. Got {object_.__class__}, expected {model}")


def check_unique_of_field_in_catalog(value: any, field_name: str, catalog_name: str) -> None:
    """Raise RuntimeError if there is value of field in catalog.

    Raises:
        RuntimeError
    """
    for element in _data[catalog_name]:
        if element[field_name] == value:
            logging.warning("Trying duplicate unique field value")
            raise RuntimeError(f"Field {field_name} is unique. Got {value}, it isn't unique in {catalog_name}")

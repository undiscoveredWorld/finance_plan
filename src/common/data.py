import ast
import copy
import logging

from pydantic import BaseModel

from settings import PATH_TO_DATA_FILE

_data: dict[str, list[dict]] = {}


class Catalog:
    """Class to encystment work with _data."""

    _catalog_name: str

    def __init__(self, catalog_name: str):
        """Initialize the Catalog.

        Args:
            catalog_name: Name of the catalog(key in _data). Must be str. Cannot be empty str -- ""
        Raises:
            RuntimeError
        """
        self._set_catalog_name(catalog_name)
        _data[self._catalog_name] = []

    def get_catalog_name(self) -> str:
        return self._catalog_name

    def _set_catalog_name(self, catalog_name: str) -> None:
        """Set name of catalog.

        Args:
            catalog_name: Name of the catalog(key in _data). Must be str. Cannot be empty str -- ""
        """
        _check_catalog_name_engaged(catalog_name)
        if type(catalog_name) is str and catalog_name != "":
            self._catalog_name = catalog_name

    def clear_catalog(self) -> None:
        _data[self._catalog_name] = []

    def add_element(self, element: dict) -> None:
        """Add an element to catalog.

        Args:
            element: Element to adding. Cannot contain id field(key)
        Raises:
            RuntimeError
        """
        _check_id_field_exist(element)
        _data[self._catalog_name].append(element)

    def get_all_elements(self) -> list[dict]:
        result = _put_in_all_elements_id_field(_data[self._catalog_name])
        return result

    def update_element(self, id_: int, new_element: dict) -> None:
        """Update element in _data.

        Raises:
            IndexError, RuntimeError
        """
        _check_id_field_exist(new_element)
        for key, value in new_element.items():
            if value is not None:
                _data[self._catalog_name][id_][key] = value

    def delete_element(self, id_: int) -> None:
        """Delete element in _data.

        Raises:
            IndexError
        """
        _data[self._catalog_name].pop(id_)


def save_data_to_json_file() -> None:
    """Open or create a json file and write in it current state of data.

    Raises:
        RuntimeError
    """
    if not _is_data_types_valid():
        logging.warning("Data is busy")
        raise RuntimeError("Cannot save data to json file. Data is busy")
    with open(PATH_TO_DATA_FILE, 'w', encoding='utf-8') as file:
        file.write(
            str(_data)
        )


def load_data_to_ram_from_json_file() -> None:
    """Open file and read it in ram.

    Raises:
        FileNotFoundError
    """
    with open(PATH_TO_DATA_FILE, 'r', encoding='UTF-8') as file:
        global _data
        data = file.read()
        data_dict = ast.literal_eval(data)
        _data = data_dict


def check_object_is_subclass_of_model(object_: BaseModel, model: type[BaseModel]) -> None:
    """Raise RuntimeError if object is not subclass of model.

    Raises:
        RuntimeError
    """
    if not issubclass(object_.__class__, model):
        logging.warning(f"Trying create object by invalid model. Got {object_.__class__}, expected {model}")
        raise RuntimeError(f"Got an invalid model to create. Got {object_.__class__}, expected {model}")


def check_unique_of_field_in_catalog(value: any, field_name: str, catalog_name: str) -> None:
    """Raise RuntimeError if there is value of field in catalog.

    Raises:
        RuntimeError
    """
    for element in _data[catalog_name]:
        if element[field_name] == value:
            logging.info("Trying duplicate unique field value")
            raise RuntimeError(f"Field {field_name} is unique. Got {value}, it isn't unique in {catalog_name}")


def _check_catalog_name_engaged(catalog_name: str) -> None:
    """Raise RuntimeError if catalog name is engaged.

    Raises:
        RuntimeError
    """
    if catalog_name in _data.keys():
        logging.warning("Trying to create catalog with engaged name")
        raise RuntimeError("Catalog name is engaged")


def _check_id_field_exist(element: dict):
    """Raise RuntimeError if element have id field.

    Raises:
        RuntimeError
    """
    if "id" in element.keys():
        logging.warning("Trying create element with id field")
        raise RuntimeError("Element contains reserved field -- id.")


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


def _put_in_all_elements_id_field(elements: list[dict]) -> list[dict]:
    """Put field id in any element in elements."""
    result: list[dict] = copy.deepcopy(elements)
    for i in range(len(result)):
        result[i]["id"] = i
    return result

import copy
import logging

from common.data import _data


class Catalog:
    """Class to encystment work with _data."""

    _catalog_name: str

    def __init__(self, catalog_name: str):
        """Initialize the Catalog.

        Args:
            catalog_name: Name of the catalog(key in _data). Must be str. Cannot be empty str -- ""
        Raises:
            RuntimeError
            ValueError
        """
        self._set_catalog_name(catalog_name)
        _data[self._catalog_name] = []

    def get_catalog_name(self) -> str:
        return self._catalog_name

    def _set_catalog_name(self, catalog_name: str) -> None:
        """Set name of catalog.

        Args:
            catalog_name: Name of the catalog(key in _data). Must be str. Cannot be empty str -- ""
        Raises:
            RuntimeError
            ValueError
        """
        _check_catalog_name_engaged(catalog_name)
        if type(catalog_name) is str and catalog_name != "":
            self._catalog_name = catalog_name
        else:
            raise ValueError("Cannot create catalog. Name must be a string but not empty.")

    def clear_catalog(self) -> None:
        _data[self._catalog_name] = []

    def add_element(self, element: dict) -> None:
        """Add an element to catalog.

        Args:
            element: Element to adding. Cannot contain id field(key)
        Raises:
            ValueError
        """
        _check_id_field_exist(element)
        _data[self._catalog_name].append(element)

    def get_all_elements(self) -> list[dict]:
        result = _put_in_all_elements_id_field(_data[self._catalog_name])
        return result

    def update_element(self, id_: int, new_element: dict) -> None:
        """Update element in _data.

        Raises:
            ValueError
            IndexError
        """
        _check_id_field_exist(new_element)
        for key, value in new_element.items():
            if value is not None and value != _data[self._catalog_name][id_][key]:
                _data[self._catalog_name][id_][key] = value

    def delete_element(self, id_: int) -> None:
        """Delete element in _data.

        Raises:
            IndexError
        """
        _data[self._catalog_name].pop(id_)


def _check_catalog_name_engaged(catalog_name: str) -> None:
    """Raise RuntimeError if catalog name is engaged.

    Raises:
        RuntimeError
    """
    if catalog_name in _data.keys():
        logging.warning("Trying to create catalog with engaged name")
        raise RuntimeError("Catalog name is engaged")


def _check_id_field_exist(element: dict):
    """Raise ValueError if element have id field.

    Raises:
        ValueError
    """
    if "id" in element.keys():
        logging.warning("Trying create element with id field")
        raise ValueError("Element contains reserved field -- id.")


def _put_in_all_elements_id_field(elements: list[dict]) -> list[dict]:
    """Put field id in any element in elements."""
    result: list[dict] = copy.deepcopy(elements)
    for i in range(len(result)):
        result[i]["id"] = i
    return result

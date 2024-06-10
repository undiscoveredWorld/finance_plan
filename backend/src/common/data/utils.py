import logging

from pydantic import BaseModel


def check_object_is_subclass_of_model(object_: BaseModel, model: type[BaseModel]) -> None:
    """Raise TypeError if object is not subclass of model.

    Raises:
        TypeError: if object is not subclass of model
    """
    if not issubclass(object_.__class__, model):
        logging.warning(f"Trying create object by invalid model. Got {object_.__class__}, expected {model}")
        raise TypeError(f"Got an invalid model to create. Got {object_.__class__}, expected {model}")

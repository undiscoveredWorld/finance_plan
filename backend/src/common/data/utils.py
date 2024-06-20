import logging

from fastapi import UploadFile

from pydantic import BaseModel


def check_object_is_subclass_of_model(object_: BaseModel, model: type[BaseModel]) -> None:
    """Raise TypeError if object is not subclass of model.

    Raises:
        TypeError: if object is not subclass of model
    """
    if not issubclass(object_.__class__, model):
        logging.warning(f"Trying create object by invalid model. Got {object_.__class__}, expected {model}")
        raise TypeError(f"Got an invalid model to create. Got {object_.__class__}, expected {model}")


def create_uploaded_file(file: UploadFile, path_to_file: str):
    """Create file from UploadFile."""
    contents = file.file.read()
    with open(path_to_file, "wb") as f:
        f.write(contents)


def convert_return_to_list_of_model(model: type[BaseModel]) -> callable:
    """Convert return to list of model.

    To use func must return list of objects with properties as like as model.
    Don't work with DB Models, that have from_attributes fields.

    Returns: decorator, that converts the return to list of model
    """
    def decorator(func: callable) -> callable:
        def inner_func(*_args, **_kwargs) -> list[model]:
            func_result: list = func(*_args, **_kwargs)
            func_result_model: list[model] = []
            for f in func_result:
                func_result_model.append(model.model_validate(f.__dict__))
            return func_result_model
        return inner_func
    return decorator

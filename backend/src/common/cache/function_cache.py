import ast
from pydantic import BaseModel

from common.cache.redis_connect import (
    get_value_from_redis,
    add_value_to_redis,
    invalidate_key,
)


def redis_cache_list_models(key: str) -> callable(callable):
    """Return decorator for caching function in redis.

    Function must return a list of BaseModel or None.
    """

    def decorator(func: callable):
        model: type = object

        def inner_func(*args, **kwargs):
            nonlocal model
            value = get_value_from_redis(key)
            if value is None:
                func_result = func(*args, **kwargs)
                model = _get_model_of_func_result(func_result)
                func_result_str = _convert_func_result_to_str(func_result)
                add_value_to_redis(key, str(func_result_str))
                return func_result

            value_model = _convert_str_value_to_list_of_model_objects(model, value)

            return value_model

        return inner_func

    return decorator


def _get_model_of_func_result(func_result: list[BaseModel]) -> type:
    model: type = object
    if type(func_result) is list:
        if len(func_result) > 0:
            model = func_result[0].__class__
    return model


def _convert_func_result_to_str(func_result: list[BaseModel]) -> str:
    func_result_dumped: list[dict] = _dump_func_result(func_result)
    func_result_str: str = str(func_result_dumped)
    return func_result_str


def _dump_func_result(func_result: list[BaseModel]) -> list[dict]:
    func_result_dumped: list[dict] = []
    for row in func_result:
        func_result_dumped.append(row.model_dump())
    return func_result_dumped


def _convert_str_value_to_list_of_model_objects(model, value):
    value_json: list[dict] = ast.literal_eval(value.decode('utf-8'))
    value_model: list[BaseModel] = []
    if issubclass(BaseModel, model):
        for v in value_json:
            value_model.append(model.model_validate(v))
    return value_model


def invalidate_cache_by_call(key: str):
    """Return decorator to invalidate cache by call of inner func."""
    def decorator(func):
        def inner_func(*args, **kwargs):
            invalidate_key(key)
            result_func = func(*args, **kwargs)

            return result_func

        return inner_func

    return decorator

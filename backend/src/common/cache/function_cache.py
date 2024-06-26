import ast
import logging

from pydantic import BaseModel, ValidationError

from common.cache.redis_connect import (
    get_value_from_redis,
    add_value_to_redis,
    invalidate_key,
)


def redis_cache_list_models(key: str, cache_model: type[BaseModel]) -> callable(callable):
    """Return decorator for caching function in redis.

    Function must return a list of BaseModel or None.
    Args:
        key:
        cache_model: the model the cache will work with. when data is received from cache, it will be validated against the MODEL
    """

    def decorator(func: callable):
        MODEL: type[BaseModel] = cache_model

        def inner_func(*args, **kwargs):
            nonlocal MODEL
            cached_value = get_value_from_redis(key)
            if type(cached_value) is not bytes:
                value = None
            else:
                value = _convert_bytes_cache_to_list_of_model_objects(value=cached_value, model=MODEL)

            if value is None:
                func_result = func(*args, **kwargs)
                func_result_str = _convert_func_result_to_str(func_result)
                add_value_to_redis(key, str(func_result_str))
                return func_result

            return value

        return inner_func

    return decorator


def _convert_func_result_to_str(func_result: list[BaseModel]) -> str:
    func_result_dumped: list[dict] = _dump_func_result(func_result)
    func_result_str: str = str(func_result_dumped)
    return func_result_str


def _dump_func_result(func_result: list[BaseModel]) -> list[dict]:
    func_result_dumped: list[dict] = []
    for row in func_result:
        func_result_dumped.append(row.model_dump())
    return func_result_dumped


def _convert_bytes_cache_to_list_of_model_objects(value: bytes, model: type[BaseModel] | None) -> list | None:
    value_json: list[dict] | None = _get_json_list_or_none_from_bytes(value)
    if value_json is None:
        return value_json

    value_model: list[BaseModel] = []
    if issubclass(model, BaseModel):
        for v in value_json:
            try:
                value_model.append(model.model_validate(v))
            except ValidationError as e:
                logging.exception(e)
                return None
    return value_model


def _get_json_list_or_none_from_bytes(value_bytes: bytes) -> list[dict] | None:
    if type(value_bytes) is not bytes:
        return None

    try:
        result = ast.literal_eval(value_bytes.decode('utf-8'))
        if type(result) is list:
            return result
        else:
            return None
    except Exception as e:
        logging.warning("Error while converting str value to list of model")
        logging.exception(e)
        return None


def invalidate_cache_by_call(key: str):
    """Return decorator to invalidate cache by call of inner func."""

    def decorator(func):
        def inner_func(*args, **kwargs):
            invalidate_key(key)
            result_func = func(*args, **kwargs)
            return result_func

        return inner_func

    return decorator

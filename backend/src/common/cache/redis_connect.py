import redis

from settings import (
    REDIS_HOST,
    REDIS_PORT,
)

pool = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, db=0)
redis_conn = redis.Redis(connection_pool=pool)


def add_value_to_redis(key, value):
    redis_conn.set(key, value)


def get_value_from_redis(key) -> any:
    return redis_conn.get(key)


def invalidate_key(key):
    redis_conn.delete(key)

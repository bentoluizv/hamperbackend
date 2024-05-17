import redis
from dynaconf import settings

REDIS_URL = settings["REDIS_URL"]

redis_connection = redis.from_url(REDIS_URL)

def set_redis_value(key, value):
    redis_connection.set(key, value)

def delete_redis_value(key):
    redis_connection.delete(key)

def get_redis_value(key):
    redis_connection.get(key)
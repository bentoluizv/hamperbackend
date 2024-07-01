import redis
from dynaconf import settings

url = settings["REDIS_URL"]

redis_connection = redis.Redis.from_url(url)


def set_redis_value(key, value):
    redis_connection.set(key, value)

def delete_redis_value(key):
    redis_connection.delete(key)

def get_redis_value(key):
    redis_connection.get(key)
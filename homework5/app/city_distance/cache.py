from redis import Redis

rd = Redis()


def redis_get(key):
    return rd.get(key)


def redis_set(key, value):
    rd.set(key, value)

from aiogram.fsm.storage.redis import RedisStorage
from redis.asyncio import Redis
# import redis
# from aiogram.fsm.storage.memory import MemoryStorage


# memory_fms: MemoryStorage = MemoryStorage()
# redis = Redis(host='localhost', port=6379, db=0)


redis = Redis(host='localhost')
memory_fms = RedisStorage(redis=redis)

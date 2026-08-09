from db.memory_fms import memory_fms


async def test_connection_redis():
    try:
        await memory_fms.redis.ping()
        print("Redis подключён")
    except Exception as e:
        print(f"Redis недоступен. Ошибка:\n{e}")

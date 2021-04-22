# -*- coding: UTF-8 -*-
__author__ = u'antonyuck'
import aioredis
import asyncio
async def test():
    redis = aioredis.Redis(connection_pool=aioredis.ConnectionPool.from_url("redis://localhost", socket_timeout=1))
    await redis.get('key')

asyncio.get_event_loop().run_until_complete(test())

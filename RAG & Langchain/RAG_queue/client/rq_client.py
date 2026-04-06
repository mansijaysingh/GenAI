from redis import asyncio
import redis
from rq import Queue

queue=Queue(connection=redis.asyncio.Redis(host='localhost', port=6379))


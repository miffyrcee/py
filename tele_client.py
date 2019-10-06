import asyncio
import os
import random

from telethon import TelegramClient

file_dir = os.path.dirname(__file__)
sess_path = os.path.join(file_dir, 'session_01')

api_id = 1057762
api_hash = '570890ca93e311e32e37a59e15cd5368'
client = TelegramClient(sess_path, api_id, api_hash)


async def check():
    await client.send_message('@TouhouNetworkBot', '/checkin')
    await client.send_message('@MengdiBot', '/checkin')
    await asyncio.sleep(random.randint(43200, 86400))
    await check()


with client:
    client.loop.run_until_complete(check())

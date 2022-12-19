import asyncio
from aiohttp import ClientSession

async def hello(url):
    async with ClientSession() as session:
        while True:
            await session.get(url)

loop = asyncio.new_event_loop()

loop.run_until_complete(hello("https://iccup.com/community/thread/1603767.html"))

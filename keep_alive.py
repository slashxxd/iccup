import asyncio
from aiohttp import ClientSession
import random
from bs4 import BeautifulSoup as BS


a = [chr(i) for i in range(97, 123)]

async def hello(url):
    async with ClientSession() as session:
        while True:
            b = a
            r1 = await session.get(url, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", "cookie": "threads_read=a%3A5%3A%7Bi%3A1603940%3Bi%3A1671475959%3Bi%3A1604016%3Bi%3A1671475586%3Bi%3A1600840%3Bi%3A1671474926%3Bi%3A1604012%3Bi%3A1671473995%3Bi%3A1604011%3Bi%3A1671473948%3B%7D; forums_read=a%3A1%3A%7Bi%3A408%3Ba%3A2%3A%7Bs%3A4%3A%22time%22%3Bi%3A1670322439%3Bs%3A4%3A%22read%22%3Bb%3A0%3B%7D%7D; media=screen; _ga=GA1.2.268213764.1665660534; _ym_uid=1665660539114445962; _ym_d=1665660539; _gid=GA1.2.775531604.1671362115; newlang7=1; SID=t6mq1rcigjvnf2l283t0ieefk1; _ym_isad=2; _ym_visorc=b; _gat=1; last_session_new=13d628dfb6a1806504928f5162116e5d; last_session=997cc208141bc5322fb8c4892428d0ac"})
            token = BS(await r1.read(), 'lxml').find("input", type="hidden").get("value")
            r = await session.post(url, data={"icon": "2", "title": ''.join(random.shuffle(b)), "comment": ''.join(random.shuffle(b)), "registration": "Отправить", "token": token}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36", "cookie": "threads_read=a%3A5%3A%7Bi%3A1603940%3Bi%3A1671475959%3Bi%3A1604016%3Bi%3A1671475586%3Bi%3A1600840%3Bi%3A1671474926%3Bi%3A1604012%3Bi%3A1671473995%3Bi%3A1604011%3Bi%3A1671473948%3B%7D; forums_read=a%3A1%3A%7Bi%3A408%3Ba%3A2%3A%7Bs%3A4%3A%22time%22%3Bi%3A1670322439%3Bs%3A4%3A%22read%22%3Bb%3A0%3B%7D%7D; media=screen; _ga=GA1.2.268213764.1665660534; _ym_uid=1665660539114445962; _ym_d=1665660539; _gid=GA1.2.775531604.1671362115; newlang7=1; SID=t6mq1rcigjvnf2l283t0ieefk1; _ym_isad=2; _ym_visorc=b; _gat=1; last_session_new=13d628dfb6a1806504928f5162116e5d; last_session=997cc208141bc5322fb8c4892428d0ac"})

loop = asyncio.new_event_loop()

loop.run_until_complete(hello("https://iccup.com/community/newthread/408.html"))

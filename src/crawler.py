
import aiohttp
from aiosocks.connector import ProxyConnector
from typing import List, Callable, Tuple
from config import *
import traceback
import os
import asyncio
import datetime
import random

async def get_job_page(start:int, end: int, processor: Callable[[str], dict], timegap: SECOND =5) -> Tuple[dict, set]:
    failed = set()
    sucess = {}
    conn = ProxyConnector(remote_resolve=True)
    
    async with aiohttp.ClientSession(connector=conn) as sess:
        for page in range(start, end):
            host, port = random.choice(PROXY_LIST)
            url = os.path.join(V2EX_HOST, JOB_PAGE.format(page=page))
            try:
                ua = random.choice(USER_AGENT)
                async with sess.get(url, headers={'user-agent': ua}, proxy=f'socks5://{host}:{port}') as r:
                    res = await r.text()
                    sucess[url] = processor(res)
            except Exception as e:
                print(url, str(e))
                traceback.print_exc()
                failed.add(url)
            await asyncio.sleep(timegap)
    return sucess, failed
    
                
async def get_topic_detail(topic_ids: List[int], processor: Callable[[str, dict], dict], timegap: SECOND=15):
    failed = set()
    sucess = {}
    conn = ProxyConnector(remote_resolve=True)
    async with aiohttp.ClientSession(connector=conn) as sess:
        for topic_id in topic_ids:
            host, port = random.choice(PROXY_LIST)
            api_url = os.path.join(V2EX_HOST, TOPIC_API.format(topic_id=topic_id))
            url = os.path.join(V2EX_HOST, TOPIC_PAGE.format(topic_id=topic_id))
            try:
                html, json = None, None
                ua = random.choice(USER_AGENT)
                async with sess.get(api_url, headers={'user-agent': ua}, proxy=f'socks5://{host}:{port}') as r:
                    count = r.headers['x-rate-limit-remaining']
                    if int(count) > 0:
                        json = await r.json()
                    else:
                        current = int(datetime.datetime.now().timestamp())
                        nxt = int(r.headers['x-rate-limit-reset'])
                        if nxt > current:
                            await asyncio.sleep(nxt - current)
                        else:
                            failed.add(topic_id)
                ua = random.choice(USER_AGENT)
                async with sess.get(url, headers={'user-agent': ua}, proxy=f'socks5://{host}:{port}') as r:
                    html = await r.text()
                sucess[topic_id] = processor(html, json[0])
            except Exception as e:
                print(url, str(e))
                traceback.print_exc()
                failed.add(topic_id)
            await asyncio.sleep(timegap)
    return sucess, failed




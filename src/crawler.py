import aiohttp
from typing import List, Callable, Tuple
from config import *
import traceback
import os
import asyncio
import datetime


async def get_job_page(start:int, end: int, processor: Callable[[str], dict], timegap: SECOND =5) -> Tuple[dict, set]:
    failed = set()
    sucess = {}
    async with aiohttp.ClientSession() as sess:
        for page in range(start, end + 1):
            url = os.path.join(V2EX_HOST, JOB_PAGE.format(page=page))
            try:
                async with sess.get(url) as r:
                    res = await r.text()
                    sucess[url] = processor(res)
            except Exception as e:
                print(url, traceback.format_exception(e))
                failed.add(url)
            await asyncio.sleep(timegap)
    return sucess, failed
    
                
async def get_topic_detail(topic_ids: List[int], processor: Callable[[str, dict], dict], timegap: SECOND=30):
    failed = set()
    sucess = {}
    async with aiohttp.ClientSession() as sess:
        for topic_id in topic_ids:
            api_url = os.path.join(V2EX_HOST, TOPIC_API.format(topic_id=topic_id))
            url = os.path.join(V2EX_HOST, TOPIC_PAGE.format(topic_id=topic_id))
            try:
                html, json = None, None
                async with sess.get(api_url) as r:
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
                async with sess.get(url) as r:
                    html = await r.json()
                sucess[topic_id] = processor(html, json)
            except Exception as e:
                print(topic_id, traceback.format_exception(e))
                failed.add(topic_id)
            await asyncio.sleep(timegap)
    return sucess, failed




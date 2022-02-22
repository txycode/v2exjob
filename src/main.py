
from crawler import get_job_page, get_topic_detail
from processor import job_page_processor, topic_page_processor
import asyncio
import json
import os
current_path = os.path.dirname(os.path.abspath(__file__))

async def fetch_job_page():

    start = 1
    end = 2500
    duration = 50
    failed_set = set()
    while start < end:
        success, failed = await get_job_page(start, start + duration, job_page_processor)
        failed_set = failed_set.union(failed)
        with open(f'{current_path}/data/success{start}.json', 'w') as f:
            json.dump(success, f)
        start += 50
    with open(f'{current_path}/data/failed.json', 'w') as f:
        json.dump(failed_set, f)

async def fetch_topic_detail():
    failed_set = set()
    for i in range(1, 2500, 500):
        with open(f'{current_path}/data/success{i}.json', 'r') as f:
            res = json.load(f)
            for topics in res.values():
                success, failed = await get_topic_detail(topics, topic_page_processor, 2)
                failed_set = failed_set.union(failed)
                for topic_id in success.keys():
                    with open(f'{current_path}/data/topic_{topic_id}.json', 'w') as w:
                        success[topic_id]['create_datetime'] = str(success[topic_id]['create_datetime'])
                        json.dump(success[topic_id], w, ensure_ascii=False)
        with open(f'{current_path}/data/missing_topic{i}.json', 'w') as f:
            json.dump(failed_set, f)
            failed_set = set()

asyncio.get_event_loop().run_until_complete(fetch_job_page())
asyncio.get_event_loop().run_until_complete(fetch_topic_detail())
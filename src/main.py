
from crawler import get_job_page, get_topic_detail
from processor import job_page_processor, topic_page_processor
import asyncio
import json

async def main():

    start = 1
    end = 2500
    success, failed = await get_job_page(start, end, job_page_processor)
    # print(success, failed)
    with open('success.json', 'w') as f:
        json.dump(success, f)
    with open('failed.json', 'w') as f:
        json.dump(failed, f)



asyncio.get_event_loop().run_until_complete(main())
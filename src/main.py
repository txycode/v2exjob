
from crawler import get_job_page
from processor import job_page_processor
import asyncio
import json

async def main():

    start = 1
    end = 2500
    duration = 50
    failed_set = set()
    while start < end:
        success, failed = await get_job_page(start, start + duration, job_page_processor)
        failed_set.union(failed)
        with open(f'success{start}.json', 'a') as f:
            json.dump(success, f)
        start += 50
    with open(f'failed.json', 'w') as f:
        json.dump(failed_set)
        



asyncio.get_event_loop().run_until_complete(main())
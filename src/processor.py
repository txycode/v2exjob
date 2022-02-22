from bs4 import BeautifulSoup
from config import *
from datetime import datetime
from model import Topic
import re

pattern = re.compile(r'(?P<clcik>\d+) 次点击')

def job_page_processor(html: HTML):
    bf = BeautifulSoup(html)
    target_ids = []
    for a in bf.find_all("a", {"class": "topic-link"}):
        href = a.attrs['href']
        target_id = []
        for c in href:
            if c.isdigit():
                target_id.append(c)
            if c == '#':
                break
        
        target_ids.append(int(''.join(target_id)))

    return target_ids



def topic_page_processor(html: HTML, json: dict) -> dict:
    bf = BeautifulSoup(html)
    small = bf.find_all("small", {"class": "gray"})
    clicks = 0
    if small:
        for st in small[0].contents:
            r = pattern.search(st)
            if r:
                clicks = int(r.groups()[0])
    topic = Topic(
        id = json.get('id'),
        create_time=json.get('created'),
        create_datetime=datetime.fromtimestamp(json.get('created'), GMT8),
        content=json.get('content'),
        title=json.get('title'),
        click=clicks,
        user_id=json.get('member').get('id'),
        user_name=json.get('member').get('username'),
        reply=json.get('replies')
    )
    return topic.dict()





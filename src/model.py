from pydantic import BaseModel
from datetime import datetime

class Topic(BaseModel):
    id: int
    create_time: int
    create_datetime: datetime
    content: str
    title: str
    reply: int
    click: int
    user_id: int
    user_name: str
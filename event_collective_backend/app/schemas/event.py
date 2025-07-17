from datetime import datetime
from pydantic import BaseModel


class EventCreate(BaseModel):
    title: str
    start_time: datetime
    end_time: datetime
    location: str | None = None
    description: str | None = None


class EventRead(EventCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

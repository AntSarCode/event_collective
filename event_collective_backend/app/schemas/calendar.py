from datetime import datetime
from pydantic import BaseModel

class CalendarEventCreate(BaseModel):
    title: str
    start_time: datetime
    end_time: datetime
    description: str | None = None
    location: str | None = None

class CalendarEventRead(CalendarEventCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

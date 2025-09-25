from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict

class CalendarEventBase(BaseModel):
    title: str
    description: Optional[str] = None
    start_time: datetime
    end_time: datetime
    location: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class CalendarEventCreate(CalendarEventBase):
    pass

class CalendarEventUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    location: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)

class CalendarEventRead(CalendarEventBase):
    id: int
    model_config = ConfigDict(from_attributes=True)

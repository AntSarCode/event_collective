from sqlalchemy.orm import Session
from typing import List

from app.models.event import Event
from app.schemas.calendar import CalendarEventCreate

def create_event(db: Session, event_in: CalendarEventCreate) -> Event:
    event = Event(**event_in.model_dump())
    db.add(event)
    db.commit()
    db.refresh(event)
    return event

def get_all_events(db: Session) -> List[Event]:
    return db.query(Event).order_by(Event.start_time).all()

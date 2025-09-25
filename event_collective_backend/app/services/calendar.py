from sqlalchemy.orm import Session
from typing import List, Optional

from app.models.event import Event
from app.schemas.calendar import CalendarEventCreate, CalendarEventUpdate

def create_event(db: Session, event_in: CalendarEventCreate) -> Event:
    event = Event(**event_in.model_dump())
    db.add(event)
    db.commit()
    db.refresh(event)
    return event

def get_all_events(db: Session) -> List[Event]:
    return db.query(Event).order_by(Event.start_time).all()

def update_event(db: Session, event_id: int, event_in: CalendarEventUpdate) -> Optional[Event]:
    evt = db.query(Event).filter(Event.id == event_id).first()
    if not evt:
        return None
    for k, v in event_in.model_dump(exclude_unset=True).items():
        setattr(evt, k, v)
    db.commit()
    db.refresh(evt)
    return evt

def delete_event(db: Session, event_id: int) -> None:
    evt = db.query(Event).filter(Event.id == event_id).first()
    if evt:
        db.delete(evt)
        db.commit()

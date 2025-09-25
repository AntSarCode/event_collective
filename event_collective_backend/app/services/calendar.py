from sqlalchemy.orm import Session
from app.models.event import Event
from app.schemas.calendar import CalendarEventCreate, CalendarEventUpdate

def create_event(db: Session, data: CalendarEventCreate) -> Event:
    ev = Event(**data.model_dump())
    db.add(ev)
    db.commit()
    db.refresh(ev)
    return ev

def get_all_events(db: Session) -> list[Event]:
    return db.query(Event).order_by(Event.start_time).all()

def get_event_by_id(db: Session, event_id: int) -> Event | None:
    return db.query(Event).filter(Event.id == event_id).first()

def update_event(db: Session, event_id: int, data: CalendarEventUpdate) -> Event | None:
    ev = db.query(Event).filter(Event.id == event_id).first()
    if not ev:
        return None
    payload = data.model_dump(exclude_unset=True)
    for k, v in payload.items():
        setattr(ev, k, v)
    db.commit()
    db.refresh(ev)
    return ev

def delete_event(db: Session, event_id: int) -> bool:
    ev = get_event_by_id(db, event_id)
    if not ev:
        return False
    db.delete(ev)
    db.commit()
    return True

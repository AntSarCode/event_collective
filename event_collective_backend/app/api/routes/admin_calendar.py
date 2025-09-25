from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.schemas.calendar import CalendarEventCreate, CalendarEventUpdate, CalendarEventRead
from app.services import calendar_service

router = APIRouter(prefix='/admin/calendar', tags=['admin-calendar'])

@router.get('/', response_model=List[CalendarEventRead])
def list_events(db: Session = Depends(get_db)):
    return calendar_service.get_all_events(db)

@router.post('/', response_model=CalendarEventRead)
def post_event(data: CalendarEventCreate, db: Session = Depends(get_db)):
    return calendar_service.create_event(db, data)

@router.get('/{event_id}', response_model=CalendarEventRead)
def get_event(event_id: int, db: Session = Depends(get_db)):
    ev = calendar_service.get_event_by_id(db, event_id)
    if not ev:
        raise HTTPException(status_code=404, detail='Event not found')
    return ev

@router.put('/{event_id}', response_model=CalendarEventRead)
def put_event(event_id: int, data: CalendarEventUpdate, db: Session = Depends(get_db)):
    ev = calendar_service.update_event(db, event_id, data)
    if not ev:
        raise HTTPException(status_code=404, detail='Event not found')
    return ev

@router.delete('/{event_id}')
def delete_event(event_id: int, db: Session = Depends(get_db)):
    ok = calendar_service.delete_event(db, event_id)
    if not ok:
        raise HTTPException(status_code=404, detail='Event not found')
    return {'ok': True}

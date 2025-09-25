from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.calendar import CalendarEventCreate, CalendarEventRead, CalendarEventUpdate
from app.services import calendar_service
from app.api.deps import get_current_admin_user, get_db

router = APIRouter()

@router.get("/", response_model=List[CalendarEventRead])
def get_all_events(
    db: Session = Depends(get_db),
    admin_user=Depends(get_current_admin_user)
):
    return calendar_service.get_all_events(db)

@router.post("/", response_model=CalendarEventRead, status_code=status.HTTP_201_CREATED)
def create_event(
    event_in: CalendarEventCreate,
    db: Session = Depends(get_db),
    admin_user=Depends(get_current_admin_user)
):
    return calendar_service.create_event(db, event_in)

@router.put("/{event_id}", response_model=CalendarEventRead)
def update_event(
    event_id: int,
    event_in: CalendarEventUpdate,
    db: Session = Depends(get_db),
    admin_user=Depends(get_current_admin_user)
):
    return calendar_service.update_event(db, event_id, event_in)

@router.delete("/{event_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_event(
    event_id: int,
    db: Session = Depends(get_db),
    admin_user=Depends(get_current_admin_user)
):
    calendar_service.delete_event(db, event_id)
    return None

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.message import (
    MessageCreate,
    MessageRead,
    MessageUpdate,
)
from app.services import message_service
from app.api.deps import get_current_admin_user, get_db

router = APIRouter()

@router.get("/", response_model=List[MessageRead])
def get_all_messages_route(
    db: Session = Depends(get_db),
    _admin_user = Depends(get_current_admin_user),
):
    return message_service.get_all_messages(db)


@router.post("/", response_model=MessageRead, status_code=status.HTTP_201_CREATED)
def create_message_route(
    message_in: MessageCreate,
    db: Session = Depends(get_db),
    _admin_user = Depends(get_current_admin_user),
):
    return message_service.create_message(db, message_in)


@router.put("/{message_id}", response_model=MessageRead)
def update_message_route(
    message_id: int,
    message_in: MessageUpdate,
    db: Session = Depends(get_db),
    _admin_user = Depends(get_current_admin_user),
):
    return message_service.update_message(db, message_id, message_in)


@router.delete("/{message_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_message_route(
    message_id: int,
    db: Session = Depends(get_db),
    _admin_user = Depends(get_current_admin_user),
):
    message_service.delete_message(db, message_id)
    return None
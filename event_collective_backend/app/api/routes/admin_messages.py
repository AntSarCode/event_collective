from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.message import AdminMessageCreate, AdminMessageRead
from app.services import message_service
from app.api.deps import get_current_admin_user, get_db

router = APIRouter()

@router.get("/", response_model=List[AdminMessageRead])
def get_all_messages(
    db: Session = Depends(get_db),
    admin_user = Depends(get_current_admin_user)
):
    return message_service.get_all_admin_messages(db)

@router.post("/", response_model=AdminMessageRead, status_code=status.HTTP_201_CREATED)
def create_message(
    message_in: AdminMessageCreate,
    db: Session = Depends(get_db),
    admin_user = Depends(get_current_admin_user)
):
    return message_service.create_admin_message(db, message_in)

@router.delete("/{message_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_message(
    message_id: int,
    db: Session = Depends(get_db),
    admin_user = Depends(get_current_admin_user)
):
    message_service.delete_admin_message(db, message_id)
    return None

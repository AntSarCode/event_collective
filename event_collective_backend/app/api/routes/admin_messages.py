from app.database import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.message import MessageCreate, MessageRead, MessageUpdate
from app.services import message_service
from app.api.deps import get_current_admin_user, get_db

router = APIRouter()

@router.get("/", response_model=List[MessageRead])
async def get_all_messages(
    db: AsyncSession = Depends(get_db),
    admin_user = Depends(get_current_admin_user)
):
    return await message_service.get_all_messages(db)


@router.post("/", response_model=MessageRead, status_code=status.HTTP_201_CREATED)
async def create_message(
    message_in: MessageCreate,
    db: AsyncSession = Depends(get_db),
    admin_user = Depends(get_current_admin_user)
):
    return await message_service.create_message(db, message_in)


@router.put("/{message_id}", response_model=MessageRead)
async def update_message(
    message_id: int,
    message_in: MessageUpdate,
    db: AsyncSession = Depends(get_db),
    admin_user = Depends(get_current_admin_user)
):
    return await message_service.update_message(db, message_id, message_in)


@router.delete("/{message_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_message(
    message_id: int,
    db: AsyncSession = Depends(get_db),
    admin_user = Depends(get_current_admin_user)
):
    await message_service.delete_message(db, message_id)
    return None

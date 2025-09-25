from typing import List, Optional
from sqlalchemy.orm import Session

from app.models.message import Message
from app.schemas.message import MessageCreate, MessageUpdate


def get_all_messages(db: Session) -> List[Message]:
    return db.query(Message).order_by(Message.created_at.desc()).all()


def create_message(db: Session, data: MessageCreate) -> Message:
    msg = Message(**data.model_dump())
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return msg


def update_message(db: Session, message_id: int, data: MessageUpdate) -> Optional[Message]:
    msg = db.query(Message).filter(Message.id == message_id).first()
    if not msg:
        return None
    payload = data.model_dump(exclude_unset=True)
    for k, v in payload.items():
        setattr(msg, k, v)
    db.commit()
    db.refresh(msg)
    return msg


def delete_message(db: Session, message_id: int) -> bool:
    msg = db.query(Message).filter(Message.id == message_id).first()
    if not msg:
        return False
    db.delete(msg)
    db.commit()
    return True

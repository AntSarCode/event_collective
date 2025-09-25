from sqlalchemy.orm import Session
from typing import List

from app.models.message import AdminMessage
from app.schemas.message import AdminMessageCreate

def create_admin_message(db: Session, message_in: AdminMessageCreate) -> AdminMessage:
    message = AdminMessage(**message_in.model_dump())
    db.add(message)
    db.commit()
    db.refresh(message)
    return message

def get_all_admin_messages(db: Session) -> List[AdminMessage]:
    return db.query(AdminMessage).order_by(AdminMessage.received_at.desc()).all()

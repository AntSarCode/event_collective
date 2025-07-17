from sqlalchemy.orm import Session
from typing import List

from app.models.contact_message import ContactMessage
from app.schemas.contact_message import ContactMessageCreate

def create_contact_message(db: Session, message_in: ContactMessageCreate) -> ContactMessage:
    message = ContactMessage(**message_in.model_dump())
    db.add(message)
    db.commit()
    db.refresh(message)
    return message

def get_all_messages(db: Session) -> List[ContactMessage]:
    return db.query(ContactMessage).order_by(ContactMessage.created_at.desc()).all()

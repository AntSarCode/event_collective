from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.schemas.contact_message import ContactMessageCreate, ContactMessageRead

from app.services import contact_service

router = APIRouter(prefix="/contact", tags=["contact"])


@router.post("/submit", response_model=ContactMessageRead, status_code=status.HTTP_201_CREATED)
def submit_contact_form(
    message: ContactMessageCreate,
    db: Session = Depends(get_db)
):
    return contact_service.create_contact_message(db, message)


@router.get("/all", response_model=list[ContactMessageRead])
def get_all_messages(db: Session = Depends(get_db)):
    return contact_service.get_all_messages(db)

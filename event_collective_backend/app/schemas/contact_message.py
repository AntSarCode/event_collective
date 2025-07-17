from datetime import datetime
from pydantic import BaseModel, EmailStr

class ContactMessageCreate(BaseModel):
    name: str
    email: EmailStr
    subject: str | None = None
    message: str

class ContactMessageRead(ContactMessageCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

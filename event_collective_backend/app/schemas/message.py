from datetime import datetime
from pydantic import BaseModel, EmailStr

class AdminMessageCreate(BaseModel):
    sender_name: str
    sender_email: EmailStr
    subject: str | None = None
    content: str

class AdminMessageRead(AdminMessageCreate):
    id: int
    received_at: datetime

    class Config:
        orm_mode = True

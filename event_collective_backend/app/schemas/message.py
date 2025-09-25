from pydantic import BaseModel, ConfigDict
from datetime import datetime

class MessageBase(BaseModel):
    subject: str
    body: str
    sender: str
    recipient: str


class MessageCreate(MessageBase):
    pass


class MessageUpdate(BaseModel):
    subject: str | None = None
    body: str | None = None
    recipient: str | None = None


class MessageRead(MessageBase):
    id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class MessageInDB(MessageBase):
    id: int
    created_at: datetime
    updated_at: datetime | None = None
    model_config = ConfigDict(from_attributes=True)

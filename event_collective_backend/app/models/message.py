from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from app.models.base import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String(255), nullable=False)
    body = Column(Text, nullable=False)
    sender = Column(String(255), nullable=False)
    recipient = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, nullable=True)

    def __repr__(self) -> str:  # pragma: no cover
        return f"<Message id={self.id} subject={self.subject!r} sender={self.sender!r}>"


class AdminMessage(Base):
    __tablename__ = "admin_messages"

    id = Column(Integer, primary_key=True, index=True)
    subject = Column(String(255), nullable=False)
    body = Column(Text, nullable=False)
    sender = Column(String(255), nullable=False)
    recipient = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, nullable=True)

    def __repr__(self) -> str:  # pragma: no cover
        return f"<AdminMessage id={self.id} subject={self.subject!r} sender={self.sender!r}>"
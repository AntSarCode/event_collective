from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

from app.models.base import Base


class AdminMessage(Base):
    __tablename__ = "admin_messages"

    id = Column(Integer, primary_key=True, index=True)
    sender_name = Column(String, nullable=False)
    sender_email = Column(String, nullable=False)
    subject = Column(String, nullable=True)
    content = Column(Text, nullable=False)
    received_at = Column(DateTime, default=datetime.utcnow)

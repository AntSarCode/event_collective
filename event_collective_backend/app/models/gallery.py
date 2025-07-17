from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.models.base import Base


class GalleryImage(Base):
    __tablename__ = "gallery_images"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    url = Column(String, nullable=False)
    alt_text = Column(String, nullable=True)
    uploaded_at = Column(DateTime, default=datetime.utcnow)

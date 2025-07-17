from datetime import datetime
from pydantic import BaseModel

class GalleryImageCreate(BaseModel):
    filename: str
    url: str
    alt_text: str | None = None

class GalleryImageRead(GalleryImageCreate):
    id: int
    uploaded_at: datetime

    class Config:
        orm_mode = True

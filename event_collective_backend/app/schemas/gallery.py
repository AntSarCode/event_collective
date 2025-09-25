from datetime import datetime
from pydantic import BaseModel, ConfigDict

class GalleryImageCreate(BaseModel):
    filename: str
    url: str
    alt_text: str | None = None

class GalleryImageRead(GalleryImageCreate):
    id: int
    uploaded_at: datetime

    model_config = ConfigDict(from_attributes=True)

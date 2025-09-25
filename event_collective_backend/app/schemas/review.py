from datetime import datetime
from pydantic import BaseModel, ConfigDict

class ReviewCreate(BaseModel):
    name: str
    rating: int
    message: str

class ReviewRead(ReviewCreate):
    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)

from datetime import datetime
from pydantic import BaseModel

class ReviewCreate(BaseModel):
    name: str
    rating: int
    message: str

class ReviewRead(ReviewCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

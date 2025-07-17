from pydantic import BaseModel

class ServiceCreate(BaseModel):
    name: str
    description: str | None = None
    price: float | None = None
    category: str | None = None

class ServiceRead(ServiceCreate):
    id: int

    class Config:
        orm_mode = True

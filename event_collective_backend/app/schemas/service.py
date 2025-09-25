from pydantic import BaseModel, ConfigDict

class ServiceCreate(BaseModel):
    name: str
    description: str | None = None
    price: float | None = None
    category: str | None = None

class ServiceRead(ServiceCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)

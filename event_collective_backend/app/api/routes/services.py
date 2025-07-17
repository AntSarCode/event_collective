from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.api.deps import get_db
from app.schemas.service import ServiceCreate, ServiceRead
from app.services import service_service

router = APIRouter(prefix="/services", tags=["services"])


@router.post("/add", response_model=ServiceRead, status_code=status.HTTP_201_CREATED)
def add_service(
    service: ServiceCreate,
    db: Session = Depends(get_db)
):
    return service_service.create_service(db, service)


@router.get("/all", response_model=List[ServiceRead])
def get_all_services(db: Session = Depends(get_db)):
    return service_service.get_all_services(db)

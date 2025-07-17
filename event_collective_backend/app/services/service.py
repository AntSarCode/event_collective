from sqlalchemy.orm import Session
from typing import List

from app.models.service import Service
from app.schemas.service import ServiceCreate

def create_service(db: Session, service_in: ServiceCreate) -> Service:
    service = Service(**service_in.model_dump())
    db.add(service)
    db.commit()
    db.refresh(service)
    return service

def get_all_services(db: Session) -> List[Service]:
    return db.query(Service).order_by(Service.name).all()

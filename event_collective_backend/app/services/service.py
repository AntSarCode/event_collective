from __future__ import annotations
from typing import Optional, List

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.models.service import Service
from app.schemas.service import ServiceCreate


def create_service(db: Session, service_in: ServiceCreate) -> Service:
    """Create a new Service from validated input.

    Uses Pydantic v2's `.model_dump()` to obtain field values.
    Raises the original IntegrityError if constraints (e.g., unique name) are violated.
    """
    service = Service(**service_in.model_dump())
    db.add(service)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        # Re-raise so the router or error handler can return a 409/400 as appropriate
        raise
    db.refresh(service)
    return service


def get_all_services(db: Session) -> List[Service]:
    """Return all services sorted by name."""
    return db.query(Service).order_by(Service.name).all()


def get_service_by_id(db: Session, service_id: int) -> Optional[Service]:
    """Fetch a single Service, or None if not found."""
    return db.query(Service).filter(Service.id == service_id).first()


def delete_service(db: Session, service_id: int) -> bool:
    """Delete a Service by id. Returns True if deleted, False if not found."""
    svc = get_service_by_id(db, service_id)
    if not svc:
        return False
    db.delete(svc)
    db.commit()
    return True

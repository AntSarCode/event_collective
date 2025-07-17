from sqlalchemy.orm import Session
from typing import Type, TypeVar, Optional

ModelType = TypeVar("ModelType")

def get_by_id(db: Session, model: Type[ModelType], id: int) -> Optional[ModelType]:
    return db.query(model).filter(model.id == id).first()

def delete_by_id(db: Session, model: Type[ModelType], id: int) -> bool:
    obj = db.query(model).filter(model.id == id).first()
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False

def create_instance(db: Session, model: Type[ModelType], data: dict) -> ModelType:
    instance = model(**data)
    db.add(instance)
    db.commit()
    db.refresh(instance)
    return instance

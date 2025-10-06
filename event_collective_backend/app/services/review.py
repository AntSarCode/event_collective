from sqlalchemy.orm import Session
from typing import List

from app.models.review import Review
from app.schemas.review import ReviewCreate

def create_review(db: Session, review_in: ReviewCreate) -> Review:
    review = Review(**review_in.model_dump())
    db.add(review)
    db.commit()
    db.refresh(review)
    return review

def get_all_reviews(db: Session) -> List[Review]:
    return db.query(Review).order_by(Review.created_at.desc()).all()

def get_featured_reviews(db: Session, limit: int = 5):
    return db.query(Review).order_by(Review.created_at.desc()).limit(limit).all()

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.api.deps import get_db
from app.schemas.review import ReviewCreate, ReviewRead
from app.services import review_service

router = APIRouter(prefix="/reviews", tags=["reviews"])


@router.post("/submit", response_model=ReviewRead, status_code=status.HTTP_201_CREATED)
def submit_review(
    review: ReviewCreate,
    db: Session = Depends(get_db)
):
    return review_service.create_review(db, review)


@router.get("/all", response_model=List[ReviewRead])
def get_all_reviews(db: Session = Depends(get_db)):
    return review_service.get_all_reviews(db)

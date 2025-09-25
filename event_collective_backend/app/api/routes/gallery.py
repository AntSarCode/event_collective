from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.api.deps import get_db
from app.schemas.gallery import GalleryImageRead
from app.services import gallery_service

router = APIRouter(prefix="/gallery", tags=["gallery"])


@router.post("/upload", response_model=GalleryImageRead)
def upload_image(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    try:
        return gallery_service.save_image(db, file)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Upload failed: {str(e)}"
        )


@router.get("/all", response_model=List[GalleryImageRead])
def get_all_images(db: Session = Depends(get_db)):
    return gallery_service.get_all_images(db)

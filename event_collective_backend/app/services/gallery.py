from sqlalchemy.orm import Session
from typing import List
from app.models.gallery import GalleryImage

def save_image(db: Session, file) -> GalleryImage:
    # In a real app, upload to storage service and generate URL
    fake_url = f"https://cdn.event-collective.com/{file.filename}"
    image = GalleryImage(
        filename=file.filename,
        url=fake_url,
        alt_text=None
    )
    db.add(image)
    db.commit()
    db.refresh(image)
    return image

def get_all_images(db: Session) -> List[GalleryImage]:
    return db.query(GalleryImage).order_by(GalleryImage.uploaded_at.desc()).all()

def get_homepage_strip(db: Session, limit: int = 18):
    return db.query(GalleryImage).order_by(GalleryImage.uploaded_at.desc()).limit(limit).all()

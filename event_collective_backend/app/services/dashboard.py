from sqlalchemy.orm import Session

from app.models.user import User
from app.models.review import Review
from app.models.contact_message import ContactMessage
from app.models.gallery import GalleryImage

def get_overview_data(db: Session) -> dict:
    return {
        "user_count": db.query(User).count(),
        "review_count": db.query(Review).count(),
        "contact_count": db.query(ContactMessage).count(),
        "gallery_image_count": db.query(GalleryImage).count()
    }

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.services.service import get_featured_services_for_home
from app.services.gallery import get_homepage_strip
from app.services.review import get_featured_reviews
from app.schemas.service import ServiceRead
from app.schemas.gallery import GalleryImageRead
from app.schemas.review import ReviewRead

router = APIRouter(prefix="/public/home", tags=["public"])

@router.get("", response_model=dict)
def get_home(db: Session = Depends(get_db)):
    services = get_featured_services_for_home(db, limit=3)
    gallery = get_homepage_strip(db, limit=18)
    reviews = get_featured_reviews(db, limit=5)

    # Build a left-rail nav from service categories if available; fallback to client’s labels
    # e.g., “Rentals”, “Coordinating”
    categories = []
    for s in services:
        if s.category and s.category not in categories:
            categories.append(s.category)
    if not categories:
        categories = ["Rentals", "Coordinating", "Contact"]

    nav = [{"label": c, "href": f"/services?category={c.lower()}"} for c in categories if c.lower() != "contact"]
    nav.append({"label": "Contact", "href": "/contact"})

    payload = {
        "settings": {
            "brand_palette": "offwhite_black",   # or "offwhite_taupe"
            "hero_title": "The Event Collective",
            "hero_subtitle": "Modern, classy coordination & rentals.",
            "cta_text": "Inquire",
            "cta_href": "/contact",
            "fb_url": "",
            "ig_url": "",
            "tiktok_url": ""
        },
        "nav": nav,
        "services": [ServiceRead.model_validate(s) for s in services],
        "gallery": [GalleryImageRead.model_validate(g) for g in gallery],
        "reviews": [ReviewRead.model_validate(r) for r in reviews],
    }
    return payload

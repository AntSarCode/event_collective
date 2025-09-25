from fastapi import APIRouter
from app.api.routes import (
    auth, dashboard, gallery, services, reviews,
    contact, admin_calendar, admin_messages
)

api_router = APIRouter()

# Public
api_router.include_router(auth.router)
api_router.include_router(gallery.router)
api_router.include_router(services.router)
api_router.include_router(reviews.router)
api_router.include_router(contact.router)

# Protected
api_router.include_router(dashboard.router)  # dashboard now serves /dashboard/overview

# Admin
api_router.include_router(admin_calendar.router)
api_router.include_router(admin_messages.router)

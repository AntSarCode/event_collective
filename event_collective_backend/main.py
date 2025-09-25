from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.api_router import api_router
from app.core.events import register_events
from app.config import get_settings

settings = get_settings()

app = FastAPI(title=settings.app_name, debug=settings.debug)

# Register startup/shutdown
register_events(app)

# CORS Middleware
origins = [o.strip() for o in (settings.allowed_origins or "").split(",") if o.strip()] or ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root health check
@app.get("/")
def root():
    return {"message": "The Event Collective API is running"}

# Mount API router
app.include_router(api_router, prefix="/api")

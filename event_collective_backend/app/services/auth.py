from __future__ import annotations
from datetime import timedelta
from typing import Optional

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.user import User
from app.core.security import verify_password, create_access_token, decode_access_token
from app.config import get_settings

__all__ = [
    "authenticate_user",
    "generate_access_token",
    "verify_access_token",
]

def authenticate_user(db: Session, username: str, password: str) -> Optional[User]:
    """Authenticate a user by case-insensitive username and password."""
    user = (
        db.query(User)
        .filter(func.lower(User.username) == func.lower(username))
        .first()
    )
    if user and verify_password(password, user.hashed_password):
        return user
    return None

def generate_access_token(user_id: int) -> str:
    """Create a short-lived JWT access token for the given user id."""
    settings = get_settings()
    expire_minutes = getattr(settings, "access_token_expire_minutes", 30) or 30
    return create_access_token(
        data={"sub": str(user_id)},
        expires_delta=timedelta(minutes=expire_minutes),
    )

def verify_access_token(token: str, db: Session) -> Optional[User]:
    """Validate a JWT and return the associated User, or None if invalid/expired."""
    try:
        payload = decode_access_token(token)
    except Exception:
        return None
    user_id: Optional[str] = None
    if isinstance(payload, dict):
        user_id = payload.get("sub")
    if not user_id:
        return None
    return db.query(User).filter(User.id == int(user_id)).first()

from sqlalchemy.orm import Session
from datetime import timedelta

from app.models.user import User
from app.core.security import verify_password, create_access_token
from app.config.settings import get_settings

def authenticate_user(db: Session, username: str, password: str) -> User | None:
    user = db.query(User).filter(User.username == username).first()
    if user and verify_password(password, user.hashed_password):
        return user
    return None

def generate_access_token(user_id: int) -> str:
    settings = get_settings()
    return create_access_token(
        data={"sub": str(user_id)},
        expires_delta=timedelta(minutes=settings.access_token_expire_minutes)
    )

def verify_access_token(token: str, db: Session) -> User | None:
    from app.core.security import decode_access_token

    payload = decode_access_token(token)
    user_id: str | None = payload.get("sub")
    if user_id is None:
        return None
    return db.query(User).filter(User.id == int(user_id)).first()

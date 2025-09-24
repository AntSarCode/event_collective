from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user
from app.services import auth
from app.schemas.user import Token, UserRead

router = APIRouter(prefix="/auth", tags=["auth"])

@router.get("/me", response_model=UserRead)
def me(current_user = Depends(get_current_user)):
    return current_user

@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(user.id)
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/logout")
def logout():
    # Placeholder for token blacklist or session cleanup if needed
    return {"msg": "Successfully logged out"}

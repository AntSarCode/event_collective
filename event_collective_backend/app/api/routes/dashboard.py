from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db, get_current_user
from app.models.user import User

router = APIRouter(prefix="/dashboard", tags=["dashboard"])


@router.get("/overview", response_model=dict)
def get_dashboard_overview(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    try:
        # Minimal placeholder payload; expand with real stats later
        return {
            "user": {
                "id": current_user.id,
                "username": getattr(current_user, "username", None),
                "is_admin": getattr(current_user, "is_admin", False),
            },
            "status": "ok",
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Dashboard data retrieval failed: {str(e)}"
        )

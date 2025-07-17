from fastapi import HTTPException, status


NotAuthorized = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Not authorized",
    headers={"WWW-Authenticate": "Bearer"},
)

InvalidToken = HTTPException(
    status_code=status.HTTP_403_FORBIDDEN,
    detail="Invalid or expired token",
)

from .auth import (
    authenticate_user,
    create_access_token,
    verify_access_token,
)


class _AuthServiceProxy:
    from .auth import authenticate_user, create_access_token, verify_access_token

auth_service = _AuthServiceProxy()

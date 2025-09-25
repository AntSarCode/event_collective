# Service package aliases and re-exports to keep router imports working.

from . import auth   as auth_service
from . import calendar as calendar_service
from . import contact  as contact_service
from . import dashboard as dashboard_service
from . import gallery  as gallery_service
from . import message  as message_service
from . import review   as review_service
from . import service  as service_service
from . import user     as user_service

# Back-compat function names expected by routers
from .auth import authenticate_user, generate_access_token as create_access_token

__all__ = [
    "auth_service","calendar_service","contact_service","dashboard_service",
    "gallery_service","message_service","review_service","service_service","user_service",
    "authenticate_user","create_access_token",
]

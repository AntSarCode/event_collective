import re
from pydantic import EmailStr, ValidationError

def is_valid_email(email: str) -> bool:
    try:
        EmailStr.validate(email)
        return True
    except ValidationError:
        return False

def is_strong_password(password: str) -> bool:
    pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$")
    return bool(pattern.match(password))

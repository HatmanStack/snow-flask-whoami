"""Input validation for snow-flask-whoami application."""
import re
from typing import Optional

MAX_NAME_LENGTH = 100
MAX_ADDRESS_LENGTH = 500
SAFE_PATTERN = re.compile(r'^[\w\s\-\.\'\,\#]+$')


class ValidationError(ValueError):
    """Raised when input validation fails."""
    pass


def validate_name(name: Optional[str]) -> str:
    """Validate and sanitize a name input."""
    if not name or not name.strip():
        raise ValidationError("Name is required")
    name = name.strip()
    if len(name) > MAX_NAME_LENGTH:
        raise ValidationError(f"Name must be {MAX_NAME_LENGTH} characters or less")
    if not SAFE_PATTERN.match(name):
        raise ValidationError("Name contains invalid characters")
    return name


def validate_address(address: Optional[str]) -> str:
    """Validate and sanitize an address input."""
    if not address or not address.strip():
        raise ValidationError("Address is required")
    address = address.strip()
    if len(address) > MAX_ADDRESS_LENGTH:
        raise ValidationError(f"Address must be {MAX_ADDRESS_LENGTH} characters or less")
    return address

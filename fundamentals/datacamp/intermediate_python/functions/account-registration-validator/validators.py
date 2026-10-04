import re


def validate_name(name):
    """
    Validate a user's name.

    Rules:
    - Must be a string.
    - Cannot be empty.
    - Must contain only letters and spaces.
    - Length must be between 2 and 50 characters.

    Returns:
        bool
    """
    if not isinstance(name, str):
        return False

    name = name.strip()

    if len(name) < 2 or len(name) > 50:
        return False

    pattern = r"^[A-Za-z ]+$"

    return bool(re.fullmatch(pattern, name))


def validate_email(email):
    """
    Validate an email address.

    Rules:
    - Must follow the format username@domain.extension

    Returns:
        bool
    """
    if not isinstance(email, str):
        return False

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    return bool(re.fullmatch(pattern, email))


def validate_password(password):
    """
    Validate a password.

    Rules:
    - At least 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character

    Returns:
        bool
    """
    if not isinstance(password, str):
        return False

    if len(password) < 8:
        return False

    if not re.search(r"[A-Z]", password):
        return False

    if not re.search(r"[a-z]", password):
        return False

    if not re.search(r"\d", password):
        return False

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False

    return True
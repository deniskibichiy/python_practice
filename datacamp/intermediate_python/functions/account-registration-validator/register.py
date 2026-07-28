from validators import (
    validate_name,
    validate_email,
    validate_password,
)


def validate_user(name, email, password):
    if not validate_name(name):
        raise ValueError("Invalid name.")

    if not validate_email(email):
        raise ValueError("Invalid email.")

    if not validate_password(password):
        raise ValueError("Invalid password.")

    return True


try:
    validate_user(
        "Denis",
        "denismutai5@gmail.com",
        "Denis#4932"
    )
    print("Registration successful!")

except ValueError as error:
    print(error)
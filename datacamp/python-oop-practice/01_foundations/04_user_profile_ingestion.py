
"""
Level 2: Class Methods & Alternative Constructors

Scenario: User Profile Ingestion

Create a UserProfile class for an authentication system.

Instance Attributes: username (str), email (str), role (str, e.g., "admin", "member").

Class Attribute: allowed_roles = ["admin", "member", "guest"].
Class Method / Alternative Constructor: from_csv_string(csv_data) — takes a string like "johndoe,john@example.com,admin" and returns a new UserProfile instance.

Class Method / Alternative Constructor: create_guest(username) — returns a UserProfile with email="guest@system.local" and role="guest".

Validation: Ensure role is inside allowed_roles. Raise a ValueError if invalid.
"""
class UserProfile:
    ALLOWED_ROLES = ["admin", "member", "guest"]
    def __init__(self,username, email, role):
        self.username = username
        self.email = email
        if role in self.ALLOWED_ROLES:
            self.role = role
        else:
            raise ValueError("Role not allowed")

    @classmethod

    def create_guest(cls, username):
        email = "guest@system.local"
        role = "guest"
        return cls(username, email, role)
    

    
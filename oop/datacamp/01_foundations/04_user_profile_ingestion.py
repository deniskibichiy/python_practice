
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

    def from_csv_string(cls,csv_data):
        user = csv_data.rsplit(", ")
        return cls(user)

    @classmethod

    def create_guest(cls, username):
        username = username
        email = "guest@system.local"
        role = "guest"
        return cls(username, email, role)
    
if __name__ == "__main__":
    # 1. Test Standard Instantiation & Validation
    user1 = UserProfile(username="alice", email="alice@example.com", role="admin")
    assert user1.username == "alice"
    assert user1.role == "admin"

    try:
        invalid_user = UserProfile(username="hacker", email="hacker@site.com", role="superuser")
        assert False, "Should have raised ValueError for invalid role"
    except ValueError as e:
        assert "allowed_roles" in str(e) or "role" in str(e).lower()

    # 2. Test Alternative Constructor: from_csv_string
    csv_input = "johndoe,john@example.com,member"
    user2 = UserProfile.from_csv_string(csv_input)
    assert isinstance(user2, UserProfile)
    assert user2.username == "johndoe"
    assert user2.email == "john@example.com"
    assert user2.role == "member"

    # 3. Test Alternative Constructor: create_guest
    guest = UserProfile.create_guest(username="visitor123")
    assert isinstance(guest, UserProfile)
    assert guest.username == "visitor123"
    assert guest.email == "guest@system.local"
    assert guest.role == "guest"

    print("Level 2 Tests Passed Successfully!")
    
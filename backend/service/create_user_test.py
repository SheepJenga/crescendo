from backend.clients import crescendo_clients
from .create_user import create_user

def test_create_user():
    create_user(crescendo_clients, "test", "test", "test@gmail.com", "test")

test_create_user()
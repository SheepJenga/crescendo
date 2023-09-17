from ..models.user import User

def create_user(clients, first_name, last_name, email, username):
    db = clients.db_client
    user = User(first_name, last_name, email, username)
    return db.create(user)
    
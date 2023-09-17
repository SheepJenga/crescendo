from backend.models.account import Account

def create_user(clients, first_name, last_name, email, username, profile_picture):
    db = clients.db_client
    account = Account(username, email, first_name, last_name, profile_picture)
    return db.create(account, conds={"email": email})

from backend.models.account import Account

def create_user(clients, first_name, last_name, email, username):
    db = clients.db_client
    account = Account(first_name, last_name, email, username)
    return db.create(account)

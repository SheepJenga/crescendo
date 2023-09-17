from clients import *
from db_client import *

db_client = Datastore()
crescendoClients = Clients(db_client, None)

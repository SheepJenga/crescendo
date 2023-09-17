from sqlalchemy import create_engine
import psycopg2
import os
from ..models.user import User


mp = {
    User.id: 324,
}
print(mp)
def initDB():
    host=os.environ['DB_HOST']
    database=os.environ['DB_NAME']
    username=os.environ['DB_USERNAME']
    password=os.environ['DB_PASSWORD']

    engine = create_engine(f'postgresql://{username}{(":" + password) if password else password }@{host}/{database}')


    
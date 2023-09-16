from sqlalchemy import create_engine
import psycopg2
import os
from ..models.base import Base

def initDB():
    conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD']
    )

    engine = create_engine('postgresql+psycopg2://scott:tiger@localhost/test')
    
    Base.metadata.create_all(engine)

    
"""
IMPORTANT: only run to refresh local environment/perform setup.
"""
import os
from sqlalchemy import create_engine
import psycopg2
from psycopg2 import sql

from backend.models.base import Base

def run_command(command):
    code = os.system(command)
    print(f"{command} ran with exit code {code}")

def create_database(db_name, user_name):
    # Replace with your PostgreSQL server configuration
    conn = psycopg2.connect(
        host="localhost",
        database="postgres", # default PostgreSQL administrative database
        user=user_name,
        password=""
    )
    conn.autocommit = True

    cursor = conn.cursor()

    # db_name = "your_database_name"
    create_db_query = sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name))

    cursor.execute(create_db_query)

    conn.commit()
    conn.close()
    cursor.close()

def build_tables(db_name, user_name):
    conn = psycopg2.connect(
            host="localhost",
            database=db_name,
            user=user_name,
            password='')

    engine = create_engine(f'postgresql://{user_name}@localhost/crescendo')
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    conn.close()


if __name__ == "__main__":
#     run_command("brew services start postgresql@16")
    DB = 'crescendo'
    USER = 'shepardjiang' # REPLACE THIS W YOUR DEFAULT PSQL USER NAME (it should be the string that appears when you type "psql" in terminal)
    try:
        create_database(DB, USER)
    except:
        print("Database already exists, skipping creation")

    build_tables(DB, USER)

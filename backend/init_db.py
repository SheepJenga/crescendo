import os
import psycopg2
from psycopg2 import sql
# from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

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

def populate_database(db_name, user_name):
    conn = psycopg2.connect(
            host="localhost",
            database=db_name,
            user=user_name,
            password='')

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a command: this creates a new table
    cur.execute('DROP TABLE IF EXISTS books;')
    cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
                                    'title varchar (150) NOT NULL,'
                                    'author varchar (50) NOT NULL,'
                                    'pages_num integer NOT NULL,'
                                    'review text,'
                                    'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                    )
    conn.commit()

    cur.close()
    conn.close()

def insert_data(db_name, user_name):
    # Insert data into the table
    conn = psycopg2.connect(
        host="localhost",
        database=db_name,
        user=user_name,
        password='')

    # Open a cursor to perform database operations
    cur = conn.cursor()

    cur.execute('INSERT INTO books (title, author, pages_num, review)'
                'VALUES (%s, %s, %s, %s)',
                ('A Tale of Two Cities',
                'Charles Dickens',
                489,
                'A great classic!')
                )


    cur.execute('INSERT INTO books (title, author, pages_num, review)'
                'VALUES (%s, %s, %s, %s)',
                ('Anna Karenina',
                'Leo Tolstoy',
                864,
                'Another great classic!')
                )

    conn.commit()

    cur.close()
    conn.close()

if __name__ == "__main__":
#     run_command("brew services start postgresql@16")
    DB = 'TEST3'
    USER = 'shepardjiang' # REPLACE THIS W YOUR DEFAULT PSQL USER NAME (it should be the string that appears when you type "psql" in terminal)
    create_database(DB, USER)
    populate_database(DB, USER)
    insert_data(DB, USER)

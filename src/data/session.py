import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "session.db")


# initializes the database (if not existing)
def init_session():
    with sqlite3.connect(DB_PATH) as connect:
        cursor = connect.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS session (loggedin_user TEXT NOT NULL) """
        )

        connect.commit()


# this will check if the table has row
def check_session():
    with sqlite3.connect(DB_PATH) as connect:
        cursor = connect.cursor()
        cursor.execute("""
        SELECT COUNT(loggedin_user) FROM session
        """)

    is_empty = cursor.fetchone()[0] == 0
    return is_empty


# this wil svae the user session
def save_session(username):
    with sqlite3.connect(DB_PATH) as connect:
        cursor = connect.cursor()
        cursor.execute(
            """
        INSERT INTO session 
        VALUES (?)
        """,
            (username,),
        )


# this will claen the user session
def clear_session():
    with sqlite3.connect(DB_PATH) as connect:
        cursor = connect.cursor()
        cursor.execute("""
        DELETE FROM session
        """)

        connect.commit()
        cursor.close()


init_session()

import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "account.db")


# initializes the database (if not existing)
def init_db():
    with sqlite3.connect(DB_PATH) as connect:
        cursor = connect.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
        ) 
        """)

        connect.commit()


init_db()

import os
import sqlite3

from src.exceptions.exceptions import UserNotFoundError

DB_PATH = os.path.join("src/data/", "account.db")


def get_all_user():
    try:
        with sqlite3.connect(DB_PATH) as connect:
            cursor = connect.cursor()
            cursor.execute("""
            SELECT * FROM users
            """)

            rows = cursor.fetchall()

            return {"success": True, "response": rows}
    except sqlite3.Error:
        return {
            "success": False,
            "response": "Error: Something happened fetching all users.",
        }


def get_user(username):
    try:
        with sqlite3.connect(DB_PATH) as connect:
            cursor = connect.cursor()
            cursor.execute(
                """
            SELECT * FROM users
            WHERE username = ?
            """,
                (username,),
            )

            result = cursor.fetchone()

            if result is None:
                raise UserNotFoundError()

            return {"success": True, "response": result}
    except sqlite3.Error:
        return {
            "success": False,
            "response": "Error: Something happened fetching the user.",
        }
    except UserNotFoundError as e:
        return {
            "success": False,
            "response": e.message,
        }


def create_user(username, password):
    try:
        with sqlite3.connect(DB_PATH) as connect:
            cursor = connect.cursor()
            cursor.execute(
                """
            INSERT INTO users(username, password) VALUES (?, ?)
            """,
                (username, password),
            )

            connect.commit()
            return {"success": True, "response": f'User "{username} added succesfully"'}
    except sqlite3.IntegrityError:
        return {
            "success": False,
            "response": f'Error: Username "{username}" already exists.',
        }
    except sqlite3.Error:
        return {
            "success": False,
            "response": f"Error: Something happened upon creating the account.",
        }

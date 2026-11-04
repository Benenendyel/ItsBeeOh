from src.repository.account_repository import (
    create_user as repo_create_user,
    get_all_user as repo_get_all_user,
    get_user as repo_get_user,
)

from src.helper.bcrypt import hash_password, validate_password


def create_user(username, password):
    username = username.strip()
    password = password.strip()

    res = repo_create_user(username, hash_password(password))

    return res


def validate_register_credential(username, password):
    username = username.strip()
    password = password.strip()

    res = repo_create_user(username, password)

    return {"success": res["success"], "reponse": res["response"]}


def validate_login_credential(username, password):
    username = username.strip()
    password = password.strip()

    res = repo_get_user(username)

    if res["success"]:
        if validate_password(password, res["response"][2]):
            return {"success": True, "response": "User account found!"}
        else:
            return {"success": False, "response": "Error: Passwords do not match."}

    else:
        return {"success": False, "response": res["response"]}


def get_all_user():
    res = repo_get_all_user()

    return res


create_user("VenAngel", "JustOne")

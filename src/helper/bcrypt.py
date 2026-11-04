import bcrypt


def hash_password(password):
    password_bytes = password.encode("utf-8")

    salt = bcrypt.gensalt()
    hashed_bytes = bcrypt.hashpw(password_bytes, salt)

    return hashed_bytes.decode("utf-8")


def validate_password(input_password, hashed_password):
    password_bytes = input_password.encode("utf-8")
    hash_bytes = hashed_password.encode("utf-8")

    return bcrypt.checkpw(password_bytes, hash_bytes)

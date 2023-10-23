class UserAlreadyExists(Exception):
    message = "User already exists."


class UserNotFound(Exception):
    message = "User not found."

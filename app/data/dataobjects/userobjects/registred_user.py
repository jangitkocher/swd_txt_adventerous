import hashlib
import re

from .user import User, UserException


class RegisteredUser(User):
    def __init__(self, first_name: str, last_name: str, user_name: str, password: str):
        super(RegisteredUser, self).__init__(user_name)
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.secure_password(password)
        pass

    @staticmethod
    def secure_password(password: str) -> str:
        """
        Encodes password.
        :param password: (str) given password
        :return: (str) encoded password
        """
        return hashlib.sha512(password.encode()).hexdigest()

    def __dict__(self) -> dict:
        return {
            "fist_name": self.first_name,
            "last_name": self.last_name,
            "user_name": self.user_name,
            "password": self.password
        }

    @staticmethod
    def is_alpha_numeric(user_name: str) -> bool:
        """
        Checks if given string is alphanumeric.
        :param user_name: (str) user_name or string to be checked
        :return: (bool) True if the user_name consists only alphanumeric chars else False
        """
        return bool(re.search("^[a-zA-Z0-9_]*&", user_name))


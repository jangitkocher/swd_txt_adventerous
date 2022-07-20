from .database import DataBaseManager, ObjectName
from .dataobjects import User, RegisteredUser, Player


class UserFactory:
    def __init__(self):
        """
        This class manages User objects.
        """
        self.database = DataBaseManager("127.0.0.1", 27017)
        pass

    @staticmethod
    def get_new_user() -> User:
        return User()

    def get_registered_user(self, user_name) -> RegisteredUser:
        return RegisteredUser(*self.database.get_object(ObjectName.REGISTERED_USER, {"user_name": user_name}))

    def register_user(self, first_name: str, last_name: str, user_name: str, password: str) -> RegisteredUser:
        registered_user = RegisteredUser(first_name, last_name, user_name, password)
        self.database.add_object(ObjectName.REGISTERED_USER, registered_user.__dict__())
        return registered_user

    def login_user(self, user_name: str, password: str) -> RegisteredUser:
        password_secure = RegisteredUser.secure_password(password)
        search_param = {"user_name": user_name, "password": password_secure}
        registered_user_data = self.database.get_object(ObjectName.REGISTERED_USER, search_param)
        registered_user = RegisteredUser(registered_user_data["fist_name"], registered_user_data["last_name"],
                                         registered_user_data["user_name"], registered_user_data["password"])
        return registered_user

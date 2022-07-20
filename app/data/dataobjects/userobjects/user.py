class User:
    STANDARD_USERNAME = "Anonymous"

    def __init__(self, user_name=STANDARD_USERNAME):
        self.user_name = user_name
        pass

    def __str__(self):
        return self.user_name


class UserException(Exception):
    pass

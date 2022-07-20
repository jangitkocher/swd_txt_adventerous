from .registred_user import RegisteredUser


class Player(RegisteredUser):
    """
    Player inherits of class User.
    """
    def __init__(self, registered_user: RegisteredUser):
        super(Player, self).__init__(*registered_user.__dict__())
        pass





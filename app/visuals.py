from copy import deepcopy as copy
from data import User, RegisteredUser, Player, Point, Size


class UserInput:
    SEARCH_FOR_GAME = "search"
    SHOW_ALL_GAMES = "show"
    REGISTER = "register"
    LOGIN = "login"
    LOGOUT = "logout"
    CREATE_GAME = "create"
    STATS = "stats"
    EXIT = "exit"
    RETRY = "retry"
    YES = "yes"

    N = "n"
    E = "e"
    S = "s"
    W = "w"
    ALL_POSSIBLE_MOVES = [N, E, S, W]
    ALL_POSSIBLE_INPUTS = [SEARCH_FOR_GAME, SHOW_ALL_GAMES, REGISTER, LOGIN, LOGOUT, CREATE_GAME, STATS, EXIT, RETRY,
                           YES, N, E, S, W]

    @staticmethod
    def move_to_point(move) -> Point:
        if move in UserInput.ALL_POSSIBLE_MOVES:
            if move in UserInput.N:
                return Point(0, 1)
            elif move in UserInput.E:
                return Point(1, 0)
            elif move in UserInput.S:
                return Point(0, -1)
            elif move in UserInput.W:
                return Point(-1, 0)

    pass


class Console:
    """
    Class manages console outputs.
    """

    def __init__(self):
        pass

    @staticmethod
    def show_main_menu(current_user) -> str:
        """
        Shows main menu.
        :return: (str) user input if existing
        """
        show_main_menu = True
        while show_main_menu:
            print("Welcome the TextAdventure")
            print(f"Current user: {current_user}")
            print(f"\nOptions:")
            print(f"Enter '{UserInput.SEARCH_FOR_GAME}' to search for a game.")
            print(f"Enter '{UserInput.SHOW_ALL_GAMES}' to show all available games.")

            if type(current_user) is User:
                print(f"Enter '{UserInput.REGISTER}' to register.")
                print(f"Enter '{UserInput.LOGIN}' to login.")

            if type(current_user) is RegisteredUser:
                print(f"Enter '{UserInput.CREATE_GAME}' to create a game.")
                print(f"Enter '{UserInput.STATS}' to show game stats.")
                print(f"Enter '{UserInput.LOGOUT}' to logout.")

            print(f"Enter '{UserInput.EXIT}' to exit.")

            user_input = input("Option: ")
            if user_input in UserInput.ALL_POSSIBLE_INPUTS:
                return user_input
            else:
                print("Unknown input, pls try again.")
        pass

    @staticmethod
    def register_dialog(register_func):
        """
        Starts register dialog.
        :return: None
        """
        try_to_register = True
        while try_to_register:
            print("Register:")
            first_name = input("First name: ")
            last_name = input("Last name: ")
            user_name = input("Username: ")
            password = input("Password: ")

            try:
                registered_user = register_func(first_name, last_name, user_name, password)
                print("Successfully registered")
                return registered_user
            except Exception:
                print("Registration was not successful")
                print(f"Enter '{UserInput.EXIT}' to exit the registration process.")
                print(f"Enter '{UserInput.RETRY}' to try again.")
                try_to_register = True if input("Input: ") is UserInput.RETRY else False
        return None

    @staticmethod
    def login_dialog(login_func):
        try_to_login = True
        while try_to_login:
            print("Login: ")
            user_name = input("Username: ")
            password = input("Password: ")

            try:
                registered_user = login_func(user_name, password)
                print("Login successful")
                return registered_user
            except Exception:
                print("Login failed")
                print(f"Enter '{UserInput.EXIT}' to exit the login process.")
                print(f"Enter '{UserInput.RETRY}' to try again.")
                try_to_login = True if input("Input: ") is UserInput.RETRY else False
        return None

    @staticmethod
    def logout_dialog():
        print("Logout")
        print("Are you sure?")
        print(f"Enter '{UserInput.EXIT}' to exit the logout process.")
        print(f"Enter '{UserInput.YES}' to accept.")
        return True if input("Input: ") in UserInput.YES else False

    def search_for_game_dialog(self):
        pass

    def create_game_dialog(self, current_user, create_game_func):
        try_to_create_game = True
        while try_to_create_game:
            print("Creating game")
            name = input("Game name: ")
            width = int(input("Game field width: "))
            height = int(input("Game field height: "))
            size = Size(width, height)
            x = int(input("Start position x: "))
            y = int(input("Start position y: "))
            start_pos = Point(x, y)

            try:
                game = create_game_func(name, current_user.user_name, size, start_pos)
                print(f"Game {name} created succesfully")
                self.add_location_to_game(game)
                return game
            except Exception:
                print("Game creation failed")
                print(f"Enter '{UserInput.EXIT}' to exit the game creating process.")
                print(f"Enter '{UserInput.RETRY}' to try again.")
                try_to_create_game = True if input("Input: ") in UserInput.RETRY else False
        pass

    @staticmethod
    def add_location_to_game(game):
        try_to_add_location_to_game = True
        while try_to_add_location_to_game:
            print("Add location to game")
            x = int(input("Pos x: "))
            y = int(input("Pos y: "))
            pos = Point(x, y)
            name = input("Location name: ")

            try:
                game.place_object_on_game_field(name, pos)
                print("Added location successful")
                print("Add a other location?")
                print(f"Enter '{UserInput.EXIT}' to exit the logout process.")
                print(f"Enter '{UserInput.YES}' to accept.")
                try_to_add_location_to_game = True if input("Input: ") in UserInput.YES else False
            except Exception:
                print("Add location failed")
                print(f"Enter '{UserInput.EXIT}' to exit the add location process.")
                print(f"Enter '{UserInput.RETRY}' to try again.")
                try_to_add_location_to_game = True if input("Input: ") in UserInput.RETRY else False
        pass

    def show_all_games_dialog(self, get_all_games_func):
        try_show_all_games_dialog = True
        while try_show_all_games_dialog:
            print("Show all games")
            all_games = get_all_games_func()
            num_games = len(all_games)

            if num_games > 0:
                for idx, game in enumerate(all_games):
                    print(f"{idx}. {game.name} created by {game.user_name}")

                print("Choose Game")
                print(f"Enter '{UserInput.EXIT}' to exit the add location process.")
                print(f"Enter game number to chose a game")
                user_input = input("Input: ")
                if user_input == UserInput.EXIT:
                    return None
                else:
                    return self.play_game_dialog(all_games[int(user_input)])
            else:
                print("No game found")
                try_show_all_games_dialog = False
        pass

    @staticmethod
    def play_game_dialog(game):
        try_to_play_the_game = True
        while try_to_play_the_game:
            Grid.show(game.width, game.height, game.player_pos, copy(game.game_field))
            print(f"Enter '{UserInput.EXIT}' to return to main menu.")
            print(f"Enter '{UserInput.N}' '{UserInput.E}' '{UserInput.S}' '{UserInput.W}' to move")
            user_input = input("Input: ")
            if user_input in UserInput.ALL_POSSIBLE_MOVES:
                try:
                    game.move(UserInput.move_to_point(user_input))
                    game.save_game()
                    Grid.show(game.width, game.height, game.player_pos, copy(game.game_field))
                except Exception as InvalidMoveException:
                    print(InvalidMoveException)
            elif user_input in UserInput.EXIT:
                print("Do you want to exit the game?")
                print(f"Enter '{UserInput.EXIT}' to exit the game '{game.name}'.")
                print(f"Enter '{UserInput.YES}' to accept.")
                try_to_play_the_game = True if user_input in UserInput.YES else False

        pass


class Grid:
    @staticmethod
    def show(width: int, height: int, player_pos: Point, game_field):
        width += 1
        height += 1
        space = len(str(max(width, height)-1))
        game_field[player_pos.x][player_pos.y] = "X"
        content_line = "# | values |"
        dashes = "-".join("-" * space for _ in range(height))
        frame_line = content_line.replace("values", dashes)
        frame_line = frame_line.replace("#", " " * space)
        frame_line = frame_line.replace("| ", "+-").replace(" |", "-+")
        print(frame_line)

        for i, row in enumerate(reversed(game_field), 1):
            values = " ".join(f"{v:{space}s}" for v in row)
            line = content_line.replace("values", values)
            line = line.replace("#", f"{width - i:{space}d}")
            print(line)
        print(frame_line)

        num_line = content_line.replace("|", " ")
        num_line = num_line.replace("#", " " * space)
        height_nums = " ".join(f"{i:<{space}d}" for i in range(height))
        num_line = num_line.replace("values", height_nums)
        print(num_line)
        pass

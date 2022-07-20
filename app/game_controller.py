from visuals import Console, UserInput

from data import UserFactory, GameFactory


# TODO singleton
class GameController:
    visuals = Console()

    game_factory = GameFactory()
    user_factory = UserFactory()

    def __init__(self):
        self.game_running: bool = False
        self.current_user = self.user_factory.get_new_user()
        pass

    def start_game(self):
        self.game_running = True
        while self.game_running:
            user_input = self.visuals.show_main_menu(self.current_user)
            self.get_game_option(user_input)
        pass

    def get_game_option(self, user_input: str):
        if user_input == UserInput.SEARCH_FOR_GAME:
            self.visuals.search_for_game_dialog()

        elif user_input == UserInput.SHOW_ALL_GAMES:
            self.visuals.show_all_games_dialog(self.game_factory.get_all_games)

        elif user_input == UserInput.REGISTER:
            return_val = self.visuals.register_dialog(self.user_factory.register_user)
            if return_val is not None:
                self.current_user = return_val

        elif user_input == UserInput.LOGIN:
            return_val = self.visuals.login_dialog(self.user_factory.login_user)
            if return_val is not None:
                self.current_user = return_val

        elif user_input == UserInput.CREATE_GAME:
            self.visuals.create_game_dialog(self.current_user, self.game_factory.create_game)

        elif user_input == UserInput.LOGOUT:
            if self.visuals.logout_dialog():
                self.current_user = self.user_factory.get_new_user()

        elif user_input == UserInput.EXIT:
            self.exit_game()

        pass

    def exit_game(self):
        self.game_running = False
        pass

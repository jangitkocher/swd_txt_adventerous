from .database import DataBaseManager, ObjectName
from .dataobjects import Game, Point, Size


class GameFactory:
    def __init__(self):
        self.database = DataBaseManager("127.0.0.1", 27017)
        pass

    def search_for_game(self, name: str) -> Game:
        game_data = self.database.get_object(ObjectName.GAME, search_param={"name": name})
        return Game(game_data['name'], game_data['user_name'], game_field=game_data['game_field'],
                    start_pos=Point(game_data["start_pos"]["x"], game_data["start_pos"]["y"]))

    def create_game(self, name: str, user_name: str, size: Size, start_pos: Point) -> Game:
        game = Game(name=name, user_name=user_name, start_pos=start_pos)
        game.save_game = lambda _: self.update_game(game)
        game.game_field = game.create_new_game_field(size)
        self.database.add_object(ObjectName.GAME, game.__dict__())
        return game

    def update_game(self, game: Game):
        update_function = {"$set": game.__dict__()}
        self.database.update_object(ObjectName.GAME, search_param={"name": game.name}, update_function=update_function)

    def get_all_games(self) -> list:
        return [Game(game_data['name'], game_data['user_name'], game_data['game_field'],
                     start_pos=Point(game_data["start_pos"]["x"], game_data["start_pos"]["y"])) for game_data in
                self.database.get_all_objects(ObjectName.GAME)]

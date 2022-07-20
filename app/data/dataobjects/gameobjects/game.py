from .units import Point, Size


class Game:
    def __init__(self, name: str, user_name: str, game_field=None, start_pos: Point = Point(0, 0)):
        """
        This class represents a game field.
        :param name: (str) name of the game field
        :param game_field: (2D array) represents a 2D plane
        """
        self.name = name
        self.user_name = user_name
        self.game_field = game_field
        self.start_pos = start_pos
        self.player_pos = self.start_pos

        self.save_game = None
        pass

    def move(self, direction: Point):
        if self.point_inside_game_field(self.player_pos + direction):
            self.player_pos = self.player_pos + direction
        else:
            raise GameMoveException("You can't move in this direction.")
        pass

    @property
    def width(self) -> int:
        return len(self.game_field[0]) if self.game_field is not None else 0

    @property
    def height(self) -> int:
        return len(self.game_field) if self.game_field is not None else 0

    @staticmethod
    def create_new_game_field(size: Size):
        return [["." for _ in range(size.height)] for _ in range(size.width)]

    def get_game_field_position(self, point: Point):
        """
        Returns specific game field position at given coordinates.
        :param point: (Point) represents (x, y) coordinates
        :return: (str) if value at given Point is not None
        """
        if self.point_inside_game_field(point):
            return self.game_field[point.x][point.y]

    def set_start_point(self, start_point: Point) -> None:
        """
        Sets the initial position of the player.
        :param start_point: (Point) represents (x, y)
        :raise GameFieldException if given Point is not inside game field
        :return: None
        """
        if self.point_inside_game_field(start_point):
            self.start_pos = start_point
        else:
            raise GameFieldException("Start point is not in the game field")
        pass

    def place_object_on_game_field(self, name: str, point: Point) -> None:
        """
        Places an object in the game field.
        :param name: (str) name of the Object placed in game field
        :param point: (Point) position of Object to be placed at
        :raise GameFieldException if given Point is not inside game field
        :return: None
        """
        if self.point_inside_game_field(point):
            self.game_field[point.x][point.y] = name
        pass

    def point_inside_game_field(self, point: Point) -> bool:
        """
        checks if a given point is in the game field.
        :param point: (Point) represents (x, y)
        :return: (bool) True if point is in the field else False
        """
        if point.x <= self.width and point.y <= self.height:
            return True
        else:
            return False

    def __dict__(self):
        return {
            "name": self.name,
            "game_field": self.game_field,
            "start_pos": self.start_pos.__dict__(),
            "user_name": self.user_name
        }


class GameFieldException(Exception):
    pass


class GameMoveException(Exception):
    pass

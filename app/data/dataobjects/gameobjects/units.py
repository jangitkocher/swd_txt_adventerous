class Point:
    def __init__(self, x: int, y: int):
        """
        This class represents a Point (in a gamefield).
        :param x: (int) x coordinate
        :param y: (int) y coordinate
        """
        self.x = x
        self.y = y
        pass

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __dict__(self):
        return {
            "x": self.x,
            "y": self.y
        }


class Size:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        pass

    def __dict__(self):
        return {
            "width": self.width,
            "height": self.height
        }

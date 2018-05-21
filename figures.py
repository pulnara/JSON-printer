import matplotlib.pyplot as plt


class Screen:
    def __init__(self, fg_color, bg_color, height, width):
        self.fg_color = fg_color
        self.bg_color = bg_color
        self.height = height
        self.width = width


class Figure:
    def __init__(self, color):
        self.color = color

    def get_artist(self):
        return self.artist


class Point(Figure):
    def __init__(self, color, x, y):
        super().__init__(color)
        self.x = x
        self.y = y
        self.artist = plt.Circle((self.x, self.y), 1, color=self.color)


class Polygon(Figure):
    def __init__(self, color, points):
        super().__init__(color)
        self.points = points
        self.artist = plt.Polygon(self.points, color=self.color)


class Rectangle(Figure):
    def __init__(self, color, x, y, height, width):
        super().__init__(color)
        self.x = x
        self.y = y
        self.artist = plt.Rectangle((self.x, self.y), width, height, color=self.color)


class Square(Figure):
    def __init__(self, color, x, y, size):
        super().__init__(color)
        self.artist = plt.Rectangle((x, y), size, size, color=color)


class Circle(Figure):
    def __init__(self, color, x, y, radius):
        super().__init__(color)
        self.x = x
        self.y = y
        self.radius = radius
        self.artist = plt.Circle((self.x, self.y), radius=self.radius, color=self.color)


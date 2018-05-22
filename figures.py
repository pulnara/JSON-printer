import matplotlib.pyplot as plt


class Screen:
    def __init__(self, fg_color, bg_color, height, width):
        self.__fg_color = fg_color
        self.__bg_color = bg_color
        self.__height = height
        self.__width = width

    @property
    def background(self):
        return plt.Rectangle((0, 0), self.__width, self.__height, color=self.__bg_color)

    @property
    def canvas(self):
        return plt.figure(figsize=(self.__width, self.__height), dpi=1)

    @property
    def fg_color(self):
        return self.__fg_color


class Figure:
    def __init__(self, color):
        self._color = color

    def artist(self):
        return None

    @staticmethod
    def create(color, fig):
        return None


class Point(Figure):
    def __init__(self, color, x, y):
        super().__init__(color)
        self.__x = x
        self.__y = y

    def artist(self):
        return plt.Circle((self.__x, self.__y), 1, color=self._color)

    @staticmethod
    def create(color, fig):
        return Point(color, fig['x'], fig['y'])


class Polygon(Figure):
    def __init__(self, color, points):
        super().__init__(color)
        self.__points = points

    def artist(self):
        return plt.Polygon(self.__points, color=self._color)

    @staticmethod
    def create(color, fig):
        return Polygon(color, fig['points'])


class Rectangle(Figure):
    def __init__(self, color, x, y, height, width):
        super().__init__(color)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def artist(self):
        return plt.Rectangle((self.__x, self.__y), self.__width, self.__height, color=self._color)

    @staticmethod
    def create(color, fig):
        return Rectangle(color, fig['x'], fig['y'], fig['height'], fig['width'])


class Square(Figure):
    def __init__(self, color, x, y, size):
        super().__init__(color)
        self.__x = x
        self.__y = y
        self.__size = size

    def artist(self):
        return plt.Rectangle((self.__x, self.__y), self.__size, self.__size, color=self._color)

    @staticmethod
    def create(color, fig):
        return Square(color, fig['x'], fig['y'], fig['size'])


class Circle(Figure):
    def __init__(self, color, x, y, radius):
        super().__init__(color)
        self.__x = x
        self.__y = y
        self.__radius = radius

    def artist(self):
        return plt.Circle((self.__x, self.__y), radius=self.__radius, color=self._color)

    @staticmethod
    def create(color, fig):
        return Circle(color, fig['x'], fig['y'], fig['radius'])

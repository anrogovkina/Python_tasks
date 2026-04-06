class Shape:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


# Класс прямоугольник
class Rectangle(Shape):
    def __init__(self, height, width, x=0, y=0):
        super().__init__(x, y)
        self.height = height
        self.width = width

    # Площадь
    def area(self):
        return self.height * self.width


# Класс квадрат
class Square(Rectangle):
    def __init__(self, side, x=0, y=0):
        super().__init__(side, side, x, y)

    @property
    def height(self):
        return self._height

    @property
    def width(self):
        return self._width

    # Установка значения высоты
    @height.setter
    def height(self, value):
        self._height = self._width = value

    # Установка значения ширины
    @width.setter
    def width(self, value):
        self._width = self._height = value


# Пример использования
if __name__ == "__main__":
    rectangle = Rectangle(2, 3)  # прямоугольник
    print(f"Высота: {rectangle.height}, ширина: {rectangle.width}")
    square = Square(2)  # квадрат
    print(f"Высота: {square.height}, ширина: {square.width}")
    print(f"Площадь прямоугольника: {rectangle.area()}")
    print(f"Площадь квадрата: {square.area()}")
    square.width = 3  # изменяем ширину кварата
    print(f"Высота: {square.height}, ширина: {square.width}")
    print(f"Площадь квадрата: {square.area()}")
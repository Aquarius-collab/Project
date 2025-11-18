class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


rect = Rectangle(10, 5)
sq = Square(6)
tri = Triangle(8, 4)

print("Area of Rectangle:", rect.area())
print("Area of Square:", sq.area())
print("Area of Triangle:", tri.area())
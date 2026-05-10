class Shape:
    def area(self):
        """Base method - to be overridden"""
        pass
    def display(self):
        print(f"Shape: {self.__class__.__name__}")
        print(f"Area: {self.area()}")
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159 * self.radius ** 2
print("=== Area Calculator using Inheritance ===")
shapes = [
    Rectangle(5, 3),
    Square(4),
    Triangle(6, 4),
    Circle(3)
]
for shape in shapes:
    shape.display()

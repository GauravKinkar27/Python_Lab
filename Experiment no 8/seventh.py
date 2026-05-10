class Shape:
    def area(self):
        print("Area of shape (to be overridden)")
        return 0
    def description(self):
        return "This is a shape"
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def description(self):
        return f"This is a rectangle with length={self.length}, breadth={self.breadth}"
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159 * self.radius ** 2
    def description(self):
        return f"This is a circle with radius={self.radius}"
shapes = [Rectangle(5, 3), Circle(4)]
for shape in shapes:
    print(f"\n{shape.description()}")
    print(f"Area: {shape.area():.2f}")



class Shape:
    def __init__(self, name):
        self.name = name
        print(f"Shape constructor called for {self.name}")

    def display_info(self):
        print(f"This is a {self.name}")


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
        print(f"Circle constructor called for {self.name}")

    def calculate_area(self):
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width
        print(f"Rectangle constructor called for {self.name}")

    def calculate_area(self):
        return self.length * self.width



circle = Circle(name="Circle", radius=5)
rectangle = Rectangle(name="Rectangle", length=4, width=6)


circle.display_info()
print("Circle area:", circle.calculate_area())

rectangle.display_info()
print("Rectangle area:", rectangle.calculate_area())

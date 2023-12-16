

class Shape:
    def __init__(self, name):
        self.name = name

    def describe(self):
        return f"This is a {self.name}"

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2


circle_instance = Circle(name="circle", radius=5)


print(circle_instance.describe())
print(circle_instance.area())

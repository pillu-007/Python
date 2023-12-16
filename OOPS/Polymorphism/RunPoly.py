
# Runtime polymorphism in OOP allows a method to be executed based on the actual type of an object at runtime
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

def calculate_area(shape_obj):
    return shape_obj.area()

circle_obj = Circle(radius=5)
square_obj = Square(side_length=4)

area1 = calculate_area(circle_obj)
area2 = calculate_area(square_obj)

print(area1)
print(area2)

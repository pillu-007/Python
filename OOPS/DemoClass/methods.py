


class MathOperations:
    # Class variable
    pi = 3.14

    def __init__(self, radius):
        # Instance variable
        self.radius = radius

    # Instance method to calculate the area of a circle
    def calculate_area(self):
        return MathOperations.pi * self.radius * self.radius

    # Class method to update the value of pi
    @classmethod
    def update_pi(cls, new_value):
        cls.pi = new_value

    # Static method to check if a number is even
    @staticmethod
    def is_even(number):
        return number % 2 == 0


circle = MathOperations(5)

area = circle.calculate_area()
print(f"Area of the circle: {area}")

MathOperations.update_pi(new_value=3.14159)

number_to_check = 8
if MathOperations.is_even(number_to_check):
    print(f"{number_to_check} is even.")
else:
    print(f"{number_to_check} is not even.")

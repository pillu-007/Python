
# Program on Global Variables...

# Global Variable
PI = 3.14159

def calculate_circle_area(radius):
    # Local variable within the function
    area = PI * (radius ** 2)
    return area

# Get user input for the radius
user_radius = 2

# Calculate and display the area
circle_area = calculate_circle_area(user_radius)
print("Area of Circle is ", circle_area)

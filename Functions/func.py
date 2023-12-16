'''
FUNCTIONS

Functions in Python are blocks of reusable code that perform a specific task.
'''

def greet(name):
    """This function greets the person passed in as a parameter."""
    print("Hello, " + name + "!")

greet("prabhu")



def add_numbers(x, y):
    """This function adds two numbers and returns the result."""
    result = x + y
    return result

sum_result = add_numbers(5, 3)
print("Sum:", sum_result)


# Default Parameters
def power(base, exponent=2):
    """This function raises the base to the power of the exponent (default is 2)."""
    result = base ** exponent
    return result


power_result1 = power(2)
power_result2 = power(2, 3)

print("Power (default exponent):", power_result1)
print("Power (custom exponent):", power_result2)


# Variable Number of Arguments
# Arbitrary Positional Arguments
# stored all the elements as tuple
def calculate_sum(*args):
    """This function calculates the sum of variable number of arguments."""
    total = sum(args)
    return total


sum1 = calculate_sum(1, 2, 3)
sum2 = calculate_sum(4, 5, 6, 7)

print("Sum 1:", sum1)
print("Sum 2:", sum2)


# keyword arguments
# When using **kwargs, the items returned will be key-value pairs
def display_info(**kwargs):
    """Display information provided as keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Using **kwargs to pass keyword arguments
display_info(name="prabhu", age=22, city="Adilabad", occupation="Engineer")



#Lambda Functions (Anonymous Functions)

multiply = lambda x, y: x * y
result = multiply(3, 4)
print("Product:", result)




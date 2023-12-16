

# Decorator is a function which can take a function as argument and extend its functionality
# and returns modified function with extended functionality.

# The main objective of decorator functions is we can extend the functionality of existing
# functions without modifies that function.

def greet(name):
    print(f"Hello, {name}!")

# But we want to modify this function to provide different message if name is Sunny
# We can do this without modifying wish() function by using decorator.

def uppercase_decorator(func):
    def wrapper(name):
        modified_name = name.upper()
        func(modified_name)
    return wrapper

@uppercase_decorator
def greet(name):
    print(f"Hello, {name}!")

# Using the decorated function
greet("sai")
greet("prabhu")

print("#"*15)

# we can  call same function with decorator and without decorator:

def uppercase_decorator(func):
    def wrapper(name):
        modified_name = name.upper()
        func(modified_name)
    return wrapper

def greet(name):
    print(f"Hello, {name}!")

# Applying the decorator to the greet function
decorated_greet = uppercase_decorator(greet)

# Using the decorated function
greet("vikram")
greet("manish")

# Using the decorated function obtained from the decorator
decorated_greet("Madhu")
decorated_greet("yogesh")



def smart_division(func):
    def inner(a, b):
        print("We are dividing", a, "with", b)
        if b == 0:
            print("OOPS...cannot divide")
            return
        else:
            return func(a, b)
    return inner

@smart_division
def division(a, b):
    return a / b

print(division(20,2))
print(division(20,0))

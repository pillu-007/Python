

def uppercase_decorator(func):
    def wrapper(name):
        return func(name).upper()
    return wrapper

def exclamation_decorator(func):
    def wrapper(name):
        return func(name) + "!"
    return wrapper

@exclamation_decorator
@uppercase_decorator
def greet(name):
    return f"Hello, {name}"

result = greet("prabhu")
print(result)


# Generators
# Generator is a function which is responsible to generate a sequence of values.
# We can write generator functions just like ordinary functions, but it uses yield keyword to
# return values.

def mygen():
    print("yielding of letters will be started....")
    yield 'A'
    yield 'B'
    yield 'C'
    print("yielding of letters completed....")

# Creating a generator object
g = mygen()

# Using the next() function to iterate over the generator
print(next(g))
print(next(g))
print(next(g))
print(next(g, 'no values to iterate'))


# If you try to call g() directly, it will raise an error
# TypeError: 'generator' object is not callable

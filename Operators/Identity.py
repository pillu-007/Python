# Identity operator 'is' example
x = [1, 2, 3]
y = [1, 2, 3]
z = x

# Check if x and y refer to different objects
print("x is y:", x is y)  # False

# Check if x and z refer to the same object
print("x is z:", x is z)  # True

# Identity operator 'is not' example
a = "hello"
b = "world"
c = "hello"


# Check if a and b do not refer to the same object
print("a is not b:", a is not b)  # True

# Check if a and c  refer to the same object
print("a is c:", a is c)  # True


# float to int
x=3.24
print(int(x))

print()

# string to int
x='124'
print(int(x))

print()

# boolean to int
x=False
print(int(x))

print()

# boolean to int

x=True
print(int(x))

print()


# int to bool
x=0
print(bool(x))
print()

# float to bool
x=3.2
print(bool(x))
print()

# string to bool
x='sai'
print(bool(x))
print()

x=''
print(bool(x))
print()

# int to string
x=0
print(str(x))
print()

# float to string
x=0.23
print(str(x))
print()

#boolean to string
x=True
print(str(x))
print()

x=False
print(str(x))
print()


# int to float
x=14
print(float(x))
print()

# boolean to float
x=True
print(float(x))
print()

x=False
print(float(x))
print()


#string to float
x='214'
print(float(x))
print()

x='214.24'    # here we have to give in base-10
print(float(x))
print()

# x='sai'
# print(float(x)) -----------> This will give us error
# print()


# Implicit type casting (automatic)
x = 5  # Integer
y = 3.14  # Float

result_implicit = x + y  # Implicit casting of x to float
print( result_implicit)  # Output: 8.14

# Explicit type casting (manual)
a = "42"  # String
b = 7  # Integer

result_explicit = int(a) + b  # Explicit casting of a to integer
print(result_explicit)  # Output: 49

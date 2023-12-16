
# Taking input from the user
name = input("Enter your name: ")
print(type(name))
print("Hello, " + name + "!")

# Taking an integer input
age = int(input("Enter your age: "))
print(age)

# Taking a float input
height = float(input("Enter your height in meters: "))
print(height)


# Taking multiple inputs in a single line using split()
inputs = input("Enter your name, age, and height (separated by spaces): ")

# Splitting the inputs into a list
input_list = inputs.split()

# Extracting values from the list
name = input_list[0]
age = int(input_list[1])
height = float(input_list[2])

# Printing the inputs
print("Name:", name)
print("Age:", age)
print("Height:", height)


a,b,c =[int(x)  for x in input("enter three numbers").split()]
print("the sum of 3 numbers are ", a+b+c)


# using eval function
a= eval(input("inter one number"))
print(a)



# If try with multiple except blocks available then based on raised exception the
# corresponding except block will be executed.

# If try with multiple except blocks available then the order of these except blocks is
# important .Python interpreter will always consider from top to bottom until matched
# except block identified.

try:
 x=int(input("Enter First Number: "))
 y=int(input("Enter Second Number: "))
 print(x/y)
except ZeroDivisionError :
 print("Can't Divide with Zero")
except ValueError:
 print("please provide int value only")

print()

# try:
#  x = int(input("Enter First Number: "))
#  y = int(input("Enter Second Number: "))
#  print(x / y)
# except ArithmeticError:    # here ArithmeticError is the parent class of ZeroDivisionError , so it can handle ZeroDivisionError .
#  print("ArithmeticError")
# except ZeroDivisionError:
#  print("ZeroDivisionError")

print()

try:
 x=int(input("Enter First Number: "))
 y=int(input("Enter Second Number: "))
 print(x/y)
except (ZeroDivisionError,ValueError) as msg:
 print("Plz Provide valid numbers only and problem is: ",msg)


# Default except block:
# We can use default except block to handle any type of exceptions.
# In default except block generally we can print normal error messages.

try:
 x=int(input("Enter First Number: "))
 y=int(input("Enter Second Number: "))
 print(x/y)
except ZeroDivisionError:
 print("ZeroDivisionError:Can't divide with zero")
except:
 print("Default Except:Plz provide valid input only")


# *** Note: If try with multiple except blocks available then default except block should be
# last,otherwise we will get SyntaxError.


# The following code will give error because the default exception is placed at first and it will catch all the exception

# try:
#  print(10/0)
# except:
#  print("Default Except")
# except ZeroDivisionError:
#  print("ZeroDivisionError")

# The following are various possible combinations of except blocks
# 1. except ZeroDivisionError:
# 1. except ZeroDivisionError as msg:
# 3. except (ZeroDivisionError,ValueError) :
# 4. except (ZeroDivisionError,ValueError) as msg:
# 5. except :
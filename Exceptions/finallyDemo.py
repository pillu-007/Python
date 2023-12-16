import os

# finally block:

# 1. It is not recommended to maintain clean up code(Resource Deallocating Code or
# Resource Releasing code) inside try block because there is no guarentee for the execution
# of every statement inside try block always.

# 2. It is not recommended to maintain clean up code inside except block, because if there
# is no exception then except block won't be executed.

# try:
#  Risky Code
# except:
#  Handling Code
# finally:
#  Cleanup code


# Case-1: If there is no exception

try:
 print("try")
except:
 print("except")
finally:
 print("finally")

 # Case - 2: If there is an exception raised but handled :


try:
 print("try")
 print(10/0)
except ZeroDivisionError:
 print("except")
finally:
 print("finally")

 # Case - 3: If there is an exception raised but not handled:

 # try:
 #     print("try")
 #     print(10 / 0)
 # except NameError:
 #  print("except")
 # finally:
 #  print("finally")

  # Note: There is only one situation where finally block won't be executed ie whenever we are using os._exit(0) function.


try:
 print("try")
 os._exit(0)
except NameError:
 print("except")
finally:
 print("finally")
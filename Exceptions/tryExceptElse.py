

# else block with try-except-finally:

# We can use else block with try-except-finally blocks.
# else block will be executed if and only if there are no exceptions inside try block.

# try:
#  Risky Code
# except:
#  will be executed if exception inside try
# else:
#  will be executed if there is no exception inside try
# finally:
#  will be executed whether exception raised or not raised and handled or not
#  handled

# Case -1 : if exception raised and handled the control flow wont enter in else block

# try:
#  print("try")
#  print(10/0)
# except:
#  print("except")
# else:
#  print("else")
# finally:
#  print("finally")

 # Case -2 : if exception is not raised in try block then the control flow will enter in else block

try:
     print("try")
     print(10 / 2)
except:
     print("except")
else:
     print("else")
finally:
     print("finally")
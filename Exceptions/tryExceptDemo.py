
# try with except

print("before try block")
try:
 print(10/'ten')
except ZeroDivisionError as msg:
 print("exception raised and its description is:",msg)
print("after the except block")
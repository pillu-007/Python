
# Types of Exceptions:
#
# In Python there are 2 types of exceptions are possible.
#     1. Predefined Exceptions
#     2. User Definded Exceptions
#
#
# 1. Predefined Exceptions:
#
# Also known as in-built exceptions
# The exceptions which are raised automatically by Python virtual machine whenver a
# particular event occurs, are called pre defined exceptions.
#
# Eg 1: Whenever we are trying to perform Division by zero, automatically Python will raise
# ZeroDivisionError.
# print(10/0)

# 2. User Defined Exceptions:
#
# Also known as Customized Exceptions or Programatic Exceptions
# Some time we have to define and raise exceptions explicitly to indicate that something
# goes wrong ,such type of exceptions are called User Defined Exceptions or Customized
# Exceptions


class AgeOutOfRangeException(Exception):
    def __init__(self, age, min_age, max_age):
        self.msg = f"Sorry, the age {age} is not within the allowed range ({min_age}-{max_age})."

try:
    age = int(input("Enter Age: "))
    min_allowed_age = 18
    max_allowed_age = 60

    if age < min_allowed_age or age > max_allowed_age:
        raise AgeOutOfRangeException(age, min_allowed_age, max_allowed_age)

except ValueError:
    print("Please enter a valid age.")

except AgeOutOfRangeException as aoe_ex:
    print(aoe_ex.msg)

else:
    print("Age is within the allowed range. Proceed with the next steps.")


days=['MOn', 'tue','wed',"Thrus",'Fri']
enum_days=enumerate(days)
print(next(days))
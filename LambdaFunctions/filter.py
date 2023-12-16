#
# filter() function:

# We can use filter() function to filter values from the given sequence based on some
# condition.

#syntax:
# filter(function,sequence)

# where function argument is responsible to perform conditional check
# sequence can be list or tuple or string.


# without lambda Function:
def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False

l = [0, 5, 10, 15, 20, 25, 30]
l1 = list(filter(isEven, l))
print("The list of elements after filtering list l :",l1)

print()

# with lambda Function:
l2 = [0, 5, 10, 15, 20, 25, 30]

# Filter even numbers using a lambda function
even_numbers = list(filter(lambda x: x % 2 == 0, l2))
print("List of even numbers:", even_numbers)

# Filter odd numbers using a lambda function
odd_numbers = list(filter(lambda x: x % 2 != 0, l2))
print("List of odd numbers:", odd_numbers)


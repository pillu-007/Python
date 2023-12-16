from functools import reduce

# reduce() function:

# reduce() function reduces sequence of elements into a single element by applying the
# specified function.

#syntax:
# reduce(function,sequence)

# reduce() function present in functools module and hence we should write import
# statement.


l1=[10,20,30,40,50]
sum=reduce(lambda x,y:x+y,l1)
product=reduce(lambda x,y:x*y,l1)
print("The sum of elements in list l1 is :",sum)
print("The product of elements in list l1 is :",product)

# it's important to note that reduce works on a single iterable unlike map function.....


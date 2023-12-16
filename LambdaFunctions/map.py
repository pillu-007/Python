

# map() function:

# For every element present in the given sequence,apply some functionality and generate
# new element with the required modification. For this requirement we should go for
# map() function.

# Eg: For every element present in the list perform double and generate new list of doubles.

# Syntax:
# map(function,sequence)

# The function can be applied on each element of sequence and generates new sequence.

# Without lambda

l = [1, 2, 3, 4, 5]
def doubleIt(x):
    return 2 * x

l1 = list(map(doubleIt, l))
print("The list l after doubling every element in it :",l1)


# with lambda

l1 = [1, 2, 3, 4, 5]
l2 = list(map(lambda x: 2 * x, l))
print(l2)

# We can apply map() function on multiple lists also and also
# the numbers of elements in both list dont need to be same.....


list1=[1,2,3,4,5,6,7,8]
list2=[1,2,3,4,5,6]
list3=list(map(lambda x,y:x*y,list1,list2))
print("After multiplying list1 with list2 the new list is :",list3)


class A:
    def __int__(self,a):
        self.a=a


class B(A):
    def __int__(self,b,a):
        super().__init__(a)
        self.b=b

class C(B):
    def __int__(self,c,a,b):
        super().__init__(self,a,b,c)
        self.c=c





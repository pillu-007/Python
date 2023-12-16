
def outer() :
    print(" i am inside the outer function")
    def inner(a,b):
        print(" i am inside the inner function")
        print("The sum of two numbers are :", a+b)
    inner(2,3)
    inner(10,23)
    inner(40,60)

outer();

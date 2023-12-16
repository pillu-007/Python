

def outer() :
    print(" outer function started execution.....")
    def inner():
        print("inner function executed....")
    print("outer function returning inner function....")
    return inner

out=outer()
out()
out()
out()
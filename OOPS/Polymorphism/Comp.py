# Mrthod overloading
# python doesnot support method overLoading
#it will take the last mathod defined as one method only...


class MathOperations:
    def add(self, x, y):
        return x + y

    def add(self, x, y, z):
        return x + y + z

    def add(self, *a):
        return sum(a)

math_obj = MathOperations()
# result1 = math_obj.add(1, 2)
result2 = math_obj.add(1, 2, 3)
print("The sum of three numbers is : ",result2)

# class
# A class in Python is a blueprint for creating objects. It encapsulates data (attributes) and functions (methods) that operate on the data.
# the value to the self parameter is assigned by python virtual machine ....and we can use any word in place of self keywrod.
# objects are real existance of a class

class Student:
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks

    def print_student_info(self):
        print("Name:", self.name)
        print("Roll No:", self.rollno)
        print("Marks:", self.marks)


student1 = Student("saiprabhu", "124", 88)
student1.print_student_info()



# if we dont provide constructor PVM  internally creates one constructor with in it and executes it.
class Test:

    def __init__(self):
        print("hello i am constructor")
    def hello(self):
        print("Hii this is prabhu.")


t1 = Test()
t1.hello()
t1.__init__()
t1.__init__()


# constructor overloading is not possible in python
#in the below one the latest constructor will be considered and all other will be of waste

class Testing:

    def __init__(self):
        print("hello i am constructor")

    def __init__(self,name):
        self.name=name
        print("hello i am %s", (name))

    def hello(self):
        print("Hii this is prabhu.")

# t1=Testing()   --------> This line results us in error
t1 = Testing('prabhu')
t1.hello()
t1.__init__('sai')
t1.__init__('vikram')

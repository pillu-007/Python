# Encapsulation

class MyClass:
    def __init__(self, value):
        self.Age = value


   #getter
    def get_Age(self):
        return self.Age


  #Setter
    def set_Age(self, new_value):
        self.Age = new_value

obj = MyClass(22)
print("The value of age is : ",obj.get_Age())
obj.set_Age(23)
print("The value of age is After setting to new value : ",obj.get_Age())

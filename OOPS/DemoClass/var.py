

# Instance variables , Static Variables , Local varaibles....

class Employee:
    # Class variable (static variable)
    company_name = "Zemoso"

    def __init__(self, employee_name):
        # Instance variable
        self.employee_name = employee_name

    def log_hours(self, hours_worked):
        # Local variable
        print("{} worked {} hours".format(self.employee_name, hours_worked))

    def display_information(self):
        # Accessing and displaying all types of variables
        print("Company name:", Employee.company_name)
        print("Employee name:", self.employee_name)


emp1 = Employee(employee_name="saiprabhu")

emp1.log_hours(hours_worked=8)

emp1.display_information()

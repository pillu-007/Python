class Engine:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
        print(f"Engine constructor called for {self.fuel_type} engine")

    def start_engine(self):
        print("Engine started")


class ElectricMotor:
    def __init__(self, motor_type):
        self.motor_type = motor_type
        print(f"ElectricMotor constructor called for {self.motor_type} motor")

    def charge_battery(self):
        print("Battery charging")


class HybridCar(Engine, ElectricMotor):
    def __init__(self, brand, fuel_type, motor_type):

        Engine.__init__(self, fuel_type)
        ElectricMotor.__init__(self, motor_type)
        self.brand = brand
        print(f"HybridCar constructor called for {self.brand}")

    def drive(self):
        print(f"Driving the {self.brand} hybrid car")


hybrid_car = HybridCar(brand="Toyota", fuel_type="Gasoline", motor_type="Electric")


hybrid_car.start_engine()
hybrid_car.charge_battery()
hybrid_car.drive()

# MultiLevel Inheritance


class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
        print(f"Vehicle constructor called for {self.vehicle_type}")

    def start_engine(self):
        print(f"Starting the {self.vehicle_type} engine")


class Car(Vehicle):
    def __init__(self, vehicle_type, brand):
        super().__init__(vehicle_type)
        self.brand = brand
        print(f"Car constructor called for {self.vehicle_type} ({self.brand})")

    def drive(self):
        print(f"Driving the {self.brand} car")


class ElectricCar(Car):
    def __init__(self, vehicle_type, brand, battery_type):
        super().__init__(vehicle_type, brand)
        self.battery_type = battery_type
        print(f"ElectricCar constructor called for {self.vehicle_type} ,{self.brand}, {self.battery_type}")

    def charge(self):
        print(f"Charging the {self.brand} electric car")



electric_car = ElectricCar(vehicle_type="Electric Car", brand="Tesla", battery_type="Lithium-ion")


electric_car.start_engine()
electric_car.drive()
electric_car.charge()
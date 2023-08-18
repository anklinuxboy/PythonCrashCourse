class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
    
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def get_reading(self):
        print(f"The car has {self.odometer} miles on it.")

    def update_odometer(self, miles):
        if miles >= self.odometer:
            self.odometer = miles
        else:
            print("You can't roll back the miles")

class ElectricCar(Car):
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 140

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery")

new_car = Car('lucid', 'air', 2022)
print(new_car.get_descriptive_name())
new_car.get_reading()
new_car.odometer = 100

electric_car = ElectricCar('tesla', 'model s', 2019)
print(electric_car.get_descriptive_name())


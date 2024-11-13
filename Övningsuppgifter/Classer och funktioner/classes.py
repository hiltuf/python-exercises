class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        return "The car is starting."

class ElectricCar(Car):
    def __init__(self, brand, battery_capacity):
        super().__init__(brand)  # Anropar föräldraklassens konstruktor
        self.battery_capacity = battery_capacity
    def start(self):
        return "The electric car is starting on electricity."


electric_car = ElectricCar("Tesla", 75)
print(electric_car.start())  # Output: "The electric car is starting on electricity."


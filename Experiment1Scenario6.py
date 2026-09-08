class Car:
    def __init__(self, brand, model, fuel_type, price):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
        self.price = price

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Fuel Type:", self.fuel_type)
        print("Price: ₹", self.price)

    def refuel(self):
        print(f"{self.model} is being refueled with {self.fuel_type}.")


class ElectricCar(Car):
    def __init__(self, brand, model, price, battery_capacity):
        super().__init__(brand, model, "Electric", price)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print("Battery Capacity:", self.battery_capacity, "kWh")

    def refuel(self):
        print(f"{self.model} is being charged using an electric charging station.")


# Creating objects
car = Car("Toyota", "Camry", "Petrol", 4500000)
electric_car = ElectricCar("Tesla", "Model 3", 4500000, 60)

print("----- Petrol Car -----")
car.display_info()
car.refuel()

print("\n----- Electric Car -----")
electric_car.display_info()
electric_car.refuel()

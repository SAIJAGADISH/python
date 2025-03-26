# Base class
class Vehicle:
    def __init__(self,make, model):
        self.make = make
        self.model = model

    def start(self):
        print(f"\n{self.make} {self.model} is starting.\n")

# Derived class inheriting from Vehicle
class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors
        super().start()
    # Override start method for Car
    def start(self):
        print(f"{self.make} {self.model} with {self.doors} doors is starting with a smooth ignition.")

# Another derived class
class Truck(Vehicle):
    def __init__(self, make, model, payload):
        super().__init__(make, model)
        self.payload = payload
        super().start()
    # Truck may use the base start or have its own version
    def start(self):
        print(f"{self.make} {self.model} truck carrying {self.payload} kg is starting with heavy-duty power.")

# Creating instances
car = Car("Toyota", "Camry", 4)
truck = Truck("Ford", "F-150", 1500)

car.start()     # Output: Toyota Camry with 4 doors is starting with a smooth ignition.
truck.start()   # Output: Ford F-150 truck carrying 1500 kg is starting with heavy-duty power.

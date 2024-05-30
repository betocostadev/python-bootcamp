# Python - Introduction to Object Oriented Programming in Python
# Inheritance - Simple Inheritance
# Inheritance is a powerful feature in object oriented programming.
# It refers to defining a new class with little or no modification to an existing class.
# The new class is called derived (or child) class and the one from which it inherits
# is called the base (or parent) class.
print(
    "======== Python - Introduction to Object Oriented Programming in Python ========"
)
print("\n=== Simple Inheritance ===\n")


class Vehicle:
    def __init__(self, make, model, wheel_number, year):
        self.make = make
        self.model = model
        self.wheel_number = wheel_number
        self.year = year

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{key}: {value}' for key, value in self.__dict__.items()])}"

    def start_engine(self):
        return "Engine started"


class Motorcycle(Vehicle):
    pass


class Car(Vehicle):
    pass


class Truck(Vehicle):
    def __init__(self, make, model, wheel_number, year):
        super().__init__(make, model, wheel_number, year)
        self.cargo = []

    def load_cargo(self, item):
        self.cargo.append(item)
        return f"{item} loaded"

    def unload_cargo(self, item):
        self.cargo.remove(item)
        return f"{item} unloaded"

    def has_cargo(self):
        print(
            "Truck is not loaded"
            if not self.cargo
            else f"Truck is loaded with {', '.join(self.cargo)}"
        )
        return self.cargo


bmw = Car("BMW", "X5", 4, 2021)
print(bmw)
print(bmw.start_engine())

hayabusa = Motorcycle("Suzuki", "Hayabusa", 2, 2020)
print(hayabusa)
print(hayabusa.start_engine())

cybertruck = Truck("Tesla", "Cybertruck", 6, 2022)
cybertruck.load_cargo("Laptop")
cybertruck.load_cargo("Tablet")
print(cybertruck)
print(cybertruck.start_engine())
cybertruck.has_cargo()
print("Unloading Laptop...")
cybertruck.unload_cargo("Laptop")
print(cybertruck)

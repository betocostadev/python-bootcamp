# Python - Introduction to Object Oriented Programming in Python
# Not based on the course

# Composition
# Composition is a concept that models a has a relationship.
# It enables creating complex types by combining objects of other types.
# This means that a class Composite can contain an object of another class Component.

print(
    "======== Python - Introduction to Object Oriented Programming in Python ========"
)
print("\n=== Composition ===\n")


class Engine:
    def __init__(self, type):
        self.type = type

    def start(self):
        return f"{self.type} engine started"


class Wheels:
    def __init__(self, number):
        self.number = number

    def rotate(self):
        return f"{self.number} wheels are rotating"


class Car:
    def __init__(self, engine_type, wheel_number):
        self.engine = Engine(engine_type)
        self.wheels = Wheels(wheel_number)

    def start(self):
        return self.engine.start(), self.wheels.rotate()


class Motorcycle:
    def __init__(self, engine_type, wheel_number):
        self.engine = Engine(engine_type)
        self.wheels = Wheels(wheel_number)

    def start(self):
        return self.engine.start(), self.wheels.rotate()


# In this code, Car and Motorcycle classes are composed of Engine and Wheels objects.
# When you create a Car or Motorcycle object, you specify the type of engine and the number of wheels,
# and these are used to create Engine and Wheels objects that belong to the Car or Motorcycle.

# The start method in Car and Motorcycle classes calls the start method of the Engine object
# and the rotate method of the Wheels object, demonstrating that a Car or Motorcycle object can
# use the functionality of its component objects.

bmw = Car("V8", 4)
harley = Motorcycle("V2", 2)
print("bmw")
print(bmw.start())
print("harley")
print(harley.start())

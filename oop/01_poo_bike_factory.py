# John has a bike factory and he wants to keep track of the bikes he sells.
# The program must inform the bike color, model, year, and price.
# Create a class Bike with the following attributes:
# color, model, year, price and a method to get the bike info.
# also the bikes must have the methods to horn, accelerate and brake.

print(
    "======== Python - Introduction to Object Oriented Programming in Python ========"
)
print("\n=== Challenge: Bike Factory ===\n")


class Bike:
    # Add a docstring to the class
    """Class to represent a Bike"""

    def __init__(self, model, color, year, price) -> None:
        self.model = model
        self.color = color
        self.year = year
        self.price = price
        self.is_horn = False
        self.is_accelerating = False
        self.is_braking = False

    def horn(self):
        self.is_horn = not self.is_horn
        return "Honking..." if self.is_horn else "Horn stopped."

    def accelerate(self):
        self.is_accelerating = True
        return "Accelerating..."

    def brake(self):
        self.is_braking = True
        return "Braking..."

    def get_info(self):
        return f"Bike Information:\nModel: {self.model}, Color: {self.color}, Year: {self.year}, Price: {self.price}"

    def __str__(self) -> str:
        pass
        return f"{self.__class__.__name__}: {', '.join([f'{key}: {value}' for key, value in self.__dict__.items()])}"


b1 = Bike("B1", "Red", 2021, 1500)
print(b1.model, b1.color)
print(b1.get_info())
print(b1.accelerate())
print(b1.horn())  # Bike.horn(b1)
print(b1.horn())
print(b1.brake(), "\n")
# Calling the __str__ method
print(b1)

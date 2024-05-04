# Python - Introduction to Object Oriented Programming in Python
# Interfaces and Abstract Classes

# An interface is a blueprint for a class. It can be used to define the methods that a class must implement.
# An interface is like a class with all the methods as abstract methods.
# An abstract class is a class that contains one or more abstract methods.
# An abstract method is a method that is declared, but contains no implementation.
# Abstract classes cannot be instantiated, and require subclasses to provide implementations for the abstract methods.
# Abstract classes can have both abstract methods and concrete methods.

# In Python, we can create an interface by using the abc module.
# The abc module provides the ABC class, which is used to create abstract classes.
# The ABC class is a metaclass that can be used to create abstract classes.
# To create an abstract class, we need to inherit from the ABC class and use the
# @abstractmethod decorator to mark the methods as abstract.

# Let's see an example of an interface and an abstract class in Python.
from abc import ABC, abstractmethod


print("======== Python - Introduction to Object Oriented Programming in Python ========")
print("\n=== Interfaces and Abstract Classes ===\n")


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{key}: {value}' for key, value in self.__dict__.items()])}"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{key}: {value}' for key, value in self.__dict__.items()])}"


rectangle = Rectangle(5, 10)

print(rectangle)
print(f"Area: {rectangle.area()}")
print(f"Perimeter: {rectangle.perimeter()}")
print()

circle = Circle(7)

print(circle)
print(f"Area: {circle.area()}")
print(f"Perimeter: {circle.perimeter()}")
# In this code, we define an interface Shape with two abstract methods area() and perimeter().
# We then create two concrete classes Rectangle and Circle that implement the Shape interface.
# The Rectangle class has methods to calculate the area and perimeter of a rectangle, and the Circle class has
# methods to calculate the area and perimeter of a circle.
# Both the Rectangle and Circle classes inherit from the Shape interface and provide implementations for the
# abstract methods area() and perimeter().
# The Shape interface acts as a blueprint for the Rectangle and Circle classes, ensuring that they have the
# required methods to calculate the area and perimeter of a shape.
# When we run the code, we create instances of the Rectangle and Circle classes
# and call the area() and perimeter() methods to calculate the area and perimeter of the shapes.
# The output shows the area and perimeter of the rectangle and circle objects.

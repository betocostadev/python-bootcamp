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
from datetime import date


print("======== Python - Introduction to Object Oriented Programming in Python ========")
print("\n=== Interfaces and Abstract Classes ===\n")


# Using an interface
# ABC stands for Abstract Base Class
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


# Using a remote control class to show another example
print("\nUsing a remote control class to show another example\n")


class RemoteControl(ABC):
    @abstractmethod
    def turn_on(self):
        raise NotImplementedError("Subclass must implement abstract method")

    @abstractmethod
    def turn_off(self):
        pass

    # Abstract properties
    @property
    def brand(self):
        raise NotImplementedError("Subclass must implement abstract method")


class TVRemoteControl(RemoteControl):
    def turn_on(self):
        return "TV turned on"

    def turn_off(self):
        return "TV turned off"

    @property
    def brand(self):
        return "Samsung"


class ACRemoteControl(RemoteControl):
    def turn_on(self):
        return "AC turned on"

    def turn_off(self):
        return "AC turned off"

    @property
    def brand(self):
        return "LG"


tvremote = TVRemoteControl()
acremote = ACRemoteControl()

print(tvremote.turn_on())
print(tvremote.turn_off())
print(tvremote.brand)
print(acremote.turn_on())
print(acremote.turn_off())
print(acremote.brand)


# Using class methods
print("\nUsing class methods\n")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # A class method is a method that is bound to the class and not the object of the class.
    # They have the access to the state of the class as it takes
    # a class parameter that points to the class and not the object instance.
    # It can modify a class state that would apply across all the instances of the class.
    # For example, it can modify a class variable that will be applicable to all the instances.
    # It is defined using the @classmethod decorator.
    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, date.today().year - birth_year)

    # A static method is also a method that is bound to the class and not the object of the class.
    # A static method can't access or modify class state.
    # It is present in a class because it makes sense for the method to be present in class.
    # It is defined using the @staticmethod decorator.
    @staticmethod
    def is_adult(age):
        return age > 18

    def display(self):
        print(f"{self.name} is {self.age} years old")


alice = Person("Alice", 25)
# Note that you can call the method from_birth_year without creating an instance of the class.
john = Person.from_birth_year("John", 1990)

alice.display()
john.display()

print(f"Is Alice an adult? {Person.is_adult(alice.age)}")
print(f"Is John an adult? {Person.is_adult(john.age)}")

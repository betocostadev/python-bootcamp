# Python - Introduction to Object Oriented Programming in Python
# Intro
# Object Oriented Programming (OOP) is a programming paradigm that relies on the concept of classes and objects.
# It is used to structure a software program into simple, reusable pieces of code blueprints (usually called classes),
# which are used to create individual instances of objects.
# There are many object-oriented programming languages including JavaScript, C++, Java, and Python.


# Classes and Objects
# A class is a blueprint for the object.
# We can think of class as a sketch of a parrot with labels.
# It contains all the details about the name, colors, size etc. Based on these descriptions, we can study
# about the parrot. Here, parrot is an object.
# The example for class of parrot can be :
# class Parrot:
#     pass

# Here, we use the 'class' keyword to define an empty class Parrot. From class, we construct instances.
# An instance is a specific object created from a particular class.
# Example:
# obj = Parrot()
# Here, obj is an object of class Parrot.
# Like function definitions begin with the 'def' keyword in Python, class definitions begin with a 'class' keyword.
# The first string inside the class is called docstring and has a brief description about the class.
# Although not mandatory, this is recommended.
# The 'pass' keyword is used to avoid getting an error. It is used as a placeholder.

print(
    "======== Python - Introduction to Object Oriented Programming in Python ========"
)
print("\n=== Intro: Classes and Objects ===\n")


class Dog:

    def __init__(self) -> None:
        pass
        self.name = "Nameless Dog"
        self.age = 2
        self.color = "Brown"
        self.breed = "German Shepherd"
        self.is_barking = False

    def bark(self):
        self.is_barking = True
        return "Woof! Woof!"

    def stop_barking(self):
        self.is_barking = False
        return "Dog stopped barking."

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def get_is_barking(self):
        return self.is_barking

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Color: {self.color}, Breed: {self.breed}"


rex = Dog()
print(rex.get_info())
rex.set_name("Rex")
print(rex.get_info())
print(f"Is Rex barking? {rex.is_barking}")
print(rex.bark())

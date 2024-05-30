# Python - Introduction to Object Oriented Programming in Python
# Polymorphism
# Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).
# Suppose, we need to color a shape, there are multiple shapes (rectangle, square, circle).
# However we could use the same method to color any shape. This concept is called Polymorphism.

print(
    "======== Python - Introduction to Object Oriented Programming in Python ========"
)
print("\n=== Polymorphism ===\n")
print(
    "Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types)."
)
print(
    """
Using Polymorphism, with Inheritance, we can create a method in the parent class that can be overridden
by a subclass."""
)

# Using polymorphism with inheritance
# The method bark() is defined in both the parent class and the child class.
# The child class overrides the method bark() of the parent class.
# This is an example of polymorphism.


class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{key}: {value}' for key, value in self.__dict__.items()])}"


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


class Fish(Animal):
    def speak(self):
        return f"{self.name} says Blub!"


max = Dog("Max")
felix = Cat("Felix")
nemo = Fish("Nemo")

print(max)
print(max.speak())
print(felix)
print(felix.speak())
print(nemo)
print(nemo.speak())


# Now, let's see how to use polymorphism with a function.
# Using polymorphism with a function
# The function animal_speak() takes an object as an argument and calls the speak() method on that object.
# The speak() method is defined in each of the classes Dog, Cat, and Fish.
# The speak() method is overridden in each of the classes Dog, Cat, and Fish.
# This is an example of polymorphism.


def animal_speak(animal):
    return animal.speak()


print("\nUsing polymorphism with a function")
print(animal_speak(max))
print(animal_speak(felix))
print(animal_speak(nemo))

# With this you can see why the concept of Composition can have a better approach than Inheritance.
# Inheritance can be very useful, but it can also be very limiting.
# Composition can be used to overcome some of the limitations of Inheritance.
# Composition is a concept that models a has a relationship.
# It enables creating complex types by combining objects of other types.
# This means that a class Composite can contain an object of another class Component.
# Check the composition file to understand this concept better.

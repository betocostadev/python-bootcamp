# Python - Introduction to Object Oriented Programming in Python
# Constructors and Destructors

# Constructors
# Constructors are generally used for instantiating an object.
# The task of constructors is to initialize(assign values) to the data members of the class when an
# object of class is created. In Python, the method __init__() is a constructor method.

print(
    "======== Python - Introduction to Object Oriented Programming in Python ========"
)
print("\n=== Constructors and Destructors ===\n")


class Robot_Dog:
    def __init__(self, name, age, color, breed, farting=True) -> None:
        self.name = name
        self.age = age
        self.color = color
        self.breed = breed
        self.farting = farting

    def bark(self):
        return "Woof! Woof!"

    def stop_barking(self):
        return "Dog stopped barking."

    def get_is_farting(self):
        return self.farting

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{key}: {value}' for key, value in self.__dict__.items()])}"

    # Destructor

    def __del__(self):
        print(f"{self.name} is being destroyed :(")


jamal = Robot_Dog("Jamal", 3, "Black", "Electric Labrador")

print(jamal.bark())
print(jamal)
print("Now, Jamal is not farting anymore.")
# Jamal will be destroyed since the program will end it's execution.
# But if we want to destroy Jamal before the end of the program, we can use the 'del' keyword.
# del jamal
# print(jamal)  # NameError: name 'jamal' is not defined

# Destructors are called when an object gets destroyed.
# In Python, destructors are not needed as much needed in C++
# because Python has a garbage collector that handles memory management automatically.
# The __del__() method is a known as a destructor method in Python.

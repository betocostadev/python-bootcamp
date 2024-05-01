# Python - Introduction to Object Oriented Programming in Python
# Inheritance - Multiple Inheritance
# Multiple inheritance is a feature in which a class can inherit attributes and methods
# from more than one parent class.

print("======== Python - Introduction to Object Oriented Programming in Python ========")
print("\n=== Multiple Inheritance ===\n")


class Father:
    def __init__(self):
        self.father_name = "Odin"

    def print_father_name(self):
        return self.father_name


class Mother:
    def __init__(self):
        self.mother_name = "Frigga"

    def print_mother_name(self):
        return self.mother_name


class Child(Father, Mother):
    def __init__(self, name, **kwargs):
        self.name = name
        super().__init__(**kwargs)
        Father.__init__(self)
        Mother.__init__(self)

    def print_parent_names(self):
        return self.print_father_name(), self.print_mother_name()

    def print_full_name(self):
        return f"{self.name} {self.father_name} {self.mother_name}"


class SuperChild(Child):
    def __init__(self, power, **kwargs):
        self.power = power
        super().__init__(**kwargs)

    def get_mro(self):
        return self.__class__.mro()

    def print_info(self):
        return f"Super child {self.name} has the power of {self.power}"


thor = Child("Thor")
print(thor.print_parent_names())
print(thor.print_full_name())

print("\nThe super child")

beto = SuperChild(name="Beto", power="Flying")
print(beto.print_parent_names())
print(beto.print_full_name())
print(beto.print_info())
print(beto.get_mro())

# In this code, Child class is inheriting from both Father and Mother classes.
# This is known as multiple inheritance. When you create a Child object, it will have both
# the father_name attribute from Father class and the mother_name attribute from Mother class.

# The print_parent_names method in Child class calls the print_father_name method from
# Father class and the print_mother_name method from Mother class,
# demonstrating that a Child object can use the functionality of its parent classes.

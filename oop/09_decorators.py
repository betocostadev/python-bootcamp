# Python - Introduction to Object Oriented Programming in Python
# Decorators
# Decorators are a design pattern in Python that allows a user to
# add new functionality to an existing object without modifying its structure.

print("======== Python - Introduction to Object Oriented Programming in Python ========")
print("\n=== Decorators ===\n")

# Example using a decorator


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


def say_hello():
    print("Hello!")


say_hello = my_decorator(say_hello)
say_hello()

# The @ symbol is used to apply the decorator to the function.
# The following code is equivalent to the previous code.


print("\n=== Using the @ symbol ===\n")


@my_decorator
def say_hello():
    print("Hello!")


say_hello()


print("\n=== Decorators with an calculator example ===\n")


def calculate(operation):
    def sum(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if (b == 0):
            return "Error: Division by zero!"
        return a / b

    if operation == "+":
        return sum
    elif operation == "-":
        return subtract
    elif operation == "*":
        return multiply
    elif operation == "/":
        return divide
    else:
        return "Error: Invalid operation!"


print(calculate("+")(10, 5))
print(calculate("-")(10, 5))


def calculate_decorator(func):
    def wrapper(a, b):
        print("The result is: ", func(a, b))
    return wrapper


calculate_decorator(calculate("+"))(10, 5)

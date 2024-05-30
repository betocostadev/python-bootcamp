# Python - Introduction to Object Oriented Programming in Python
# Decorators
# Decorators are a design pattern in Python that allows a user to
# add new functionality to an existing object without modifying its structure.

from functools import wraps

print(
    "======== Python - Introduction to Object Oriented Programming in Python ========"
)
print("\n=== Decorators 2 ===\n")
print("Using decorators with *args and **kwargs\n")


def duplicate_args(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}")
        print(f"Keyword arguments: {kwargs}")
        func(*args, **kwargs)  # It's calling the function but not returning the value.

    return wrapper


@duplicate_args
def learn(tecnology, hours):
    print(f"Learning {tecnology.upper()} for {hours} hours a week.")


learn_python = learn("Python", hours=10)
print(
    learn_python
)  # None, because the duplicate_args decorator does not return a value.
print(
    """
Notice that we only have the print statements from the decorator,
not the print statement from the function. """
)
print(
    learn.__name__
)  # wrapper, because the decorator is returning the wrapper function.


# Using introspection to keep the original function name
# The functools module provides a decorator called wraps that can be used to keep the original function name.
# The wraps decorator is used to keep the original function name when using decorators.
print("\n=== Using the wraps decorator ===\n")


def introspection_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}")
        print(f"Keyword arguments: {kwargs}")
        return func(
            *args, **kwargs
        )  # In this case we will return the value, but it's not necessary.

    return wrapper


@introspection_args
def learning(tecnology, hours):
    print(f"Learning {tecnology.upper()} for {hours} hours a week.")


learning("Flutter", hours=8)

print(learning.__name__)  # learning, because we are using the wraps decorator.

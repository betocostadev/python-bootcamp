# Python - Introduction to Object Oriented Programming in Python
# Decorators
# Decorators are a design pattern in Python that allows a user to
# add new functionality to an existing object without modifying its structure.

print("======== Python - Introduction to Object Oriented Programming in Python ========")
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
print(learn_python)  # None, because the duplicate_args decorator does not return a value.
print(learn.__name__)  # wrapper, because the decorator is returning the wrapper function.

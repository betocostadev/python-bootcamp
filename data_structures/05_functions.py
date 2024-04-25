# Python Data Structures
# 5 - Functions
# Functions are reusable pieces of code that can be called to perform a specific task.
# Functions are defined using the def keyword, followed by the function name and parentheses ().
# Functions can have arguments, which are values passed to the function.
# Functions can have return values, which are values returned by the function.
print("===== Python Data Structures =====")
print("5 - Functions")

# By default, Python functions return None


def show_message():
    print("Hello, World!")


show_message()


def show_name(name):
    print(f"Hello, {name}!")


show_name("John")


def show_name_default(name="Anonymous"):
    print(f"Hello, {name}!")


show_name_default()


def show_name_and_age(name="Bob", age=25):
    print(f"Hello, {name}! You are {age} years old.")


# If you name the parameters, you can pass them in any order
show_name_and_age(age=30, name="Alice")


def gets_num_before_and_after(num):
    return num - 1, num + 1


print("\n=== Retuning multiple values ===")
nums = gets_num_before_and_after(5)  # (4, 6)
# Will return a tuple with the values
print(nums)


def register_car(make, model, year):
    return f"Car registered: {year} {make} {model}"


print(register_car("Kia", "Sportage", 2022))
print(register_car(make="BMW", model="X1", year=2021))
# It's possible to use args (*), this way the values will be returned as a tuple
# Using kwargs (**), the values will be returned as a dictionary
bmwx6 = register_car(**{"make": "BMW", "model": "X6", "year": 2018})
bmwx4 = register_car(*{"BMW", "X4", 2023})
print(bmwx6)
print(bmwx4)


print("\n=== Lambda functions ===")


def show_poem(title, *args, **kwargs):
    text = "\n".join(args)
    metadata = "\n".join(f"{key.capitalize()}: {value}" for key, value in kwargs.items())
    message = f"{title}\n\n{text}\n\n{metadata}"
    print(message)


show_poem("The Raven",
          "Once upon a midnight dreary",
          "While I pondered, weak and weary",
          "Over many a quaint and curious volume of forgotten lore",
          author="Edgar Allan Poe",
          year=1845)


print("\n=== Lambda functions ===")
# Lambda functions are anonymous functions that can be defined in a single line
# Lambda functions can have any number of arguments, but can only have one expression
# Lambda functions are often used as arguments to higher-order functions
# Lambda functions can be assigned to variables, but are usually used inline
# Lambda functions are useful for simple, short functions that don't need a name


def double(x):
    return x * 2


print(double(1500))


print("\n=== Many arguments ===")
# Functions can accept many arguments:
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#       -----------    ----------     ----------
#         |             |                  |
#         |        Positional or keyword   |
#         |                                - Keyword only
#          -- Positional only


def create_car(make, model, year, /, color, *, engine, transmission="Manual"):
    return f"Car: {year} {make} {model} {color} {engine} {transmission}"

# The arguments before the / are positional only
# The arguments after the * are keyword only
# The arguments between / and * can be positional or keyword


print(create_car("Kia", "Sportage", 2022, "Red", engine="2.0L", transmission="Automatic"))

# Forcing the arguments to be passed as named arguments
print("\n=== Forcing named arguments ===")


def create_airplane(*, make, model, year):
    return f"Airplane: {year} {make} {model}"


# The arguments after the * are keyword only
print(create_airplane(make="Boeing", model="747", year=2010))


# Closures in Python
print("\n=== Closures in Python ===")
# A closure is a function that captures the environment in which it was defined
# A closure can access variables from the outer function, even after the outer function has finished executing
# A closure can be used to create a function that returns other functions


def outer_function(*, subject):
    message = f"I'm learning {subject}!"

    def inner_function():
        print(message)

    return inner_function


outer_function(subject="Python")()


print("\n=== Higher-order functions ===")
# Higher-order functions are functions that accept other functions as arguments
# Higher-order functions can also return functions as output


def sum_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def show_calc_function(a, b, *, operation):
    if operation == "sum":
        return sum_numbers(a, b)
    elif operation == "subtract":
        return subtract_numbers(a, b)
    else:
        return None


print(show_calc_function(97, 433, operation="sum"))

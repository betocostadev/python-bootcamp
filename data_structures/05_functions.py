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

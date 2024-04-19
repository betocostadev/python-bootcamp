# Strings in Python
# Strings in Python are immutable sequences of characters.

print("\n==== Strings in Python ====")
single_quote_string = 'Single quote string'
double_quote_string = "Double quote string"
triple_quote_string = """Triple quote string
    can span multiple lines"""

menu = """
    ========== Menu ==========
        1 - Withdraw
        2 - Deposit
        3 - Exit
    Thanks for using our ATM
"""

print(single_quote_string)
print(double_quote_string)
print(triple_quote_string)
print("\n")
print(menu)

# String methods
# Strings in Python have many built-in methods to manipulate them.
print("\n==== String methods ====")
course = " pyThon courSE "
print(course)
print(course.upper())
print(course.lower())
print(course.title())
print(course.title().strip())

python_course = "Python"
print(python_course.center(10, "*"))
print(".".join(python_course))

# String interpolation
# String interpolation is the process of evaluating a string containing one or more placeholders.
print("\n==== String interpolation ====")
# Can be used like in C:
name = "Carl Sagan"
age = 62
print("Name: %s, Age: %d" % (name, age))

# Using the format method
print("Famous scientist {0} died at the age of {1}".format(name, age))
print("Just so you know, the famous scients {name}, sadly died. He was {age} years old.".format(name=name, age=age))

neil = {
    "name": "Neil deGrasse Tyson",
    "age": 65
}

print("Famous scientist {name} is {age} years old".format(**neil))

# But there are also f strings
name = "John"
age = 25
print(f"Name: {name}, Age: {age}")

PI = 3.14159265359
print(f"Value of PI: {PI:.2f}")

gas_price = 5.9933
print(f"Gas price: {gas_price:.2f}")

# String slicing
# String slicing is a way to extract a substring from a string.
print("\n==== String slicing ====")
carl_sagan = "Carl Sagan"
print(carl_sagan[0])
print(carl_sagan[1])
print(carl_sagan[:4])
print(carl_sagan[5:])
# Step - every second char
print(carl_sagan[0:10:2])
# Mirror
print(carl_sagan[::-1])

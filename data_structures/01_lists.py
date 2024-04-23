# Python Data Structures
# 1 - Lists
# Lists are mutable sequences, typically used to store collections of homogeneous items.
# Lists are also used for cases where the elements are ordered and changeable.
# Lists are defined by having values between square brackets [ ].
# List items are ordered, changeable, and allow duplicate values.
print("===== Python Data Structures =====")
print("1 - Lists")
# Create a list of integers
numbers = [1, 2, 3, 4, 5]
print(numbers)
things = ["apple", 1, 3.14, "banana", 2]
print(things)
# Access items in a list
print(numbers[0])
print(numbers[1])
print(numbers[2])

print("\n=== Declaring using the list constructor var = list(string) ===")
python_list = list("Python")
print(python_list)

cars = list(("Ford", "Volvo", "BMW"))
print(cars)

print("\n=== Changing values ===")
cars[0] = "Toyota"
cars[-1] = "Mercedes"
print(cars)

for (i, car) in enumerate(cars):
    print(f"{i}: {car}")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)

# List methods
print("\n=== Some List methods ===")
print("=== append() ===")
# Add an item to the end of the list
python_list.append("e")
print(python_list)
# Add a list to the end of the list
python_list.extend(["s", "!", "!", "!"])
print(python_list)
print(python_list[8:])
print(python_list[:2])
print(python_list[1:3])
print(python_list[0:6:2])
# Print the entire list
print(python_list[::])
# Mirror the list
print(python_list[::-1])

# Accessing every element in a list
print("\n=== Accessing every element in a list ===")
for letter in python_list:
    print(letter)

months = ["January", "February", "March", "April", "May", "June", "July"]

print("\n=== Accessing every element in a list using a for loop ===")
for (idx, month) in enumerate(months):
    print(f"{idx + 1}: {month}")

# List comprehension
print("\n=== List comprehension ===")
squares = [x**2 for x in range(10)]
print(squares)
even_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
# 1 - Return value, 2 - Iteration, 3 - Condition
even = [num for num in even_numbers if num % 2 == 0]
print(even)

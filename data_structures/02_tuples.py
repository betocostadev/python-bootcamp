# Python Data Structures
# 2 - Tuples
# Tuples are immutable sequences, typically used to store collections of heterogeneous data.
# Tuples are also used for cases where an immutable sequence of homogeneous data is needed,
# such as allowing storage in a set or dict instance.
print("===== Python Data Structures =====")
print("2 - Tuples")
# Create a tuple of integers
numbers = (1, 2, 3, 4, 5,)
print(numbers)
# Create a tuple of strings
fruits = tuple(("apple", "banana", "cherry",))
print(fruits)
# Access items in a tuple
print("=== Access items in a tuple ===")
print(fruits[0])
print(fruits[1])

for (i, fruit) in enumerate(fruits):
    print(f"{i}: {fruit}")
# Remember that tuples are immutable
# fruits[0] = "orange"
# fruits.append("orange")
# fruits.extend(["orange", "grape"])
# fruits.remove("banana")
# The above operations will raise an error
# Declaring using the tuple constructor var = tuple(string)
python_tuple = tuple("Python")
print(python_tuple)
print("Ocurrences of y in Python: ", python_tuple.count("y"))
print(python_tuple.index("o"))

matrix = (
    (1, 2, 3),
    ("a", "b", "c"),
    (True, False, True),
)
print(matrix)
print("1 + 1 is equal to the matrix element [0][1]", matrix[0][1])

carros = ("gol")
print(isinstance(carros, tuple))

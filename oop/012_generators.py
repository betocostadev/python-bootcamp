# Python - Introduction to Object Oriented Programming in Python
# Generators
# Generators are a type of iterable, like lists or tuples.
# They can be created using functions and the yield statement.
#
# The yield statement is used to return a value from a generator.
# The yield statement pauses the function and saves the state of the function.
# The yield statement can be used multiple times in a function.
#
# Generators are used to create iterators.
# They are a simple way to create iterators using functions.
# Generators are memory efficient because they don't store all the values in memory.
# Generators are used to work with large data sets.
# Generators are used in loops to iterate over the elements of a sequence.
#
# The following example shows how to create a generator using a function.
# The function is called my_generator and it returns a generator object.

print("======== Python - Introduction to Object Oriented Programming in Python ========")
print("\n=== Generators ===\n")


def my_generator():
    yield 1
    yield 2
    yield 3


gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
# print(next(gen))  # StopIteration

# The following example shows how to create a generator using a for loop.
# The for loop iterates over the elements of the generator.

print("\n=== Using a for loop ===\n")

for number in my_generator():
    print(number)

# The following example shows how to create a generator using a function.

print("\n=== Using a generator with a function ===\n")


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


for number in fibonacci(10):
    print(number)

# Python - Introduction to Object Oriented Programming in Python
# Iterators
# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object that implements the iterator protocol,
# which consists of the methods __iter__() and __next__().

# Iterator vs Iterable
# Lists, tuples, dictionaries, and sets are all iterable objects.
# They are iterable containers which you can get an iterator from.

# Iterators are commonly used in loops to iterate over the elements of a sequence.
# An example is when reading a file or a list of elements.

print("======== Python - Introduction to Object Oriented Programming in Python ========")
print("\n=== Iterators ===\n")

# Example of an iterator
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
# print(next(myit))  # StopIteration


print("\n=== Create an iterator ===\n")


class MyNumbers:
    def __iter__(self):
        self.num = 0
        return self

    # We use the Stop Iteration exception to stop the iteration
    def __next__(self):
        next = self.num
        self.num += 1
        if self.num <= 6:
            return next
        else:
            raise StopIteration

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{key}: {value}' for key, value in self.__dict__.items()])}"


numbers = MyNumbers()
newit = iter(numbers)
print(numbers)
print(next(newit))
print(next(newit))

# Using another array only to keep iterating over the numbers
print("\n=== Using another array only to keep iterating over the numbers ===\n")
for number in newit:
    print(number)

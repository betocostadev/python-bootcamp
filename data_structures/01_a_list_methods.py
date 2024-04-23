print("===== Python Data Structures =====")
print("===== List Methods =====")
print("===== Coppying and Appending =====")
python_string = ["P", "y", "t", "h"]
print(python_string)
# Copying a list
python_string_complete = python_string.copy()
python_string_complete.extend(["o", "n"])
print(python_string_complete)

# Compare if it's the same object
print("=== Compare the two list ids ===")
print(id(python_string), id(python_string_complete))

print("\n=== Merging two lists into a third list ===")
cars1 = ["Bugatti", "Ford", "Volvo", "BMW", "Mercedes"]
cars2 = ["Ferrari", "Lamborghini", "Porsche", "BMW", "Audi"]
cars3 = cars1.copy()
cars3.extend(cars2)
print(cars1)
print(cars2)
print(cars3)

# Index
print("\n=== Index ===")
# Get the index of an item
print(cars3.index("BMW"))
# Lists are like stacks, so the last item added is the first to be removed
print(cars3.pop())
print(cars3.pop(2))
print(cars3)
cars3.remove("BMW")
print(cars3)
print("\n=== Sorting ===")
print("Reverse")
cars3.sort(reverse=True)
print(cars3)
# Default sorting
print("Normal")
cars3.sort()
print(cars3)

# Sorting by the smallest string first
print("Smallest string first")
cars3.sort(key=lambda x: len(x))
print(cars3)
print("\nCars list length is", len(cars3))
sorted_cars = sorted(cars3, key=lambda x: len(x))
print(sorted_cars)

test = [n**2 if n > 6 else n for n in range(10) if n % 2 == 0] 
print(test)

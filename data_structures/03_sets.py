# Python Data Structures
# 3 - Sets
# Sets are unordered collections of unique items.
# Sets are defined by having values between curly brackets { }.
# Set items are unordered, unchangeable, and do not allow duplicate values.
# Sets are mutable, but since they are unordered, indexing has no meaning.
print("===== Python Data Structures =====")
print("3 - Sets")
country_set = {"Brazil", "USA", "China", "Russia", "India", "Brazil"}
# Brazil will be removed from the set since it is a duplicate
print(country_set)

numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 7, 6]
numbers.sort()
unique_numbers = set(numbers)
print(unique_numbers)

print("\n=== Set methods ===")
# Add an item to a set
country_set.add("Germany")
print(country_set)
# Add multiple items to a set
country_set.update(["Japan", "Italy", "France"])
print(country_set)
# Remove an item from a set
country_set.remove("USA")
print(country_set)
# Remove an item from a set without raising an error if the item is not found
country_set.discard("USA")
print(country_set)
# Remove and return an arbitrary item from a set
print(country_set.pop())
other_countries = {"Mexico", "Canada", "Brazil", "Australia"}
# Union of two sets
print("\nUnion of two sets")
print(other_countries)
all_countries = country_set.union(other_countries)
print(all_countries)
# Get the intersection of two sets
print("\nIntersection of two sets")
print(country_set)
print(other_countries)
print("Intersection")
print(country_set.intersection(other_countries))
# Difference between two sets
print("\nDifference between two sets")
print(country_set)
print(other_countries)
print("Difference")
print(country_set.difference(other_countries))
"Mexico" in other_countries  # True

# Some other usable methods are:
# symmetric_difference() - Returns a set with the symmetric differences of two sets
# isdisjoint() - Returns True if two sets have no intersection
# issubset() - Returns True if another set contains this set
# issuperset() - Returns True if this set contains another set
# copy() - Returns a copy of the set
# clear() - Removes all elements from the set
# len() - Returns the number of elements in the set
# del - Deletes the set

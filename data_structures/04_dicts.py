# Python Data Structures
# 4 - Dicts
# Dictionaries are mutable collections of key-value pairs.
# Dictionaries are defined by having values between curly brackets { }.
# Dictionary items are ordered, changeable, and do not allow duplicate values.
# Dictionaries are indexed by keys, which can be any immutable type.
# Dictionaries are used to store data values in key:value pairs.
print("===== Python Data Structures =====")
print("4 - Dicts")
person1 = dict(name="John", age=36, country="USA")
person2 = {"name": "Beto", "age": 38, "country": "Netherlands"}

person2["city"] = "Amsterdam"
# person2.occupation = "Software Engineer" # This will raise an error
person2["occupation"] = "Software Engineer"
print(person1)
print(person2)

# Using dicts inside a dict
print("\n=== Using dicts inside a dict ===")
contacts = {
    "john.doe@gmail.com": {"name": "John Doe", "phone": "+1234567890"},
    "crimson.bro@outlook.com": {"name": "Crimson Bro", "phone": "+0987654321"},
    "jason@fred.com": {"name": "Jason Fred", "phone": "+1234567890"}
}
print(contacts)
print(f'Johns phone is:  {contacts["john.doe@gmail.com"]["phone"]}')

print("\n=== Dict methods ===")
# Accessing items
print(person1["name"])
print(person1.get("age"))
# Using the get method avoid an error if the key does not exist
print(person1.get("city"))

# Changing values
person1["age"] = 40
print(person1)

# Looping through a dictionary
print("\n=== Looping through a dictionary ===")
for key in person1:
    print(key, person1[key])

# Getting only the values
print("\n=== Getting only the values ===")
for value in person1.values():
    print(value)

# Getting both keys and values
print("\n=== Getting both keys and values ===")
for key, value in person1.items():
    print(key, value)

# Check if a key exists
print("\n=== Check if a key exists ===")
if "country" in person1:
    print("Yes, 'country' is one of the keys in the person1 dictionary")

print("city" in contacts["crimson.bro@outlook.com"])

# Length of a dictionary
print("\n=== Length of a dictionary ===")
print(len(person1))

# Copy a dictionary
print("\n=== Copy a dictionary ===")
person3 = person1.copy()
print(person3)

# Clear a dictionary
print("\n=== Clear a dictionary ===")
person3.clear()
print(f"New person 3 = {person3}")

# Create keys using fromkeys()
print("\n=== Create keys using fromkeys() ===")
keys = ["name", "age", "country"]
# Below the last parameter is the default value for the keys
person3 = dict.fromkeys(["name", "age", "country"], "unknown")
print(person3)

# The hashable type can be any immutable type
person4 = dict.fromkeys(["name", "age", "country"], ["Patrickson", 0, "Finland"])
print(person4)

# Get all keys
print("\n=== Get all keys ===")
person1["city"] = "New York"
print(person1.keys())

# Pop an item
print("\n=== Pop an item ===")
# Using {} as the second parameter of Pop will avoid an error if the key does not exist
# The second parameter is the default value if the key does not exist
contacts.pop("jason@fred.com", {})
print(contacts)

# setdefault
print("\n=== Setdefault ===")
# If the key does not exist, set it with the default value
print(person1.setdefault("occupation", "Unemployed"))
print(person1)

# Update a dictionary
print("\n=== Update a dictionary ===")
# If there are keys that already exist, they will be updated
# If there are new keys, they will be added
contacts.update({"crimson.bro@outlook.com": {"name": "Crimson Brocolli", "city": "Amsterdam"}})
print(contacts)

# Delete a key
print("\n=== Delete a key ===")
del contacts["crimson.bro@outlook.com"]["city"]
print(contacts)

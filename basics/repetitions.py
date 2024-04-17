# Python repetition structures
#

# For loop
print("\n==== For loop ====")
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# Else in for loop
print("\n==== Else in for loop ====")
zero_string = ""

for char in zero_string:
    print(char)
else:
    print("No chars in the string")

# Range
print("\n==== Range ====")
print(list(range(5)))  # [0, 1, 2, 3, 4

for i in range(5):
    print(i)

# Range with start and end
print("\n==== Range with start and end ====")
for i in range(2, 5):
    print(i)

# Range with start, end and step
print("\n==== Range with start, end and step ====")
for i in range(1, 10, 2):
    print(i)

# While loop
print("\n==== While loop ====")
count = 0
while count < 5:
    print(count)
    count += 1

# Break
print("\n==== Break ====")
count = 0
while count < 5:
    print(count)
    if count == 2:
        break
    count += 1

# Continue
print("\n==== Continue ====")
count = 0
while count < 5:
    count += 1
    if count == 2:
        print("Skipping 2")
        continue
    print(count)

# Removing chars from a string
print("\n==== Removing chars from a string ====")
py3 = "Python 3"
print(f'String: {py3}')

while py3:
    print(py3)
    py3 = py3[1:]

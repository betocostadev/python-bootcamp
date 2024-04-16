# Built-in functions
# input - reads the user input
# print - prints the output to the console
# type - returns the type of the variable
num1 = input("Enter the number to be multiplied: ")
num2 = input("Enter the number to multiply with: ")
result = float(num1) * float(num2)
print(f"The result of multiplication is {result}")

name = "John"
last_name = "Doe"
print(name, last_name, sep=" ", end=".\n")
print(name, last_name, sep=" and ... ", end="\n... are the names of the user.")
print("\n")
print(5 // 2)
print("\n")
print(dir(name))

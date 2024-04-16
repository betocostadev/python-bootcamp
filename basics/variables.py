# VARIABLE DECLARATION
age = 23
# Creating more than one variable in a single line
# The parentheses are optional
betosAge, name = (38, "Beto")

print("==== Variable Declaration ====")
print("John's age is " + str(betosAge))
print(f'User {name} is {betosAge} years old.')
# There are no constants in Python, but we can use uppercase to indicate that
# a variable should be treated as a constant
# Use snake_case for variable names
AMOUNT = 1500.98
print('===there are no constants in Python===')
print("Use Upper case to indicate that a variable should be treated as a constant")
print("AMOUNT = 1500.98")
print(AMOUNT)
print("Also, variable naming pattern is snake_case")
print("BASE_URL = 'http://localhost:8080'")

# Type casting
print("\n==== Type Casting ====")
total_amount = 154
# Type of total amount is int
print(type(total_amount))
total_amount = 190.98
# Inference: Type of total amount is float now
print(type(total_amount))
print(total_amount)

print("The total amount is " + str(total_amount))
# Using f-string
print(f"f-string: The total amount is {total_amount}")
total_amount = int(total_amount)
print("The total amount is after typecasting to int is " + str(total_amount))

withdraw = "150,35"
withdraw_amount = float(withdraw.replace(",", "."))
print(withdraw_amount)

# Math operations

print(1 + 1)  # 2
print(2 - 1)  # 1
print(2 * 2)  # 4
# Basic division
print(10 / 2)  # 5.0
# Integer division (excluding the remainder)
print(10 // 2)  # 5
print(12 // 5)  # 2
print(203 // 2)  # 101
# Modulus (remainder of the division)
print(5 % 2)  # 1
print(10 % 2)  # 0
# Exponential
print(2 ** 3)  # 8
print(2 ** 4)  # 16
# Precedence
print((2 + 3) * 4)  # 20
print((10 - 5) * 2)  # 10
print(10 - 5 * 2)  # 0
print(10 ** 2 * 2)  # 200

toExp = 2
toExp **= 3
print(toExp)  # 8

# Comparison operators
print("\n==== Comparison operators ====")
print(10 > 5)  # True
print(10 < 5)  # False
print(10 == 10)  # True
print(10 != 10)  # False
print(10 >= 10)  # True
print(10 <= 10)  # True

# Logical operators
print(10 > 5 and 10 < 5)  # False
print(10 > 5 or 10 < 5)  # True
print(not 10 > 5)  # False
print((10 > 5 and 5 > 6) or (6 > 4))  # True
print("Emergency contacts")
emergency_contacts = []
print(not emergency_contacts)  # True

# Identity operators
# Test if both variables are the same object
print("\n==== Identity operators ====")
x = 10
y = 10
z = 5
z += 10

lista_vazia1 = []
lista_vazia2 = []
lista_vazia_copy = lista_vazia1

print(x is y)  # True
print(x is not z)  # True
print(lista_vazia1 is lista_vazia2)  # False
print(lista_vazia1 is lista_vazia_copy)  # True

# Membership operators
# Test if a sequence is present in an object
print("\n==== Membership operators ====")
numbers = [1, 2, 3, 4, 5]
python_course = "Python Course"
cars = ["BMW", "Audi", "Mercedes", "Toyota"]

print(1 in numbers)  # True
print(6 not in numbers)  # True
print("Python" in python_course)  # True
print("BMW" in cars)  # True
print("Ferrari" not in cars)  # True
print("Lamborghini" in cars)  # False

# Banking
print("\n==== Banking ====")
balance = 1000
withdraw = 250
limit = 200
special_account = True

# Making the code cleaner
HAS_ENOUGH_FUNDS = balance >= withdraw
IS_WITHIN_LIMIT = withdraw <= limit

can_withdraw = (HAS_ENOUGH_FUNDS and IS_WITHIN_LIMIT) or (special_account and HAS_ENOUGH_FUNDS)

print(f'Balance: {balance}')
print(f'Withdraw: {withdraw}')
print(f'Limit: {limit}')
print(f'Can withdraw: {can_withdraw}')

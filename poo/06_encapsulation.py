# Python - Introduction to Object Oriented Programming in Python
# Encapsulation
# Encapsulation is one of the fundamental concepts in object-oriented programming (OOP).
# It describes the idea of wrapping data and the methods that work on data within one unit.
# This puts restrictions on accessing variables and methods directly and can prevent the accidental
# modification of data. To prevent accidental change, an object’s variable can only be changed by an
# object’s method. Those types of variables are known as private variable.

print("======== Python - Introduction to Object Oriented Programming in Python ========")
print("\n=== Encapsulation ===\n")


class Account:
    def __init__(self, account_number=None, balance=0.0, bonus=None) -> None:
        self.account_number = account_number  # Public variable
        self._balance = balance  # Private variable
        self._bonus = bonus  # Protected variable

    def deposit(self, value) -> str:  # Public method
        if value > 0:
            self._balance += value
            return f"Deposit of {value} was successful"
        return "Deposit value must be greater than 0"

    def _validate_withdraw(self, value):  # Protected method
        if 0 < value <= self._balance:
            return True
        return False

    def withdraw(self, value):
        if self._validate_withdraw(value):
            self._balance -= value
            return f"Withdrawal of {value} was successful"
        return "Withdrawal value must be greater than 0 and less than or equal to the balance"

    # Getter method - Not necessary in Python
    # More common would be to use the property decorator
    def get_balance(self) -> float:
        return self._balance

    # Property is used to access private variables
    # It is a way to encapsulate a getter and setter method in a single method
    # It can be used to create a property of a class that cannot be accessed directly
    # It can get, set, and delete a value
    # It can be used to get something in a DB and return it as an object
    # It can be used to generate computed values
    @property
    def bonus(self):
        return self._bonus or 0

    @bonus.setter
    def bonus(self, value):
        _bonus = self._bonus or value
        _value = value or 0
        self._bonus = _bonus + _value

    @bonus.getter
    def bonus(self):
        return self._bonus or 0

    @bonus.deleter
    def bonus(self):
        self._bonus = -1
        # del self._bonus

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{key}: {value}' for key, value in self.__dict__.items()])}"


cc1 = Account("3721", 100.0)
print(cc1.get_balance())
print(cc1.deposit(0))
print(cc1.deposit(50.0))
print(cc1.get_balance())
print(cc1.withdraw(80.0))
print(cc1.withdraw(100))

print(f"Balance: {cc1.get_balance()}")
print(f"Account bonus: {cc1.bonus}")
print(cc1)
cc1.bonus = 10
print(f"Account bonus: {cc1.bonus}")
del cc1.bonus
print(cc1)
# print(f"Account bonus: {cc1.bonus}")
# If using del on the bonus property before and trying to get now, the result would be:
# AttributeError: 'Account' object has no attribute '_bonus'

print("After setting the bonus -1 instead o using del on the bonus property:")
cc1.bonus = 20
print(cc1.bonus)
print(cc1)

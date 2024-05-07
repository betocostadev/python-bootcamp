# Create a command line application that simulates a simple bank account.
# The application should have the following features:
# Create user
# Create account - Tie the account to a user

# Users must be registered using the following fields
# Name, date_birth, document, address
# Address is a string and must have the following fields and in the format below:
# Street, number - neighborhood - city/state
# Only document number must be registered
# Only one account per user (Document - CPF)
# User can have more than one banking account - Account 1: 1, account 2: 2, etc.
# Document is a string and must have only numbers

# Account
# Account number - must be generated automatically
# All of the user accounts must be saved in a list
# Balance - must be zero when the account is created
# Statements - must be empty when the account is created
# Withdrawal limit - must be 500
# Withdrawal count - must be zero when the account is created
# Withdrawal limit per day - must be 3
# Account will have the following fields:
# agency, account_number, user (document)
# Account agency must be 0001

# Other features:
# Deposit money
# Withdraw money
# Check statements
# The system will allow the user to withdraw 3 times a day with a maximum of 500 per withdrawal.

# This system is based in the baking2.py file. 
# The main difference is that we will use OOP concepts to create the system.

class Client:
    def __init__(self, name: str, date_birth: str, document: str, address: str):
        self.name = name
        self.date_birth = date_birth
        self.document = document
        self.address = address

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{key}: {value}' for key, value in self.__dict__.items()])}"

    def __eq__(self, other) -> bool:
        return self.document == other.document

    def __hash__(self) -> int:
        return hash(self.document)


user1 = Client("John Doe", "01/01/1990", "12345678901", "123 Main St - Downtown - New York/NY")
user2 = Client("Jane Doe", "01/01/1995", "98765432101", "123 Main St - Downtown - New York/NY")
print(user1)
print(user2)
print(user1 == user2)
print(hash(user1))
print(hash(user2))

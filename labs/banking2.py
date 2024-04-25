# Create a command line application that simulates a simple bank account.
# The application should have the following features:
# Create user
# Create account - Tie the account to a user

# Users must be registered using the following fields
# Name, data_birth, document, address
# Address is a string and must have the following fields and in the format below:
# Street, number - neighborhood - city/state
# Only document number must be registered
# Only one account per user (Document - CPF)
# User can have more than one banking account - Account 1: 01, account 2: 02, etc.
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
# Check balance
# The system will allow the user to withdraw 3 times a day with a maximum of 500 per withdrawal.

balance = 0
limit = 500
statements = ""
withdrawal_count = 0
WITHDRAWAL_LIMIT = 3


print("\n==== Welcome to DIO Bank 2 ====\n")

menu = """
=========== Menu ===========
Press a number to select an option
    1 - Create your account
    2 - Access your account
    1 - Deposit
    2 - Withdraw
    3 - Statements
    4 - Exit
"""

# def make_withdrawal(*, balance, value, statements, limit, num_withdrawals, withdrawal_limit):
#     return balance, statements

# def make_deposit(balance, value, statements):
#     return balance, statements

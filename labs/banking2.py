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

app_menu = """
================ Welcome to DIO Bank 2 =================
Press a number to select an option
    1 - Create your account
    2 - Access your account
    3 - Exit
"""

create_user_message = """Let's create your account.
Please enter the following information:
Document - only numbers (i.e. 12345678901)
"""

# def make_withdrawal(*, balance, value, statements, limit, num_withdrawals, withdrawal_limit):
#     return balance, statements

# def make_deposit(balance, value, statements):
#     return balance, statements

# 1 - Deposit
# 2 - Withdraw
# 3 - Statements

users = []


def initiate():
    option = input(app_menu)

    if (option == "1"):
        return create_user()
    elif (option == "2"):
        print("Will access the account")
    elif (option == "3"):
        print("Thanks for using DIO Bank 2, bye!")
        return
    else:
        print("Invalid option")
        return initiate()

    return


def create_user():
    print(create_user_message)
    document = input("Enter your document number: ")

    # Check if the user already exists in the users list
    for user in users:
        if user["document"] == document:
            print("\nUser already exists")
            return initiate()

    name = input("Enter your name: ")
    birth_date = input("Enter your birth date (i.e. 01/04/1986): ")
    address = input("Enter your address (i.e. Street, number - neighborhood - city/state): ")

    print(f"\nPlease check that your information is correct:\n"
          f"Name: {name}\nBirth date: {birth_date}\nDocument: {document}\nAddress: {address}")
    confirm = input("\nDo you want to confirm? (y/n)")

    if (confirm == "y"):

        accounts = list()
        new_user = {
            "document": document,
            "name": name,
            "birth_date": birth_date,
            "address": address,
            "accounts": accounts
        }

        users.append(new_user)
        print("\nUser created successfully")
        print(users)
        return create_account(document)
    elif (confirm == "n"):
        print("\nPlease enter your information again")
        return create_user()
    else:
        print("\nInvalid option")
        return initiate()


def create_account(document):
    print("\nCreating account")

    user = {}
    for user in users:
        if user["document"] == document:
            user = user

    agency = "0001"
    account_number = len(user["accounts"]) + 1

    new_account = {
        "agency": agency,
        "account_number": account_number,
        "user": document,
        "balance": 0,
    }

    print("\nAccount created successfully")
    print(new_account)
    user["accounts"].append(new_account)
    print(users)
    return

    # return banking(

# def banking():
#     selected_user = {}
#     for user in users:
#         if user["document"] == document:
#             selected_user = user
#     print("Selected user is: ", selected_user)
#     return initiate()


initiate()

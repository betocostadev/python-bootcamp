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

banking_menu = """
================ Account options =================
Press a number to select an option
    1 - Deposit
    2 - Withdraw
    3 - Check statements
    4 - Back to accounts
    5 - Back to main menu
    6 - Exit
"""

account_info_menu = """
Press a number to select an option
    1 - Back to accounts
    2 - Back to main menu
"""

ACCOUNT_TEMPLATE = {
    "agency": "0001",
    "account_number": "",
    "user": "",
    "balance": 0,
    "statements": [],
    "limit": 500,
    "withdrawal_count_today": 0,
    "withdrawal_limit_per_day": 3
}

users = []

# Initiate the app


def initiate():
    option = input(app_menu)

    if (option == "1"):
        return create_user()
    elif (option == "2"):
        login_user(document=input("Enter your document number: "))
    elif (option == "3"):
        print("Thanks for using DIO Bank 2, bye!")
        return
    else:
        print("Invalid option")
        return initiate()

    return

# Create a user


def create_user():
    print(create_user_message)
    document = input("Enter your document number: ")

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

    if (confirm == "y".lower() or confirm == "y".upper()):

        accounts = list()
        new_user = {
            "document": document,
            "name": name,
            "birth_date": birth_date,
            "address": address,
            "accounts": accounts
        }

        users.append(new_user)
        print(f"\nUser {new_user['name']} created successfully!")
        print(users)
        return create_account(document)
    elif (confirm == "n"):
        print("\nPlease enter your information again")
        return create_user()
    else:
        print("\nInvalid option")
        return initiate()

# Create an account


def create_account(document):
    print("\nCreating account")

    user = {}
    for user in users:
        if user["document"] == document:
            user = user

    account_number = len(user["accounts"]) + 1

    new_account = ACCOUNT_TEMPLATE.copy()
    new_account["account_number"] = account_number
    new_account["user"] = document

    print("\nAccount created successfully!")
    print(f"\nAgency: {new_account['agency']}",
          f"\nAccount: {new_account['account_number']}",
          f"\nBalance: {new_account['balance']}")

    user["accounts"].append(new_account)

    return select_account(document=document)

# Log the user in


def login_user(*, document):
    user = {}
    for user in users:
        if user["document"] == document:
            user = user
    if not user:
        print("\nUser not found")
        return initiate()

    return select_account(document=document)

# Let the user select an account


def select_account(*, document):
    selected_user = {}
    for user in users:
        if user["document"] == document:
            selected_user = user
        else:
            print("\nUser not found")
            return initiate()

        print(f"\n=== Welcome to your banking account, {selected_user['name']}. ===\n")
        print("Please select an option:")
        print("1 - Create a new account")
        for i, account in enumerate(selected_user['accounts'], start=2):
            print(f"{i} - Agency: {account['agency']}, Account: {account['account_number']}")
        print(f"{len(selected_user['accounts']) + 2} - View accounts information")
        print(f"{len(selected_user['accounts']) + 3} - Back to main menu")

        option = input()

        if option == '1':
            create_account(document)
        elif 2 <= int(option) <= len(selected_user['accounts']) + 1:
            selected_account = selected_user['accounts'][int(option) - 2]
            return banking(selected_account)
        elif option == str(len(selected_user['accounts']) + 2):
            return view_accounts(selected_user)
        elif option == str(len(selected_user['accounts']) + 3):
            return initiate()
        else:
            print("Invalid option, please try again.")
            return select_account(document=document)

# View the user accounts information


def view_accounts(selected_user):
    print("\n=== Your accounts information ===")
    print(f"\nUser: {selected_user['name']}, Document: {selected_user['document']}")
    for i, account in enumerate(selected_user['accounts'], start=1):
        print(f"\nAccount {i} - Agency: {account['agency']}, Account: {account['account_number']}, "
              f"Balance: {account['balance']}")

    option = input(account_info_menu)

    if (option == "1"):
        return select_account(document=selected_user['document'])
    elif (option == "2"):
        return initiate()
    else:
        print("Invalid option")
        return view_accounts(selected_user)

# Banking functions


def banking(selected_account):
    print(f"""\nAgency: {selected_account["agency"]}, Account: {selected_account["account_number"]}""")

    def deposit(selected_account):
        deposit_amount = float(input("Enter the amount to deposit: "))
        if deposit_amount <= 0:
            print("Invalid amount")
            return deposit(selected_account)

        selected_account["balance"] += deposit_amount
        deposit_statement = f"Deposited: R${deposit_amount}, Balance: R${selected_account['balance']}"
        selected_account["statements"].append(deposit_statement)
        print(deposit_statement)
        return banking(selected_account)

    def withdraw(selected_account):
        withdrawal_amount = float(input("Enter the amount to withdraw: "))
        withdrawal_day_limit_reached = selected_account["withdrawal_count_today"] >= \
            selected_account["withdrawal_limit_per_day"]

        if withdrawal_amount <= 0:
            print("Invalid amount")
            return withdraw(selected_account)
        elif withdrawal_day_limit_reached:
            print("\nWithdrawal limit reached for today")
            return banking(selected_account)
        elif withdrawal_amount > selected_account["balance"]:
            print("\nInsufficient funds")
            return banking(selected_account)
        elif withdrawal_amount > selected_account["limit"]:
            print("\nWithdrawal limit exceeded")
            return banking(selected_account)
        else:
            selected_account["withdrawal_count_today"] += 1
            selected_account["balance"] -= withdrawal_amount
            withdrawal_statement = f"Withdrawn: R${withdrawal_amount}, Balance: R${selected_account['balance']}"
            selected_account["statements"].append(withdrawal_statement)
            print(withdrawal_statement)
            return banking(selected_account)

    def show_statements(selected_account):
        print("\n========== Statements ==========")
        for statement in selected_account["statements"]:
            print(statement)
        return banking(selected_account)

    option = input(banking_menu)

    if (option == "1"):
        return deposit(selected_account)
    elif (option == "2"):
        print("Withdrawal")
        return withdraw(selected_account)
    elif (option == "3"):
        return show_statements(selected_account)
    elif (option == "4"):
        return select_account(document=selected_account["user"])
    elif (option == "5"):
        return initiate()
    elif (option == "6"):
        print("Thanks for using DIO Bank 2, bye!")
        return
    else:
        print("Invalid option")
        return banking(selected_account)


initiate()

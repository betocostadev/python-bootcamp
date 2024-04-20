# Create a command line application that simulates a simple bank account.
# The application should have the following features:
# Deposit money
# Withdraw money
# Check balance
# The system will allow the user to withdraw 3 times a day with a maximum of 500 per withdrawal.

balance = 0
limit = 500
statements = ""
withdrawal_count = 0
WITHDRAWAL_LIMIT = 3


print("\n==== Welcome to DIO Bank 1 ====\n")

menu = """
=========== Menu ===========
Press a number to select an option
    1 - Deposit
    2 - Withdraw
    3 - Statements
    4 - Exit
"""


withdrawal_daily_limit_exceeded_message = "You have reached the withdrawal limit for today. Try again tomorrow."
withdrawal_limit_exceeded_message = f"You have reached the withdrawal limit: {limit}"

insuficient_funds_message = f"""
=== Insufficient balance ===
Your balance is: R${balance}
"""

invalid_amount_message = "======= Invalid amount ======="
statements_message = "======= Statements ========="


while True:
    option = input(menu)

    if (option == "1"):
        deposit = float(input("Enter the amount to deposit: "))
        if (deposit <= 0):
            print(invalid_amount_message)
            continue
        else:
            balance += deposit
            statements += f"Deposited: R${deposit}, Balance: R${balance}\n"
            print(f"\nDeposited: R$ {deposit}, Balance: R${balance}")

    elif (option == "2"):
        if (withdrawal_count >= WITHDRAWAL_LIMIT):
            print(withdrawal_daily_limit_exceeded_message)
        else:
            withdrawal = float(input("Enter the amount to withdraw: "))
            if (withdrawal > 0 and withdrawal <= balance):
                if (withdrawal <= limit):
                    balance -= withdrawal
                    withdrawal_count += 1
                    statements += f"Withdrawn: R${withdrawal}, Balance: R${balance}\n"
                    print(f"Withdrawn: R$ {withdrawal}, Balance: R${balance}")
                else:
                    print(withdrawal_limit_exceeded_message)
            elif (withdrawal <= 0):
                print(invalid_amount_message)
            else:
                print(insuficient_funds_message)

    elif (option == "3"):
        print(f"{statements_message}\n{statements}")

    elif (option == "4"):
        print("Thanks for using our ATM")
        break

    else:
        print("Invalid option. Try again.")
        continue

# Create a command line application that simulates a simple bank account.

# This system is based in the baking2.py file.
# The main difference is that we will use OOP concepts to create the system.

from abc import ABC, abstractmethod
from datetime import datetime
# import textwrap


class Client:
    def __init__(self, address: str):
        self.address = address
        self.accounts = []

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{key}: {value}' for key, value in self.__dict__.items()])}"

    def make_transaction(self, account, transaction):
        transaction.register(account)

    def add_account(self, account):
        self.accounts.append(account)


class Person(Client):
    def __init__(self, name: str, date_birth: datetime, document: str, address: str, ):
        super().__init__(address)
        self.name = name
        self.date_birth = date_birth
        self.document = document

    def __str__(self) -> str:
        return f"{super().__str__()} - Address: {self.address}"


class Account:
    def __init__(self, number, client: Client):
        self._balance = 0
        self._number = number
        self._agency = "0001"
        self._client = client
        self._statements = Statements()

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{key}: {value}' for key, value in self.__dict__.items()])}"

    @classmethod
    def new_account(cls, client: Client, number):
        return cls(number, client)

    @property
    def balance(self):
        return self._balance

    @property
    def number(self):
        return self._number

    @property
    def agency(self):
        return self._agency

    @property
    def client(self):
        return self._client

    @property
    def statements(self):
        return self._statements

    def withdraw(self, amount):
        exceed_limit = amount > self._balance

        if exceed_limit:
            print("@@@ Operation failed! You don't have enough balance to withdraw this amount. @@@")

        elif amount > 0:
            self._balance -= amount
            self.statements.add_statement(Transaction(self, -amount))
            print("=== Operation successful! Withdraw made successfully ===")
            return True

        else:
            print("@@@ Operation failed! Invalid amount. @@@")

        return False

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.statements.add_statement(Transaction(self, amount))
            print("=== Operation successful! Deposit made successfully ===")
            return True

        else:
            print("@@@ Operation failed! Invalid amount. @@@")

        return False


class CheckingAccount(Account):
    def __init__(self, number, client: Client, limit=500, withdrawal_limit_per_day=3):
        super().__init__(number, client)
        self.limit = limit
        self._withdrawal_count_today = 0
        self._withdrawal_limit_per_day = withdrawal_limit_per_day

    def withdraw(self, amount):
        exceed_limit = amount > self.limit
        exceed_withdrawal_limit_per_day = self._withdrawal_count_today >= self._withdrawal_limit_per_day
        # number_of_withdrawals_today =
        # len([transaction for transaction in self.statements.transactions if transaction["type"] === Withdrawal])

        if exceed_limit:
            print("@@@ Operation failed! You don't have enough balance to withdraw this amount. @@@")

        elif exceed_withdrawal_limit_per_day:
            print("@@@ Operation failed! You have reached the withdrawal limit for today. @@@")

        elif amount > 0:
            self._withdrawal_count_today += 1
            return super().withdraw(amount)

        else:
            print("@@@ Operation failed! Invalid amount. @@@")

        return False

    def __str__(self) -> str:
        return f"""\
            Agency: {self.agency}
            Account: {self.number}
            Balance: R${self.balance}
            Limit: R${self.limit}
            """


class Transaction(ABC):
    @property
    def amount(self):
        pass

    @classmethod
    @abstractmethod
    def register(self, account):
        pass


class Statements:
    def __init__(self):
        self._transactions = []

    @property
    def transactions(self):
        return self._transactions

    def add_statement(self, transaction: Transaction):
        self._transactions.append(
            {
                "type": transaction.__class__.__name__,
                "amount": transaction.amount,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
        )

    def check_statements(self):
        return self._transactions


class Deposit(Transaction):
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def register(self, account: Account):
        success = account.deposit(self.amount)

        if success:
            self._account.statements.add_statement(self)
            return True
        else:
            return False


class Withdrawal(Transaction):
    def __init__(self, amount):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    def register(self, account: Account):
        success = account.withdraw(self.amount)

        if success:
            account.statements.add_statement(self)
            return True
        else:
            return False


def menu():
    menu = """\n
    ========== MENU ==========
    [d]\tDeposit
    [w]\tWithdraw
    [s]\tCheck balance
    [nc]\tNew Client
    [l]\tList accounts
    [na]\tNew Account
    [q]\tQuit
    ==========================
    """

    # return input(textwrap.dedent(menu))
    return input(menu)


def filter_client(document, clients):
    return [client for client in clients if client.document == document]


def get_client_account(client):
    if not client.accounts:
        print("No accounts found for this client.")
        return None

    print(client)
    return client.accounts[0]


def make_deposit(clients):
    document = input("Enter your document: ")
    client = filter_client(document, clients)

    if not client:
        print("@@@ Client not found! @@@")
        return

    account = get_client_account(client)
    if not account:
        print("@@@ Account not found! @@@")
        return

    amount = float(input("Enter the amount to deposit: "))

    if account:
        client.make_transaction(account, Deposit(amount))


def make_withdraw(clients):
    document = input("Enter your document: ")
    client = filter_client(document, clients)

    if not client:
        print("@@@ Client not found! @@@")
        return

    account = get_client_account(client)
    if not account:
        print("@@@ Account not found! @@@")
        return

    amount = float(input("Enter the amount to withdraw: "))

    if account:
        client.make_transaction(account, Withdrawal(amount))


def show_statements(clients):
    document = input("Enter your document: ")
    client = filter_client(document, clients)

    if not client:
        print("@@@ Client not found! @@@")
        return

    print("Will get client account")
    print(client.accounts)

    account = get_client_account(client)
    if not account:
        print("@@@ Account not found! @@@")
        return

    print("\n ======== STATEMENTS ======== ")
    transactions = account.statements.check_statements()
    statements = ""
    if not transactions:
        statements = "No transactions found."
    else:
        for transaction in transactions:
            statements += f"{transaction['date']} - {transaction['type']} - {transaction['amount']}\n"

    print(statements)
    print(f"Balance: {account.balance:.2f}")
    print(" ============================= ")


def create_client(clients):
    name = input("Enter your name: ")
    date_birth = input("Enter your date of birth (yyyy-mm-dd): ")
    document = input("Enter your document: ")
    address = input("Enter your address: ")

    client = Person(name, date_birth, document, address)
    clients.append(client)
    print(f"Client {client.name} added successfully.")
    return client


def list_accounts(accounts):
    if not accounts:
        print("@@@ No accounts found! @@@")
        return

    for account in accounts:
        print(account)


def create_account(account_number, clients, accounts):
    document = input("Enter your document: ")
    client = filter_client(document, clients)

    if not client:
        print("@@@ Client not found! @@@")
        return

    account = CheckingAccount.new_account(client, account_number)
    accounts.append(account)
    print(client)
    print(accounts)
    # client.accounts.append(account)
    print(f"Account {account.number} added successfully.")


def main():
    clients = []
    accounts = []

    while True:
        option = menu()

        if option == "d":
            make_deposit(clients)

        elif option == "w":
            make_withdraw(clients)

        elif option == "s":
            show_statements(clients)

        elif option == "nc":
            create_client(clients)

        elif option == "l":
            list_accounts(accounts)

        elif option == "na":
            account_number = len(accounts) + 1
            create_account(account_number, clients, accounts)

        elif option == "q":
            print("Quitting...")
            break

        else:
            print("Invalid option.")
            continue


main()

# Create a command line application that simulates a simple bank account.

# This system is based in the baking2.py file.
# The main difference is that we will use OOP concepts to create the system.

from abc import ABC, abstractmethod
from datetime import datetime


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
        return f"Account {account} added"


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
        self.statements = Statements()

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
            Owner: {self.client.name}
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
        return f"Transaction {transaction} added"

    def check_statements(self):
        return self.transactions


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

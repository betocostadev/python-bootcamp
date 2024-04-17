# Python conditionals

balance = 1500.0
withdraw = 1200.0
withdraw2 = 400.0
print("\n==== Banking ====")
print("If else")


def withdraw_money(balance, withdraw):

    if balance >= withdraw:
        balance -= withdraw
        return balance
    else:
        return "Insufficient funds"


print(withdraw_money(balance, withdraw))  # 300
print(withdraw_money(balance, withdraw2))  # 1100
print(withdraw_money(balance, 2000.50))  # Insufficient funds


# Nested if
print("\n==== Nested if ====")


def withdraw_money_with_limit(balance: float, withdraw: float, limit: float = 100.0):
    if balance >= withdraw:
        balance -= withdraw
        return balance, "Withdrawal successful"
    else:
        if balance < withdraw and withdraw <= limit + balance:
            limit -= withdraw - balance
            return balance, limit, "Withdrawal successful, but you are using your limit"
        else:
            return balance, limit, "Insufficient funds"


print(withdraw_money_with_limit(1500, 1000, 200))  # (500, 'Withdrawal successful')
print(withdraw_money_with_limit(1500, 1500, 0))  # (1500, 0, 'Withdrawal successful')
print(withdraw_money_with_limit(1500, 1600))  # (1500, 100, 'Withdrawal successful, but you are using your limit')
print(withdraw_money_with_limit(1500, 1800, 350))  # (1500, 100, 'Withdrawal successful, but you are using your limit')
print(withdraw_money_with_limit(1500, 2000, 350))  # (1500, 350, 'Insufficient funds')

print("\n==== Elif ====")

age = 18

if age < 18:
    print("You are a minor")
elif age == 18:
    print("You are 18 years old")
else:
    print("You are an adult")

print("\n==== Ternary operator ====")

age = 18
message = "You are an adult" if age >= 18 else "You are a minor"
print(message)

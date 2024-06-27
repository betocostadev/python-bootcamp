# Learning Python with SQL: 09 - Managing Transactions
# MANAGING TRANSACTIONS

import sqlite3

from pathlib import Path

ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / "clients.db")

print("MANAGING TRANSACTIONS")
print(f"DB Connection: {conn}")

cursor = conn.cursor()
cursor.row_factory = sqlite3.Row

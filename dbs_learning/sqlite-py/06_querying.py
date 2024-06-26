# Learning Python with SQL: 06 - Querying Data
# Link: https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
# QUERYING DATA

import sqlite3

from pathlib import Path

ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / "clients.db")

print("QUERYING DATA")
print(f"DB Connection: {conn}")

cursor = conn.cursor()

print("\nGet client from the clients.db database using the fetchone() method")


# Get client function using fetchone()
def get_client(cursor, id):
    client = cursor.execute("SELECT * FROM clients WHERE id = ?", (id,)).fetchone()
    return client


client = get_client(cursor, 1)
print(client)


print("\nFetching all clients - fetchall()")


def list_clients(cursor):
    clients = cursor.execute("SELECT * FROM clients").fetchall()
    return clients


clients = list_clients(cursor)

for client in clients:
    print(client)


# Getting all clients e-mails
print("\nFetching all clients e-mails - fetchall()")
emails = cursor.execute("SELECT email FROM clients").fetchall()

for email in emails:
    print(email)

# Learning Python with SQL: 07 - Using SQLite Row Factory
# USING SQLITE ROW FACTORY

import sqlite3

from pathlib import Path

ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / "clients.db")

print("USING SQLITE ROW FACTORY")
print(f"DB Connection: {conn}")

# Set the row_factory attribute to sqlite3.Row
# Using sqlite3.Row, the cursor will return a row object
# The row object allows you to access the columns by name
# The row object is a mapping object
# The row object is a dictionary-like object
conn.row_factory = sqlite3.Row

cursor = conn.cursor()

print("\nGet client from the clients.db database using row_factory")


# Get client function using fetchone()
def get_client(cursor, id):
    client = cursor.execute("SELECT * FROM clients WHERE id = ?", (id,)).fetchone()
    result = dict(client)
    return result


client = get_client(cursor, 1)
print(client)


# Get all clients using fetchall() and row_factory
print("\nFetching all clients - fetchall()")


def list_clients(cursor):
    clients = cursor.execute("SELECT * FROM clients").fetchall()
    # Result for each: <sqlite3.Row object at 0xxxxxxxx>
    # Convert each row object to a dictionary
    result = [dict(client) for client in clients]
    return result


clients = list_clients(cursor)

for client in clients:
    print(client)

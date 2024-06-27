# Learning Python with SQL: 09 - Managing Transactions
# https://docs.python.org/3/library/sqlite3.html#transaction-control
# MANAGING TRANSACTIONS

import sqlite3

from pathlib import Path

ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / "clients.db")

print("MANAGING TRANSACTIONS")
print(f"DB Connection: {conn}")

cursor = conn.cursor()
cursor.row_factory = sqlite3.Row

# The default isolation level is None
# The isolation level None means that the autocommit mode is disabled
# In the autocommit mode, each SQL statement is a transaction
# The autocommit mode is enabled by setting the isolation level to None
# The isolation level None is the default mode for SQLite3

# conn.isolation_level = None
# conn.isolation_level = ""
# conn.isolation_level = "DEFERRED"

# Managing transactions to avoid data corruption or errors


def add_client(conn, cursor, data):
    try:
        # Notice that this code is wrong!
        # The clients db has an autoincrement id
        cursor.execute("INSERT INTO clients (id, name, email) VALUES (?, ?, ?);", data)
        # Commit the changes
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        # Rollback the changes
        conn.rollback()


def update_client(conn, cursor, name, email, id):
    try:
        data = (name, email, id)
        cursor.execute("UPDATE clients SET name = ?, email = ? WHERE id = ?;", data)
        # Commit the changes
        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        # Rollback the changes
        conn.rollback()


def get_client(cursor, id):
    try:
        client = cursor.execute("SELECT * FROM clients WHERE id = ?", (id,)).fetchone()
        result = dict(client)
        return result
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None


# Will raise an error because the id cannot be provided
print("\nAdding a new client")
new_client = (1, "Betina Silva", "betina@atlas.com")
print(new_client)

add_client(conn, cursor, new_client)

print("\nFetching an existing client")
client = get_client(cursor, 6)
print(client["email"])

update_client(conn, cursor, "Jurema Silva", "jurema@outlook.com", 6)

print("\nFetching the updated client")
client = get_client(cursor, 6)
print(client["email"])

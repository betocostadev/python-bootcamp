# Learning Python with SQL: 02 - Updating Data
# Link: https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
# DELETING DATA

import sqlite3

from pathlib import Path

ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / "clients.db")

print("DELETING DATA")
print(f"DB Connection: {conn}")

cursor = conn.cursor()

print("CLIENTS")
clients = cursor.execute("SELECT * FROM clients")

for client in clients:
    print(client)


# Deleting a client from the clients.db database


def delete_client(conn, cursor, id):
    cursor.execute("DELETE FROM clients WHERE id = ?", (id,))
    # Commit the changes
    conn.commit()


delete_client(conn, cursor, 8)

print("CLIENTS")
clients = cursor.execute("SELECT * FROM clients")

for client in clients:
    print(client)

# Close the connection
conn.close()

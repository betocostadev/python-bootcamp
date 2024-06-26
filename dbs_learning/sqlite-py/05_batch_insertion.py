# Learning Python with SQL: 05 - Batch Insertion
# Link: https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
# BATCH INSERTION

import sqlite3

from pathlib import Path

ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / "clients.db")

print("BATCH INSERTION")
print(f"DB Connection: {conn}")

cursor = conn.cursor()

print("\nCLIENTS")
clients = cursor.execute("SELECT * FROM clients")

for client in clients:
    print(client)


# Batch insertion
def insert_clients(conn, cursor, clients):
    cursor.executemany("INSERT INTO clients (name, email) VALUES (?, ?)", clients)
    # Commit the changes
    conn.commit()


clients = [
    ("Mario Bru", "mario@gmail.com"),
    ("Peach Prin", "peach@icloud.com"),
    ("Tonin Pardo", "pardin@outlook.com"),
]

insert_clients(conn, cursor, clients)


print("\nCLIENTS")
clients = cursor.execute("SELECT * FROM clients")

for client in clients:
    print(client)

# Close the connection
conn.close()

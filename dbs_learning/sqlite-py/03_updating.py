# Learning Python with SQL: 02 - Updating Data
# Link: https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
# UPDATING DATA

import sqlite3

from pathlib import Path

ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / "clients.db")

print(f"DB Connection: {conn}")

cursor = conn.cursor()


# Update the data
# Using (?, ?) as placeholders for the values
# This is a good practice to avoid SQL injection attacks
# johns_name = ("John Travolta", 3)
# johns_email = ("john.travs@outlook.com", 3)
# cursor.execute("UPDATE clients SET name = ? WHERE id = ?", johns_name)
# cursor.execute("UPDATE clients SET email = ? WHERE id = ?", johns_email)


def update_client(conn, cursor, name, email, id):
    data = (name, email, id)
    cursor.execute("UPDATE clients SET name = ?, email = ? WHERE id = ?;", data)
    # Commit the changes
    conn.commit()


update_client(conn, cursor, "Jurema Silva", "jurema@gmail.com", 6)

clients = cursor.execute("SELECT * FROM clients")

for client in clients:
    print(client)

# Close the connection
conn.close()

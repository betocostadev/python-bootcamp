# Learning Python with SQL: 02 - Updating Data
# Link: https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
# CONNECTING TO SQLITE3

import sqlite3

from pathlib import Path

ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / "clients.db")

print(f"DB Connection: {conn}")

cursor = conn.cursor()

johns_name = ("John Travolta", 3)
johns_email = ("john.travs@outlook.com", 3)

# Update the data
# Using (?, ?) as placeholders for the values
# This is a good practice to avoid SQL injection attacks
cursor.execute("UPDATE clients SET name = ? WHERE id = ?", johns_name)
cursor.execute("UPDATE clients SET email = ? WHERE id = ?", johns_email)

# Commit the changes
conn.commit()

clients = cursor.execute("SELECT * FROM clients")

for client in clients:
    print(client)

# Close the connection
conn.close()

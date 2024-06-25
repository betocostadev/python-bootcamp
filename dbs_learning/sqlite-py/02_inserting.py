# Learning Python with SQL: 02 - Inserting Data
# Link: https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
# CONNECTING TO SQLITE3

import sqlite3

from pathlib import Path

ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / "clients.db")

print(f"DB Connection: {conn}")

cursor = conn.cursor()

data_one = ("Beto Anthens", "beto.ant@gmail.com")

# Insert a row of data
# Using (?, ?) as placeholders for the values
# This is a good practice to avoid SQL injection attacks
cursor.execute("INSERT INTO clients (name, email) VALUES (?, ?)", data_one)

# Commit the changes
conn.commit()

# Close the connection
conn.close()

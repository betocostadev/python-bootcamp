# Learning Python with SQL: 01 - Connecting to SQLite3
# Link: https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
# CONNECTING TO SQLITE3

import sqlite3

# Put the db into the same folder as the script

from pathlib import Path

ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / "clients.db")

print(f"DB Connection: {conn}")

# Create the database cursor
# The cursor object is an instance of the cursor class and is used to execute SQL statements in SQLite3.

cursor = conn.cursor()


# Create a table
def create_table(cursor, table_name, columns):
    cursor.execute(f"CREATE TABLE {table_name} ({columns})")


# create_table(cursor, "clients", "id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(100), email VARCHAR(150)")

# Commit the changes
# conn.commit()

data_one = ("James Jameson", "jameson@outlook.com")

# Insert a row of data
# Using (?, ?) as placeholders for the values
# This is a good practice to avoid SQL injection attacks
cursor.execute("INSERT INTO clients (name, email) VALUES (?, ?)", data_one)

# Commit the changes
conn.commit()

# Close the connection
conn.close()

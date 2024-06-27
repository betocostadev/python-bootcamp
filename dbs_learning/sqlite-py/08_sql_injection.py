# Learning Python with SQL: 08 - SQL Injection
# SQL INJECTION

import sqlite3

from pathlib import Path

ROOT_PATH = Path(__file__).parent

conn = sqlite3.connect(ROOT_PATH / "clients.db")

print("SQL INJECTION")
print(f"DB Connection: {conn}")

cursor = conn.cursor()
cursor.row_factory = sqlite3.Row


client_id = input("Enter the client ID: ")
# Security vulnerability
# An attacker can use SQL injection to manipulate the query
# Try in the console 200 OR email="beto.m@gmail.com" and see the result
client = cursor.execute(f"SELECT * FROM clients WHERE id = {client_id}").fetchone()

# Avoid SQL injection
# Use placeholders to pass the values
# client = cursor.execute("SELECT * FROM clients WHERE id = ?", (client_id,)).fetchone()

print(dict(client))

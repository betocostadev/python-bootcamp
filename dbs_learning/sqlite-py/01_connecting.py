# Learning Python with SQL: 01 - Connecting to SQLite3
# Link: https://www.sqlitetutorial.net/sqlite-python/sqlite-python-select/
# CONNECTING TO SQLITE3

import sqlite3

# Put the db into the same folder as the script

from pathlib import Path

ROOT_PATH = Path(__file__).parent

con = sqlite3.connect(ROOT_PATH / "clients.db")

print(con)

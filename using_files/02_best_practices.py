# Python - Introduction to Object Oriented Programming in Python
# Best practices when using files
from pathlib import Path

print(
    "\n======== Python - Introduction to Object Oriented Programming in Python ========\n"
)
print("======== Best Practices when using files ========")

ROOT_PATH = Path(__file__).parent

# with statement
# The with statement is used to wrap the execution of a block of code.
# This is done for better management of resources.
# It simplifies exception handling by encapsulating common preparation and cleanup tasks
# in so-called context managers.
with open(ROOT_PATH / "example.txt", "r") as txt_file:
    # Using with, if there is an error, the file will be closed automatically
    content = txt_file.readlines()
    print("\nReading all lines of the file in list format: ")
    for line in content:
        print(line)


# Check if the file was correctly opened
# Also use the encoding parameter to avoid encoding errors
print("\n==== Checking if the file was correctly opened before using it ====\n")
try:
    with open(ROOT_PATH / "example.txt", "r", encoding="utf-8") as txt_file:
        content = txt_file.readline()
        print(content)
except FileNotFoundError as e:
    print("File not found: ", e)
except PermissionError as e:
    print("Permission denied: ", e)
except IOError as e:
    print("I/O error: ", e)
except Exception as e:
    print("An error occurred: ", e)

print("Is the file closed? ", txt_file.closed)


# Append to a file using with and encoding
print("\n==== Appending to a file ====\n")
try:
    with open(ROOT_PATH / "example.txt", "a", encoding="utf-8") as txt_file:
        txt_file.write("\nName: Vecna, Years: 160")
except FileNotFoundError as e:
    print("File not found: ", e)
except PermissionError as e:
    print("Permission denied: ", e)
except IOError as e:
    print("I/O error: ", e)
except Exception as e:
    print("An error occurred: ", e)

print("New file contents:")

try:
    with open(ROOT_PATH / "example.txt", "r", encoding="utf-8") as txt_file:
        content = txt_file.read()
        print(content)
except FileNotFoundError as e:
    print("File not found: ", e)
except Exception as e:
    print("An error occurred: ", e)

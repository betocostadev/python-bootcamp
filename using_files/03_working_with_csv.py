# Python - Introduction to Object Oriented Programming in Python
# Working with CSV files

import csv
from pathlib import Path


print("\n======== Python - Introduction to Object Oriented Programming in Python ========\n")
print("======== Working with CSV files ========")

ROOT_PATH = Path(__file__).parent

# Will create a new file if there is none, and will overwrite the file if it already exists
try:
    with open(ROOT_PATH / 'example.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'LastName', 'Age'])
        writer.writerow(['John', 'Doe', 30])
        writer.writerow(['Jane', 'Doe', 28])
        print("File written successfully.")
except PermissionError as e:
    print("Permission denied: ", e)
except IOError as e:
    print("I/O error: ", e)
except Exception as e:
    print("An error occurred: ", e)


print("\nReading the file: ")
try:
    with open(ROOT_PATH / 'example.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
except PermissionError as e:
    print("Permission denied: ", e)
except IOError as e:
    print("I/O error: ", e)
except Exception as e:
    print("An error occurred: ", e)


try:
    with open(ROOT_PATH / 'example.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Vecna', 'The Undying', 160])
        print("File written successfully.")
except PermissionError as e:
    print("Permission denied: ", e)
except FileNotFoundError as e:
    print("File not found: ", e)
except IOError as e:
    print("I/O error: ", e)
except Exception as e:
    print("An error occurred: ", e)


# Notice that we are using DictReader below, we will not the header row
print("\nReading the file again: ")
try:
    with open(ROOT_PATH / 'example.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print([row['Name'], row['LastName'], row['Age']])
except PermissionError as e:
    print("Permission denied: ", e)
except FileNotFoundError as e:
    print("File not found: ", e)
except IOError as e:
    print("I/O error: ", e)
except Exception as e:
    print("An error occurred: ", e)

# The code above creates a CSV file, writes to it, reads from it, appends to it, and reads from it again

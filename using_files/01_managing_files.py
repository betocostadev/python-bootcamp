# Python - Introduction to Object Oriented Programming in Python
# Managing files

import os
import shutil
from pathlib import Path

print("\n======== Python - Introduction to Object Oriented Programming in Python ========\n")
print("======== Managing files ========")

# We will deal mainly with TXT and CSV files
# Since they are the most common file types in data processing

print("\nRoot path: ")
print(__file__)

ROOT_PATH = Path(__file__).parent
# os.mkdir(ROOT_PATH / 'new_folder')

print("\nCreating a new file: ")
file = open(ROOT_PATH / 'new_folder' / 'new_file.txt', 'w')
print("Created file path: ", file.name)

print("\nRenaming a file:")
os.rename(ROOT_PATH / 'new_folder' / 'new_file.txt', ROOT_PATH / 'new_folder' / 'renamed_file.txt')
print("Renamed file path: ", ROOT_PATH / 'new_folder' / 'renamed_file.txt')

print("\nCreating and writing to a new file:")
file2 = open(ROOT_PATH / 'new_folder' / 'new_file2.txt', 'w')
file2.write("This is a new file.")
print("Created file path: ", file2.name)

print("\nMoving the new file to another folder:")
shutil.move(ROOT_PATH / 'new_folder' / 'new_file2.txt', ROOT_PATH / 'example_dir' / 'new_file2.txt')
print("Moved file path: ", ROOT_PATH / 'example_dir' / 'new_file2.txt')

# os.remove(ROOT_PATH / 'new_folder' / 'renamed_file.txt')
# os.remove(ROOT_PATH / 'new_folder')

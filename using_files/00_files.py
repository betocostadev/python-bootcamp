# Python - Introduction to Object Oriented Programming in Python
# Manipulating files

print(
    "\n======== Python - Introduction to Object Oriented Programming in Python ========\n"
)
print("======== Manipulating files ========")

# We will deal mainly with TXT and CSV files
# Since they are the most common file types in data processing

# TXT files
# Opening a file
# file = open('file.txt', 'r')  # r - read mode
# file = open('file.txt', 'w')  # w - write mode
# file = open('file.txt', 'a')  # a - append mode
# file = open('file.txt', 'r+')  # r+ - read and write mode
# file = open('file.txt', 'w+')  # w+ - write and read mode
# file = open('file.txt', 'a+')  # a+ - append and read mode

# Reading a file
# file = open('file.txt', 'r')
# content = file.read() # Reads the entire file
# content = file.readline()  # Reads the first line
# content = file.readlines()  # Reads all lines and returns a list
# print(content)
# file.close()

print("\nReading files\n")
txt_file = open("using_files/example.txt", "r")
content = txt_file.readline()  # Can use an int to limit the number of characters read
# It reads line by line, you can keep calling the function for the next lines
print("Reading the file line by line: ")
print(content)
content = txt_file.readline()  # Will read the next line
print(content)  # Will print the next line
txt_file.close()

txt_file = open("using_files/example.txt", "r")
content = txt_file.readlines()
print("\nReading all lines of the file in list format: ")
for line in content:
    print(line)
txt_file.close()

print("\nReading the entire file: ")
txt_file = open("using_files/example.txt", "r")
content = txt_file.read()
print(content)
txt_file.close()

# Reading line by line and checking the end of the file
print("\nIterating over the file content:")
txt_file = open("using_files/example.txt", "r")

while len(line := txt_file.readline()):
    print(line)

txt_file.close()


print("\nWriting files\n")
# Writing a file
new_txt_file = open("using_files/new_file.txt", "w")

new_txt_file.write("This is a new file.\n")
new_txt_file.writelines(["This is the second line.\n", "This is the third line.\n"])
new_txt_file.write("This is the fourth line.\n")
new_txt_file.close()
